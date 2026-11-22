"""Numerical checks for intrinsic/ambient metric distortion of round cylinder sidewalls.

Run: python verify.py. Standard-library only. These finite tests are not proofs.
"""
import math
import random

PI = math.pi
BETA = (PI*PI-4)/(16*PI)

def stretch(theta, x):
    if theta == 0 and x == 0:
        return 1.0
    return math.sqrt((theta*theta+x*x)/(4*math.sin(theta/2)**2+x*x))

def theta_root(z):
    lo,hi=0.0,PI
    for _ in range(90):
        mid=(lo+hi)/2
        val=mid/(2*math.sin(mid/2)) if mid else 1
        if val<z:lo=mid
        else:hi=mid
    return (lo+hi)/2

def simpson(f, lo, hi, n=6000):
    assert n%2==0
    if lo==hi:return 0.0
    dx=(hi-lo)/n
    acc=f(lo)+f(hi)
    for j in range(1,n):
        acc+=(4 if j%2 else 2)*f(lo+j*dx)
    return acc*dx/3

def exact_tail(z,h):
    if z<=1:return 1.0
    if z>=PI/2:return 0.0
    t0=theta_root(z)
    def density(t):
        rad=(t*t-4*z*z*math.sin(t/2)**2)/(z*z-1)
        q=math.sqrt(max(0.0,rad))/h
        a=min(1.0,q)
        return 2*a-a*a
    return simpson(density,t0,PI)/PI

def two_dimensional_midpoint(z,h,n=600):
    total=0
    for i in range(n):
        theta=PI*(i+.5)/n
        for j in range(n):
            v=(j+.5)/n
            if stretch(theta,h*v)>z:
                total+=2*(1-v)
    return total/(n*n)

def coefficient(h):
    return 32/(3*h*math.sqrt(PI*(PI*PI-4)))

def crossover(lam):
    L=math.sqrt(BETA)*lam
    if L<=1:return 2/PI-L*L/(3*PI)
    return 8/(3*PI*L)-1/(PI*L*L)

def check():
    count=0
    assert math.isclose(stretch(PI,0), PI/2)
    count+=1
    for h in (.2,.7,1.5,4.0):
        vals=[exact_tail(z,h) for z in (1.1,1.2,1.3,1.4,1.5)]
        assert all(vals[j]>vals[j+1]>0 for j in range(4))
        count+=1
    for z in (1.05,1.2,1.4,1.55):
        vals=[exact_tail(z,h) for h in (.2,.7,1.5,4.)]
        assert all(vals[j]>vals[j+1]>0 for j in range(3))
        count+=1
    for z,h in ((1.1,.4),(1.3,1),(1.45,2)):
        a=exact_tail(z,h)
        b=two_dimensional_midpoint(z,h,n=550)
        assert abs(a-b)<.004,(z,h,a,b)
        count+=1
    for h in (.5,2.0):
        e1,e2=1e-4,1e-5
        a=exact_tail(PI/2-e1,h)/(coefficient(h)*e1**1.5)
        b=exact_tail(PI/2-e2,h)/(coefficient(h)*e2**1.5)
        assert abs(b-1)<.02 and abs(b-1)<abs(a-1),(h,a,b)
        count+=1
    for lam in (0.0,.5,2., 1/math.sqrt(BETA), 4., 10.):
        h=max(1e-13,lam*math.sqrt(1e-5))
        obs=exact_tail(PI/2-1e-5,h)/1e-5
        assert abs(obs-crossover(lam))<.002,(lam,obs,crossover(lam))
        count+=1
    # A dimensionless aspect ratio is recoverable from any fixed-threshold tail.
    z=1.4
    h=1.28
    target=exact_tail(z,h)
    lo,hi=.001,100.
    for _ in range(50):
        mid=(lo+hi)/2
        if exact_tail(z,mid)>target:lo=mid
        else:hi=mid
    assert abs((lo+hi)/2-h)<2e-6
    count+=1
    # Dirichlet(1,1/2,1) predicted first moments (2/5, 1/5, 2/5).
    # Sample uniformly in the leading sublevel region via a direct rejection method.
    rng=random.Random(391)
    means=[0.,0.,0.]
    n=0
    for _ in range(150000):
        y=rng.random()
        w=rng.random()
        if y+w*w<1:
            vals=(y,w*w,1-y-w*w)
            for j in range(3):means[j]+=vals[j]
            n+=1
    means=[x/n for x in means]
    assert n>70000 and max(abs(a-b) for a,b in zip(means,(.4,.2,.4)))<.01,(n,means)
    count+=1
    print('CYLINDER_STRETCH_TAIL_CHECKS_OK',count,'Dirichlet_samples',n)

if __name__=='__main__':check()
