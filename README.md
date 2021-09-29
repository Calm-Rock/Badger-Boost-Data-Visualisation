# Badger Boost Data Visualization

This is a submission for [this](https://gitcoin.co/issue/Badger-Finance/gitcoin/27/100026488)(Create Visualization of Badger Boost Data) Gitcoin Hackathon.

This is the link to the Dashboard : https://badger-data-visualization.herokuapp.com/

### Step 1:
Preprocessed the older dates data set. It had 77 files out of which 6 files didn't had native and non-native dataset values. Calculated the Sum of Native and Non-Native Balance for each day and created two dataframes for the same and saved it as csv files.

### Step 2
Extracted the live value of Sum of Native and Non-Native tokens for all users from [this](https://badger-analytics.herokuapp.com/boosts) link and appended it to the old data dataframes.

### Step 3 
Made an area chart of the Individual daily sum of Native and Non Native balance which shows the change with time. 0 on x-axis represents the first data point (when boost was implemented)

### Step 4
Added a rerun button get the latest plot

I used the Stramlit python library to make the dashboard.

The '''boosts''' folder contains the prvious or old boosts data in JSON format.

The 'Native_Balance_historical.csv' and the 'Non_Native_Balance_historical.csv' updates everyday.

The Procfile, setup.sh and requirements.txt files are needed to deploy the Streamlit app on heroku.See[this](https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd) tutorial for more details.

