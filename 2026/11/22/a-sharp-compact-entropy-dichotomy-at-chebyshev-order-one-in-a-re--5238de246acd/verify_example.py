"""Non-certifying finite diagnostic for the two entropy regimes of the CLICM map.
Uses Python standard library only. The theorem and proof do not depend on these samples.
"""
import math

def T(n,t): return math.cos(n*math.acos(t))
def Tp(n,t): return n*math.sin(n*math.acos(t))/math.sqrt(1-t*t)
def phase(a,b,t): return a/(t*(1-t))+b
def dphase(a,t): return -a*(1-2*t)/(t*t*(1-t)*(1-t))
def f(n,a,b,t): return T(n,t)*math.sin(phase(a,b,t))
def evals(n,a,b,t):
    p=phase(a,b,t)
    A=T(n,t)*math.cos(p)*dphase(a,t)
    B=Tp(n,t)*math.sin(p)
    return A+B,A-B

def bisect(fn, l,r, target):
    fl=fn(l)-target; fr=fn(r)-target
    assert fl*fr<=0,(l,r,target,fl,fr)
    for _ in range(65):
        m=(l+r)/2
        if (fn(m)-target)*fl<=0:r=m
        else:l=m;fl=fn(l)-target
    return (l+r)/2

def inv_phase(theta,a,b):
    # theta-b=a/(t(1-t)), small root
    z=a/(theta-b)
    return 2*z/(1+math.sqrt(1-4*z))

def test(n,a=20,b=2.5,d=0.01,N=5):
    I=(d,2*d)
    s=1 if T(n,d)>0 else -1
    mlo=int((phase(a,b,2*d)-2*math.pi)/(2*math.pi))
    mhi=int((phase(a,b,d)+2*math.pi)/(2*math.pi))+1
    intervals=[]
    for m in range(mlo,mhi):
        theta=2*math.pi*m
        if s>0: left_ph,right_ph=theta+math.pi/2,theta
        else: left_ph,right_ph=theta,theta-math.pi/2
        z1=inv_phase(left_ph,a,b)
        z2=inv_phase(right_ph,a,b)
        l,r=sorted((z1,z2))
        if not(d<l<r<2*d):continue
        if min(f(n,a,b,l),f(n,a,b,r))>d+1e-10:continue
        if max(f(n,a,b,l),f(n,a,b,r))<2*d-1e-10:continue
        zlo=bisect(lambda t:f(n,a,b,t),l,r,d)
        zhi=bisect(lambda t:f(n,a,b,t),l,r,2*d)
        l2,r2=sorted((zlo,zhi))
        for t in (l2,(l2+r2)/2,r2):
            lambdas=evals(n,a,b,t)
            assert all(abs(x)>2 for x in lambdas), (n,m,t,lambdas)
        intervals.append((l2,r2))
    assert len(intervals)>=N,(n,len(intervals))
    print(f'nu={n}, a={a}, b={b}, I={I}, branch_count={len(intervals)}, five_branch_samples={intervals[:N]}')
    print('  both eigenvalues abs >2 on sampled endpoints/midpoints (finite diagnostic only).')

for n in [1.0001,1.5,2.,3.,3.5]:
    d=1e-5 if n==1.0001 else 0.01
    test(n,d=d)
# Test exact identity for n=1 at diverse values.
for x,y in [(0.2,0.3),(-0.7,0.2),(0.6,-0.4)]:
    X=y*math.sin(phase(20,2.5,x))
    Y=x*math.sin(phase(20,2.5,y))
    assert abs(X*Y)<=abs(x*y)+1e-12
print('product Lyapunov inequality tested at three nonsingular states.')
