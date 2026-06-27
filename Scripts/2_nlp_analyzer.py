import pandas as pd
from textblob import TextBlob

print("Loading raw reviews...")
df = pd.read_csv("raw_reviews.csv")

# Define the NLP function
def calculate_sentiment(text):
    # TextBlob calculates polarity from -1.0 (highly negative) to 1.0 (highly positive)
    score = TextBlob(str(text)).sentiment.polarity
    
    # Categorize based on the mathematical score
    if score > 0.1:
        return "Positive", score
    elif score < -0.1:
        return "Negative", score
    else:
        return "Neutral", score

print("Running NLP Sentiment Engine...")
# Apply the NLP function to the Review_Text column
df[['Sentiment_Category', 'Polarity_Score']] = df['Review_Text'].apply(
    lambda x: pd.Series(calculate_sentiment(x))
)

# Save the processed data
df.to_csv("analyzed_reviews.csv", index=False)
print("Success: Data processed and saved as analyzed_reviews.csv!")