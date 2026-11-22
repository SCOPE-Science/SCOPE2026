"""Independent quadrature and incidence checks for paired inellipses of a square.
The analytic formula is proved in RESULT.md; these tests are diagnostics, not the proof.
"""
import math
import random
from scipy.integrate import quad

def exact_area(k,l):
    if k>l: k,l=l,k
    a=math.acos(k); b=math.acos(l)
    return b*math.sin(a)+(math.pi-a)*math.sin(b)

def numeric_area(k,l):
    def rho2(theta,c):
        return (1-c*c)/(1-c*math.cos(2*theta))
    t0=math.acos((k+l)/(1+k*l))/2
    return 2*(quad(lambda th:min(rho2(th,k),rho2(th,l)),0,t0,epsabs=2e-12,epsrel=2e-12)[0]+quad(lambda th:min(rho2(th,k),rho2(th,l)),t0,math.pi/2,epsabs=2e-12,epsrel=2e-12)[0])

def crossings(k,l):
    q=1+k*l; m=k+l
    a=math.sqrt((q+math.sqrt(q*q-m*m))/2)
    b=m/(2*a)
    return ((a,b),(b,a),(-a,-b),(-b,-a))

def f(x,y,k):
    return x*x-2*k*x*y+y*y-(1-k*k)

rng=random.Random(20261119)
n=0; max_area=0; max_res=0; min_jac=1e9
samples=[(-.9,.2),(-.5,.5),(.2,.8),(-.9,-.8),(0,0.9)]
samples += [tuple(sorted((rng.uniform(-.98,.98),rng.uniform(-.98,.98)))) for _ in range(200)]
for k,l in samples:
    if abs(k-l)<1e-9: continue
    exact=exact_area(k,l); numeric=numeric_area(k,l)
    err=abs(exact-numeric)
    max_area=max(max_area,err)
    assert err<2e-9,(k,l,exact,numeric,err)
    pts=crossings(k,l)
    for x,y in pts:
        res=max(abs(f(x,y,k)),abs(f(x,y,l)))
        max_res=max(max_res,res)
        assert res<5e-14
        assert abs(x)<1 and abs(y)<1
        det=4*(l-k)*(x*x-y*y)
        assert abs(det)>1e-12
        min_jac=min(min_jac,abs(det))
    n+=1
print({'tested_parameter_pairs':n,'max_abs_overlap_error':max_area,
       'max_abs_incidence_error':max_res,'min_transversality_jacobian':min_jac})
