import pandas as pd
import numpy as np
def acessfile(n,date):
    df=pd.read_csv(f"""/Users/lovelakhwani/PycharmProjects/Python-Projects/Weather Api/Data/TG_STAID{n}.txt""",skiprows=20,parse_dates=["    DATE"])
    # print(df.columns) Index(['STAID', ' SOUID', '    DATE', '   TG', ' Q_TG'], dtype='object')
    df["   TG"]=df['   TG'].mask(df['   TG']==-9999,np.nan)
    df["TEMP"]=df['   TG']/10
    return(df.loc[df['    DATE']==date]['TEMP'].squeeze())
def getfilename():
    df=pd.read_csv("Data/stations.txt",skiprows=17)
    return(df[["STAID","STANAME                                 "]])

def station(station_name):
    df=pd.read_csv(f"""Data/TG_STAID{station_name}.txt""",skiprows=20,parse_dates=["    DATE"])
    df=df.to_dict(orient="records")
    return df

def getyear(station_name,year):
    df = pd.read_csv(f"""Data/TG_STAID{station_name}.txt""", skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return (result)