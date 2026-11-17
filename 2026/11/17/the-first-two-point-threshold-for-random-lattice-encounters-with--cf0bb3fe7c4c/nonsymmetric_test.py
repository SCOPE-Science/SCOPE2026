"""Optional independent polygonal-overlap quadrature for a noncentral convex body.

Requires NumPy, SciPy and Shapely. This finite-resolution check is not a proof.
"""
import numpy as np
from math import pi,sqrt
from shapely.geometry import Polygon
from shapely.affinity import translate
from scipy.integrate import simpson

d=.09;u=.03
T=np.linspace(0,2*pi,2048,endpoint=False)
h=1+d*np.cos(2*T)+u*np.cos(3*T)
hprime=-2*d*np.sin(2*T)-3*u*np.sin(3*T)
poly=Polygon(np.array([h*np.cos(T)-hprime*np.sin(T),h*np.sin(T)+hprime*np.cos(T)]).T)
D=2+2*d; rho1=1-3*d-8*u;rho2=1-3*d+8*u
ks=1/rho1+1/rho2; kB=1/(rho1+rho2)
co=2*D**1.5/(ks*(D*kB-1))**.5
print('geometry',poly.is_valid,D,rho1,rho2,kB*D,co,flush=True)
for eps in [.015,.007,.003]:
 t=1/D+eps
 q=Polygon(np.asarray(poly.exterior.coords)[:-1]*t)
 maxth=2*sqrt(2*D*eps/(D*kB-1))
 ths=np.linspace(-maxth,maxth,151)
 areas=[]
 for th in ths:
  ar=q.intersection(translate(q,xoff=np.cos(th),yoff=np.sin(th))).area
  areas.append(ar)
 p2=4/(2*pi)*simpson(areas,x=ths)
 ratio=p2/(co*eps*eps)
 print(eps,p2,co*eps*eps,ratio,flush=True)
 assert abs(ratio-1)<.08
print('ASYMMETRIC_CURVATURE_LENS_CHECK_OK')
