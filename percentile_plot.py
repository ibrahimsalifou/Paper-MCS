plt.rcParams['text.usetex'] = True
plt.rcParams["font.family"] = "ubuntu"
import matplotlib.patches as patches
from matplotlib import gridspec
fig = plt.figure(figsize=(10, 10), dpi=300)
gs = gridspec.GridSpec(nrows=3, ncols=2, wspace=0.1, hspace=0.05)



# Rainfall
ax0 =  add_axes(gs[0,0], fig)
ax1 =  add_axes(gs[1,0], fig)
ax2 =  add_axes(gs[2,0], fig)

# percentile
ax3 =  add_axes(gs[0,1], fig)
ax4 =  add_axes(gs[1,1], fig)
ax5 =  add_axes(gs[2,1], fig)

ax0.set_title(r'\textbf{a) 18 June 2018}', loc= 'left', fontsize = 12)
ax1.set_title(r'\textbf{c) 19 June 2018}', loc= 'left', fontsize = 12)
ax2.set_title(r'\textbf{e) 18-19 June 2018}', loc= 'left', fontsize = 12)


ax3.set_title(r'\textbf{b) Percentile of 18 June 2018 }', loc= 'left', fontsize = 12)
ax4.set_title(r'\textbf{d) Percentile of 19 June 2018  }', loc= 'left', fontsize = 12)
ax5.set_title(r'\textbf{f) Percentile of 18-19 June 2018 }', loc= 'left', fontsize = 12)

 

# ax8.set_title(r'g) \textbf{D-1}', loc= 'left', fontsize = 8)
# ax8.set_title(r'\textbf{Initialized 18-06-2018-00Z}', loc= 'center', fontsize = 8)

# ax9.set_title(r'h) \textbf{D-1}', loc= 'left', fontsize = 8)
# ax9.set_title(r'\textbf{Initialized 18-06-2018-12Z}', loc= 'center', fontsize = 8)

lon = dd.lon.values
lat = dd.lat.values
Cmap = cmaps.BlAqGrYeOrRe
Cmap.set_under('white')

cmap=cmaps.WhBlGrYeRe

ax0.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())
ax1.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())
ax2.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())
ax3.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())
ax4.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())
ax5.set_extent([-18,14,2,15], crs=ccrs.PlateCarree())

d1819 = dd.precipitation[1,:,:] + dd.precipitation[2,:,:]



d=5
#dd = gpm_daily

Cnt = ax0.pcolormesh(dd.lon[::d], dd.lat[::d], dd.precipitation[1,:,:][::d,::d].T.values, cmap=Cmap, vmin = 5, vmax = 160)
ax1.pcolormesh(dd.lon[::d], dd.lat[::d], dd.precipitation[2,:,:][::d,::d].T.values, cmap=Cmap, vmin = 5, vmax = 160)
ax2.pcolormesh(dd.lon[::d], dd.lat[::d], d1819[::d,::d].T.values, cmap=Cmap, vmin = 5, vmax = 160)


Pct = ax3.pcolormesh(perc.lon[::d], perc.lat[::d], perc.percentile[1,:,:][::d,::d].T, cmap=cmap, vmin = 60, vmax = 100) # 18 June
ax4.pcolormesh(perc.lon[::d], perc.lat[::d], perc.percentile[2,:,:][::d,::d].T.values, cmap=cmap, vmin = 60, vmax = 100) # 19 June
ax5.pcolormesh(perc.lon[::d], perc.lat[::d], perc_2day.percentile[2,:,:][::d,::d].T.values, cmap=cmap, vmin = 60, vmax = 100) # 19 June



center_lat_vortex, center_lon_vortex = 5.34, -3.97

# --- Boîte autour du vortex ---
lon_min_vortex = center_lon_vortex - 0.5
lon_max_vortex = center_lon_vortex + 0.5
lat_min_vortex = center_lat_vortex - 0.5
lat_max_vortex = center_lat_vortex + 0.5

width_vortex = lon_max_vortex - lon_min_vortex
height_vortex = lat_max_vortex - lat_min_vortex

# axes = [ax0,ax1,ax2,ax3,ax4,ax5]
# for i in range(6):
    

#     rect_vortex = patches.Rectangle((lon_min_vortex, lat_min_vortex), width_vortex, height_vortex,
#                                     linewidth=1.2, edgecolor='m', facecolor='none',
#                                     transform=mapcrs, zorder=10, label='Vortex box')
#     axes[i].add_patch(rect_vortex)


# np.arange(0., 150. + 25., 25.)
clb = fig.colorbar(Cnt,
                 ax=[ax0,  ax1,  ax2],
                 ticks=np.arange(5., 150. + 25., 25.),
                 drawedges=False,
                 orientation='horizontal',
                 shrink=1,aspect = 20,
                 pad=0.04,
                 spacing='uniform',
                 extendfrac=None,
                 extendrect=False) #

clb_perc = fig.colorbar(Pct,
                 ax=[ax3,  ax4,  ax5],
                 ticks=np.arange(60, 110,10),
                 drawedges=False,
                 orientation='horizontal',
                 shrink=1,aspect = 20,
                 pad=0.04,
                 spacing='uniform',
                 extendfrac=None,
                 extendrect=True) #


clb.set_label('Precipitation amount'+ ' ' + '$[mm]$', fontsize = 12.)
clb_perc.set_label('Percentile', fontsize = 12.)


ax0.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)
ax1.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)
ax2.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)
ax3.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)
ax4.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)
ax5.scatter(-3.97, 5.34, marker="*", s=40, c='white', edgecolors='k', zorder=100)




gv.add_major_minor_ticks(ax0, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)
gv.add_major_minor_ticks(ax1, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)
gv.add_major_minor_ticks(ax2, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)
gv.add_major_minor_ticks(ax3, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)
gv.add_major_minor_ticks(ax4, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)
gv.add_major_minor_ticks(ax5, x_minor_per_major=4, y_minor_per_major=4, labelsize=8)

ax0.tick_params(axis='both', which='major', length=2.9)  
ax0.tick_params(axis='both', which='minor', length=1.9)
ax1.tick_params(axis='both', which='major', length=2.9)  
ax1.tick_params(axis='both', which='minor', length=1.9)
ax2.tick_params(axis='both', which='major', length=2.9)  
ax2.tick_params(axis='both', which='minor', length=1.9)
ax3.tick_params(axis='both', which='major', length=2.9)  
ax3.tick_params(axis='both', which='minor', length=1.9)
ax4.tick_params(axis='both', which='major', length=2.9)  
ax4.tick_params(axis='both', which='minor', length=1.9)
ax5.tick_params(axis='both', which='major', length=2.9)  
ax5.tick_params(axis='both', which='minor', length=1.9)
# plt.suptitle('Target : 18-06-2018 00UTC',y= 0.92, fontsize=14)

#fig.tight_layout()


# plt.savefig("/home/salifou/Documents/Passport/REVISON/IMERG-version_percentile.png",bbox_inches="tight", dpi=600)
# plt.savefig("/home/salifou/Documents/Passport/REVISON/IMERG-version_percentile.pdf",bbox_inches="tight", dpi=600)

plt.show()
