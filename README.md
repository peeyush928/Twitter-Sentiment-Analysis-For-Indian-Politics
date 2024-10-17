# Twitter-Sentiment-Analysis-For-Indian-Politics
A Logistic Regression model on the Sentiment Classification of tweets.

This project performs sentiment analysis on tweets using the dataset of 1.6 million tweets. It involves fetching the dataset, preprocessing and stemming it, and analyzing the sentiments (positive, negative, neutral) using Natural Language Processing techniques. A relevant vector-based classifier is declared for the classification of sentiment tweets and then training the model on the dataset using Logistic Regression and machine learning techniques.

## Benefits of Twitter Sentiment Analysis

1. **Real-Time Feedback and Political Insights**:
   - This can also assist with crisis management by identifying and addressing negative trends before they escalate. Organizations can directly control the flow of hate speeches and violence.

2. **Customer Insights and Product Feedback**:
   - Understand customer preferences, behavior, and pain points by analyzing tweets related to your product or service. Use this feedback to guide product development and improve customer satisfaction.

3. **Brand Monitoring and Trend Analysis**:
   - Discover emerging trends and shifts in the public interest by analyzing sentiment around specific topics or products. This data can be useful for predicting future trends and guiding business strategy.

4. **Campaign Optimization**:
   - Measure the effectiveness of marketing campaigns by tracking sentiment before, during, and after the campaign. Use this data to refine messaging and improve public relations strategies in real time.





## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)


## Installation

### Prerequisites

To run this project, you'll need the following:

- Python 3.x
- Kaggle account and API key (for downloading the dataset)

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/twitter-sentiment-analysis.git
    cd twitter-sentiment-analysis
    ```

2. Install required packages:

    ```bash
    pip install kaggle
    ```

    Alternatively, run the following command if additional packages are needed (list them in `requirements.txt`):

    ```bash
    pip install -r requirements.txt
    ```

### Kaggle API Setup

1. Download your **Kaggle API credentials** (`kaggle.json`) from your Kaggle account.
2. Place `kaggle.json` in the root of your project or configure the path using the following commands in the notebook or terminal:

    ```bash
    mkdir -p ~/.kaggle
    cp kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

## Usage

### Download and Extract Dataset

The notebook automates the process of downloading and extracting the **Sentiment140** dataset. Simply run the notebook and it will:

1. Fetch the dataset from Kaggle:

    ```bash
    !kaggle datasets download -d kazanova/sentiment140
    ```

2. Extract the dataset:

    ```python
    from zipfile import ZipFile
    dataset = '/content/sentiment140.zip'
    
    with ZipFile(dataset, 'r') as zip:
        zip.extractall()
        print('The dataset is extracted')
    ```

### Run Sentiment Analysis

Once the dataset is prepared, further steps in the notebook will include:

1. **Preprocessing**: Clean and preprocess the tweets.
2. **Modeling**: Apply machine learning models to classify sentiments.
3. **Visualization**: Optionally, you can visualize the sentiment trends using libraries like `matplotlib` or `seaborn`.

## Project Structure

```plaintext
twitter-sentiment-analysis/
│
├── TSA.ipynb                # Jupyter notebook for sentiment analysis
├── kaggle.json              # Kaggle API credentials (not included in the repo)
├── data/                    # Numpy, Pandas, and Seaborn for datasets
├── models/                  # Logistic Regression(Machine Learning Model)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


