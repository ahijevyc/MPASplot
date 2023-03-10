import datetime
from fieldinfo import fieldinfo,readNCLcm
import numpy as np

# fieldinfo should have been imported from fieldinfo module.
# Copy fieldinfo dictionary for MPAS. Change some fnames.
fieldinfo['precip']['fname'] = ['rainnc']
fieldinfo['precipacc']['fname'] = ['rainnc']
fieldinfo['sbcape']['fname'] = ['sbcape']
fieldinfo['mlcape']['fname'] = ['mlcape']
fieldinfo['mucape']['fname'] = ['cape']
fieldinfo['sbcinh']['fname'] = ['sbcin']
fieldinfo['mlcinh']['fname'] = ['mlcin']
fieldinfo['pwat']['fname'] = ['precipw']
fieldinfo['mslp']['fname'] = ['mslp']
fieldinfo['td2']['fname'] = ['surface_dewpoint']
fieldinfo['td2depart']['fname'] = ['surface_dewpoint']
fieldinfo['pblh']['fname'] = ['hpbl']
fieldinfo['hmuh']['fname'] = ['updraft_helicity_max']
fieldinfo['hmuh03']['fname'] = ['updraft_helicity_max03']
fieldinfo['hmuh01']['fname'] = ['updraft_helicity_max01']
fieldinfo['rvort1']['fname'] = ['rvort1_max']
fieldinfo['hmup']['fname'] = ['w_velocity_max']
fieldinfo['hmdn']['fname'] = ['w_velocity_min']
fieldinfo['hmwind']['fname'] = ['wind_speed_level1_max']
fieldinfo['hmgrp']['fname'] = ['grpl_max']
fieldinfo['cref']['fname'] = ['refl10cm_max']
fieldinfo['ref1km']['fname'] = ['refl10cm_1km']
for ztop in ['3','1']:
    fieldinfo['srh'+ztop]['fname'] = ['srh_0_'+ztop+'km']
for ztop in ['6','1']:
    fieldinfo['shr0'+ztop+'mag']['fname'] = ['uzonal_'+ztop+'km', 'umeridional_'+ztop+'km', 'uzonal_surface', 'umeridional_surface']
fieldinfo['zlfc']['fname'] = ['lfc']
fieldinfo['zlcl']['fname'] = ['lcl']
for plev in ['200', '250','300','500','700','850','925']:
    fieldinfo['hgt'+plev]['fname'] = ['height_'+plev+'hPa']
    fieldinfo['speed'+plev]['fname'] = ['uzonal_'+plev+'hPa','umeridional_'+plev+'hPa']
    fieldinfo['temp'+plev]['fname'] = ['temperature_'+plev+'hPa']
for plev in ['500', '700', '850']:
    fieldinfo['td'+plev]['fname'] = ['dewpoint_'+plev+'hPa']
    fieldinfo['vort'+plev] = {'levels' : np.array([0,9,12,15,18,21,24,27,30,33])*1e-5, 'cmap': readNCLcm('prcp_1'), 'fname': ['vorticity_'+plev+'hPa']}
fieldinfo['vortpv']        = {'levels' : [0,9,12,15,18,21,24,27,30,33], 'cmap': readNCLcm('prcp_1'), 'fname': ['vort_pv']}
for plev in ['300', '500', '700', '850', '925']:
    fieldinfo['rh'+plev]['fname'] = ['relhum_'+plev+'hPa']
fieldinfo['speed10m']['fname'] = ['u10', 'v10']
fieldinfo['speed10m-tc']['fname'] = ['u10','v10']
fieldinfo['stp']['fname'] = ['sbcape','lcl','srh_0_1km','uzonal_6km','umeridional_6km','uzonal_surface','umeridional_surface']
fieldinfo['crefuh']['fname'] = ['refl10cm_max', 'updraft_helicity_max']
fieldinfo['wind10m']['fname'] = ['u10','v10']
fieldinfo['shr06']  =  { 'fname'  : ['uzonal_6km','umeridional_6km','uzonal_surface','umeridional_surface'] }
fieldinfo['shr01']  =  { 'fname'  : ['uzonal_1km','umeridional_1km','uzonal_surface','umeridional_surface'] }

# Enter wind barb info for list of pressure levels
for plev in ['200', '250', '300', '500', '700', '850', '925']:
    fieldinfo['wind'+plev] = { 'fname' : ['uzonal_'+plev+'hPa', 'umeridional_'+plev+'hPa'] }
