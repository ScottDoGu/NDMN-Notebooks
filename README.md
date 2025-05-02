# NDMN-Notebooks
## Project Summary

This is a project for Purdue's National Data Mine Network where we are working with the USDA's Forest Inventory and Analysis (FIA) program.

## List of initial notebooks and directory structure

1. **CostaRica-Notebook Directory** - Stores all notebooks and files regarding the Costa Rican dataset
   - **[DanV1_Final.ipynb](/CostaRica-Notebook/DanV1_Final.ipynb)** - Fall 2024's all-in-one notebook
   - **[DanV2_Pipeline.ipynb](/CostaRica-Notebook/DanV2_Pipeline.ipynb)** - Spring 2025's, **parent**, all-in-one notebook with a template based on the Gantt Chart
   - **[John-CostaRica](/CostaRica-Notebook/John-CostaRica.ipynb)** - John's Costa Rican notebook that acquires data from GEE
   - **Archived Directory** - Stores Gabriel's old Fall 24' notebooks
   - **Costa Rican Data Directory** - Stores the Costa Rican data 
     - **[Classification_Plots.zip](/CostaRica-Notebook/Costa%20Rican%20Data/Classification_Plots.zip)** - Original Costa Rican data given by Daniel
     - **[Cleaned-Classification-Data.csv](/CostaRica-Notebook/Costa%20Rican%20Data/Cleaned-Classification-Data.csv)** - 'Cleaned-up' version of original dataset (not completely clean)
     - **[DanV1-Classification-Data.csv](/CostaRica-Notebook/Costa%20Rican%20Data/DanV1-Classification-Data.csv)** Dataset after acquisition from GEE (uncleaned)


2. **ShawneeNF Directory** - Stores John's Shawnee National Forest notebook
   - **[ShawneeNF_TCC.ipynb](/ShawneeNF/ShawneeNF_TCC.ipynb)** - Discusses how to "build a simple random sample of point locations, extract remotely sensed data for those locations, and use that data to estimate % Tree Cover for the Shawnee National Forest."
  
3. **Geopipeline Directory** - Stores the final, all-in-one, parent notebook along with its required data files, etc.
   - **[geo_pipeline.ipynb](GeoPipeline/geo_pipeline.ipynb)** - This is the parent notebook that begins from importing the Costa Rican data and ending at generating a GEE visualization

> Note: There are three other directories in the`CostaRica Notebook Directory`for each section's team:
> 1. `Data Acquisition Team`
> 2. `Modeling Team`
> 3. `Visualization and Maps Team`
> 
> All of these have a directory called`Independent Notebooks`for independent testing by specific individuals.
> 
> **Important:** They all also contain their own version of a blank parent notebook ([DanV2_Pipeline.ipynb](/CostaRica-Notebook/DanV2_Pipeline.ipynb)), so
> one team is not interfering with another. There's probably a better way to do this, but this'll work for now.



