# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:06:12 2016

@author: ptg
"""

import numpy as np

import astropy.constants as acon
c = acon.c.value

dtheta = np.radians( 5. / 60. /60. )  # 5 arcmin -> degrees -> radians

f = 2000e6 # Hz

d = 1.22 * c / ( f * dtheta ) / 1000.

print "Frequency (MHz)"
print f / 1e6

print "Wavelenth (m)"
print c / f

print "Baseline (km)"
print d


