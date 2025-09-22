
from netCDF4 import Dataset
import xarray as xr
import os
import matplotlib
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request
import zipfile 
import matplotlib.patches as mpatches
#import contextily as cx
#import plotly.express as px
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
import geocat.viz as gv
import warnings
warnings.filterwarnings("ignore")

os.chdir('/media/salifou/Transcend/Working_directory')

contries_path = r'commune _events_cas.csv' # commune _events_cas.csv
df = pd.read_csv(contries_path, sep = ',')
### using geopandas to convert long and lat to points
df_geo = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(
   df.longitude, df.latitude))


contries_path = r'commune _events _evidence.csv' # commune _events_cas.csv
df = pd.read_csv(contries_path, sep = ',')
### using geopandas to convert long and lat to points
df_geo_e = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(
   df.longitude, df.latitude))

df_geo['coords'] = df_geo['geometry'].apply(lambda x: x.representative_point().coords[:])
df_geo['coords'] = [coords[0] for coords in df_geo['coords']]

df_geo_e['coords'] = df_geo_e['geometry'].apply(lambda x: x.representative_point().coords[:])
df_geo_e['coords'] = [coords[0] for coords in df_geo_e['coords']]



plt.rcParams['text.usetex'] = True
fig, ax = plt.subplots(1, figsize = (8,6), dpi=200)
#fig.subplots_adjust(hspace = 0.25)

plt.rcParams['axes.linewidth'] = 1.1
plt.rcParams.update({'font.size': 12})
#plt.rcParams["font.family"] = "ubuntu"


Img_Xsize, Img_Ysize = 1., 1.
IncMjor, IncMnor = 4,4
crs = ccrs.PlateCarree()
ax.tick_params(axis = 'both', labelsize = 8.)
ax.tick_params(axis='both', direction = 'in', which = 'major', length = 4., width = 1.)
ax.tick_params(axis='both', direction = 'in', which = 'minor', length = 7.)
ax.xaxis.grid(which = "major", color='None', linestyle='--', linewidth = 2., alpha = 0.4)
ax.yaxis.grid(which = "major", color='None', linestyle='--', linewidth = 2., alpha = 0.4)

lon_formatter = LongitudeFormatter(zero_direction_label = True)
ax.xaxis.set_major_formatter(lon_formatter)
ax.xaxis.set_major_formatter(lon_formatter)

lat_formatter = LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

gv.add_lat_lon_ticklabels(ax)
gv.add_major_minor_ticks(ax, labelsize=10)
ax.yaxis.set_major_formatter(LatitudeFormatter(degree_symbol=''))
ax.xaxis.set_major_formatter(LongitudeFormatter(degree_symbol=''))

Cmap = cmaps.BlAqGrYeOrRe
Cmap.set_under('white')


ax.set_xticks(np.arange(-5., 5., 0.2))
ax.set_yticks(np.arange(5., 6, 0.1))

path = '/media/salifou/Transcend/Map_creation/final_map.shp'
gdf = gpd.read_file(path)
data = gdf.to_crs(epsg=4326)
#gdf = gdf[gdf.ADM2_FR == "Abidjan"]; gdf
data = gdf.to_crs(epsg=4326)

AA= data
AA.plot(ax= ax, color = 'white', edgecolor = 'black', linewidth=0.9, 
        legend = True)

Ticks  = np.arange(50, 300. + 25., 25.)

legend_kwds = dict(orientation='vertical', label='Precipitation amount [mm]', pad = 0.5, shrink = 1, ticks = Ticks)

from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)

from matplotlib.colors import BoundaryNorm
import matplotlib as mpl


levels = np.linspace(50, 300, 100)

cmap = mpl.cm.get_cmap("jet")
#cmap.set_under('white')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=False)


cax = divider.append_axes("right", size="2%", pad=0.1)

cax.set_ylabel('Precipitation amount [mm]', rotation=90, fontsize = 12)

cax.tick_params(labelsize='10')


df_geo.plot(column = 'cumul',categorical=False ,
            edgecolor = 'black', markersize = 100, vmin= 50, vmax= 300,
            cmap = Cmap, ax= ax , cax= cax,
            legend_kwds = legend_kwds, 
            legend = True)

BB = df_geo_e.plot(column = 'evidence',categorical=False ,
            edgecolor = 'k',marker = 'D', markersize = 100, vmin= 50, vmax= 300,
            cmap = Cmap,ax= ax , cax= cax,
            legend_kwds = legend_kwds, 
            legend = True)

import matplotlib.patheffects as path_effects

# Common text style
text_style = {
    'fontsize': 8,
    'color': 'k',
    'fontweight': 'bold',
    'fontstyle': 'italic',
    'family': 'Arial',
    'path_effects': [path_effects.Stroke(linewidth=1.2, foreground='white'), path_effects.Normal()]
}


texts =[ax.text(row.coords[0]+0.001, row.coords[1],fontsize = 6.5, s=row["Commune"], 
                horizontalalignment='left') for idx, row in df_geo_e.iterrows()]

texts =[ax.text(row.coords[0]-0.001, row.coords[1]-0.015,fontsize = 8.5, s=row["cumul"],color = 'b',weight='bold',style='italic',
                horizontalalignment='right') for idx, row in df_geo.iterrows()]

texts =[ax.text(row.coords[0]-0.001, row.coords[1]-0.015,fontsize = 6.5, s=row["evidence"],color = 'b',weight='bold',style='italic',
                horizontalalignment='right') for idx, row in df_geo_e.iterrows()]

texts = [
    ax.text(
        row.coords[0], row.coords[1],
        fontsize=6.5,
        s=row["Commune"],
        color='k',
        horizontalalignment='right',
        fontstyle='italic',
        family='Arial'  # or 'sans-serif', 'monospace', or specific font
    )
    for idx, row in df_geo.iterrows()
]


plt.minorticks_off()

gv.add_major_minor_ticks(ax, x_minor_per_major=5, y_minor_per_major=4, labelsize=12)
ax.tick_params(axis='both', which='both', length=3.9, left=True, right=True)


# plt.savefig("/home/salifou/Documents/Passport/REVISON/Figure_2.png",bbox_inches="tight", dpi=600)
# plt.savefig("/home/salifou/Documents/Passport/REVISON/Figure_2.pdf",bbox_inches="tight", dpi=600)

plt.show()
