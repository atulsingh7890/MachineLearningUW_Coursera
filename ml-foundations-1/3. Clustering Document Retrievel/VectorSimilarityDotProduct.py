# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 23:30:07 2016

@author: atsingh
"""

import numpy as np

a = np.array([1,3,2,1,2,1,1])

p = np.array([7 ,0 ,2, 1, 0, 0, 1])
q = np.array([1, 7, 0, 0, 2, 0, 1])
r = np.array([1, 0, 0, 0, 7, 1, 2])
s = np.array([0, 2, 0, 0, 7, 1, 1])

print np.dot(a,p),np.dot(a,q),np.dot(a,r),np.dot(a,s)