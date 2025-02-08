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

# Create a figure with a grid layout
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows, 2 columns

# Plot 1: Sentiment Score Distribution
axs[0, 0].hist(df['sentiment'], bins=10, color='blue', edgecolor='black')
axs[0, 0].set_title('Sentiment Score Distribution')
axs[0, 0].set_xlabel('Sentiment Score')
axs[0, 0].set_ylabel('Frequency')

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

# Plot 4: Time-Based Sentiment Trend (Optional)
if 'timestamp' in df.columns:
    df.set_index('timestamp', inplace=True)
    df.resample('1T').mean()['sentiment'].plot(ax=axs[1, 1], color='red')
    axs[1, 1].set_title('Sentiment Trend Over Time')
    axs[1, 1].set_xlabel('Time')
    axs[1, 1].set_ylabel('Average Sentiment')

# Adjust layout and display
plt.tight_layout()
plt.show()
