import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('yahoo_data.xlsx')

#print(df.describe(), df.head())

# Defining columns "Daily Return" and "Daily Change"
df["Daily_Return"] = df["Adj Close**"].pct_change()
df["Daily_Change"] = df["Adj Close**"].diff()
df["Cumulative_Return"] = (1 + df["Daily_Return"] / 100).cumprod()
# Cleaning and Formatting
# Removing leading and trailing spaces, and cleaning the dataframe
df.rename(columns=lambda x: x.strip().replace(" ", "_").replace("*", ""), inplace=True)

# Converting the Date column to datetime object, setting Date column as the index
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# First rows are NaN as there is no previous row for the diff() and pct_change() to work with, this replaces them with 0
df["Daily_Return"] = df["Daily_Return"].fillna(0)
df["Daily_Change"] = df["Daily_Change"].fillna(0)

# Filling Nulls with the word "Blank"
#df = df.fillna("Blank")

print(df.head())
#print(df.dtypes)


#print(df.isnull().sum())

#print(df.isnull().sum())

# Matplotlib Section


# Stock Price History - Plot
plt.figure(figsize=(12,6)) # Set dimensions
plt.plot(df.index, df["Adj_Close"], label="Adjusted Close", color="Blue") # Set X and Y axis 
plt.title("Stock Price History") # Plot title
plt.xlabel("Date") # X Axis name
plt.ylabel("Price in $") # Y Axis name
plt.legend() # Show legend (Shows labels)
plt.grid(True) # Show a grid in the background
plt.show() # Show plot

# Daily returns over time - Plot
plt.figure(figsize=(12,6)) # Set dimensions
plt.plot(df.index, df["Daily_Return"], label="Daily Return", color="Green") # Set X and Y axis 
plt.title("Daily returns over time") # Plot title
plt.xlabel("Date") # X Axis name
plt.ylabel("Daily Return (in $)") # Y Axis name
plt.legend() # Show legend (Shows labels)
plt.grid(True) # Show a grid in the background
plt.show() # Show plot


plt.figure(figsize=(12,6)) # Set dimensions
plt.plot(df.index, df["Cumulative_Return"], label="Cumulative Return", color="Red") # Set X and Y axis 
plt.title("Cumulative returns over time") # Plot title
plt.xlabel("Date") # X Axis name
plt.ylabel("Returns (in $)") # Y Axis name
plt.legend() # Show legend (Shows labels)
plt.grid(True) # Show a grid in the background
plt.show() # Show plot

