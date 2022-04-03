<h1>Web scraping and case study using Guardian API</h1>
<p>The app is created in pycharm using python, pandas and plotly</p>
<h3>Table of Content</h3>

* [General info](#general-info)
* [Requirements](#requirements)
* [Setup](#setup)
* [File structure](#file-structure)

## General info
The project uses the Guardian API for the web scraping of all articles related to Justin Trudeau.
It then store these articles in the csv format. The pandas library is used for the data
analysis and plotly is used for the data visualization.

### Web Scrapping the data
Guardian API is a very interactive API and helps to understand the API structure easily.
With the help of requests and python library it is easy to download the data for the search term.
The structure of the post helps you to select the required columns for the analysis. These
columns could be selected and then appended using the python functionalities.

### Data Analysis
When the articles are saved as a dataframe it is present locally and could be used for any
analysis purposes. With the help of plotly, interactive graphs are created.

### Automatic Email
As a step further, the application also provide you with the facility to automatically send 
the updated info to the users automatically. The email and mime functionality of 
internet data handling python library allows you to easily attach an image or send a html text
to the users automatically.
	
## Requirements
Project uses:
* APScheduler== 3.9.1
* backports.zoneinfo==0.2.1
* kaleido==0.2.1
* numpy==1.21.5
* pandas==1.3.5
* pip==21.1.2
* plotly==5.6.0
* python-dateutil==2.8.2
* pytz==2022.1
* requests==2.27.1
* setuptools==57.0.0
* six==1.16.0	1.16.0
* tenacity==8.0.1
* tzdata==2022.1
* tzlocal==4.1
* urllib3==1.26.9
* wheel==0.36.2
	
## Setup
To run this project, download it and run python filename.py from the same directory

```
$ cd ../automate_alert
$ python filename.py

```
## File structure
The repository consist of three .py files namely:
1. collect_article.py
2. automate_alert.py
3. full_automate.py
4. CaseStudy.ipynb

<b>collect_article.py: </b>  This file will collect all the data using API, analyze the data
and then save plots created in the same directory. It will also save the scrapped data.

<b>automate_alert.py: </b> This file will collect the saved file in the same directory and send the data to
the users in the receiving list. The data is sent as an attached image file as well as
html content.

<b>full_automate.py: </b> This file will collect the data and send it to receiver. It is the
combination of above two steps. But it will not go in detail analysis as done by the 
collect_article.py file. The objective of the file is to send the updated data to the users.

<b>CaseStudy.ipynb: </b> This file shows the step by step data collection process and analysis done

