import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

#produces a color
def color_prod(e):
    if e < 1000:
        return 'green'
    elif e >= 1000 and e < 3000:
        return "orange"
    else:
        return "red"      
    

map = folium.Map(location=[5.144,10.524],zoom_start=6,tiles="Stamen Terrain")


fg = folium.FeatureGroup(name="My Map")

for lt, lg,el in zip(lat,lon,elv):
    fg.add_child(folium.Marker(location=[lt,lg], popup=str(el)+"m",icon=folium.Icon(color=color_prod(el))))

fg.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000
else "red"}))

map.add_child(fg)

map.save("Map1.html")
