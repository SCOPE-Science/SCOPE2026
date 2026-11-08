"""Exact independent finite checks for weighted wheel spanning trees.

Run with python3 checker.py. Uses only the Python standard library.
The asymptotic theorem is established analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations

checks=0

def check(flag, label):
    global checks
    assert flag, label
    checks += 1

def tau_coefficients(n):
    # P_n(t)=2T_n(1+t/2)-2, computed without floating point.
    a,b=[2],[2,1]   # 2T_0, 2T_1
    for _ in range(1,n):
        c=[0]*(len(b)+1)
        for j,v in enumerate(b):
            c[j] += 2*v
            c[j+1] += v
        for j,v in enumerate(a): c[j]-=v
        a,b=b,c
    b[0]-=2
    return b

def brute_wheel_counts(n):
    # Vertices 0..n-1 on rim, hub n; tree has n edges.
    edges=[(j,(j+1)%n,0) for j in range(n)] + [(j,n,1) for j in range(n)]
    counts=[0]*(n+1)
    for selected in combinations(edges,n):
        parent=list(range(n+1))
        def find(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        okay=True
        for u,v,_ in selected:
            a,b=find(u),find(v)
            if a==b:
                okay=False
                break
            parent[a]=b
        if okay:
            counts[sum(s for _,_,s in selected)] += 1
    return counts

def moments(counts,t):
    w=[c*t**i for i,c in enumerate(counts)]
    Z=sum(w)
    mu=sum(i*x for i,x in enumerate(w))/Z
    sec=sum(i*i*x for i,x in enumerate(w))/Z
    return mu, sec-mu*mu

def variance_from_tau(coeffs,t):
    Z=sum(c*t**i for i,c in enumerate(coeffs))
    Z1=sum(i*c*t**(i-1) for i,c in enumerate(coeffs) if i)
    Z2=sum(i*(i-1)*c*t**(i-2) for i,c in enumerate(coeffs) if i>1)
    mean=t*Z1/Z
    return mean,t*t*Z2/Z+mean-mean*mean

for n in range(3,9):
    brute=brute_wheel_counts(n)
    p=tau_coefficients(n)
    check(brute==p,('weighted tree counts',n,brute,p))
    check(p[0]==0 and p[1]==n*n and p[-1]==1,('endpoint coefficients',n))
    for t in (Fraction(1),Fraction(2),Fraction(3),Fraction(7,5)):
        a,b=moments(brute,t)
        x,y=variance_from_tau(p,t)
        check(a==x and b==y,('exact moments',n,t))

# Compare independently differentiated Chebyshev polynomial to the finite-size
# spectral expression using mpmath-free ordinary double precision, as a check
# only (not a proof).
import math
for n in range(3,41):
    p=tau_coefficients(n)
    for t in (0.5,1.0,2.0,4.0):
        cf=[float(x) for x in p]
        # Use stable polynomial Horner evaluation.
        z=sum(c*t**i for i,c in enumerate(cf))
        m=sum(i*c*t**i for i,c in enumerate(cf)) /z
        v=sum((i*i)*c*t**i for i,c in enumerate(cf))/z -m*m
        spec=math.fsum(t*(2-2*math.cos(2*math.pi*j/n))/(t+2-2*math.cos(2*math.pi*j/n))**2 for j in range(1,n))
        check(abs(v-spec)<1e-7,('spectral variance',n,t,v,spec))
print('VERIFY_OK',checks,'checks')
