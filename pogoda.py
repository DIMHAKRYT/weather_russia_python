import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

# данные на данный момент
time_now = datetime.now()
out_time = str(time_now.strftime("%H" + ":" + "%M"))
hour = int(time_now.strftime("%H"))
year = str(time_now.strftime("%Y"))
month = str(int(time_now.strftime("%m")) - 1)
day = str(time_now.strftime("%d"))
# данные на следующий день
next_day_raw = datetime.now() + timedelta(days=1)
next_day = str(next_day_raw.strftime("%d"))
sear = year + "," + month + "," + day
sear_next_day = year + "," + month + "," + next_day
# данные на послезавтра
next_next_day_raw = datetime.now() + timedelta(days=2)
next_next_day = str(next_next_day_raw.strftime("%d"))
sear_last = year + "," + month + "," + next_day
sear_last_next_day = year + "," + month + "," + next_next_day
# получение кода страницы meteoinfo
url = "https://meteoinfo.ru/forecasts/russia/moscow-area/moscow" # ссылка на погоду вашего города такого же формата
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
ready = str(soup.find_all("div", class_="tabs__content"))
# поиск данных на сегодня
copy_com = ready[ ready.find("{x: Date.UTC(" + sear) :
     int(ready.find("{x: Date.UTC(" + sear_last)) - 2]

print("Время " + out_time)

# вывод данных о погоде на сегодня
while True:

    time_tem = copy_com[: copy_com.find(")")]
    time_tem = time_tem[time_tem.rfind(",") + 1 :]

    temp = copy_com[copy_com.find("y:") + 2 : copy_com.find(", ind")]

    copy_com = copy_com.replace(copy_com[: int(copy_com.find("}")) + 2], "")

    if int(time_tem) < hour - 1:
        continue

    print(" в " + time_tem + ":00 температура: " + temp)

    if len(copy_com) <= 0:
        break

# поиск данных на завтра
copy_com = ready[ ready.find("{x: Date.UTC(" + sear_next_day) :
    int( ready.find("{x: Date.UTC(" + sear_last_next_day) ) - 2]

# вывод данных о погоде на завтра
print("Завтра: ")

while True:

    time_tem = copy_com[: copy_com.find(")")]
    time_tem = time_tem[time_tem.rfind(",") + 1 :]

    temp = copy_com[copy_com.find("y:") + 2 : copy_com.find(", ind")]

    copy_com = copy_com.replace(copy_com[: int(copy_com.find("}")) + 2], "")

    print(" в " + time_tem + ":00 температура: " + temp)

    if len(copy_com) <= 0:
        break

# время до закрытия окна
time.sleep(20)
