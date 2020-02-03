# News-Scraper
This is a script that scrapes news headlines from the [Reuters US News](https://www.reuters.com/news/us) webpage, saving them to the filepath:
```
'~/downloads/us_news.csv'
```
*This script was written with Mac OS in mind. For now it is not assured that this will work in, say, a Windows environment.*

One can either run the script manually or schedule it to run using cron or something similar. Once collected, the data is stored under the following column names, in order from left to right:

Category | Time_Updated | Time_Gathered | Headline | Brief
--- | --- | --- | --- | ---
