
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
#import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
from scipy.constants import gas_constant as rgas
import numpy as np
from matplotlib.patches import Rectangle ## to add symbol of case study
import matplotlib.cm as cm
import matplotlib as mpl
#plt.rcParams["font.family"] = "sans-serif"
import matplotlib
from matplotlib.colors import BoundaryNorm
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import geopandas as gpd
#import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import metpy.calc as mpcalc
import warnings
import geocat.viz as gv
import cmaps
import warnings
warnings.filterwarnings("ignore")

EXTENT = [-16,10,3,14]


CoastFlag = False

IncMjor, IncMnor = 2, 1
mapcrs = ccrs.PlateCarree()

# Set up the projection of the data; if lat/lon then PlateCarree is what you want
datacrs = ccrs.PlateCarree()

EXTENT = [-16,10,3,14]


plt.rcParams["font.family"] = "ubuntu"
warnings.filterwarnings("ignore")



#### 12Z

efi_fc14_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-14_12UTC.nc')
efi_fc15_12 = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-15_12UTC.nc')
efi_fc16_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-16_12UTC.nc')
efi_fc17_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-17_12UTC.nc')
efi_fc18_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-18_12UTC.nc')
efi_fc19_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/efi_12UTC/efi_2018-06-19_12UTC.nc')


sot_14_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-14_12UTC.nc')
sot_15_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-15_12UTC.nc')
sot_16_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-16_12UTC.nc')
sot_17_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-17_12UTC.nc')
sot_18_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-18_12UTC.nc')
sot_19_12  = xr.open_dataset(r'/home/salifou/Documents/Passport/REVISON/sot/sot_2018-06-19_12UTC.nc')


def add_axes(grid_space, fig):
    
    ax = fig.add_subplot(grid_space,
                         projection=ccrs.PlateCarree())
    ax.set_extent([-16,14,3,15], crs=ccrs.PlateCarree())

    # Usa geocat.viz.util convenience function to set axes parameters
    gv.set_axes_limits_and_ticks(ax,
                                 ylim=(3, 15),
                                 xticks=np.arange(-16, 14, 4),
                                 yticks=np.arange(3, 19, 4))

    # Use geocat.viz.util convenience function to make plots look like NCL
    # plots by using latitude, longitude tick labels
    gv.add_lat_lon_ticklabels(ax)
    # Remove the degree symbol from tick labels
    ax.yaxis.set_major_formatter(LatitudeFormatter(degree_symbol=''))
    ax.xaxis.set_major_formatter(LongitudeFormatter(degree_symbol=''))

    # Use geocat.viz.util convenience function to add minor and major tick lines
    gv.add_major_minor_ticks(ax,  labelsize=6)

    # Make sure that tick marks are only on the left and bottom sides of subplot
    ax.tick_params('both', direction = 'in', which='both', top=False, right=False, width=0.5, length = 3.5)
    ax.minorticks_off()
    # Add land to the subplot
    ax.add_feature(cfeature.BORDERS,
                   facecolor='gray',
                   edgecolor='gray',
                   linewidths=1.5,
                   zorder=3)
    ax.add_feature(cfeature.COASTLINE,
                   facecolor='k',
                   edgecolor='gray',
                   linewidths=1.1,
                   zorder=3)
    ax.scatter(-3.97,5.34, marker="*", s = 40, c= 'm', zorder = 100)

    # # Set subplot titles
    # gv.set_titles_and_labels(ax,
    #                          lefttitle='GPM_3IMERGDF_V07',
    #                          lefttitlefontsize=10,
    #                          righttitle=convert_date(date),
    #                          righttitlefontsize=10)
    #ax.set_title(convert_date(date), loc= 'right', fontsize=12, y=1.05, x = 0.5, fontweight = 'bold')

    return ax
    
    
import numpy as np
from matplotlib import colors

