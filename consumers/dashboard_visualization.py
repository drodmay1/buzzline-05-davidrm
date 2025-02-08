import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
db_path = "../data/buzz.sqlite"
conn = sqlite3.connect(db_path)

# Load data into a pandas DataFrame
query = """
SELECT timestamp, sentiment, keyword_mentioned, message_length
FROM streamed_messages;
"""
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Ensure sentiment column is numeric and drop invalid rows
df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')  # Convert invalid values to NaN
df_clean = df.dropna(subset=['sentiment'])  # Remove rows with NaN in sentiment

# Set timestamp as the index for resampling
if not df_clean.empty:
    df_clean.set_index('timestamp', inplace=True)

# Create a figure with subplots (2x2 layout)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows, 2 columns

# Plot 1: Sentiment Score Distribution
if not df_clean.empty:
    axs[0, 0].hist(df_clean['sentiment'], bins=10, color='blue', edgecolor='black')
    axs[0, 0].set_title('Sentiment Score Distribution')
    axs[0, 0].set_xlabel('Sentiment Score')
    axs[0, 0].set_ylabel('Frequency')
else:
    axs[0, 0].text(0.5, 0.5, 'No valid sentiment data', fontsize=12, ha='center')

# Plot 2: Message Length Distribution
axs[0, 1].hist(df['message_length'], bins=10, color='green', edgecolor='black')
axs[0, 1].set_title('Message Length Distribution')
axs[0, 1].set_xlabel('Message Length')
axs[0, 1].set_ylabel('Frequency')

# Plot 3: Keyword Mentions
if 'keyword_mentioned' in df.columns:
    keyword_counts = df['keyword_mentioned'].value_counts()
    axs[1, 0].bar(keyword_counts.index, keyword_counts.values, color='orange', edgecolor='black')
    axs[1, 0].set_title('Keyword Mentions in Messages')
    axs[1, 0].set_xlabel('Keyword')
    axs[1, 0].set_ylabel('Count')
    axs[1, 0].tick_params(axis='x', rotation=45)
else:
    axs[1, 0].text(0.5, 0.5, 'No keyword data available', fontsize=12, ha='center')

# Plot 4: Sentiment Trend Over Time
if not df_clean.empty:  # Only proceed if there's valid sentiment data
    sentiment_trend = df_clean['sentiment'].resample('1min').mean()  # Resample by 1 minute
    sentiment_trend.plot(ax=axs[1, 1], color='red')
    axs[1, 1].set_title('Sentiment Trend Over Time')
    axs[1, 1].set_xlabel('Time')
    axs[1, 1].set_ylabel('Average Sentiment')
else:
    axs[1, 1].text(0.5, 0.5, 'No sentiment trend data', fontsize=12, ha='center')

# Adjust layout and display
plt.tight_layout()
plt.show()
