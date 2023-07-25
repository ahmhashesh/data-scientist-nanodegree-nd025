# data-scientist-nanodegree-nd025
This repository is for the udacity DataScience Nanodegree, it includes the projects required to complete this nanodegree.
## Project: Write a Data Science Blog Post
In this project, I am writing a data science blog post on medium to describe the CRISP-DM Process. This article is trying to answer three main questions:
* What are the most popular Programming Language in 2022?
* What is the relation between having a certain language and Knowing other languages?
* What is the relation between working with a certain language and Salary?
The data used for generating these results can be found [Here](https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip) and was not included here to save the space.
you can find this article on medium in the following link: [Programming Languages Insights](https://medium.com/@ahmhashesh/programming-languages-insights-95d57079511b).

### Summary of the result:
We found that Java Script is still holding her position as the most widely used programming language and the most wanted language to learn. <br>
We also illustrated the relation between working with one programming language and another, and found that working with Java Script for example requires or has a relation with working with HTML/CSS and TypeScript.<br>
Finally, we discussed discussed the relation between working with a programming language and the salary.
<br>


The code is based on python 3.8 and the following python liberaries were used in the project:
* pandas==1.5.3
* numpy==1.23.5
* seaborn==0.12.2
* matplotlib==3.3.4
* matplotlib-inline==0.1.6<br>

You can install the requirements by using the following command:
	``` pip install -r requirements.txt ```

### Files Description:
* README.md: Description of the project.
* requirements.txt: Python libraries needed to run the code.
* Write a Data Science Blog Post.ipynb: Jupyter Notebook include the code used to write the medium article [Programming Languages Insights](https://medium.com/@ahmhashesh/programming-languages-insights-95d57079511b).
### Data Source:
The data used for generating these results can be found [Here](https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip).
### License: MIT License
<br>
Feel free to provide any feedback.

## Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

### Summary of the model used:
We used the TF-IDF along with CountVectorizer as a text pipeline and then implemented a multioutput classifier using the Random Forest Classifier to predict the categories of each message.
 

<br>
