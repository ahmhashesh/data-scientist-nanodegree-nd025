import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Loads the data from the csv files and concatenate them

    Parameter
    ---------
    messages_filepath : str
        The messages cvs file.
    categories_filepath : str
        The categories cvs file.

    Returns
    -------
    DataFrame
        DataFrame with data from both csvs concatenated
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on= 'id')
    categories = df["categories"].str.split(";",expand=True )
    row = categories.T[0]
    row = row.apply(lambda x: x[:-2])
    category_colnames = list(row)
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda a: a[-1])
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories],axis = "columns" )
    df.drop(['categories'], axis=1, inplace= True)
    return df

def clean_data(df):
    """
    removes the duplicates in the dataframe
    Parameter
    ---------
    df : DataFrame
        dataframe to be cleaned.
        
    Returns
    -------
    DataFrame
        DataFrame with data cleaned.
    """
    df = df[~df.duplicated()]
    # replacing mislabled related column data with value of 2 
    df["related"].replace(2, 1, inplace=True)
    return df

def save_data(df, database_filename):
    """
    Creates a sqlalchemy engine and save the dataframe to it. 
    Parameter
    ---------
    df : DataFrame
        dataframe to be saved.
    database_filename: 
        database file name
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('DataFrame', engine, index=False, if_exists='replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()