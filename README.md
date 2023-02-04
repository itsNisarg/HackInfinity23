# HackInfinity23
HackInfinity'23 organized by DCEI

### Team Details: DeepMinds
* Dhruv Shah
* Pranav Patel
* Pathik Patel
* Manjal Shah
* Nisarg Suthar

# Real time Bitcoin future price predictor

## Introduction
You can predict real live BTC/USDT price for next(5min/10min/20min) to get an idea how you should go along with your next trade. Our prediciton model
is build on deep stacked RNN's(GRU) on plenty of previous BTC/USDT price data of '1m' time interval.

## Running the App
1. Clone this repository: `git clone https://github.com/itsNisarg/HackInfinity23.git`
2. Change into the directory: `cd HackInfinity`
3. Install the requirements: `pip install -r requirements.txt`
4. Connect to your local postgres database by changing password in script where it is necessary and run livedatastreamer.py to set a live streaming data feed into the database 
5. Run the app: `streamlit run app.py`

## Usage
The app will open in your default web browser at `http://localhost:8501/` and you can interact with app.

### 1. Home page
![Home page](Home.png)

### 2. 5 min prediciton 
![5 min prediction](five.png)

### 3. 10 min prediciton 
![10 min prediciton ](ten.png)

### 4. 20 min prediciton 
![20 min prediciton ](twenty.png)

