import json
import matplotlib.pyplot as plt
from pprint import pprint


us = {}
ch = {}
with open ('GDP.json') as f:
    f = f.read()
    f = json.loads(f)
    for i in range(len(f[1])):
        if f[1][i]['date'][-1] == '0' or f[1][i]['date'][-1] == '5':
            date = float (f[1][i]['date'])
            name = f[1][i]['country']['id']
            gdp = float(f[1][i]['value'])
            us[date] = gdp
        

with open ('China.json') as f:
    f = f.read()
    f = json.loads(f)
    for i in range(len(f[1])):
        if f[1][i]['date'][-1] == '0' or f[1][i]['date'][-1] == '5':
            date = float (f[1][i]['date'])
            name = f[1][i]['country']['id']
            gdp = float(f[1][i]['value'])
            ch[date] = gdp

pd={}
spd={}
with open ('US population 1960.json') as f:
    f = f.read()
    f= json.loads(f)
    for i in range(1,len(f[1])):
        population = float((f[1][i]['value']))
        date = f[1][i]['date']
        pd[date] = population
            

plt.plot(list(us.keys()),list(us.values()))
plt.plot(list(ch.keys()),list(ch.values()))

plt.title('China and US GDPs')
plt.xlabel('Year')
plt.ylabel ('GDP value')
plt.savefig('gdp.png')
plt.show()

for elem in sorted(pd.keys()):
    spd[elem] = pd[elem]

plt.plot(sorted(list(spd.keys())),list(spd.values()))
plt.xticks(rotation = 'vertical')
plt.title('US Population Since 1960')
plt.xlabel('Year')
plt.ylabel('Population')
plt.savefig('USPop.png')
plt.show()

with open ('index.html', 'w') as f:
    
    text = ('<head>' +
        '<meta name="description" content="Henry\'s analysis of GDPs and Population.">' +
        '<title> Henry\'s Data </title></head>' +
        '<h1> China and US GDP Data </h1>' +
        '<p> The following is a summary of the US and China\'s GDP statistics. It is broken down by the date, GDP value, and country. The graph plots the data in terms of the date on the x axis and GDP value on the Y axis. </p>' +
        '<p> I downloaded the GDP data from one of the JSON data sets that Professor Izbicki provided. The JSON files are lists with dictionaries inside of them. Then, I opened the JSON file using the ' +
        'with open function. Then, I made empty dictionaries for both the US and China GDP datasets. After that, I plotted the US data through the plt.plot function ' +
        'and did the same thing with the China data.'+
        'Both of the GDPs are growing essentially exponentially because the two countries have the two largest GDP\'s in the world. They are also economic competitors.' +
        '<p><a href="http://api.worldbank.org/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json" >Link</a> is the USA data set and <a href= ' +
        '"http://api.worldbank.org/countries/CHN/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json">Link</a> is where the China data set is from. </p>' +
        '<img src="gdp.png">'+
        '<h2> US Population Data </h2>' +
        '<p> The following is a summary of the US population growth since 1960. It is broken down by the year and the population statistic of that time. It plots' +
        ' the year on the x axis and the population on the y axis.'+
        '<p> I downloaded this data from the JSON data sets that Professor Izbicki provided. The JSON files are lists with dictionaries inside of them.' +
        'Then, I opened the JSON file using the with open function. Then I made an empty dictionary for the US data set. I then plotted it using the plt.plot function.' +
        'The US\'s population has been growing since 1960.'+
        '<p><a href="http://api.worldbank.org/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json" >Link</a is the US population data set. </p> <br>' +
        '<img src="USPop.png"> <p>penis</p>')
    f.write(text)


