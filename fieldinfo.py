from collections import defaultdict
import os # for NCARG_ROOT
import numpy as np

def readcm(name):
    '''Read colormap from file formatted as 0-1 RGB CSV'''
    fh = open(name, 'r')
    rgb = np.loadtxt(fh)
    fh.close()
    return rgb.tolist()

def readNCLcm(name):
    '''Read in NCL colormap for use in matplotlib
       Replaces original function in /glade/u/home/wrfrt/wwe/python_scripts/fieldinfo.py
    '''

    # comments start with ; or #
    # first real line is ncolors = 256 (or something like that)
    # The rest is bunch of rgb values, one trio per line.

    fh = open(os.getenv('NCARG_ROOT')+'lib/ncarg/colormaps/%s.rgb'%name, 'r')
    rgb = np.loadtxt(fh, comments=[';', '#', 'n']) # treat ncolors=x as a comment (cause it starts with `n`)
    fh.close()
    if rgb.max() > 1:
        rgb = rgb/255.0
    return rgb.tolist()


fieldinfo = defaultdict(dict)

fieldinfo.update({
  # surface and convection-related entries
  'precip'       :{ 'levels' : [0,0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.75,1,1.5,2,2.5,3.0], 'cmap': [readNCLcm('precip2_17lev')[i] for i in (0,1,2,4,5,6,7,8,10,12,13,14,15)], 'fname':['rainnc'] },
  'precip-24hr'  :{ 'levels' : [0,0.01,0.05,0.1,0.25,0.5,0.75,1.0,1.25,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12,13], 'cmap': [readNCLcm('precip2_17lev')[i] for i in (0,1,2,4,5,6,7,8,10,12,13,14,15,16,17)]+['#777777', '#AAAAAA', '#CCCCCC', '#EEEEEE']+[readNCLcm('sunshine_diff_12lev')[i] for i in (4,2,1)], 'fname':['rainnc'] },
  'precip-48hr'  :{ 'levels' : [0,0.05,0.1,0.25,0.5,0.75,1.0,1.25,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,15.0,20,25], 'cmap': [readNCLcm('precip2_17lev')[i] for i in (0,1,2,4,5,6,7,8,10,12,13,14,15,16,17)]+['#777777', '#AAAAAA', '#CCCCCC', '#EEEEEE']+[readNCLcm('sunshine_diff_12lev')[i] for i in (4,2,1)], 'fname':['rainnc'] },
  'precipacc'    :{ 'levels' : [0,0.01,0.05,0.1,0.25,0.5,0.75,1.0,1.25,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0], 'cmap': [readNCLcm('precip2_17lev')[i] for i in (0,1,2,4,5,6,7,8,10,12,13,14,15,16,17)]+['#777777', '#AAAAAA', '#CCCCCC', '#EEEEEE']+[readNCLcm('sunshine_diff_12lev')[i] for i in (4,2,1)], 'fname':['rainnc'] },
  'sbcape'       :{ 'levels' : [100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000],
                    'cmap'   : ['#eeeeee', '#dddddd', '#cccccc', '#aaaaaa']+readNCLcm('precip2_17lev')[3:-1], 'fname': ['sbcape'] },
  'mlcape'       :{ 'levels' : [100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000],
                    'cmap'   : ['#eeeeee', '#dddddd', '#cccccc', '#aaaaaa']+readNCLcm('precip2_17lev')[3:-1], 'fname': ['mlcape'] },
  'mucape'       :{ 'levels' : [10,25,50,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000],
                    'cmap'   : ['#eeeeee', '#dddddd', '#cccccc', '#aaaaaa']+readNCLcm('precip2_17lev')[3:-1], 'fname': ['cape'] },
  'sbcinh'       :{ 'levels' : [50,75,100,150,200,250,500], 'cmap': readNCLcm('topo_15lev')[1:], 'fname': ['sbcin'] },
  'mlcinh'       :{ 'levels' : [50,75,100,150,200,250,500], 'cmap': readNCLcm('topo_15lev')[1:], 'fname': ['mlcin'] },
  'pwat'         :{ 'levels' : [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.5,3.0,3.5,4.0],
                    'cmap'   : ['#dddddd', '#cccccc', '#e1e1d3', '#e1d5b1', '#ffffd5', '#e5ffa7', '#addd8e', '#41ab5d', '#007837', '#005529', '#0029b1'],
                    'fname'  : ['precipw']},
  't2'           :{ 'levels' : range(-35,125,5), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['t2m'] },
  't2depart'     :{ 'levels' : range(-35,125,5), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['t2m'] },
  't2-0c'        :{ 'levels' : [32], 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['t2m'] },
  'mslp'         :{ 'levels' : range(960,1056,4), 'cmap':readNCLcm('nice_gfdl')[3:193], 'fname':['mslp'] },
  'td2'          :{ 'levels' : [-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,64,68,72,76,80,84],
                    'cmap':['#ad598a', '#c589ac','#dcb8cd','#e7cfd1','#d0a0a4','#ad5960', '#8b131d', '#8b4513','#ad7c59', '#c5a289','#dcc7b8','#eeeeee', '#dddddd', '#bbbbbb', '#e1e1d3', '#e1d5b1','#ccb77a','#ffffe5','#f7fcb9', '#addd8e', '#41ab5d', '#006837', '#004529', '#195257', '#4c787c'],
                    'fname'  : ['dewpoint_surface']},
  'td2depart'    :{ 'levels' : [20,25,30,35,40,45,50,55,60,64,68,72,76,80,84], 'cmap'   : ['#eeeeee', '#dddddd', '#bbbbbb', '#e1e1d3', '#e1d5b1','#ccb77a','#ffffe5','#f7fcb9', '#addd8e', '#41ab5d', '#006837', '#004529', '#195257', '#4c787c'],
                    'fname'  : ['dewpoint_surface']},
  'thetae'       :{  'levels' : range(300,365,5), 'cmap': ['#eeeeee', '#dddddd', '#cccccc', '#aaaaaa']+readNCLcm('precip2_17lev')[3:-1], 'fname'  : ['t2m', 'q2', 'surface_pressure']},
  'thetapv'      :{  'levels' : np.arange(278,386,4), 'cmap': readNCLcm('WhiteBlueGreenYellowRed'), 'fname'  : ['theta_pv']},
  'rh2m'         :{  'levels' : range(0,110,10), 'cmap': readNCLcm('precip2_17lev')[:17][::-1], 'fname': ['t2m', 'surface_pressure', 'q2']},
  'pblh'         :{ 'levels' : [0,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000],
      'cmap': ['#eeeeee', '#dddddd', '#cccccc', '#bbbbbb', '#44aaee','#88bbff', '#aaccff', '#bbddff', '#efd6c1', '#e5c1a1', '#eebb32', '#bb9918'], 'fname': ['hpbl']},
  'hmuh'         :{ 'levels' : [10,25,50,75,100,125,150,175,200,250,300,400,500], 'cmap': readNCLcm('prcp_1')[1:15], 'fname': ['updraft_helicity_max']},
  'hmneguh'      :{ 'levels' : [10,25,50,75,100,125,150,175,200,250,300,400,500], 'cmap': readNCLcm('prcp_1')[1:15], 'fname': ['UP_HELI_MIN']},
  'hmuh03'       :{ 'levels' : [10,25,50,75,100,125,150,175,200,250,300,400,500], 'cmap': readNCLcm('prcp_1')[1:15], 'fname': ['updraft_helicity_max03']},
  'hmuh01'       :{ 'levels' : [5,10,25,50,75,100,125,150,175,200,250,300,400,500], 'cmap': readNCLcm('prcp_1')[1:15], 'fname': ['updraft_helicity_max01']},
  'rvort1'       :{ 'levels' : [0.005,0.006,0.007,0.008,0.009,0.01,0.011,0.012,0.013,0.014,0.015], 'cmap': readNCLcm('prcp_1')[1:15], 'fname': ['rvort1_max']},
  'sspf'         :{ 'levels' : [10,25,50,75,100,125,150,175,200,250,300,400,500], 'cmap': readNCLcm('prcp_1')[:15], 'fname': ['updraft_helicity_max','WSPD10MAX','HAIL_MAXK1']},
  'hmup'         :{ 'levels' : [4,6,8,10,12,14,16,18,20,24,28,32,36,40,44,48], 'cmap': readNCLcm('prcp_1')[1:16], 'fname': ['w_velocity_max'] },
  'hmdn'         :{ 'levels' : [2,3,4,6,8,10,12,14,16,18,20,22,24,26,28,30], 'cmap': readNCLcm('prcp_1')[1:16], 'fname': ['w_velocity_min'] },
  'hmwind'       :{ 'levels' : range(10,44,2), 'cmap': readNCLcm('prcp_1')[:16], 'fname': ['wind_speed_level1_max'] },
  'hmgrp'        :{ 'levels' : [0.01,0.1,0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,4.0,5.0], 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['graupelnc'] },
  'cref'         :{ 'levels' : range(5,75,5), 'cmap': readcm('/glade/u/home/sobash/RT2015_gpx/cmap_rad.rgb')[1:14], 'fname': ['refl10cm_max'] },
  'crefuh'       :{ 'levels' : range(5,75,5), 'cmap': readcm('/glade/u/home/sobash/RT2015_gpx/cmap_rad.rgb')[0:13], 'fname': ['refl10cm_max', 'updraft_helicity_max'] },
  'ref1km'       :{ 'levels' : range(5,75,5), 'cmap': readcm('/glade/u/home/sobash/RT2015_gpx/cmap_rad.rgb')[1:14], 'fname': ['refl10cm_1km'] },
  'srh3'         :{ 'levels' : [50,100,150,200,250,300,400,500], 'cmap': readNCLcm('perc2_9lev'), 'fname': ['srh_0_3km'] },
  'srh1'         :{ 'levels' : [50,100,150,200,250,300,400,500], 'cmap': readNCLcm('perc2_9lev'), 'fname': ['srh_0_1km'] },
  'shr06mag'     :{ 'levels' : range(30,85,5), 'cmap': readNCLcm('perc2_9lev'), 'fname': ['uzonal_6km', 'umeridional_6km', 'uzonal_surface', 'umeridional_surface']},
  'shr01mag'     :{ 'levels' : range(30,85,5), 'cmap': readNCLcm('perc2_9lev'), 'fname': ['uzonal_1km', 'umeridional_1km', 'uzonal_surface', 'umeridional_surface']},
  'zlfc'         :{ 'levels' : [0,250,500,750,1000,1250,1500,2000,2500,3000,3500,4000,5000], 'cmap': [readNCLcm('nice_gfdl')[i] for i in [3,20,37,54,72,89,106,123,141,158,175,193]], 'fname': ['lfc'] },
  'zlcl'         :{ 'levels' : [0,250,500,750,1000,1250,1500,2000,2500,3000,3500,4000,5000], 'cmap': [readNCLcm('nice_gfdl')[i] for i in [3,20,37,54,72,89,106,123,141,158,175,193]], 'fname': ['lcl'] },
  'ltg1'         :{ 'levels' : [0.1,0.5,1,1.5,2,2.5,3,4,5,6,7,8,10,12], 'cmap': readNCLcm('prcp_1')[:15], 'fname': ['LTG1_MAX'] },
  'ltg2'         :{ 'levels' : [0.1,0.5,1,1.5,2,2.5,3,4,5,6,7,8,10,12], 'cmap': readNCLcm('prcp_1')[:15], 'fname': ['LTG2_MAX'] },
  'ltg3'         :{ 'levels' : [0.1,0.5,1,1.5,2,2.5,3,4,5,6,7,8,10,12], 'cmap': readNCLcm('prcp_1')[:15], 'fname': ['LTG3_MAX'] },
  'olrtoa'       :{ 'levels' : range(70,340,10), 'cmap': readcm('/glade/u/home/sobash/RT2015_gpx/cmap_satir.rgb')[32:1:-1], 'fname': ['olrtoa'] },

  # winter fields
  'thck1000-500' :{ 'levels' : [480,486,492,498,504,510,516,522,528,534,540,546,552,558,564,570,576,582,588,592,600], 'cmap':readNCLcm('perc2_9lev'), 'fname':['GHT_PL', 'GHT_PL'], 'arraylevel':[0,5]}, # CSS mod
  'thck1000-850' :{ 'levels' : range(82,163,3), 'cmap':readNCLcm('perc2_9lev'), 'fname':['GHT_PL', 'GHT_PL'], 'arraylevel':[0,2]}, # CSS mod

  # pressure level entries
  'hgt200'       :{ 'levels' : range(10900, 12500, 60), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_200hPa']},
  'hgt250'       :{ 'levels' : range( 9700, 11080, 60), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_250hPa']},
  'hgt300'       :{ 'levels' : range( 8400, 10080, 60), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_300hPa']},
  'hgt500'       :{ 'levels' : range( 4800,  6060, 60), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_500hPa']},
  'hgt700'       :{ 'levels' : range( 2700,  3330, 30), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_700hPa']},
  'hgt850'       :{ 'levels' : range( 1200,  1680, 30), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_850hPa']},
  'hgt925'       :{ 'levels' : range(  550,  1060, 30), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['height_925hPa']},
  'speed200'     :{ 'levels' : range(25, 115, 5), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_200hPa','umeridional_200hPa']},
  'speed250'     :{ 'levels' : range(25, 115, 5), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_250hPa','umeridional_250hPa']},
  'speed300'     :{ 'levels' : range(25, 115, 5), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_300hPa','umeridional_300hPa']},
  'speed500'     :{ 'levels' : range(15, 105, 5), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_500hPa','umeridional_500hPa']},
  'speed700'     :{ 'levels' : range( 5,  90, 5), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_700hPa','umeridional_700hPa']},
  'speed850'     :{ 'levels' : range( 6,  78, 4), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_850hPa','umeridional_850hPa']},
  'speed925'     :{ 'levels' : range( 6,  78, 4), 'cmap': readNCLcm('wind_17lev'), 'fname': ['uzonal_925hPa','umeridional_925hPa']},
  'temp200'      :{ 'levels' : range(-65,-27,2), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_200hPa']},
  'temp250'      :{ 'levels' : range(-65,-27,2), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_250hPa']},
  'temp300'      :{ 'levels' : range(-65,-27,2), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_300hPa']},
  'temp500'      :{ 'levels' : [-41,-39,-37,-35,-33,-31,-29,-26,-23,-20,-17,-14,-11,-8,-5,-2],      'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_500hPa']},
  'temp700'      :{ 'levels' : range(-36,24,3), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_700hPa']},
  'temp850'      :{ 'levels' : range(-30,33,3), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_850hPa']},
  'temp925'      :{ 'levels' : range(-24,36,3), 'cmap': readNCLcm('nice_gfdl')[3:193], 'fname': ['temperature_925hPa']},
  'td500'        :{ 'levels' : range(-30,15,5), 'cmap' : readNCLcm('nice_gfdl')[3:193], 'fname': ['dewpoint_500hPa']},
  'td700'        :{ 'levels' : range(-30,15,5), 'cmap' : readNCLcm('nice_gfdl')[3:193], 'fname': ['dewpoint_700hPa']},
  'td850'        :{ 'levels' : range(-40,35,5), 'cmap' : readNCLcm('nice_gfdl')[3:193], 'fname': ['dewpoint_850hPa']},
  'td925'        :{ 'levels' : range(-30,35,5), 'cmap' : readNCLcm('nice_gfdl')[3:193], 'fname': ['dewpoint_925hPa']},
  'rh300'        :{ 'levels' : range(0,110,10), 'cmap' : [readNCLcm('MPL_PuOr')[i] for i in (2,18,34,50)]+[readNCLcm('MPL_Greens')[j] for j in (2,17,50,75,106,125)], 'fname': ['relhum_300hPa']},
  'rh500'        :{ 'levels' : range(0,110,10), 'cmap' : [readNCLcm('MPL_PuOr')[i] for i in (2,18,34,50)]+[readNCLcm('MPL_Greens')[j] for j in (2,17,50,75,106,125)], 'fname': ['relhum_500hPa']},
  'rh700'        :{ 'levels' : range(0,110,10), 'cmap' : readNCLcm('CBR_drywet'), 'fname': ['relhum_700hPa']},
  'rh850'        :{ 'levels' : range(0,110,10), 'cmap' : readNCLcm('CBR_drywet'), 'fname': ['relhum_850hPa']},
  'rh925'        :{ 'levels' : range(0,110,10), 'cmap' : readNCLcm('CBR_drywet'), 'fname': ['relhum_925hPa']},
  'pvort320k'    :{ 'levels' : [0,0.1,0.2,0.3,0.4,0.5,0.75,1,1.5,2,3,4,5,7,10],
                  'cmap'   : ['#ffffff','#eeeeee','#dddddd','#cccccc','#bbbbbb','#d1c5b1','#e1d5b9','#f1ead3','#003399','#0033FF','#0099FF','#00CCFF','#8866FF','#9933FF','#660099'],
                  'fname': ['PVORT_320K']},
 'speed10m'     :{ 'levels' : range(3, 54,3), 'cmap': readNCLcm('wind_17lev')[1:],'fname' : ['u10', 'v10']},
 'speed10m-tc'  :{ 'levels' : range(6,108,6), 'cmap': readNCLcm('wind_17lev')[1:],'fname' : ['u10', 'v10']},
 'stp'          :{ 'levels' : [0.5,0.75,1.0,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0], 'cmap':readNCLcm('perc2_9lev'), 'fname':['CAPE_221_SFC','CIN_221_SFC','HLCY_221_HTGY'] },
 'uhratio'      :{ 'levels' : [0.1,0.3,0.5,0.7,0.9,1.0,1.1,1.2,1.3,1.4,1.5], 'cmap':readNCLcm('perc2_9lev'), 'fname':['updraft_helicity_max03', 'updraft_helicity_max']},

  # wind barb entries
  'wind10m'      :{ 'fname'  : ['u10', 'v10'], 'skip':50 },
  'windsfc'      :{ 'fname'  : ['uzonal_surface','umeridional_surface'], 'skip':50 },
  'wind1km'      :{ 'fname'  : ['uzonal_1km','umeridional_1km'], 'skip':50 },
  'wind6km'      :{ 'fname'  : ['uzonal_6km','umeridional_6km'], 'skip':50 },
  'windpv'       :{ 'fname'  : ['u_pv','v_pv'],                  'skip':50 },
  'shr06'        :{ 'fname'  : ['uzonal_6km','umeridional_6km','uzonal_surface','umeridional_surface'], 'skip':50 },
  'shr01'        :{ 'fname'  : ['uzonal_1km','umeridional_1km','uzonal_surface','umeridional_surface'], 'skip':50 },
  'bunkers'      :{ 'fname'  : ['U_COMP_STM_6KM', 'V_COMP_STM_6KM'], 'skip':40 },
})

# Enter wind barb info for list of pressure levels
for plev in ['200', '250', '300', '500', '700', '850', '925']:
    fieldinfo['wind'+plev] = { 'fname' : ['uzonal_'+plev+'hPa', 'umeridional_'+plev+'hPa'], 'skip':50}


# Combine levels from RAIN, FZRA, ICE, and SNOW for plotting 1-hr accumulated precip for each type. Ahijevych added this
#fieldinfo['ptypes']['levels'] = [fieldinfo['precip']['levels'][1:],fieldinfo['snow']['levels'],fieldinfo['ice']['levels'],fieldinfo['fzra']['levels']]

# domains = { 'domainname': { 'corners':[ll_lat,ll_lon,ur_lat,ur_lon], 'figsize':[w,h] } }
domains = { 'CONUS' :{ 'corners': [23.1593,-120.811,46.8857,-65.0212], 'fig_width': 1080 },
            'NA'  :{ 'corners': [15.00,-170.00,65.00,-50.00], 'fig_width':1080 },
            'SGP' :{ 'corners': [25.3,-107.00,36.00,-88.70], 'fig_width':1080 },
            'NGP' :{ 'corners': [40.00,-105.0,50.30,-82.00], 'fig_width':1080 },
            'CGP' :{ 'corners': [33.00,-107.50,45.00,-86.60], 'fig_width':1080 },
            'SW'  :{ 'corners': [28.00,-121.50,44.39,-102.10], 'fig_width':1080 },
            'NW'  :{ 'corners': [37.00,-124.40,51.60,-102.10], 'fig_width':1080 },
            'SE'  :{ 'corners': [26.10,-92.75,36.00,-71.00], 'fig_width':1080 },
            'NE'  :{ 'corners': [38.00,-91.00,46.80,-65.30], 'fig_width':1080 },
            'MATL':{ 'corners': [33.50,-92.25,41.50,-68.50], 'fig_width':1080 },
}
