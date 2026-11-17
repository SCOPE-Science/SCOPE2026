#!/usr/bin/env python3
"""Independent numeric consistency checks for the explicit ellipse geometry."""
import math
import numpy as np
from scipy.spatial import Delaunay
from scipy.integrate import quad
rng=np.random.default_rng(20261113)
for n in (4,7,12):
    for trial in range(25):
        theta=np.sort(rng.random(n)*2*math.pi)
        edge_sets=[]
        for a,b in ((1.002,1.), (1.75,1.),(8.,1.),(100.,2.)):
            points=np.column_stack((a*np.cos(theta), b*np.sin(theta)))
            if n==4:
                D=np.linalg.det(np.column_stack((points,(points**2).sum(axis=1),np.ones(n))))
                formula=-16*a*b*(a*a-b*b)*math.sin(theta.sum()/2)
                for i in range(4):
                    for j in range(i+1,4):
                        formula*=math.sin((theta[j]-theta[i])/2)
                assert math.isclose(D,formula,rel_tol=2e-7,abs_tol=1e-7), (D,formula)
            simplices=Delaunay(points).simplices
            inside=set()
            for tri in simplices:
                for i,j in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])):
                    u,v=sorted((int(i),int(j)))
                    if v-u>1 and (u,v)!=(0,n-1):inside.add((u,v))
            edge_sets.append(frozenset(inside))
        assert len(set(edge_sets))==1, (n,trial,edge_sets)
for t in (0.05,0.2,0.5,0.9):
    numerical=quad(lambda v: 1/(math.pi*math.sqrt(1-v*v)),-t,t,epsabs=1e-12)[0]
    expected=2*math.asin(t)/math.pi
    assert abs(numerical-expected)<1e-10
print('ELLIPSE_DELAUNAY_FAN_CHECKS_OK')
