"""Finite-rooted-tree cavity integration for numerical comparisons."""
from scipy.integrate import cumulative_trapezoid
import numpy as np
import mpmath as mp
mp.mp.dps=30

def finite_response(degree, anomaly, path_length, side_depth=16, ngrid=30001):
    v=np.linspace(0.,1.,ngrid)
    H=1-v
    for _ in range(side_depth):
        H=1-cumulative_trapezoid(H**(degree-1),v,initial=0)
    def initial(a): return 1-cumulative_trapezoid(a*(1-v)**(a-1)*H**(degree-1),v,initial=0)
    fa=initial(anomaly)
    fb=initial(1)
    for _ in range(path_length-1):
        fa=1-cumulative_trapezoid(H**(degree-2)*fa,v,initial=0)
        fb=1-cumulative_trapezoid(H**(degree-2)*fb,v,initial=0)
    return np.trapezoid(H**(degree-1)*(fa-fb),v)

def analytic_response(q,a,r):
    L=mp.log(q-1)/(q-2)
    def base(u):
        v=mp.expm1((q-2)*u)/(q-2)
        return 1-mp.quad(lambda x:a*(1-x)**(a-1)*(1+(q-2)*x)**(-(q-1)/(q-2)),[0,v])-mp.exp(-u)
    if r==1:return mp.quad(lambda u:mp.exp(-u)*base(u),[0,L])
    return ((-1)**(r-1)/mp.factorial(r-2)*mp.quad(lambda s:base(s)*mp.exp(-s)*mp.gammainc(r-1,0,L-s),[0,L]))

for q,a in [(3,2),(3,3),(4,2)]:
  for r in [1,2,3,4,5]:
    v=finite_response(q,a,r)
    exact=float(analytic_response(q,a,r))
    err=abs(v-exact)
    print(q,a,r,format(v,'.13g'), format(exact,'.13g'), 'abs_err',format(err,'.3g'))
    assert err < 1.5e-7,(q,a,r,err)
print('PASSED 15 finite-tree cavity comparisons')
