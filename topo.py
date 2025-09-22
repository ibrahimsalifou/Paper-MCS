
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmaps
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import geocat.viz as gv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import warnings
warnings.filterwarnings("ignore")
from matplotlib import gridspec
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':30 })
plt.rcParams["font.family"] = "ubuntu"
plt.rcParams['text.usetex'] = True
import matplotlib.patheffects as path_effects
import matplotlib.patches as patches
IncMjor, IncMnor = 5,2
Img_Xsize, Img_Ysize = 10, 20
IncrZnMajr, IncrZnMinr = .1, .05
Domain_Borders = [-4.5, -3.7, 5.2, 5.65]
CoastFlag = False

Borders = [-4.5, -3.7, 5.2, 5.65]
CstFlag = False
EXTENT = [-15,15,3,15]

cmap = cmaps.OceanLakeLandSnow
newcmap = gv.truncate_colormap(cmap=cmap, minval=0.01, maxval=1)

projection = ccrs.PlateCarree()

fig = plt.figure(figsize=(15, 10), dpi=300)
gs = gridspec.GridSpec(nrows=2, ncols=1, wspace=0.2, hspace=0.1)
ax = [fig.add_subplot(gs[i, j], projection=projection) for i in range(2) for j in range(1)]

axes = ax[0]
axins = ax[1]

axes.tick_params('both', direction = 'out', which='both', top=False, right=False, width=0.7, length = 5)
axes.minorticks_off()
axes.tick_params(axis = 'both', labelsize = 12.)
lon_formatter = LongitudeFormatter(zero_direction_label = True)
axes.xaxis.set_major_formatter(lon_formatter)
axes.set_xticks(np.arange(-15., 16. + IncMjor, 5), crs = ccrs.PlateCarree())
lat_formatter = LatitudeFormatter()
axes.yaxis.set_major_formatter(lat_formatter)
axes.add_feature(cfeature.OCEAN, color='w', zorder=0)

axes.set_yticks(np.arange(3., 15. + IncMjor, 4), crs = ccrs.PlateCarree())
if (CoastFlag):
    axes.coastlines(resolution = '50m', facecolor = 'none', linewidth = 0.9, edgecolor = "k")
axes.set_extent(EXTENT)
axes.add_feature(cfeature.BORDERS,facecolor='k',edgecolor='black',linewidths=0.9,zorder=3)
axes.add_feature(cfeature.COASTLINE,facecolor='k',edgecolor='black',linewidths=0.9,zorder=3)


elev = axes.contourf(Lon , Lat, topo, cmap=newcmap, levels = np.linspace(0,2000, 50))

gv.set_titles_and_labels(axes,
                         lefttitle='',
                         righttitle='',
                         maintitle=None,
                         maintitlefontsize=15,
                         xlabel="",
                         ylabel="")


axes.add_feature(cfeature.OCEAN, zorder=0)
axes.add_feature(cfeature.BORDERS, zorder=2)


axins.tick_params('both', direction = 'out', which='both', top=False, right=False, width=0.7, length = 3)
axins.tick_params(axis = 'both', labelsize = 12.)
lon_formatter = LongitudeFormatter(zero_direction_label = True)
axins.xaxis.set_major_formatter(lon_formatter)
axins.yaxis.set_major_formatter(lat_formatter)
axins.set_xticks(np.arange(-4.5, -3.6, 0.2), crs = ccrs.PlateCarree())
axins.set_yticks(np.arange(5.2, 5.65, 0.2), crs = ccrs.PlateCarree())



if (CstFlag):
    axins.coastlines(resolution = '50m', facecolor = 'none', linewidth = 1.5, edgecolor = "k")

axins.set_extent(Borders)


# Ajout des stations
for name, lat, lon in stations:
    axes.plot(lon, lat, marker='o', color='b', markeredgecolor='black', markersize=11, transform=ccrs.PlateCarree())
    if name in ["Tabou", "Sassandra", "Daloa", "Accra", "Lome", "Lagos/Ikeja"]:
        text = axes.text(lon - 0.2, lat, name, color='k', fontsize=14, transform=ccrs.PlateCarree(), ha='right')
        text.set_path_effects([path_effects.Stroke(linewidth=0.8, foreground='k'),
                        path_effects.Normal()])
    else:
        text = axes.text(lon + 0.1, lat - 0.3, name, color='k', fontsize=14, transform=ccrs.PlateCarree())

        text.set_path_effects([path_effects.Stroke(linewidth=0.8, foreground='k'),
                        path_effects.Normal()])



FileShape = "/media/salifou/Transcend/Map_creation/District_Autonome.shp"

#district_communes.shp

ShapeAbj = shapefile.Reader(FileShape.strip())



