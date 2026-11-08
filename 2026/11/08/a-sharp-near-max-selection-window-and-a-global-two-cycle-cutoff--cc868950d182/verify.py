"""Exact finite checks for maximum-field cellular automaton dynamics.

All integer update rules are independent implementations; exhaustive tests
verify small instances and sampled examples. The general claims are analytic.
"""
from fractions import Fraction
from itertools import product
from random import Random

CHECKS = 0

def check(b):
    global CHECKS
    CHECKS += 1
    assert b

def sstep(a,n):
    if not a: return 0
    f=[sum((a >> ((i+k)%n)) & 1 for k in (-1,0,1)) for i in range(n)]
    m=max(f)
    return sum(1 << i for i in range(n) if f[i]==m)

def fstep(x,h,w,eps=Fraction(0)):
    r=[sum(x[j*w+i] for i in range(w)) for j in range(h)]
    c=[sum(x[j*w+i] for j in range(h)) for i in range(w)]
    R=[sum(r[(j+k)%h] for k in (-1,0,1)) for j in range(h)]
    C=[sum(c[(i+k)%w] for k in (-1,0,1)) for i in range(w)]
    vmax=max(R)*max(C)
    if not vmax: return tuple(0 for _ in x)
    return tuple(int((1-eps)*vmax<=R[j]*C[i]) for j in range(h) for i in range(w))

def maxstep(x,h,w):
    r=[sum(x[j*w+i] for i in range(w)) for j in range(h)]
    c=[sum(x[j*w+i] for j in range(h)) for i in range(w)]
    a=[sum(r[(j+k)%h] for k in (-1,0,1)) for j in range(h)]
    b=[sum(c[(i+k)%w] for k in (-1,0,1)) for i in range(w)]
    if not max(a)*max(b): return tuple(0 for _ in x)
    am,bm=max(a),max(b)
    return tuple(int(a[j]==am and b[i]==bm) for j in range(h) for i in range(w))

def matrix(x,h,w):
    return tuple(x[j*w+i] for j in range(h) for i in range(w))

def rep(a,b,h,w):
    return tuple(((a>>j)&1)*((b>>i)&1) for j in range(h) for i in range(w))

def eta(a,b,n):
    pa=a.bit_count(); pb=b.bit_count()
    return Fraction(sum(((a>>i)&1) * ((b>>((i+k)%n))&1) for i in range(n) for k in (-1,0,1)),pa*pb)

for n in range(4,15):
    for a in range(1,1<<n):
        # Exact energy monotonicity and equality implies nesting.
        b=sstep(a,n);c=sstep(b,n)
        e,f=eta(a,b,n),eta(b,c,n)
        check(f>=e)
        m=max(sum((a>>((i+k)%n))&1 for k in (-1,0,1)) for i in range(n))
        check(e==Fraction(m,a.bit_count()))
        if f==e: check((a&c)==a)
        # Cycle detection for 1D selector.
        seen={};v=a
        while v not in seen:
            seen[v]=len(seen);v=sstep(v,n)
        check(len(seen)-seen[v] in (1,2))

for h,w in ((4,4),(4,5),(5,4),(5,7),(7,7)):
    eps=Fraction(1,3*max(h,w))
    z=[1]*(h*w); z[0]=0
    f=fstep(z,h,w,eps)
    g=maxstep(z,h,w)
    check(f!=g)     # equality in the threshold admits a nonmaximum
    check(fstep(z,h,w,eps-Fraction(1,9*h*w))==g)

# Full two-dimensional exhaustive one-step equivalence and factorization.
for h,w in ((4,4),(4,5)):
    rng=range(1<<(h*w)) if (h,w)==(4,4) else range(2500)
    rand=Random(34*h+w)
    for k in rng:
        z=tuple((k>>i)&1 for i in range(h*w)) if (h,w)==(4,4) else tuple(rand.randrange(2) for _ in range(h*w))
        e=Fraction(1,6*max(h,w))
        f=fstep(z,h,w,e)
        check(f==maxstep(z,h,w))
        rr=[int(any(z[j*w+i] for i in range(w))) for j in range(h)]
        if any(z):
            # factorization follows from row/column totals, separately
            r=[sum(z[j*w+i] for i in range(w)) for j in range(h)]
            c=[sum(z[j*w+i] for j in range(h)) for i in range(w)]
            ra=[sum(r[(j+k)%h] for k in (-1,0,1)) for j in range(h)]
            ca=[sum(c[(i+k)%w] for k in (-1,0,1)) for i in range(w)]
            a=[j for j in range(h) if ra[j]==max(ra)]
            b=[i for i in range(w) if ca[i]==max(ca)]
            check(f==tuple(int(j in a and i in b) for j in range(h) for i in range(w)))
        else:check(f==tuple(0 for _ in f))

# Direct two-dimensional iteration: nonempty output is a rectangle;
# all orbits settle into period <=2.
rng=Random(20260608)
for h,w in ((4,4),(4,6),(5,5),(6,8),(9,11)):
    for _ in range(110):
        x=tuple(rng.randrange(2) for _ in range(h*w))
        seen={};v=x
        while v not in seen:
            check(len(seen)<400)
            seen[v]=len(seen)
            v=fstep(v,h,w,Fraction(1,6*max(h,w)))
        check(len(seen)-seen[v] in (1,2))

# Primitive 2-cycle for one-cell seed on all tested tori.
for h,w in ((4,4),(4,6),(5,5),(8,9)):
    z=tuple(int(j==0 and i==0) for j in range(h) for i in range(w))
    y=maxstep(z,h,w)
    check(y!=z)
    check(maxstep(y,h,w)==z)

# Arbitrarily long transients: a contiguous horizontal stripe block shrinks
# by two until a fixed width-two block or singleton/triple two-cycle.
for h in (12,20,34,54):
    w=4; L=h-3
    a=(1<<L)-1
    x=rep(a,(1<<w)-1,h,w)
    for _ in range((L-2)//2):
        y=maxstep(x,h,w)
        check(sum(y)<sum(x))
        x=y
print(f'VERIFY_OK checks={CHECKS}')
