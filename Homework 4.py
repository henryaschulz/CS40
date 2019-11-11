import json
import matplotlib.pyplot as plt


us = {}
ch = {}
with open ('GDP.json') as f:
    f = f.read()
    f = json.loads(f)
    for i in range(len(f[1])):
        if f[1][i]['date'][-1] == '0' or f[1][i]['date'][-1] == '5':
            date = f[1][i]['date']
            name = f[1][i]['country']['id']
            gdp = str(f[1][i]['value'])
            us[date] = gdp
        

with open ('China.json') as f:
    f = f.read()
    f = json.loads(f)
    for i in range(len(f[1])):
        if f[1][i]['date'][-1] == '0' or f[1][i]['date'][-1] == '5':
            date = f[1][i]['date']
            name = f[1][i]['country']['id']
            gdp = str(f[1][i]['value'])
            ch[date] = gdp


with open ('index.html', 'w') as f:
    
    text = ('<head>' +
        '<meta name="description" content="Henry\'s analysis of China and US GDPs.">' +
        '<title> GDP Data </title></head>' +
        '<h1> China and US GDP Data </h1>' +
        '<p> The following is a summary of the US and China\'s GDP statistics. It is broken down by the date, GDP value, and country. The graph plots the data in terms of the date on the x axis and GDP value on the Y axis. </p>' +
        '<p> I downloaded the GDP data from one of the JSON data sets that Professor Izbicki provided. Then, I opened the JSON file using the ' +
        'with open function. Then, I made empty dictionaries for both the US and China GDP datasets. After that, I wrote two identical for loops for US and China ' +
        'These for loops go through the files and find the date, country, and values of each. The JSON files are lists with dictionaries inside of them. '+
        '<p><a href="http://api.worldbank.org/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json" >Link</a> is the USA data set and <a href= ' +
        '"http://api.worldbank.org/countries/CHN/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json">Link</a> is where the China data set is from. </p>' +
        '<p> TEST </p>')
    f.write(text)    

        
    


        


"""

fig, ax=plt.subplots()
x=(us.keys())
y=ch.values()
ax.bar(x,y)
x2=[]
y2=[]
for key in sorted (us.keys()):
    plt.plot(range(len(us)), us.values())
    plt.plot(range(len(ch)), ch.values())
    x2.append('value')
    y2.append(ch[key])
    y2.append(us[key])
ax.bar (x2,y2)
plt.show()
"""
