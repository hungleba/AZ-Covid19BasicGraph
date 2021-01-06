import urllib.request
import matplotlib.pyplot as plt

def beautifyGetMonths(months):
    #Transform '2020-01' into '01/2020'
    for i in range(len(months)):
        tempList = months[i].split('-')
        newElement = tempList[1] + '/' + tempList[0][2:]
        months[i] = newElement
    months[-1] += '(updating)'


def getMonths(dataList):
    months = []
    for element in dataList:
        date = element[:7] #String slicing to get every months until the newest one
        if date not in months:
            months.append(date)
    return months

def getCD(dataList, months):
    cases = []
    deaths = []
    for currDate in months:
        caseNumbs = 0
        deathNumbs = 0
        for element in dataList:
            if element[:7] == currDate:
                newElement = element.split(',')
                if newElement[2] == '04': #Arizona's fips number is 04
                    caseNumbs = int(newElement[3])
                    deathNumbs = int(newElement[4])
        cases.append(caseNumbs)
        deaths.append(deathNumbs)
    return cases,deaths

def plot(months,cases,deaths):
    plt.figure(figsize=(15,7))
    plt.plot(months, cases, label='cases')
    plt.plot(months, deaths, label='deaths')
    plt.xlabel('Time')
    plt.title('COVID-19 graph data (ARIZONA)')
    plt.legend()
    plt.show()

def main():
    #Get and pre-processing data
    sourceLink = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    with urllib.request.urlopen(sourceLink) as rawData:
        textData = rawData.read().decode('utf-8')

    dataList = textData.split('\n') #Each element represents a separated line in data
    del dataList[0] #Delete the init description line (which is not data)

    #Extract necessary data to plot graph
    months = getMonths(dataList)
    cases,deaths = getCD(dataList, months)
    beautifyGetMonths(months)

    #Plotting graph
    plot(months,cases,deaths)


if __name__ == "__main__":
    main()
