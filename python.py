from flask import Flask, render_template, request # pip install flask
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

Shoppers= pd.read_csv("online_shoppers_intention.csv",sep=",")
#fix the dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Shoppers['Month'] = pd.Categorical(Shoppers['Month'], categories=months, ordered=True)
plt.rcParams['figure.figsize']= [5,3]
plt.rcParams['figure.dpi']= 200
fig, ax = plt.subplots()
Shoppers[Shoppers.VisitorType=="New_Visitor"].groupby(["Month"]).ProductRelated.sum().plot()
fig.savefig('static/graph1.png')
QueryNumber = 0


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/AnalystView', methods=['GET', 'POST'])
def AnalystView():
    return render_template('AnalystView.html')

@app.route('/AnalystViewResult', methods=['GET', 'POST'])
def AnalystViewResult():
    Query = request.form['QueryPlot']
    try: 
        exec(Query)
        global QueryNumber
        QueryNumber=QueryNumber+1
        
        fig.savefig('static/Graph' + str(QueryNumber) +'.png')
        return render_template('AnalystViewResult.html',Urlpng=('static/Graph' + str(QueryNumber) +'.png'))
    except:
        return render_template('AnalystViewResultFail.html')

@app.route('/AnalystViewResultDataframe', methods=['GET', 'POST'])
def AnalystViewResultDataframe():
    Query = request.form['Query']
    try: 
        return render_template('AnalystViewResultDataframe.html',tables=exec(Query).to_html())
    except:
        return render_template('AnalystViewResultFail.html')

@app.route('/AnalystViewResultFail', methods=['GET', 'POST'])
def AnalystViewResultFail():
    return render_template('AnalystViewResultFail.html')

@app.route('/MLView')
def MLView():
    return render_template('MLView.html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

app.run(debug=True)
