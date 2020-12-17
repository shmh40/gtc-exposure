# %%
import ee
ee.Authenticate()

#%%

import folium
import geemap as emap
#%%
ee.Initialize()

#%%
collection = ee.ImageCollection("COPERNICUS/S2_SR").filterDate('2018-01-01', '2018-01-02') .filterBounds(ee.Geometry.Point(-122.1, 37.2)).select('NDVI')
# %%
print(collection.getInfo())

print(type(collection))



#%%



