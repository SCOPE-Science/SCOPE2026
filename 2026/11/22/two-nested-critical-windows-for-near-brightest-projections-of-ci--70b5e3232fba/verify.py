"""Reproducibility checks for the near-brightest random views of circular cones."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.spatial import ConvexHull

PI=math.pi

def D(a): return PI/2+a
def F(a): return math.cos(a)+D(a)*math.sin(a)
def H(a): return math.sqrt(D(a)/(math.sin(a)*math.cos(a)))
AS=brentq(lambda a: math.tan(2*a)-PI-2*a,0.4,0.78)
AC=brentq(lambda a: D(a)*(D(a)+1/math.tan(a))-PI**2,0.1,AS)
KC=H(AC)
ZC=KC*math.sin(AC)/math.sqrt(1+KC**2*math.sin(AC)**2)
S=1+KC**2*math.sin(AC)**2
DCOEF=F(AC)/S**1.5
KAPPA=(KC**2*math.cos(2*AC)-1)*S**1.5/(KC*math.cos(AC))
CCOEF=2*math.sqrt(2/KAPPA)

def brightness(k,z):
    if z>=k/math.sqrt(1+k*k):return PI*z
    v=z/(k*math.sqrt(1-z*z))
    return PI*z/2+math.sqrt(max(0,k*k-(k*k+1)*z*z))+z*math.asin(max(-1,min(1,v)))

def max_and_oblique(k):
    if k<=H(AS):return PI,None
    aa=brentq(lambda a:H(a)-k,1e-12,AS)
    z=k*math.sin(aa)/math.sqrt(1+k*k*math.sin(aa)**2)
    b=brightness(k,z)
    return max(PI,b),z

def survival(k,eps):
    M,z=max_and_oblique(k)
    cut=M-eps
    # Partition by known critical points, avoiding grid omissions near extrema.
    pts=[0.,k/math.sqrt(1+k*k),1.]
    if z is not None:pts.append(z)
    # Also include the larger root, an interior local minimum.
    if k>H(AS):
        aa=brentq(lambda a:H(a)-k,AS+1e-10,PI/2-1e-10)
        zz=k*math.sin(aa)/math.sqrt(1+k*k*math.sin(aa)**2)
        pts.append(zz)
    pts=sorted(set(pts));roots=[]
    for x,y in zip(pts[:-1],pts[1:]):
        fx=brightness(k,x)-cut;fy=brightness(k,y)-cut
        if fx*fy<0:roots.append(brentq(lambda t:brightness(k,t)-cut,x,y,xtol=1e-14))
    bounds=[0.]+roots+[1.]
    return sum(y-x for x,y in zip(bounds[:-1],bounds[1:]) if brightness(k,(x+y)/2)>cut)

# Independent geometry: project an apex and a 4096-gon approximation of the base disk.
def projected_hull(k,z):
    t=math.sqrt(1-z*z)
    # Orthonormal image coordinates: (z,0,-t) and (0,1,0).
    phi=np.linspace(0,2*PI,4096,endpoint=False)
    pts=np.column_stack([z*np.cos(phi),np.sin(phi)])
    pts=np.vstack((pts,np.array([[-k*t,0.]])))
    return ConvexHull(pts).volume

for k in [0.65,2.,KC,2.9,4.5]:
    for z in [0.,0.11,0.39,0.75,0.99,1.]:
        assert abs(projected_hull(k,z)-brightness(k,z))<3e-5,(k,z)

assert abs(KC-2.64140255206409)<1e-11
assert abs(ZC-0.58898107634912)<1e-11
assert KAPPA>0 and DCOEF>0
for dh in [1e-3,2e-4]:
    approx=-(brightness(KC,ZC+dh)-2*brightness(KC,ZC)+brightness(KC,ZC-dh))/dh**2
    assert abs(approx-KAPPA)<1e-5

for k in [1.,2.5]:
    for e in [0.001,0.0002]:
        assert abs(survival(k,e)-e/PI)<1e-10

# Shape switch: quadratic interior max vs linear polar max.
for k in [KC,3.5]:
    M,z=max_and_oblique(k)
    aa=AC if k==KC else brentq(lambda a:H(a)-k,1e-12,AS)
    curv=(k*k*math.cos(2*aa)-1)*(1+k*k*math.sin(aa)**2)**1.5/(k*math.cos(aa))
    C=2*math.sqrt(2/curv)
    for e in [1e-4,2e-5]:
        exact=survival(k,e)
        leading=C*math.sqrt(e)+(e/PI if k==KC else 0.)
        assert abs(exact/leading-1)<0.002,(k,e,exact,leading)

for lam in [-2.,-1.,0.,0.6,2.]:
    e=1e-5
    val=survival(KC+lam*e,e)
    lead=CCOEF*math.sqrt(max(0.,1+DCOEF*min(lam,0)))*math.sqrt(e)
    polar=max(0.,1-DCOEF*max(lam,0))*e/PI
    assert abs(val-(lead+polar))<3e-6,(lam,val,lead,polar)

# Second, finer window where polar and oblique contributions have equal order.
s=math.sin(AC);c=math.cos(AC);T=1+KC*KC*s*s
gkk=-3*KC*s*s*F(AC)/T**2.5
gka=D(AC)*c/T**1.5-3*KC*KC*s*c*F(AC)/T**2.5
gaa=KC*c*(1-KC*KC*math.cos(2*AC))/T**1.5
msecond=gkk-gka*gka/gaa
beta=msecond/(2*DCOEF*DCOEF)
assert msecond>0 and beta>0
for eps in [0.003,0.001,0.0003]:
    for mu in [-1.,-0.2,0.,0.5,2.]:
        k=KC-eps/DCOEF+mu*eps*eps
        measured=survival(k,eps)/eps
        target=1/PI+CCOEF*math.sqrt(max(0,DCOEF*mu+beta))
        assert abs(measured-target)<0.01,(eps,mu,measured,target)

print('CONE_RANDOM_BRIGHTNESS_CRITICAL_TAILS_OK')
print('critical_aspect',repr(KC),'latitude',repr(ZC))
print('delta_slope',repr(DCOEF),'curvature',repr(KAPPA),'sqrt_coefficient',repr(CCOEF))
print('negative_window_boundary',repr(-1/DCOEF))
print('second_derivative',repr(msecond),'inner_shift',repr(beta),'inner_boundary',repr(-beta/DCOEF))
