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

# Create a figure for multiple plots
plt.figure(figsize=(15, 10))

# Plot 1: Sentiment Score Distribution
plt.subplot(3, 1, 1)  # 3 rows, 1 column, position 1
df['sentiment'].plot(kind='hist', bins=10)
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')

# Plot 2: Message Length Distribution
plt.subplot(3, 1, 2)  # 3 rows, 1 column, position 2
df['message_length'].plot(kind='hist', bins=10)
plt.title('Message Length Distribution')
plt.xlabel('Message Length')
plt.ylabel('Frequency')

# Plot 3: Keyword Mentions (if meaningful)
if 'keyword_mentioned' in df.columns:
    plt.subplot(3, 1, 3)  # 3 rows, 1 column, position 3
    df['keyword_mentioned'].value_counts().plot(kind='bar')
    plt.title('Keyword Mentions in Messages')
    plt.xlabel('Keyword')
    plt.ylabel('Count')

# Show all plots at once
plt.tight_layout()  # Adjust spacing between plots
plt.show()