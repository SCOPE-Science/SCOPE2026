#!/usr/bin/env python3
"""Optional independent convex-hull volume check (NumPy and SciPy required).

This script checks finite low-dimensional instances, not the arbitrary-dimensional
geometric proof. The volume is computed from all permuted Weyl-chamber rays.
"""
from math import factorial
from itertools import permutations
from fractions import Fraction
import numpy as np
from scipy.spatial import ConvexHull

count=0
for n in (3,4,5):
    d=n-1
    for s in range(1,n):
        rays=[]
        for perm in permutations(range(n)):
            for j in range(1,n):
                b=np.full(n,-j/n)
                b[list(perm[:j])]+=(1.0)
                q=min(s,j)-j*s/n
                rays.append(b/q)
        # first d coordinates are an affine chart on sum-zero, with
        # Euclidean Jacobian sqrt(n), so volume ratios use the same chart.
        W=ConvexHull(np.array(rays)[:,:d],qhull_options='QJ').volume
        simplex=1/factorial(d)
        predicted=factorial(d)*n**d/(factorial(s)*factorial(n-s-1)*(n-s)**s*s**(n-s-1))
        observed=W/simplex
        assert abs(observed-predicted)<1e-8*predicted,(n,s,observed,predicted)
        count+=1
print('PASS: independent convex-hull volume ratios for',count,'(n,s) pairs')