# --- Ta palette de 31 couleurs (inchangée) ---
PRECIP_COLORS = [
    (0.85, 0.92, 1.0, 1.0),  # bleu très clair
    (0.70, 0.85, 1.0, 1.0),
    (0.55, 0.78, 1.0, 1.0),
    (0.40, 0.70, 1.0, 1.0),
    (0.25, 0.62, 1.0, 1.0),
    (0.10, 0.55, 1.0, 1.0),
    (0.0, 0.45, 0.9, 1.0),
    (0.0, 0.35, 0.8, 1.0),
    (0.0, 0.25, 0.7, 1.0),
    (0.0, 0.15, 0.6, 1.0),
    (0.0, 0.6, 0.4, 1.0),
    (0.2, 0.7, 0.2, 1.0),
    (0.5, 0.8, 0.1, 1.0),
    (0.8, 0.9, 0.0, 1.0),
    (0.95, 0.85, 0.0, 1.0),
    (1.0, 0.75, 0.0, 1.0),
    (1.0, 0.6, 0.0, 1.0),
    (1.0, 0.4, 0.0, 1.0),
    (1.0, 0.2, 0.0, 1.0),
    (0.9, 0.0, 0.0, 1.0),
    (0.9, 0.2, 0.4, 1.0),
    (0.9, 0.4, 0.6, 1.0),
    (0.95, 0.6, 0.8, 1.0),
    (0.98, 0.7, 0.9, 1.0),
    (1.0, 0.8, 1.0, 1.0),
    (0.9, 0.7, 1.0, 1.0),
    (0.8, 0.6, 1.0, 1.0),
    (0.7, 0.5, 1.0, 1.0),
    (0.6, 0.4, 1.0, 1.0),
    (0.5, 0.3, 1.0, 1.0),
    (0.4, 0.2, 1.0, 1.0)     # violet foncé
]

# --- Niveaux pour plage [0, 1] ---
PRECIP_LEVELS = np.linspace(0, 1, len(PRECIP_COLORS) + 1)  # 32 niveaux → 31 intervalles

# --- Création de la colormap et normalisation ---
PRECIP_CMAP = colors.ListedColormap(PRECIP_COLORS)

PRECIP_NORM = colors.BoundaryNorm(PRECIP_LEVELS, ncolors=PRECIP_CMAP.N)

# --- Ticks optionnels pour colorbar (ex: tous les 0.1) ---
PRECIP_CBTIX = np.round(np.linspace(0, 1, 11), 2)


plt.rcParams['text.usetex'] = True
from matplotlib import gridspec
fig = plt.figure(figsize=(10, 10), dpi=250)
gs = gridspec.GridSpec(nrows=2, ncols=2, wspace=0.1, hspace=-0.55)

d = 2
# 12Z
ax1 =  add_axes(gs[0,0], fig)
ax5 =  add_axes(gs[0,1], fig)
ax7 =  add_axes(gs[1,0], fig)
ax9 =  add_axes(gs[1,1], fig)



ax1.set_title(r'a) \textbf{D-5}', loc= 'left', fontsize = 12)
ax1.set_title(r'\textbf{Initialized 14-06-2018-12Z}', loc= 'center', fontsize = 12)



ax5.set_title(r'b) \textbf{D-3}', loc= 'left', fontsize = 12)
ax5.set_title(r'\textbf{Initialized 16-06-2018-12Z}', loc= 'center', fontsize = 12)



ax7.set_title(r'c) \textbf{D-2}', loc= 'left', fontsize = 12)
ax7.set_title(r'\textbf{Initialized 17-06-2018-12Z}', loc= 'center', fontsize = 12)



ax9.set_title(r'd) \textbf{D-1}', loc= 'left', fontsize = 12)
ax9.set_title(r'\textbf{Initialized 18-06-2018-12Z}', loc= 'center', fontsize = 12)

lon = efi_fc14.longitude.values
lat = efi_fc14.latitude.values
Cmap = PRECIP_CMAP # cmaps.WhBlGrYeRe
Cmap.set_under('white')


#### INTIATION 12Z

