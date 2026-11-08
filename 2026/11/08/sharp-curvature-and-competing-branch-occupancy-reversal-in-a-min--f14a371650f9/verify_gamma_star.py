"""Standalone numerical checks for gamma-holding split-and-return network.
Requires numpy and Python standard library. The analytic proof is separate.
"""
import math
import numpy as np

checks=0

def check(ok, text):
    global checks
    assert ok, text
    checks += 1

def occupation_formula(nu, lam, k, a, r):
    p=lam/(lam+k)
    u=((lam+k)/(lam+k+r))**nu
    v=a/(a+r)
    w=(1-v)*u/(1-v*u)
    return np.array([1-w, p*w, (1-p)*w])

def occupation_ctmc(n, lam, k, a, r):
    # n sequential exponential stages at center; exits after last stage.
    # state 0,...,n-1: center phases; n and n+1: leaves.
    p=lam/(lam+k)
    q=lam+k
    Q=np.zeros((n+2,n+2))
    def edge(i,j,h):
        if i!=j:
            Q[i,j]+=h
            Q[i,i]-=h
    for i in range(n-1):edge(i,i+1,q)
    edge(n-1,n,q*p)
    edge(n-1,n+1,q*(1-p))
    edge(n,0,a)
    edge(n+1,0,a)
    for i in range(n+2):edge(i,0,r)
    A=Q.T.copy(); A[-1,:]=1
    rhs=np.zeros(n+2); rhs[-1]=1
    z=np.linalg.solve(A,rhs)
    return np.array([sum(z[:n]), z[n], z[n+1]])

def curvature_sign(nu, lam, k,a,r):
    p=lam/(lam+k); c=r/k; v=a/(a+r)
    h=((1+c*(1-p))**nu-v)/(1-v)
    h1=-nu*c*(1+c*(1-p))**(nu-1)/(1-v)
    h2=nu*(nu-1)*c*c*(1+c*(1-p))**(nu-2)/(1-v)
    return -h2*h**3/(h-p*h1)**3

for k,a,r in [(1.,1.,1.), (2.,3.,0.2), (0.8,4.,7.), (1.1, 0.75, 1.3)]:
    for n in [1,2,3,4]:
        for lam in [0.06,0.6,1.8,7.,22.]:
            p1=occupation_ctmc(n,lam,k,a,r)
            p2=occupation_formula(n,lam,k,a,r)
            check(np.max(np.abs(p1-p2))<3e-12, ('ctmc',n,lam,p1,p2))
            check(abs(sum(p1)-1)<1e-12,'normalization')
for nu in [0.3,0.75,1.,1.3,2.,3.5]:
    for k,a,r in [(1.,1.,1.),(2.,3.,0.2)]:
        ptab=[]
        for lam in [0.2,0.6,2.,10.]:
            p=occupation_formula(nu,lam,k,a,r)
            check(np.min(p)>0 and abs(sum(p)-1)<1e-12,'gamma formula')
            ptab.append(p)
            curv=curvature_sign(nu,lam,k,a,r)
            check((abs(curv)<1e-12 if nu==1 else (curv<0 if nu>1 else curv>0)),'signed curvature')
        # linear iff nu=1, verified for four points in exact model
        dets=[]
        for i in [1,2]:
            xy=np.array([[p[1],p[2],1.] for p in (ptab[0],ptab[i],ptab[3])]); dets.append(float(np.linalg.det(xy)))
        check(all(abs(d)<1e-12 for d in dets) if nu==1 else all(abs(d)>1e-8 for d in dets),'collinearity')
print(f'PASS: {checks} independent deterministic assertions; gamma ν=1..4 checked by CTMC generators')

# Differentiation and sharp nonmonotone threshold, independently evaluated.
def y_probability(nu, lam, k, a, r):
    return float(occupation_formula(nu,lam,k,a,r)[2])

for nu in [0.4,1.,1.4,2.,3.3]:
    for k,a,r in [(1.,1.,1.), (2.,3.,0.2), (0.8,4.,7.), (1.1,.75,1.3)]:
        v=a/(a+r)
        def F(z):return v+(1+z)**(nu-1)*((nu-1)*z-1)
        for lam in [.1,.8,2.,11.]:
            z=r/(k+lam)
            dy=(y_probability(nu,lam+1.e-5,k,a,r)-y_probability(nu,lam-1.e-5,k,a,r))/(2.e-5)
            check(abs(dy)>1.e-12 and ((dy>0)==(F(z)>0)),('derivative sign',nu,k,a,r,lam,dy,F(z)))

# Exact ν=2 critical point and uniqueness, including both sides of the peak.
for k,a,r in [(1.,1.,1.),(.8,4.,7.),(1.1,.75,1.3),(.3,2.,3.)]:
    threshold=math.sqrt(r*(a+r))
    if threshold>k:
        peak=threshold-k
        peak_y=y_probability(2.,peak,k,a,r)
        for factor in [.001,.1,.5,.99,1.01,1.5,3.,20.]:
            test=max(1e-12,peak*factor)
            check(peak_y>y_probability(2.,test,k,a,r),('unique maximum',k,a,r,peak,test))
        h=peak*1e-4
        slope=(y_probability(2.,peak+h,k,a,r)-y_probability(2.,peak-h,k,a,r))/(2*h)
        check(abs(slope)<2e-8,('peak derivative',slope))
    else:
        vals=[y_probability(2.,lam,k,a,r) for lam in [.001,.01,.1,1.,10.,100.]]
        check(all(z1>z2 for z1,z2 in zip(vals,vals[1:])),('monotonic below threshold',vals))

print(f'PASS: {checks} total deterministic assertions, including sharp competitor-response threshold')
