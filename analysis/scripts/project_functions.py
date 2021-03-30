import pandas as pd
import numpy as np
import os

os.chdir('C:/Users/eilee/course-project-solo_115')

data = pd.read_excel(r'data/raw/data.xlsx')

def load_and_process(data):

    #function1
    df = (pd.DataFrame(data=data)
    .drop(columns=['locus_tag'])
    .rename(columns={"Name":"Gene Name", "gene":"Gene Symbol", "Stationary rep1":"Stationary Phase Group 1", 
                           "Stationary rep2":"Stationary Phase Group 2", "Stationary rep3":"Stationary Phase Group 3", 
                          "3h fresh media rep1":"Growth in Media (3h) Group 1", "3h fresh media rep2":"Growth in Media (3h) Group 2",
                          "3h fresh media rep3":"Growth in Media (3h) Group 3", "3h amp media rep1":"Media and Ampicillin (3h) Group 1",
                          "3h amp media rep2":"Media and Ampicillin (3h) Group 2", "3h amp media rep3":"Media and Ampicillin (3h) Group 3"}))

    
    #function2
    col = df.loc[: , "Stationary Phase Group 1":"Stationary Phase Group 3"]
    df['Avg. Stationary Phase'] = col.mean(axis=1) 

    col2 = df.loc[: , "Growth in Media (3h) Group 1":"Growth in Media (3h) Group 3"]
    df['Avg. Growth in Media (3h)'] = col2.mean(axis=1) 

    col3 = df.loc[: , "Media and Ampicillin (3h) Group 1":"Media and Ampicillin (3h) Group 3"]
    df['Avg. Media and Ampicillin (3h)'] = col3.mean(axis=1) 


    #function 3
    df2 = (pd.DataFrame(data=df)
    .sort_values("Avg. Media and Ampicillin (3h)", ascending=False) 
    .drop(columns=["Stationary Phase Group 1", "Stationary Phase Group 2", "Stationary Phase Group 3", 
                      "Growth in Media (3h) Group 1", "Growth in Media (3h) Group 2", "Growth in Media (3h) Group 3",
                      "Media and Ampicillin (3h) Group 1", "Media and Ampicillin (3h) Group 2", "Media and Ampicillin (3h) Group 3"]))
    return df2

dataset = load_and_process(data)