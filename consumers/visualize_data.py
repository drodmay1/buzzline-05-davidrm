import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
db_path = "../data/buzz.sqlite"
conn = sqlite3.connect(db_path)

# Load data into a pandas DataFrame
query = """
SELECT timestamp, urgent_count, error_count, warning_count, sentiment 
FROM streamed_messages;
"""
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot 1: Total Keyword Counts
keyword_counts = df[['urgent_count', 'error_count', 'warning_count']].sum()
keyword_counts.plot(kind='bar', figsize=(8, 5))
plt.title('Total Keyword Counts')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Plot 2: Keyword Frequency Over Time
df.set_index('timestamp')[['urgent_count', 'error_count', 'warning_count']].plot(figsize=(10, 6))
plt.title('Keyword Frequency Over Time')
plt.ylabel('Count')
plt.xlabel('Time')
plt.legend(title='Keywords')
plt.show()

# Plot 3: Sentiment Distribution
df['sentiment'].plot(kind='hist', bins=10, figsize=(8, 5))
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
