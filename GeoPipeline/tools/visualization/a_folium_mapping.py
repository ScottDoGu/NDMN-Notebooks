import folium
import geopandas as gpd

def downsample_gdf(gdf: gpd.GeoDataFrame, step: int = 10) -> gpd.GeoDataFrame:
    """downsample a GeoDataFrame by selecting every nth row."""
    return gdf.iloc[::step]

def calculate_center(gdf: gpd.GeoDataFrame) -> tuple:
    """calculate the centroid of all geometries in the GeoDataFrame."""
    mean_point = gdf.geometry.unary_union.centroid
    return mean_point.y, mean_point.x

def create_folium_map(gdf: gpd.GeoDataFrame, zoom: int = 9) -> folium.Map:
    """create a Folium map and plot circle markers for each geometry."""
    lat, lon = calculate_center(gdf)
    m = folium.Map(location=[lat, lon], zoom_start=zoom)

    for _, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=1,
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.7
        ).add_to(m)

    return m
