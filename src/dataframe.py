import pandas as pd


class DataFrame:

    def __init__(self,path):
        self.path = path
        self.delimiter = ','

    def readcsv(self):
        self.df = pd.read_csv(self.path)
        return self.df
    def readjson(self):
        self.df = pd.read_json(self.path)
        return self.df

    def head(self,row = 10):
        return self.df.head(int(row))

    def tail(self, row =10):

        return self.df.tail(int(row))

