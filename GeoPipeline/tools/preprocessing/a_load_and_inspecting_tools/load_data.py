import geopandas as gpd

def load_geodata(zip_path: str) -> gpd.GeoDataFrame:
    """
    Load geospatial data from a ZIP file into a GeoDataFrame.
    """
    gdf = gpd.read_file(zip_path)
    return gdf

def select_relevant_columns(gdf: gpd.GeoDataFrame, columns: list) -> gpd.GeoDataFrame:
    """
    Subset the GeoDataFrame to retain only relevant columns.
    """
    return gdf[columns]
