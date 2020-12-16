import folium

map = folium.Map(location=[80, -100], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(
    folium.Marker(
        location=[39.2, -99.1],
        popup="Hi i am a marker",
        icon=folium.Icon(color="green"),
    )
)
map.add_child(fg)

map.save("Map1.html")