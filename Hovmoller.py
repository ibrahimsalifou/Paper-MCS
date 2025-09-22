from matplotlib import gridspec
plt.rcParams['text.usetex'] = True


vtimes = LLWS_event.time.values.astype('datetime64[m]')#.astype('O')
lons = LLWS_event.longitude.values




fig = plt.figure(figsize=(10, 8), dpi=300)
gs = gridspec.GridSpec(nrows=1, ncols=2, wspace = 0.1, hspace=0.04)



##############################################################################################################################
ax = fig.add_subplot(gs[0,0])
ax.invert_yaxis()
levels = np.arange(0,30, 5)

dd=2
d=2

rv = ax.pcolormesh(lons[::d], vtimes[::d], LLWS_event[::d,::d],   cmap=cmaps.BlRe,  vmin = 0, vmax =35)

ax.tick_params(axis = 'x', labelsize = 10.)
ax.tick_params(axis = 'x', direction= 'in', labelsize = 6.)
lon_formatter = LongitudeFormatter(zero_direction_label = True)
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks(np.arange(-18., 14+ 2, 6))
ax.tick_params(axis='both', direction = 'out', which = 'major', length = 2.)
ax.set_yticks(vtimes[0::4])
ax.set_yticklabels(vtimes[0::4], fontsize = 8)

ax.axhline(y=specific_date_num1, color='k', linestyle='--', linewidth=1)
ax.axhline(y=specific_date_num2, color='k', linestyle='--', linewidth=1) 

ax.axvline(x = -5.75, color = "k", ls='--', lw=1)
ax.axvline(x = -3.47, color = "k", ls='--', lw=1)

ax.set_title(r' \textbf{a) LLWS}', loc= 'left', fontsize = 12)
cbar = plt.colorbar(rv, orientation='horizontal', fraction = 0.2, pad=0.05, aspect=30, extendrect=False)
cbar.set_label('$LLWS$ $~$ $[{m. s^{-1}}]$', fontsize = 10)
cbar.ax.tick_params(labelsize=15)
cbar.ax.tick_params(axis = 'both', direction = 'in', labelsize = 10., length = 4.5, width = 0.5)
ax.set_box_aspect(1)
####################################################################################################################################################

ax = fig.add_subplot(gs[0,1])
ax.invert_yaxis() 

rv = ax.pcolormesh(lons[::dd], vtimes[::dd], Percentile_LLWS[::dd,::dd],   cmap=cmaps.WhBlGrYeRe,  vmin = 0, vmax =100)

ax.tick_params(axis = 'x', labelsize = 10.)
ax.tick_params(axis = 'x', direction= 'in', labelsize = 6.)
lon_formatter = LongitudeFormatter(zero_direction_label = True)
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks(np.arange(-18., 14+ 2, 6))
ax.tick_params(axis='both', direction = 'out', which = 'major', length = 2.)
ax.set_yticks(vtimes[0::4])
ax.set_yticklabels(vtimes[0::4], fontsize = 8)
ax.set_yticklabels([])
ax.axhline(y=specific_date_num1, color='k', linestyle='--', linewidth=1)
ax.axhline(y=specific_date_num2, color='k', linestyle='--', linewidth=1) 

ax.axvline(x = -5.75, color = "k", ls='--', lw=1)
ax.axvline(x = -3.47, color = "k", ls='--', lw=1)
ax.set_title(r' \textbf{b) LLWS percentile}', loc= 'left', fontsize = 12)
cbar = plt.colorbar(rv, orientation='horizontal', fraction = 0.2, pad=0.05, aspect=30, extendrect=False, )
cbar.set_label('$Percentile$', fontsize = 10)
cbar.ax.tick_params(labelsize=15)
cbar.ax.tick_params(axis = 'both', direction = 'in', labelsize = 10., length = 4.5, width = 0.5)
# ax.set_yticks(vtimes[0::4])
# ax.set_yticklabels(vtimes[0::4], fontsize = 8)
ax.set_box_aspect(1)

#plt.savefig('/home/salifou/Documents/Passport/REVISON/LLWS_percentile_suppl.png', bbox_inches="tight", dpi=600)
# plt.savefig('/home/salifou/Documents/Passport/REVISON/LLWS_percentile_suppl.pdf', bbox_inches="tight", dpi=600)

