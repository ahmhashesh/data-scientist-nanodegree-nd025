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
### Files List:
* app: this folder contains the web application files
    * templates: 
        * go.html
        * master.html
    * DisasterResponse.db
    * run.py
* data: this folder contains the database and the csv file for training
    * disaster_categories.csv
    * disaster_messages.csv
    * DisasterResponse.db
    * process_data.py
* models: this folder containes the model pkl file and the python code for training the model.
    * classifier.pkl
    * train_classifier.py
<br>

## StarBucks Capstone Project
Every few days, Starbucks share an offer with the customers on the mobile app. The purpose is to analyze the Starbucks data and understand how users interacts with the offers sent.
### Summary of the model used:
The purpose of the project is to analyse the user behaviour and understand how the users interact with the offers.
We used matrix multiplication to calculate the relation between the user features and different offers:

#### Finding relation between user features and offers
```
mat_1 = users x user_features
mat_2 = users x offers
mat_1.T . mat_2 = user_features x offers
```

### Files List:
* data: this folder contains the database and the json file for training
    * portfolio.json
    * profile.json
    * transcript.json
* Starbucks_Capstone_notebook.ipynb: This is the main analysis code.
* requirements.txt: Python libraries needed to run the code.

The code is based on python 3.8 and the following python liberaries were used in the project:
* pandas==1.5.3
* numpy==1.23.5
* seaborn==0.12.2
* matplotlib==3.3.4
* matplotlib-inline==0.1.6

You can install the requirements by using the following command:
	``` pip install -r requirements.txt ```

### Summary of the results:
In this project, We wanted to explore customers data from Starbucks to understand the relation and users characteristics to perfectly benefit from the offers. 
From the analysis:
* we can see that different user segmentation can be done such as Joining date, gender, income and Age.
* We used only dot product to combine the different info into a relation between different users and offer features. We were able to find the user-segments which maps to the higher interactions with offers.
* We have found that Males aged between 40–80 with income between 60–80k and joined on 2017 can perform the best with both offer interaction and offer completion.
* Further user segmentation can be used based on the provided information. No need to use a machine learning model for data prediction as the relation is simple and already clear from the heatmaps.

As an improvement, I can suggest to update the data with which offer was completed for more accurate prediction on which offer would perform the best.

### Citation: This project is part of Udacity Data Science Nanodegree. The data used is provided as part of the Nanodegree.
### License: MIT License
<br>
