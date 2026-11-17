"""Independent numerical checks for areas of triangles inscribed in a horocycle."""
import math
from scipy.integrate import quad
from scipy.special import roots_jacobi


def area_formula(u,v):
    return 2*(math.atan(u/2)+math.atan(v/2)-math.atan((u+v)/2))

def area_cosine_rule(u,v):
    sides=[2*math.asinh(u/2),2*math.asinh(v/2),2*math.asinh((u+v)/2)]
    cs=[math.cosh(x) for x in sides]
    sn=[math.sinh(x) for x in sides]
    angles=[]
    for i in range(3):
        j,k=[a for a in range(3) if a!=i]
        cosang=(cs[j]*cs[k]-cs[i])/(sn[j]*sn[k])
        angles.append(math.acos(max(-1,min(1,cosang))))
    return math.pi-sum(angles)

for u,v in [(0.1,0.2),(1,1),(2,7),(10,30),(0.004,11)]:
    a=area_formula(u,v); b=area_cosine_rule(u,v)
    print('area',u,v,a,b,a-b)
    assert abs(a-b)<1e-9

def mean_scaled(L):
    def f(x):return 12*L*(1-x)**2*math.atan(2/(L*x))
    def g(x):return 12*L*x*(1-x)*math.atan(2/(L*x))
    return quad(f,0,1,epsabs=1e-9)[0]-quad(g,0,1,epsabs=1e-9)[0]
for L in (100,1000,10000):
    a=mean_scaled(L); b=24*math.log(L/2)-24
    print('mean',L,a,b,a-b)
    assert abs(a-b)<115/L

# Exact CDF of weak-limit Z, with T Beta(2,2), P uniform, Z=4/T*(1/(P*(1-P))-1).
def cdf(z):
    if z<=12:return 0
    return quad(lambda t: 6*t*(1-t)*math.sqrt((z*t-12)/(z*t+4)),12/z,1,epsabs=1e-10)[0]
for z in [13,20,50,100,1000,10000]:
    print('cdf',z,cdf(z),'z_surv',z*(1-cdf(z)))
assert 1-cdf(1e6)>0
# Fixed-seed random independent checks of the marked tail at a finite threshold.
import numpy as np
rng=np.random.default_rng(20261114)
N=400000
T=rng.beta(2.,2.,N)
P=rng.random(N)
Z=4/T*(1/(P*(1-P))-1)
z=200.
sel=Z>z
V=z*T[sel]*np.minimum(P[sel],1-P[sel])/4
print('mark',int(sel.sum()),'tail',sel.mean(), 'T_cond',T[sel].mean(), 'V_cond',V.mean(), 'fair_label',np.mean(P[sel]<.5))
assert abs(sel.mean()-(1-cdf(z)))<0.003
assert abs(T[sel].mean()-1/3)<0.015
assert abs(V.mean()-0.5)<0.015
assert abs(np.mean(P[sel]<.5)-0.5)<0.015
print('HOROCYCLE_TRIANGLE_AREA_LIMIT_CHECKS_OK')
