#!/usr/bin/env python3
"""Separately implemented tensor-product spherical-coordinate quadrature, not gamma moments."""
import numpy as np
from numpy.polynomial.legendre import leggauss
order=64
nodes,ws=leggauss(order)
angles=np.pi*(nodes+1)/4
weights=ws*np.pi/4
H=np.zeros((7,7),float)
for th,wt in zip(angles,weights):
 for ph,wp in zip(angles,weights):
  x=np.sin(th)*np.cos(ph); y=np.sin(th)*np.sin(ph); z=np.cos(th)
  v=np.array([x*(5*x*x-3),y*(5*y*y-3),z*(5*z*z-3),x*(y*y-z*z),y*(z*z-x*x),z*(x*x-y*y),x*y*z])
  H+=np.outer(v,v)*wt*wp*np.sin(th)
G=np.diag([16*np.pi/7]*3+[16*np.pi/105]*3+[4*np.pi/105])
T=np.diag(1/np.sqrt(np.diag(G)))@H@np.diag(1/np.sqrt(np.diag(G)))
p=np.pi
vals=np.array([(p-3)/(8*p),(30*p-5-np.sqrt(6505))/(240*p),
 (30*p+25-np.sqrt(4045))/(240*p), (30*p+25-np.sqrt(4045))/(240*p),
 (30*p-5+np.sqrt(6505))/(240*p),
 (30*p+25+np.sqrt(4045))/(240*p),(30*p+25+np.sqrt(4045))/(240*p)])
err=np.max(np.abs(np.linalg.eigvalsh(T)-vals))
assert err<1.e-12,err
assert abs(np.trace(T)-7/8)<1.e-12
print('NUMERIC_OCTANT_CUBIC_PASS', 'nodes=',order*order,'max_eigen_error=',err)
