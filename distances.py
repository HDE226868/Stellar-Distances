#!/usr/bin/env python

import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

ra_1 = '1:44:04'
dec_1 = '-15:56:15'
dist_1 = 11.9

ra_2 = '23:41:55'
dec_2 = '+44:10:39'
dist_2 = 10.3

def coords(ra, dec, dist):
    new_coords = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
    ra, dec = new_coords.ra.radian, new_coords.dec.radian
    
    x = dist*np.cos(dec)*np.cos(ra)
    y = dist*np.cos(dec)*np.sin(ra)
    z = dist*np.sin(dec)
    
    return x, y, z
    
def dist(ra_1, dec_1, dist_1, ra_2, dec_2, dist_2):
    x_1, y_1, z_1 = coords(ra_1, dec_1, dist_1)
    x_2, y_2, z_2 = coords(ra_2, dec_2, dist_2)
    
    separation = np.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2 + (z_2 - z_1)**2)
    
    print('The separation is {} light-years'.format(separation))

dist(ra_1, dec_1, dist_1, ra_2, dec_2, dist_2)
