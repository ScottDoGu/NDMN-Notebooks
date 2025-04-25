import folium
import geopandas as gpd

def calculate_center(gdf: gpd.GeoDataFrame) -> tuple:
    """Calculate the center of a GeoDataFrame."""
    center = gdf.geometry.centroid
    return center.y.mean(), center.x.mean()

def plot_geojson(gdf: gpd.GeoDataFrame, color_col: str = "Gana_Perdi") -> folium.Map:
    lat, lon = calculate_center(gdf)
    m = folium.Map(location=[lat, lon], zoom_start=8)

    folium.GeoJson(
        gdf,
        name="geojson",
        style_function=lambda x: {
            'fillColor': 'green' if x['properties'][color_col] == 'Gano' else 'red',
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.4
        },
        tooltip=folium.GeoJsonTooltip(fields=[color_col])
    ).add_to(m)
    return m



# how to use it in the notebook
# Plot GeoJSON-style map where Gana_Perdi is color-coded

# colored_map = plot_geojson(gdf1, color_col="Gana_Perdi")
# display(colored_map)