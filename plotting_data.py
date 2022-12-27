# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:    	Abhay Patil
# Section:  	102-522
# Assignment:   Plotting Data
# Date:     	11/28/22
#
import matplotlib.pyplot as plt

filename = 'WeatherDataCLL.csv'#file name
str = ''
with open(filename, "r") as f:#read the file
    glist = f.read()
    glist = glist.split("\n")
    glist.remove('Date,Average Daily Wind Speed (mph),Precipitation (in),Average Temperature (F),Maximum Temperature (F),Minimum Temperature (F)')
    glist.remove('')


def maxtemparray():#max temps
    i = 0
    temp = []
    while i < len(glist):
        str = (glist[i].split(','))
        temp.append(int(str[4]))
        i += 1
    return(temp)

def mintemparray():#min temps
    i = 0
    temp = []
    while i < len(glist):
        str = (glist[i].split(','))
        temp.append(int(str[5]))
        i += 1
    return(temp)

def time():#numberofdays
    i = 0
    time = []
    while i < len(glist):
        i += 1
        time.append(i)
    return(time)

def AvgWindArray():#Avg wind speed
    i = 0
    wind = []
    while i < len(glist):
        str = (glist[i].split(','))
        wind.append(float(str[1]))
        i += 1
    return(wind)

diction = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, "November":11, 'December':12}

def meantemp(month, year):#Mean temp
    i = 0
    str = ''
    lol = ''
    total = 0
    ctr = 0
    while i < len(glist):
        str = (glist[i].split(','))
        lol = str[0].split('/')
        monum = diction.get(month)
        if monum == int(lol[0]) and year == int(lol[2]):
            total += float(str[3])
            ctr += 1
        i += 1
    return total / ctr

def maxtemp(month,year):
    i = 0
    str = ''
    lol = ''
    total = 0
    max = 0
    while i < len(glist):
        str = (glist[i].split(','))
        lol = str[0].split('/')
        monum = diction.get(month)
        if monum == int(lol[0]) and year == int(lol[2]):
            if int(str[4]) > max:
                max = int(str[4])
        i += 1
    return max

def mintemp(month,year):
    i = 0
    str = ''
    lol = ''
    total = 0
    max = 100
    while i < len(glist):
        str = (glist[i].split(','))
        lol = str[0].split('/')
        monum = diction.get(month)
        if monum == int(lol[0]) and year == int(lol[2]):
            if int(str[5]) < max:
                max = int(str[5])
        i += 1
    return max

def totaltemp(month):
    total = 0
    total += int(meantemp(month, 2019))
    total += int(meantemp(month,2020))
    total += int(meantemp(month,2021))
    return total/3

def totalmax(month):
    if maxtemp(month,2019) >= maxtemp(month,2020) and maxtemp(month,2019) >= maxtemp(month,2021):
        return maxtemp(month,2019)
    elif maxtemp(month,2020) >= maxtemp(month,2019) and maxtemp(month,2020) >= maxtemp(month,2021):
        return maxtemp(month,2020)
    elif maxtemp(month,2021) >= maxtemp(month,2020) and maxtemp(month,2021) >= maxtemp(month,2019):
        return maxtemp(month,2021)

def totalmin(month):
    lol = mintemp(month,2019)
    hi = mintemp(month,2020)
    pog = mintemp(month,2021)
    if mintemp(month,2019) <= mintemp(month,2020) and mintemp(month,2019) <= mintemp(month,2021):
        return mintemp(month,2019)
    elif mintemp(month,2020) <= mintemp(month,2019) and mintemp(month,2020) <= mintemp(month,2021):
        return mintemp(month,2020)
    elif mintemp(month,2021) <= mintemp(month,2020) and mintemp(month,2021) <= mintemp(month,2019):
        return mintemp(month,2021)

def montharray():
    lol = []
    lol.append(totaltemp('January'))
    lol.append(totaltemp('February'))
    lol.append(totaltemp('March'))
    lol.append(totaltemp('April'))
    lol.append(totaltemp('May'))
    lol.append(totaltemp('June'))
    lol.append(totaltemp('July'))
    lol.append(totaltemp('August'))
    lol.append(totaltemp('September'))
    lol.append(totaltemp('October'))
    lol.append(totaltemp('November'))
    lol.append(totaltemp('December'))
    return lol

def maxarray():
    lol = []
    lol.append(totalmax('January'))
    lol.append(totalmax('February'))
    lol.append(totalmax('March'))
    lol.append(totalmax('April'))
    lol.append(totalmax('May'))
    lol.append(totalmax('June'))
    lol.append(totalmax('July'))
    lol.append(totalmax('August'))
    lol.append(totalmax('September'))
    lol.append(totalmax('October'))
    lol.append(totalmax('November'))
    lol.append(totalmax('December'))
    return lol

def minarray():
    lol = []
    lol.append(totalmin('January'))
    lol.append(totalmin('February'))
    lol.append(totalmin('March'))
    lol.append(totalmin('April'))
    lol.append(totalmin('May'))
    lol.append(totalmin('June'))
    lol.append(totalmin('July'))
    lol.append(totalmin('August'))
    lol.append(totalmin('September'))
    lol.append(totalmin('October'))
    lol.append(totalmin('November'))
    lol.append(totalmin('December'))
    return lol


fig,flat = plt.subplots()
flat.plot(time(), maxtemparray(), color="red")
flat.set_xlabel("Date")
flat.set_ylabel("Maximum Temperature, F")


flat2=flat.twinx()
flat2.plot(time(), AvgWindArray(), color="blue")
flat2.set_ylabel("Average Wind Speed, mph")
flat.set_title('Maximum Temperature and Average Wind Speed')
flat.legend(["Max Temp"], loc ="lower left")
flat2.legend(["Avg Wind"], loc ="lower right")
plt.show()

fig, history = plt.subplots()
history.hist(AvgWindArray(), color = 'g', bins = 27, linewidth=1, edgecolor='black')
history.set_xlabel('Average Wind Speed, mph')
history.set_ylabel('Number of days')
history.set_title('Histogram of Average Wind Speed')
history.set(xlim=(0, 20), ylim=(0, 105))
plt.show()

fig,scatpack = plt.subplots()
scatpack.scatter(mintemparray(), AvgWindArray(), color="black")
scatpack.set_xlabel("Minimum Temperature, F")
scatpack.set_ylabel("Average Wind Speed, mph")
scatpack.set_title('Average Wind Speed vs Minimum Temperature')
plt.show()

month = [1,2,3,4,5,6,7,8,9,10,11,12]
fig,bar21 = plt.subplots()
bar21.bar(month, montharray(), color="yellow")
bar21.plot(month, maxarray(), color="red")
bar21.plot(month, minarray(), color="blue")
bar21.set_xlabel("Month")
bar21.set_ylabel("Average Temperature, F")
bar21.set_title('Temperature by Month')
bar21.legend(["High T", "Low T"], loc ="upper left")
plt.show()