1- clean the analysis column. the amount of data in analyst reports can be reduced by 70%. I suspect after that, there is no need for summarizing the text. Each institution has its own layout. I think it can be done in a week. (I think I just need to delete everything that comes after analyst certification)

2- A lot of the tickers are not specified in json files. something must be done about them. (maybe use some cheap llm (like claude 3 haiku) to get the right ticker). I need to get the date and the country.

3- the earnings call transcripts: I must extract the text only. the charts or the tables must be omitted. (I believe everything after presentation and before copyright must be kept)

4- I must deploy the project on AWS

5- I can train a model to predict future returns by the embeddings of analyst reports. I may want to condition on firm characteristics or other variables. To interpret, I can generate a set of themes that are usually discussed in analyst reports. and analyze the predicted returns of each.


=======================
Voyage AI has good documentation on embeddings.