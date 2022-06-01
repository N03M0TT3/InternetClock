import requests
from bs4 import BeautifulSoup

def getMonth(month):
    res = ''

    if month == 'janvier':
        res = '01'
    if month == 'février':
        res = '02'
    if month == 'mars':
        res = '03'
    if month == 'avril':
        res = '04'
    if month == 'mai':
        res = '05'
    if month == 'juin':
        res = '06'    
    if month == 'juillet':
        res = '07'
    if month == 'août':
        res = '08'
    if month == 'septembre':
        res = '09'
    if month == 'octobre':
        res = '10'
    if month == 'novembre':
        res = '11'
    if month == 'décembre':
        res = '12'  

    return res


def getDay(day):
    if(int(day) < 10):
        return '0' + day
    else:
        return day


def getDate():
    
    page = requests.get("https://www.timeanddate.com/worldclock/france")

    soup = BeautifulSoup(page.content, 'html.parser')

    time = soup.find('span', class_='h1').get_text()
    # print(time)

    date = soup.find('span', id='ctdat').get_text()
    # print(date)

    listTime = time.split(' ')
    listDate = date.split(' ')


    # date format MM/DD/HH/mm/YY
    result = getMonth(listDate[2]) + getDay(listDate[1]) + listTime[0] + listTime[2] + listDate[3][2:4]
    print(result)


if __name__ == "__main__":
    getDate()