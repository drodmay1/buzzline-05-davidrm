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

# Plot 1: Sentiment Score Distribution
df['sentiment'].plot(kind='hist', bins=10, figsize=(8, 5))
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Message Length Distribution
df['message_length'].plot(kind='hist', bins=10, figsize=(8, 5))
plt.title('Message Length Distribution')
plt.xlabel('Message Length')
plt.ylabel('Frequency')
plt.show()

# Plot 3: Keyword Mentions (if meaningful)
if 'keyword_mentioned' in df.columns:
    df['keyword_mentioned'].value_counts().plot(kind='bar', figsize=(8, 5))
    plt.title('Keyword Mentions in Messages')
    plt.xlabel('Keyword')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
