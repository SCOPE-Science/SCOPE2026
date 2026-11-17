"""Reproducible supplementary checks for the circular ball-hull area profile.
Requires Python 3 standard library only.  These finite tests do not prove the theorem.
"""
import math
import random

def area_formula(R, r, s):
    assert 0 < r < R and r <= s <= 2*R-r
    a = R-r
    q = max(-1., min(1., (s*s + a*a - R*R)/(2*s*a)))
    theta = math.acos(q)
    phi = math.atan2(a*math.sin(theta),s-a*math.cos(theta))
    return R*R*(math.pi-theta-phi)+r*r*theta-a*s*math.sin(theta)

def boundary_centers(R, r, s, N=180):
    a=R-r
    q=max(-1.,min(1.,(s*s+a*a-R*R)/(2*s*a)))
    theta=math.acos(q)
    phi=math.atan2(a*math.sin(theta),s-a*math.cos(theta))
    for k in range(N+1):
        t=-theta+2*theta*k/N
        yield (a*math.cos(t),a*math.sin(t))
        t=math.pi-phi+2*phi*k/N
        yield (s+R*math.cos(t),R*math.sin(t))

def area_radial_grid(R,r,s,angles=720,centers=240):
    cs=list(boundary_centers(R,r,s,centers//2))
    total=0.
    for j in range(angles):
        t=2*math.pi*j/angles
        ux,uy=math.cos(t),math.sin(t)
        rho=float('inf')
        for x,y in cs:
            dot=x*ux+y*uy
            rr=R*R-(x*x+y*y)+dot*dot
            bound=dot+math.sqrt(max(0.,rr))
            if bound<rho:rho=bound
        total+=rho*rho
    return math.pi*total/angles

def validate():
    rng=random.Random(21072026)
    tests=0
    for R,r in [(1.,.1),(1.,.4),(1.,.9),(3.,.4),(3.,2.5)]:
        a=R-r
        mx=math.pi*R*R
        mn=math.pi*r*r
        assert abs(area_formula(R,r,r)-mn)<1e-12*R*R
        assert abs(area_formula(R,r,2*R-r)-mx)<1e-12*R*R
        last=mn
        for j in range(1,100):
            s=r+2*a*j/100
            f=area_formula(R,r,s)
            assert f>last, (R,r,s,f,last)
            last=f
            tests+=1
        for frac in [.03,.17,.4,.7,.95]:
            s=r+(2*R-2*r)*frac
            exact=area_formula(R,r,s)
            numeric=area_radial_grid(R,r,s,angles=720,centers=400)
            assert abs(numeric-exact)<.0006*R*R,(R,r,frac,exact,numeric)
            tests+=1
        low=(2*math.sqrt(2)/3)*math.sqrt(R*r/a)
        high=4*R*math.sqrt(2*R*a/(2*R-r))
        for eps in [1.e-5,2.e-6,5.e-7]:
            start=(area_formula(R,r,r+eps)-mn)/(eps**1.5)
            end=(mx-area_formula(R,r,2*R-r-eps))/math.sqrt(eps)
            assert abs(start/low-1)<.01,(R,r,eps,'low',start,low)
            assert abs(end/high-1)<.005,(R,r,eps,'high',end,high)
            tests+=2
    for j in range(1500):
        R=rng.uniform(.1,10);r=R*rng.uniform(.01,.99)
        s=r+(2*R-2*r)*rng.uniform(.0001,.9999)
        assert math.pi*r*r < area_formula(R,r,s) < math.pi*R*R
        tests+=1
    print('PASS',tests,'numeric supplementary checks; direct sampled-center radial integration in 25 nontrivial cases')

if __name__=='__main__':validate()
