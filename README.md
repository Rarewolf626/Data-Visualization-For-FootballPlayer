# Importance of Data Visualization
Data visualization is a crucial aspect of data analysis, enabling us to transform complex datasets into meaningful insights. By visualizing data, we can uncover patterns, trends, and correlations that may otherwise be hidden in raw numbers. It helps in making data-driven decisions more intuitive and accessible to a wider audience, from technical experts to stakeholders with limited technical backgrounds.

In this project, I used the [**Bokeh**](https://bokeh.org) library to create interactive and engaging visualizations. Bokeh allows for dynamic plotting, enabling users to explore and manipulate data in real-time. Whether working with large datasets or creating intricate graphs, Bokeh's flexibility and power make it a perfect tool for building sophisticated data visualizations for the web.

# Project Description
This project focuses on visualizing data from a dataset of players in the top 5 football leagues worldwide, using the Bokeh library for creating interactive visualizations. The goal is to provide an intuitive way to explore key statistics about players, such as goals scored, average age, passes completed, yellow and red cards, and more.

## Project sections
The project includes an interactive table and two dynamic charts:

1. **Interactive Table**: Displays general information like goals, average age, passes, and cards, allowing users to explore various player statistics.

2. **League Age Distribution Chart**: Visualizes the number of players in each league, categorized by age. Users can filter by league and age range to see how many players fall within specific age groups in each league.

3. **Country Representation Chart**: Shows the number of players from different countries in each league. Users can select a league and a country to view how many players from that country are present in the selected league, along with their detailed information.

This project demonstrates the power of Bokeh in creating interactive and customizable visualizations, providing an engaging way to 
analyze and explore football player data across multiple dimensions.

## dataset
For this project, I utilized the [2022-2023 Football Player Stats dataset](./2022-2023%20Football%20Player%20Stats.csv), available on [Kaggle at this link](https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats). This dataset contains comprehensive statistics for football players across the top 5 leagues during the 2022-2023 season. It includes detailed information such as player names, ages, goals, assists, passes, yellow and red cards, and other key performance metrics. The dataset is a valuable resource for analyzing player performance and exploring trends within and across leagues.

## Screenshot
1. ![Overview](./Screenshot/Screenshot%202024-09-06%20160834.png)
2. ![Customize the chart](./Screenshot/Screenshot%202024-09-06%20160844.png)
3. ![Customize the chart](./Screenshot/Screenshot%202024-09-06%20160852.png)
4. ![Customize the chart](./Screenshot/Screenshot%202024-09-06%20160902.png)
5. ![Customize the chart](./Screenshot/Screenshot%202024-09-06%20160913.png)
6. ![Customize the chart](./Screenshot/Screenshot%202024-09-06%20161028.png)

# Prerequisites
Python (3.12)
## Libraries
1. [numpy](https://numpy.org/)
2. [pandas](https://pandas.pydata.org/)
3. [bokeh](https://bokeh.org)

# How to run
To run this project, use this command:`bokeh serve --show player.py`

# File structure
1. [player.py](./player.py) It is the main file that reads the required data in this file and then takes different tabs from other files and prepares and executes the document.
2. [graf.py](./graf.py) It is a file in which charts and tables are made

# You can find me at:
1. [![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/amirmohsen-taheri)
2. [![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/AmirMohsenTaheri)
3. [instagram](https://instagram.com/pybyamir)
4. **Gmail** : **amirmohsentaheri.k@gmail.com**

# Updating...