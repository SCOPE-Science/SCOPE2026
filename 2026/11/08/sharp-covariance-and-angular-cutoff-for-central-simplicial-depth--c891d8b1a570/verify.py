"""Checks for circular sample central-depth/near-pair covariance theorem."""
from fractions import Fraction
from math import comb,pi,sqrt
from itertools import combinations
import sympy as sp
import numpy as np

checks=0
x,q=sp.symbols('x q',real=True)
# Circular separation delta has density 1/pi on [0,pi].
p3=sp.integrate(x/(2*sp.pi)/sp.pi,(x,0,sp.pi))
assert p3==sp.Rational(1,4); checks+=1
p_edge=sp.integrate(1/sp.pi,(x,0,sp.pi*q))
assert sp.simplify(p_edge-q)==0; checks+=1
joint=sp.integrate(x/(2*sp.pi)/sp.pi,(x,0,sp.pi*q))
assert sp.simplify(joint-q*q/4)==0; checks+=1
cov_2=sp.integrate((x/(2*sp.pi)-sp.Rational(1,4))**2/sp.pi,(x,0,sp.pi))
assert sp.simplify(cov_2-sp.Rational(1,48))==0; checks+=1
for n in range(3,24):
 c3=comb(n,3)
 var_tri=sp.Rational(3,16)*c3+sp.Rational(1,48)*comb(n,2)*(n-2)*(n-3)
 assert sp.simplify(var_tri-sp.Rational(n*n*(n-1)*(n-2),96))==0; checks+=1
 for den in range(2,15):
  for num in range(1,den):
   qq=sp.Rational(num,den)
   cv=sp.Rational(comb(n,2)*(n-2),4)*qq*(qq-1)
   va=comb(n,2)*qq*(1-qq)
   rr2=sp.factor(cv**2/(var_tri*va))
   assert sp.simplify(rr2-3*sp.Rational(n-2,n)*qq*(1-qq))==0; checks+=1
# Monte Carlo independent geometry, checking covariance/correlation and variance.
rng=np.random.default_rng(20261105)
for n,qq,N in [(4,.25,70000),(5,.5,70000),(8,.75,70000),(10,.5,40000)]:
 theta=rng.uniform(0,2*pi,size=(N,n))
 near=np.zeros(N,dtype=np.float64)
 for i,j in combinations(range(n),2):
  delta=np.abs(theta[:,i]-theta[:,j]);delta=np.minimum(delta,2*pi-delta)
  near+=(delta<pi*qq)
 tri=np.zeros(N,dtype=np.float64)
 for i,j,k in combinations(range(n),3):
  th=np.sort(theta[:,(i,j,k)],axis=1)
  gaps=np.diff(th,axis=1)
  g3=2*pi-th[:,2]+th[:,0]
  tri+=((gaps[:,0]<pi)&(gaps[:,1]<pi)&(g3<pi))
 theo_cov=-comb(n,2)*(n-2)*qq*(1-qq)/4
 sim_cov=np.mean((tri-np.mean(tri))*(near-np.mean(near)))
 predicted_vartri=n*n*(n-1)*(n-2)/96
 predicted_varnear=comb(n,2)*qq*(1-qq)
 assert abs(np.mean(tri)-comb(n,3)/4)<.05*max(1,comb(n,3)/4); checks+=1
 assert abs(np.var(tri)-predicted_vartri)<.06*max(1,predicted_vartri); checks+=1
 assert abs(np.var(near)-predicted_varnear)<.06*max(1,predicted_varnear); checks+=1
 assert abs(sim_cov-theo_cov)<.08*max(1,abs(theo_cov)),(n,qq,sim_cov,theo_cov); checks+=1
 print(f'simulation n={n}, q={qq}: covariance empirical={sim_cov:.6f} exact={theo_cov:.6f}')
print(f'PASS {checks} exact/simulation assertions')