path = '/media/salifou/Transcend/Map_creation/final_map.shp'
gdf = gpd.read_file(path)
data = gdf.to_crs(epsg=4326)


 
data.plot(ax=axins, alpha = 0.5, facecolor = 'none', lw = 1.3)
gv.add_lat_lon_ticklabels(axins)
gv.add_major_minor_ticks(axins, labelsize=14)

## Sodexam station name
texts =[axins.text(row.coords[0]-0.007, row.coords[1],fontsize = 10.5,color= 'r', zorder = 100, s=row["Station Name"], 
            horizontalalignment='right') for idx, row in df_geos.iterrows()]

## Evidence Station Name
texts =[axins.text(row.coords[0]+0.007, row.coords[1],fontsize = 10.5,color = 'b', zorder = 100, s=row["id"], 
            horizontalalignment='left') for idx, row in df_geoe.iterrows()]



path = '/media/salifou/Transcend/Map_creation/final_map.shp'
gdf = gpd.read_file(path)
data = gdf.to_crs(epsg=4326)

data.plot(ax=axins, alpha = 0.8, facecolor = 'none', lw = 0.5)

axins.tick_params('both', direction = 'out', which='both', top=False, right=False, width=0.7, length = 5)
axins.tick_params(axis = 'both', labelsize = 12.)



cbar = fig.colorbar(elev,
                 ax= [axes],
             ticks=np.linspace(0, 2000,9).astype(int),
             drawedges=False,
             orientation='vertical',
             shrink=1,aspect = 15,
             pad=0.005,
             spacing='uniform',
             extendfrac=None,
             extendrect=True) #



# Box = axes.get_position()
# Cbaxes = fig.add_axes([Box.x1+0.015, Box.y0, Box.width*0.02, Box.height])   
# Cbar = fig.colorbar(elev, ticks = np.arange(0,2000,250), orientation = "vertical",  cax = Cbaxes, pad=0.50,)
cbar.ax.tick_params(axis = 'both', direction = 'out', labelsize = 14., length = 5, width = 1)
cbar.set_label(label = 'Elevation [m]',  fontsize = 15., labelpad=3.)

axes.annotate(
        'a)',
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='18', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

axins.annotate(
        'b)',
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='18', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))



pays = {
    'Guinee': (-10.7, 11),    # Guinée
    "Côte \n d'Ivoire": (-5.54, 7.54),   # Côte d'Ivoire
    'Nigeria': (8.7, 8.5),      # Nigeria
    'Ghana': (-1.02, 7.95),   # Ghana
    'Togo': (0.83, 8.5),     # Togo
    'Benin': (2.32, 10.6),   #Bénin
    'Cameroon': (12, 5.22)  # CMR
}

for initials, coord in pays.items():
    Text = axes.text(
        coord[0], coord[1] + 0.5, initials,
        fontsize=18,
        ha='center',
        color='w',  # Texte noir
        fontweight='bold',  # En gras
        transform=ccrs.PlateCarree(),
        bbox=dict(facecolor='none', alpha=1, edgecolor='none')
    )

    # Contour blanc autour du texte
    Text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='k'),  # Contour blanc
        path_effects.Normal()
    ])

center_lat_vortex, center_lon_vortex = 5.34, -3.97
center_lat_era5, center_lon_era5 = 4.75, -5.25  # 5.25, -5.00

# --- Boîte autour du vortex ---
lon_min_vortex = center_lon_vortex - 0.5
lon_max_vortex = center_lon_vortex + 0.5
lat_min_vortex = center_lat_vortex - 0.5
lat_max_vortex = center_lat_vortex + 0.5

width_vortex = lon_max_vortex - lon_min_vortex
height_vortex = lat_max_vortex - lat_min_vortex

rect_vortex = patches.Rectangle((lon_min_vortex, lat_min_vortex), width_vortex, height_vortex,
                                linewidth=2, edgecolor='m', facecolor='none',
                                transform=projection, zorder=10, label='Vortex box')
axes.add_patch(rect_vortex)

# --- Boîte autour de la cellule ERA5 ---
lon_min_era5 = center_lon_era5 - 0.5
lon_max_era5 = center_lon_era5 + 0.5
lat_min_era5 = center_lat_era5 - 0.5
lat_max_era5 = center_lat_era5 + 0.5



width_era5 = lon_max_era5 - lon_min_era5
height_era5 = lat_max_era5 - lat_min_era5

rect_era5 = patches.Rectangle((lon_min_era5, lat_min_era5), width_era5, height_era5,
                              linewidth=2, edgecolor='orange', facecolor='none',
                              transform=projection, zorder=10, label='ERA5 box')
axes.add_patch(rect_era5)
#plt.savefig("/home/salifou/Documents/Passport/REVISON/Topo1_updated.png",bbox_inches="tight", dpi=1000)
plt.show()

