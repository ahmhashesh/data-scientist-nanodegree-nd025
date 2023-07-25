import sys
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def load_data(database_filepath):
    engine = create_engine("sqlite:///" + database_filepath)
    df = pd.read_sql_table("DataFrame",engine)
    df["related"].replace(2, 1, inplace=True)
    df.dropna(how="any",inplace= True)
    X = df.message.values
    colms = list(df.columns)
    for i in ['message','original','genre', 'id', 'child_alone']:
        colms.remove(i)
    Y = df[colms]
    return X, Y, colms


def tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    text = word_tokenize(text)
    filtered_sentence = []
    for w in text:
        if w not in stopwords.words("english"):
            filtered_sentence.append(w)
    
    lemmed = [WordNetLemmatizer().lemmatize(word) for word in filtered_sentence]
    return lemmed


def build_model():
    parameters = parameters = {
        'clf__estimator__min_samples_split': [2,3,5],
        'clf__estimator__max_features':[1, 2, 5, 10],
        'text_pipeline__tfidf__use_idf': [True, False]    
    }

    pipeline = Pipeline(
    [
         ('text_pipeline', Pipeline([
                 ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
             ])),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    cv = GridSearchCV(estimator=pipeline, param_grid=parameters, scoring='f1_macro', cv=None, verbose=10)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    print(classification_report(Y_test.values, y_pred, target_names=category_names))



def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()