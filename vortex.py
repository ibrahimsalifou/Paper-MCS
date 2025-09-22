import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import geocat.viz as gv
import cmaps
from matplotlib.colors import LinearSegmentedColormap
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# Définition de la colormap
Cmap = LinearSegmentedColormap.from_list('mycmap', ['blue', 'yellow', 'red'])

# Projection de la carte
mapcrs = ccrs.PlateCarree()

fig = plt.figure(dpi = 200)
ax = plt.subplot(projection=ccrs.PlateCarree())
ax.set_extent([-18,14,3,15], mapcrs)

# Ajout des côtes et des frontières
ax.coastlines(linewidths=0.8)
ax.add_feature(cfeature.BORDERS, linewidths=0.8)

# Sélection de la tranche temporelle
for k in range(0,8):

# Ajout du champ de précipitable water (PW)
    #ctr = ax.contourf(lon.values, lat.values, PW[k, :, :], cmap=Cmap, zorder=0, levels = np.linspace(20,65), transform=ccrs.PlateCarree()) #vmin=20, vmax=60, 
    
    # Vérification des dimensions avant d'afficher les streamlines
    if ERA5_ub.shape[1:] == X.shape and ERA5_vb.shape[1:] == Y.shape:
        ax.streamplot(X, Y, ERA5_ub[k], ERA5_vb[k], 
                      color='k', integration_direction='both', 
                      arrowstyle="->", arrowsize=0.9, density=2, 
                      linewidth=0.5, transform=projection)
    else:
        print("Erreur : les dimensions des champs de vent ne correspondent pas aux coordonnées !")
    
    # Configuration des axes et des labels
    gv.set_axes_limits_and_ticks(ax=ax,
                                 xlim=(-18, 14),
                                 ylim=(3, 15),
                                 xticks=np.arange(-18, 18, 4),
                                 yticks=np.arange(2, 20, 4))
    
    gv.add_lat_lon_ticklabels(ax=ax)
    ax.yaxis.set_major_formatter(LatitudeFormatter(degree_symbol=''))
    ax.xaxis.set_major_formatter(LongitudeFormatter(degree_symbol=''))
    
    # Ajout des ticks mineurs pour plus de précision
    gv.add_major_minor_ticks(ax, labelsize=10)
    #ctr = ax.contourf(lon.values, lat.values, PW[k, :, :], cmap=Cmap, zorder=0, levels = np.linspace(20,65), transform=ccrs.PlateCarree()) #vmin=20, vmax=60, 
    
    # Affichage de la figure
    plt.show()
