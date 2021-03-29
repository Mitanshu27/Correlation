import plotly.express as px
import csv
import numpy as np
def getdatasource(datapath):
    Marks = []
    RollNo = []
    with open(datapath) as f:
        a = csv.DictReader(f)
        for i in a:
            Marks.append(float(i['Marks']))
            RollNo.append(float(i['RollNo']))
    return {'x':Marks, 'y':RollNo}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print (correlation[0,1])
def setup():
    datapath = 'Student Marks vs Days Present.csv'
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup()