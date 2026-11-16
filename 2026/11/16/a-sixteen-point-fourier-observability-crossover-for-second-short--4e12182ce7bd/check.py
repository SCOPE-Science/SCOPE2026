#!/usr/bin/env python3
"""Standalone reproducibility checks for the short-span chord Fourier theorem.

Only Python standard library is required.  Rational interval tests certify the
finite transcendental inequalities; exhaustive tests corroborate exact counts.
"""
from fractions import Fraction as Q
from math import comb, cos, pi, factorial, sqrt, isclose

checks=0

def require(predicate, label):
    global checks
    checks += 1
    if not predicate:
        raise AssertionError(label)

def catalan(k):
    return comb(2*k, k)//(k+1)

def probabilities(m):
    require(m >= 4, "domain")
    p=Q(catalan(m-2),catalan(m))
    q=Q(catalan(m-4),catalan(m))
    return p,q

def lambdas(m):
    p,q=probabilities(m)
    n=2*m
    zero=p+(n-7)*q-n*p*p
    a=[float(zero)]
    for j in range(1,n):
        theta=2*pi*j/n
        d=1+2*sum(cos(k*theta) for k in (1,2,3))
        a.append(float(p)-float(q)*d)
    return a

def matchings(vertices):
    if not vertices:
        yield ()
        return
    first=vertices[0]
    for k in range(1,len(vertices),2):
        second=vertices[k]
        for left in matchings(vertices[1:k]):
            for right in matchings(vertices[k+1:]):
                yield ((first,second),)+left+right

# Exact Catalan moment counts, independently enumerating every matching.
for m in range(4,9):
    n=2*m
    p,q=probabilities(m)
    counts=[0]*n
    total=0
    for matching in matchings(tuple(range(n))):
        total+=1
        edge_set=set(matching)
        obs=[int(tuple(sorted((i,(i+3)%n))) in edge_set) for i in range(n)]
        for j in range(n):
            counts[j]+=obs[0]*obs[j]
    require(total == catalan(m),f"Catalan enumeration m={m}")
    for d in range(n):
        expected=p if d==0 else Q(0) if min(d,n-d)<=3 else q
        require(Q(counts[d],total)==expected,f"moment m={m} d={d}")

# Rigorous rational enclosure of pi via Machin's formula.
def atan_sum(x,N):
    return sum(((-1)**k)*x**(2*k+1)/Q(2*k+1) for k in range(N+1))

lo_pi=16*atan_sum(Q(1,5),21)-4*atan_sum(Q(1,239),20)
hi_pi=16*atan_sum(Q(1,5),20)-4*atan_sum(Q(1,239),21)
require(Q(314,100) < lo_pi < hi_pi < Q(315,100),"pi enclosure sanity")
require(hi_pi-lo_pi < Q(1,10**20),"pi enclosure sharp")

def cosine_sum(x,N):
    return sum((-1)**k*x**(2*k)/factorial(2*k) for k in range(N+1))

def cos_bounds_for_multiple(s,m):
    # 0 < s*pi/m < pi for m>=4 and s<=3, so cosine is decreasing.
    L=cosine_sum(Q(s,m)*hi_pi,7)
    U=cosine_sum(Q(s,m)*lo_pi,8)
    require(L<U,"alternating cosine interval")
    return L,U

# Necessary and sufficient crossover condition:
# L_0 - L_1 = q*(T(m) - (7 - D_3(pi/m))).
for m in range(4,12):
    p,q=probabilities(m)
    T=Q(2*m)*(1-p*p/q)
    lo=Q(1);hi=Q(1)
    for s in range(1,4):
        l,u=cos_bounds_for_multiple(s,m)
        lo+=2*l;hi+=2*u
    if m<=7:
        require(T < 7-hi,f"constant minimum m={m}")
    else:
        require(T > 7-lo,f"nonconstant minimum m={m}")

# For m>=12: T(m)>=12/m, while 7-D_3(pi/m)<=14*pi^2/m^2
# <140/m^2<12/m. Verify the algebraic comparison after clearing
# positive factors, and test the finite boundary m=12 separately.

for m in range(12,1000):
    p,q=probabilities(m)
    T=Q(2*m)*(1-p*p/q)
    require(T>=Q(12,m),f"rational lower T m={m}")
    require(Q(140,m*m)<Q(12,m),f"pi bound m={m}")

# Exact finite values and asymptotic upper bounds for global conditioning.
for m in range(4,8):
    p,q=probabilities(m)
    L0=p+(2*m-7)*q-2*m*p*p
    require(p+2*q < Q(21,5)*L0 if m>4 else True,
            f"sharp ratio below m=8, m={m}")
p,q=probabilities(4)
L0=p+q-8*p*p
require(L0==Q(5,98),"length-eight constant eigenvalue")
require((p+q)/L0==Q(21,5),"sharp global constant 21/5")
p,q=probabilities(8)
require((p+2*q)/(p-6*q)==Q(10,3),"m=8 global bound")
p,q=probabilities(9)
require(q/p==Q(14,143),"m=9 ratio")
require((p+2*q)/(p-7*q)==Q(19,5),"m>=9 bound")
for m in range(9,1000):
    p,q=probabilities(m)
    require(q/p<=Q(14,143),f"decreasing Catalan ratios m={m}")

# Numerical Fourier kernel reconstruction; no inference from finite tests.
for m in range(4,101):
    p,q=probabilities(m);n=2*m
    kernel=[p-p*p]+[-p*p if min(d,n-d)<=3 else q-p*p
                      for d in range(1,n)]
    vals=lambdas(m)
    for j in range(n):
        direct=sum(float(kernel[d])*cos(2*pi*j*d/n) for d in range(n))
        require(abs(vals[j]-direct)<2e-11,f"DFT m={m} j={j}")
        require(vals[j]>0,f"strict positivity m={m} j={j}")
    minimum=min(vals)
    minidx=[j for j,v in enumerate(vals) if abs(v-minimum)<1e-10]
    target=[0] if m<=7 else [1,n-1]
    require(minidx==target,f"least eigenvectors m={m}")
    ratio=max(vals)/min(vals)
    require(ratio<=4.2+1e-10,f"condition bound m={m}")

print(f"PASS: {checks} checks, including all matchings through 16 vertices, "+
      "exact rational crossover certificates, and finite Fourier diagnostics.")

