"""Standalone checks for the distributed-reset Brownian excursion theorem.
Run: python3 checker.py. Uses only the Python standard library.
Finite checks complement, but do not replace, the analytical proof.
"""
import math
import random

checks = 0

def close(x, y, tol=1e-11):
    global checks
    checks += 1
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y) <= tol*max(1., abs(x), abs(y)), (x,y)

def positive(x):
    global checks
    checks += 1
    assert x>0, x

def split(x, m, k):
    # independent interval-boundary Feynman-Kac solution
    d=math.sinh(k*m)
    a=math.sinh(k*(m-x))/d
    b=math.sinh(k*x)/d
    c=1-a-b
    close(a+b+c, 1., 2e-13)
    assert -2e-13 <= c <= 1.
    return a,b,c

def via_cycles(x0, m, k, law):
    ai,bi,ci=split(x0,m,k)
    am=bm=cm=0.
    for x,p in law:
        a,b,c=split(x,m,k)
        am+=p*a;bm+=p*b;cm+=p*c
    return bi+ci*bm/(1-cm)

def direct(x0,m,k,law):
    s=sum(p*math.exp(-k*x) for x,p in law)
    u=sum(p*math.exp(k*x) for x,p in law)
    z=math.exp(-k*x0)
    t=math.exp(-k*m)
    return t*(1-z)*(u+s/z)/((1-t)*(s+t*u))

def trial(m,k,x0,law,rng):
    # Every cycle uses its EXACT three competing-event probabilities.
    # Does not use the theorem's simplified two-exponential-moment formula.
    x=x0
    for _ in range(100000):
        a,b,c=split_no_test(x,m,k)
        v=rng.random()
        if v<a: return False
        if v<a+b: return True
        w=rng.random()
        running=0.
        for y,p in law:
            running+=p
            if w<=running:
                x=y;break
        else: x=law[-1][0]
    raise AssertionError('unusually long reset history')

def split_no_test(x,m,k):
    d=math.sinh(k*m)
    a=math.sinh(k*(m-x))/d
    b=math.sinh(k*x)/d
    return a,b,1-a-b

rng=random.Random(20261103)
for _ in range(1000):
    k=rng.uniform(.15,2.5)
    x0=rng.uniform(.1,2.5)
    sites=sorted(rng.uniform(.1,3.) for __ in range(4))
    weights=[rng.random() for __ in sites]
    q=sum(weights)
    law=list(zip(sites,[v/q for v in weights]))
    m=max(x0,max(sites))+rng.uniform(.15,3.)
    close(via_cycles(x0,m,k,law),direct(x0,m,k,law),3e-13)
    v=direct(x0,m,k,law)
    assert 0<v<1
    checks+=1

k=1.;a=1.;b=3.;x0=2.
lo=math.exp(-k*b); hi=math.exp(-k*a)
s=(lo+hi)/2
z=-math.log(s)/k
w=(s-lo)/(hi-lo)
assert 0<w<1
law_min=[(z,1.)]
law_max=[(a,w),(b,1-w)]
close(w,.5)
close((1-math.exp(-k*x0))/(1*s),4.140455109590319)
for m in [3.01,3.1,4.,5.,6.,8.,12.,16.]:
    vmin=direct(x0,m,k,law_min)
    vmax=direct(x0,m,k,law_max)
    assert vmin<vmax
    checks+=1
    for n in range(51):
        alpha=n/50.
        law=[(z,1-alpha),(a,alpha*w),(b,alpha*(1-w))]
        q=direct(x0,m,k,law)
        assert vmin-1e-13<=q<=vmax+1e-13
        checks+=1
        u=sum(p*math.exp(k*x) for x,p in law)
        q0=math.exp(-k*x0)
        t=math.exp(-k*m)
        moment_formula=t*(1-q0)*(u+s/q0)/((1-t)*(s+t*u))
        close(q,moment_formula)
        H=q*(1-t)/(t*(1-q0))
        recovered=s*(H-1/q0)/(1-t*H)
        close(recovered,u,2e-11)
    upper=direct(x0,m,k,law_max)
    close(upper,via_cycles(x0,m,k,law_max))
close(direct(x0,4.,k,law_max),.5,2e-14)
close(direct(x0,4.,k,law_min),.3444534739870579,1e-13)

# Numerical inspection of the large-threshold coefficient for the exact theorem.
for law in [law_min,law_max]:
    s_l=sum(p*math.exp(-k*x) for x,p in law)
    u_l=sum(p*math.exp(k*x) for x,p in law)
    coeff=(1-math.exp(-k*x0))*(u_l/s_l+math.exp(k*x0))
    for m in [16,20,24]:
        close(direct(x0,m,k,law)*math.exp(k*m),coeff,1e-5)

# Monte Carlo samples independent exact Brownian killed-cycle outcomes.
for law in [law_min,law_max]:
    target=direct(x0,4.,k,law)
    n=24000
    v=sum(trial(4.,k,x0,law,rng) for _ in range(n))/n
    assert abs(v-target)<6*math.sqrt(target*(1-target)/n)+.001, (v,target)
    checks+=1
print('PASS:',checks,'analytical-formula and independent diagnostic assertions')