cl = ax1.pcolormesh(lon[::d], lat[::d], efi_fc14_12.tpi[4,:,:][::d,::d].values, cmap=Cmap,vmax=1, vmin = 0 )
ax5.pcolormesh(lon[::d], lat[::d], efi_fc16_12.tpi[2,:,:][::d,::d].values, cmap=Cmap, vmax=1, vmin = 0)
ax7.pcolormesh(efi_fc17_12.longitude[::d], efi_fc17_12.latitude[::d], efi_fc17_12.tpi[1,:,:][::d,::d].values, 
               cmap=Cmap, vmax=1, vmin = 0)

ax9.pcolormesh(lon[::d], lat[::d], efi_fc18_12.tpi[0,:,:][::d, ::d].values, cmap=Cmap,vmax=1, vmin = 0 )

ax1.contour(sot_14.longitude, sot_14.latitude, sot_14_12.tpi[4,:,:].values, levels = np.arange(0.1,8), colors = 'k', linewidths = 1.5)

ax5.contour(sot_14.longitude, sot_14.latitude, sot_16_12.tpi[2,:,:].values, levels = np.arange(0.1,8), colors = "k", linewidths = 1.5) 
ax7.contour(sot_14.longitude, sot_14.latitude, sot_17_12.tpi[1,:,:].values, levels = np.arange(0.1,8), colors = "k", linewidths = 1.5)
ax9.contour(sot_14.longitude, sot_14.latitude, sot_18_12.tpi[0,:,:].values, levels = np.arange(0.1,8), colors = "k",  linewidths = 1.5)



clb = fig.colorbar(cl,
                 ax=[ax1, ax5, ax7, ax9 ]
                 ,ticks=np.arange(0, 1.01, 0.1),
                 drawedges=False,aspect = 35,
                 orientation='horizontal',
                 shrink=1,
                 pad=0.03,
                 spacing='uniform',
                 extendfrac=None,
                 extendrect=True) #


gv.add_major_minor_ticks(ax1, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
ax1.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
ax1.tick_params(axis='both', which='major', length=3.9, left=True, right=True)

gv.add_major_minor_ticks(ax5, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
ax5.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
ax5.tick_params(axis='both', which='major', length=3.9, left=True, right=True)

gv.add_major_minor_ticks(ax7, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
ax7.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
ax7.tick_params(axis='both', which='major', length=3.9, left=True, right=True)


gv.add_major_minor_ticks(ax9, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
ax9.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
ax9.tick_params(axis='both', which='major', length=3.9, left=True, right=True)

ax1.scatter(-3.97, 5.34, marker="*", s=100, c='w', edgecolors='k', zorder=100)
ax5.scatter(-3.97, 5.34, marker="*", s=100, c='w', edgecolors='k', zorder=100)
ax7.scatter(-3.97, 5.34, marker="*", s=100, c='w', edgecolors='k', zorder=100)
ax9.scatter(-3.97, 5.34, marker="*", s=100, c='w', edgecolors='k', zorder=100)


# gv.add_major_minor_ticks(ax4, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
# ax4.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
# ax4.tick_params(axis='both', which='major', length=3.9, left=True, right=True)


# gv.add_major_minor_ticks(ax5, x_minor_per_major=8, y_minor_per_major=4, labelsize=6)
# ax5.tick_params(axis='both', which='minor', length=2.9, left=True, right=True)
# ax5.tick_params(axis='both', which='major', length=3.9, left=True, right=True)

plt.suptitle('Target : 2018-06-19 0000UTC',y= 0.65, fontsize=14)

#clb1.ax.tick_params(axis = 'both', direction = 'in', labelsize = 12, length = 2, width= 0.9)
clb.ax.tick_params(axis = 'both', direction = 'in', labelsize = 12, length = 2, width= 0.9)

clb.set_label('EFI', fontsize = 12.)
#clb1.set_label('SOT', fontsize = 12.)

#plt.savefig('/home/salifou/Documents/Passport/REVISON/EFI_Figure_13.png', bbox_inches="tight", dpi=600)

  

