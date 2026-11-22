"""Finite sanity checks for interval-slope convex regression in path variation.

Run with Python 3 standard library: python verify.py
Finite tests do not replace the general proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def variation(x):
    return sum(abs(b-a) for a,b in zip(x,x[1:]))


def partition_output(h,masses,cuts):
    n=len(h)
    out=[F(0)]*n
    start=0
    for end in range(1,n+1):
        if end==n or ((cuts>>(end-1))&1):
            mass=sum(masses[start:end]); center=sum(masses[i]*h[i] for i in range(start,end))/mass
            for i in range(start,end):out[i]=center
            start=end
    return out


def check_exact_blocks():
    r=Random(7143);cases=0
    for n in range(2,10):
        for trial in range(9):
            masses=[F(r.randint(1,15)) for _ in range(n)]
            for cuts in range(1<<(n-1)):
                for e in range(n-1):
                    step=[F(0) if i<=e else F(1) for i in range(n)]
                    out=partition_output(step,masses,cuts)
                    assert variation(out)<=1, (n,cuts,e,masses)
                    cases+=1
    print('EXACT_CONSECUTIVE_BLOCK_STEP_NORMS_PASS',cases)


def p_center(y,m,p):
    lo=min(y);hi=max(y)
    if hi==lo:return lo
    def deriv(t):
        return sum(mm*pp*(1 if t>z else -1 if t<z else 0)*abs(t-z)**(pp-1)
                   for z,mm,pp in zip(y,m,p))
    for _ in range(62):
        mid=(lo+hi)/2
        if deriv(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def constrained_fit(f,m,p,l,u):
    """Small-n exact active-pattern enumeration; scalar roots by bisection."""
    n=len(f)
    best=float('inf');answer=None
    for status in product((0,1,2),repeat=n-1):
        blocks=[];start=0;offset=[0.0]
        for k,s in enumerate(status):
            if s==0:
                blocks.append((start,k+1,offset))
                start=k+1;offset=[0.0]
            else:offset.append(offset[-1]+(l[k] if s==1 else u[k]))
        blocks.append((start,n,offset))
        z=[0.0]*n
        for start,end,offset in blocks:
            c=p_center([f[i]-offset[i-start] for i in range(start,end)],
                        m[start:end],p[start:end])
            for i in range(start,end):z[i]=c+offset[i-start]
        if any(z[i+1]-z[i] < l[i]-1e-8 or z[i+1]-z[i]>u[i]+1e-8 for i in range(n-1)):
            continue
        value=sum(mm*abs(zz-ff)**pp for zz,ff,mm,pp in zip(z,f,m,p))
        if value<best:best=value;answer=z
    assert answer is not None
    return answer


def check_nonlinear():
    r=Random(2027)
    exponents=(1.25,1.5,1.8,2.,2.5,3.5,5.)
    for k in range(180):
        n=r.randint(2,5)
        m=[r.uniform(.25,4.) for _ in range(n)]
        p=[r.choice(exponents) for _ in range(n)]
        l=[r.uniform(-1.5,.5) for _ in range(n-1)]
        u=[a+(0 if r.random()<.13 else r.uniform(.2,2.0)) for a in l]
        x=[r.uniform(-3,3) for _ in range(n)]
        y=[r.uniform(-3,3) for _ in range(n)]
        X=constrained_fit(x,m,p,l,u);Y=constrained_fit(y,m,p,l,u)
        inp=variation([a-b for a,b in zip(x,y)])
        out=variation([a-b for a,b in zip(X,Y)])
        assert out<=inp+2e-6, (k,n,inp,out)
    print('HETEROGENEOUS_POWER_SLOPE_BOX_PAIRS_PASS',180)


def check_sharpness():
    # Active equalities on some edges; a positive-width edge supports an identity witness.
    l=[-.5,.7,.3,-1.0];u=[-.5,1.7,.3,2.0]
    f=[0.0]
    for a,b in zip(l,u):f.append(f[-1]+(a+b)/2)
    h=[0,0,1,1,1];g=[a+.01*b for a,b in zip(f,h)]
    for m,p in [([1,2,3,5,7],[1.5,2,4,1.25,5]),([4]*5,[3]*5)]:
        assert variation([a-b for a,b in zip(g,f)])>.0
        F=constrained_fit(f,m,p,l,u);G=constrained_fit(g,m,p,l,u)
        assert abs(variation([a-b for a,b in zip(G,F)])/.01-1)<1e-6
    # If every edge is fixed, all output differences are constant across vertices.
    l=[-.7,.4,1.3];u=l[:]
    F=constrained_fit([3,-5,4,0],[1,2,1,5],[1.5,2,4,3],l,u)
    G=constrained_fit([1,3,-2,6],[1,2,1,5],[1.5,2,4,3],l,u)
    assert variation([a-b for a,b in zip(F,G)])<1e-7
    print('SHARP_ONE_VERSUS_ZERO_DICHOTOMY_PASS')

if __name__=='__main__':
    check_exact_blocks();check_nonlinear();check_sharpness()
    print('ALL_SLOPE_BOX_BV_CHECKS_PASS')
