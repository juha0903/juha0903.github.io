import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

my_data = pd.read_csv("my_data.csv")

corona_stat = {
    "plenty" : "50명이상",
    "some" : "30명이상",
    "few" : "10명이상",
    "empty" : "10명미만",
    "no_data" : "정보없음"
}
color_dic = {
    "plenty" : "red",
    "some" : "orange",
    "few" : "purple",
    "empty" : "green",
    "no_data" : "gray"
}

stat = []
for row in my_data["확진자수"]:
    cur_stat = "no_data"
    i_row = int(row)
    if i_row >= 50:
        cur_stat = "plenty"
    elif i_row >= 30:
        cur_stat = "some"
    elif i_row >= 10:
        cur_stat = "few"
    elif i_row > 0:
        cur_stat = "empty"
    stat.append(cur_stat)

lat_mean = my_data['위도'].mean()
lng_mean = my_data['경도'].mean()
map_corona = folium.Map((lat_mean, lng_mean), zoom_start=14)

mc = MarkerCluster()
names = list(my_data['감염날짜'])
lat = list(my_data['위도'])
lng = list(my_data['경도'])

for i in range(len(names)):
    icon = folium.Icon(color=color_dic[stat[i]])
    popup = names[i] + ' ' + str(i) + ' ' + corona_stat[stat[i]] + ' ' + color_dic[stat[i]]
    mc.add_child(folium.Marker(location=[lat[i], lng[i]], popup=popup, icon=icon))
    map_corona.add_child(mc)

my_map = "index.html"
map_corona.save(my_map)
webbrowser.open(my_map)