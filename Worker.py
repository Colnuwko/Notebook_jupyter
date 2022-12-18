"""import pandas as pd
from tqdm import trange
import pymorphy2
import matplotlib.pyplot as plt

import iterator


def create_table()-> pd.DataFrame:
    create a df
    number_star = []
    text_opinion = []
    for i in range(1,6):
        iterator_work = iterator.Iterator("test_csv.csv", i)
        for j in trange(len(iterator_work.list)):
            number_star.append(i)
            text_opinion.append(read_file(iterator_work.list[j]))
    df = pd.DataFrame({
    'star': number_star,
    'text': text_opinion})
    return df
    
def read_file(elem: str)->str:
    reading a data from cs
    if elem != "['absolut path,relative path,quote']":
        directory = str(elem).split(",")
        #print(len(directory))
        if len(directory) == 3:
            with open(directory[1], "r", encoding="utf-8") as f:
                text = f.read()
            
            return text     
    return ""


def check_table(df:pd.DataFrame)->pd.DataFrame:
    check table to correct value
    print("checking")
    df=df.dropna()
    print(df.info())
    return df
"""