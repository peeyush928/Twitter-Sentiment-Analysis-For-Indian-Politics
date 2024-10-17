# Twitter-Sentiment-Analysis-For-Indian-Politics
A Logistic Regression model on the Sentiment Classification of tweets.
# Twitter Sentiment Analysis Using Sentiment140 Dataset

This project performs sentiment analysis on tweets using the **Sentiment140** dataset from Kaggle. It involves fetching the dataset, preprocessing it, and analyzing the sentiments (positive, negative, neutral) using machine learning techniques.

## Features

- Model is trained on 1.6 million tweets.
- Classifies tweet sentiments as positive or negative.
- This model is helpful and scalable for Indian Politics

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
├── data/                    # Folder for extracted datasets
├── models/                  # Folder for storing machine learning models (if applicable)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


