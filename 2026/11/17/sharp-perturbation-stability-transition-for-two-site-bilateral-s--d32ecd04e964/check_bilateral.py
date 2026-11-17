"""Independent numerical checks for two-site bilateral sharp Lipschitz theorem.
Standard library only. Not a proof of global optimality.
"""
from math import exp, isclose, sqrt
from random import Random

def rational_phi(d,c,s,p):
    t=(abs(d)/s)**p
    return d*(1-c+t)/(1+c+t)

def rational_slope(d,c,s,p):
    t=(abs(d)/s)**p
    a=1+c
    return 1-2*c*(a+(1-p)*t)/(a+t)**2

def rational_gain(c,p):
    return 1.0 if p<=1 else 1+c*(p-1)**2/(2*p*(1+c))

def gauss_phi(d,c,s):
    w=c*exp(-(d*d)/(2*s*s))
    return d*(1-w)/(1+w)

def gauss_slope(d,c,s):
    q=d*d/(2*s*s);w=c*exp(-q)
    return 1-2*w/(1+w)+4*q*w/(1+w)**2

def gauss_peak(c):
    lo,hi=1.5,8.0
    for _ in range(110):
        mid=(lo+hi)/2;w=c*exp(-mid)
        if 3*(1+w)-2*mid*(1-w)>0: lo=mid
        else:hi=mid
    q=(lo+hi)/2;w=c*exp(-q)
    return q,1+2*w*(2+w)/(1-w*w)

r=Random(478009)
for p in [0.3,0.7,1.0,1.3,2.0,4.0,8.0]:
    for c in [0.04,0.25,0.8,1.0]:
        for s in [0.2,1.0,3.7]:
            L=rational_gain(c,p)
            for _ in range(400):
                d=r.uniform(-15*s,15*s);h=1e-5*s
                assert abs((rational_phi(d+h,c,s,p)-rational_phi(d-h,c,s,p))/(2*h)-rational_slope(d,c,s,p)) < max(2e-4,abs(rational_slope(d,c,s,p))*1e-5)
                a=r.uniform(-25*s,25*s);b=r.uniform(-25*s,25*s)
                if abs(a-b)>1e-5*s:
                    quotient=abs((rational_phi(a,c,s,p)-rational_phi(b,c,s,p))/(a-b))
                    assert quotient < L+1e-10,(p,c,s,quotient,L)
            if p>1:
                dstar=s*((1+c)*(p+1)/(p-1))**(1/p)
                assert isclose(rational_slope(dstar,c,s,p),L,rel_tol=1e-11)
print('RATIONAL_ALL_84_CASES_GLOBAL_BOUNDS_AND_SHARP_DERIVATIVES_PASS')

for c in [0.01,0.1,0.5,1.0]:
    for s in [0.25,1.0,4.0]:
        q,L=gauss_peak(c)
        dstar=s*sqrt(2*q)
        assert isclose(gauss_slope(dstar,c,s),L,rel_tol=1e-12)
        for _ in range(3000):
            a=r.uniform(-12*s,12*s);b=r.uniform(-12*s,12*s)
            if abs(a-b)>1e-6*s:
                assert abs((gauss_phi(a,c,s)-gauss_phi(b,c,s))/(a-b)) < L+1e-10
print('GAUSSIAN_12_CASES_SHARP_PEAK_AND_RANDOM_SECANTS_PASS')
q,L=gauss_peak(1.0)
assert abs(q-1.9803582797687855)<1e-11
assert abs(L-1.601638930011748)<1e-10
print('GAUSSIAN_C1_PEAK',format(q,'.13f'),'GAIN',format(L,'.13f'))

# Compare independently implemented two-coordinate filter with reduced contrast identity.
for _ in range(3000):
    x,y=r.uniform(-10,10),r.uniform(-10,10)
    c=r.uniform(0.001,1.0);s=r.uniform(0.1,5.0);p=r.uniform(0.2,6.0)
    w=c/(1+(abs(x-y)/s)**p)
    fx=(x+w*y)/(1+w);fy=(y+w*x)/(1+w)
    assert abs((fx-fy)-rational_phi(x-y,c,s,p))<1e-11
    assert abs((fx+fy)-(x+y))<1e-11
print('ORIGINAL_TWO_COORDINATE_BILATER_IDENTITY_PASS_3000')
print('ALL_TWO_SITE_BILATERAL_CHECKS_PASS')

# Direct operator-norm (all-coordinate) random checks in several Banach norms.
def norm(v,q):
    return max(abs(v[0]),abs(v[1])) if q=='inf' else (abs(v[0])**q+abs(v[1])**q)**(1/q)
def pair_filter(x,y,c,s,p=None):
    d=x-y
    w=c*exp(-d*d/(2*s*s)) if p is None else c/(1+(abs(d)/s)**p)
    return ((x+w*y)/(1+w),(y+w*x)/(1+w))
for p in [0.4,1,1.8,2,4,None]:
    for c in [0.1,1.0]:
        for q in [1,1.5,2,4,'inf']:
            L=gauss_peak(c)[1] if p is None else rational_gain(c,p)
            for _ in range(1500):
                a=(r.uniform(-12,12),r.uniform(-12,12))
                b=(r.uniform(-12,12),r.uniform(-12,12))
                u=pair_filter(*a,c,1,p);v=pair_filter(*b,c,1,p)
                den=norm((a[0]-b[0],a[1]-b[1]),q)
                if den>0: assert norm((u[0]-v[0],u[1]-v[1]),q)<=L*den+1e-10
print('DIRECT_ALL_ELL_Q_PAIR_BOUNDS_PASS_90000')
