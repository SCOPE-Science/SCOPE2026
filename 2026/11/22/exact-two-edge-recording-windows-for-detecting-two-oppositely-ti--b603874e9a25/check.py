"""Numerical diagnostics for the two-species acoustic recording-window theorem.

Python 3, NumPy and SciPy. No external files, data, or network access.
Finite tests are diagnostic and do not replace the analytic proof.
"""
import itertools
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

passed = 0

def check(condition, explanation):
    global passed
    if not bool(condition):
        raise AssertionError(explanation)
    passed += 1

def uv(H, B, k, a, b, x):
    U = (a / k) * (-math.expm1(-k*x) + math.exp(-k*H)*math.expm1(k*(B-x)))
    V = (b / k) * (-math.expm1(-k*(B-x)) + math.exp(-k*H)*math.expm1(k*x))
    return U, V

def probability(H, B, k, a, b, x):
    U,V = uv(H,B,k,a,b,x)
    return math.expm1(-U)*math.expm1(-V)

def log_derivative(H, B, k, a, b, x):
    U,V = uv(H,B,k,a,b,x)
    c = -math.expm1(-k*(H-B))
    return c*(a*math.exp(-k*x)/math.expm1(U)
                -b*math.exp(-k*(B-x))/math.expm1(V))

def optimum(H,B,k,a,b):
    if log_derivative(H,B,k,a,b,0) <= 0: return 0.0
    if log_derivative(H,B,k,a,b,B) >= 0: return B
    return brentq(lambda x:log_derivative(H,B,k,a,b,x),0,B,xtol=1e-14)

rng=np.random.default_rng(79473)
for trial in range(350):
    H=float(rng.uniform(0.3,8.0))
    B=float(H*rng.uniform(0.08,0.92))
    k=float(np.exp(rng.uniform(-2,1)))
    a=float(np.exp(rng.uniform(-2.5,3)))
    b=float(np.exp(rng.uniform(-2.5,3)))
    x=optimum(H,B,k,a,b)
    check(0<=x<=B, 'argmax domain')
    U,V=uv(H,B,k,a,b,x)
    check(U>0 and V>0,'positive integrated intensities')
    for xx in np.linspace(0,B,21):
        check(probability(H,B,k,a,b,x)>=probability(H,B,k,a,b,float(xx))-1e-11,'global edge-window check')
    if x>1e-10 and x<B-1e-10:
        check(abs(log_derivative(H,B,k,a,b,x))<2e-9,'interior first order condition')
    for xx in np.linspace(0,B,10):
        # Integrate the two recording windows at 600 midpoints each independently.
        t1=(np.arange(600)+.5)*(float(xx)/600.)
        t2=H-(B-float(xx))+(np.arange(600)+.5)*((B-float(xx))/600.)
        In1=a*(xx/600*sum(np.exp(-k*t1))+(B-xx)/600*sum(np.exp(-k*t2)))
        In2=b*(xx/600*sum(np.exp(-k*(H-t1)))+(B-xx)/600*sum(np.exp(-k*(H-t2))))
        Ua,Va=uv(H,B,k,a,b,float(xx))
        check(abs(In1-Ua)<max(1,Ua)*0.0001 and abs(In2-Va)<max(1,Va)*0.0001,'independent midpoint integral')

H,B,k,b=2.,1.,1.,1.
h=-math.expm1(-k*B)/k
s=math.exp(-k*(H-B))*h
phi=lambda z,u: u/math.expm1(z*u)
acrit=brentq(lambda a:phi(s,a)-math.exp(-k*B)*phi(h,b),.01,100.)
check(abs(acrit-15.717171299688172)<1e-9,'one-sided threshold')
check(optimum(H,B,k,20.,1.)==0,'late-only regime')
check(optimum(H,B,k,1.,20.)==B,'early-only regime')
check(abs(optimum(H,B,k,1.,1.)-B/2)<1e-12,'symmetry')
check(abs(probability(H,B,k,20.,1.,0)-0.4640603908858238)<1e-12,'late-only value')
check(abs(probability(H,B,k,1.,1.,B/2)-0.14592277036360785)<1e-12,'symmetric value')

# Exhaust all finite sets of five sampled cells out of fourteen; independent check
# that no irregular/middle-only layout outperforms optimal endpoint-edge cells.
H=2.; m=5; n=14; B=H*m/n; k=1.;
for a,b in ((1.,1.),(3.,1.),(25.,1.),(1.,25.)):
    t=(np.arange(n)+.5)*H/n
    best=-1.;best_s=None
    for cells in itertools.combinations(range(n),m):
        inds=np.array(cells,dtype=int)
        U=float(a*(H/n)*sum(np.exp(-k*t[inds])))
        V=float(b*(H/n)*sum(np.exp(-k*(H-t[inds]))))
        p=math.expm1(-U)*math.expm1(-V)
        if p>best:best,best_s=p,cells
    # A finite-grid optimum may be suboptimal to a continuously variable interval.
    check(best<=probability(H,B,k,a,b,optimum(H,B,k,a,b))+0.002,'discrete exhaustive vs continuous optimum')
    edge_patterns={tuple(list(range(i))+list(range(n-(m-i),n))) for i in range(m+1)}
    check(best_s in edge_patterns,'discrete exhaustive maximizer uses endpoint cells')

for B in (0.1,0.02,0.005,0.001):
    H,k,a,b=2.,1.,9.,0.7
    x=optimum(H,B,k,a,b)
    check(abs(x/B-.5)<3.*B,'small-budget equal-split asymptotic')
print('PASS',passed,'diagnostic assertions')
print('Example threshold a_crit:',format(acrit,'.12f'))
print('Example late-only probability:',format(probability(2,1,1,20,1,0),'.12f'))
