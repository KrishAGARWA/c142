from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd 
import numpy as np
import statistics 

df = pd.read_csv("articles.csv")

total_events = df.sort_values('total_events', ascending = False)
output = total_events[['url','title','text','lang','total_events']].head(20).values.tolist()

