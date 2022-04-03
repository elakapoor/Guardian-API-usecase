import pandas as pd
import plotly.express as px
from datetime import date

df = pd.read_csv("articles_justin_trudeau_api.csv")

# creating a new date column
df["Date"] = pd.to_datetime(df["webPublicationDate"]).dt.date

# selecting specified date range
startdate = pd.to_datetime("2018-01-01").date()
today = date.today()

mask = (df['Date'] >= startdate) & (df['Date'] <= today)

df_filter = df.loc[mask]
df_filter = df_filter.sort_values(by='Date')

# creating a required format of date and article count
df_filter_count = df_filter.groupby("Date").size().reset_index().rename(columns = {
    0:"No. of articles"
})

# creating the graph
fig = px.line(df_filter_count, x = "Date", y = "No. of articles",
             color_discrete_sequence = ["#2377a4"] * len(df_filter_count))


fig.update_layout(
                 plot_bgcolor = "#ECECEC",
                  yaxis_title = "Articles Count",
                  title = "<b>Evolution of Articles Published</b>"
                 )

fig.write_image("article numbers.jpeg")
