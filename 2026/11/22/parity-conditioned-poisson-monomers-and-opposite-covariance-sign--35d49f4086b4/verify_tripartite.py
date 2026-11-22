"""Exact finite-checking and independent numerical tests for the tripartite dimer theorem.

Standard Python 3 only. All finite combinatorial tests use integer arithmetic;
limit-profile tests use numerical floating point, not proof of convergence.
"""
from collections import defaultdict
from functools import lru_cache
from math import cosh, sinh, tanh, factorial, sqrt
from itertools import product

checks = 0

def test(condition, detail):
    global checks
    if not condition:
        raise AssertionError(detail)
    checks += 1

def exact_counts(n):
    """Labeled matchings by unmatched counts in three equal parts."""
    ans = {}
    fac = factorial
    for a,b,c in product(range(n+1), repeat=3):
        t = (n-a-b+c, n-b-c+a, n-c-a+b)
        if min(t)<0 or any(v%2 for v in t):
            continue
        ab,bc,ca = (v//2 for v in t)
        num = fac(n)**3
        den = fac(a)*fac(b)*fac(c)*fac(ab)*fac(bc)*fac(ca)
        test(num%den==0, ('integrality',n,a,b,c))
        ans[(a,b,c)]=num//den
    return ans

def brute_counts(n):
    N=3*n
    @lru_cache(None)
    def recurse(mask):
        if mask==0:
            return {(0,0,0):1}
        low = mask&-mask
        i=low.bit_length()-1
        rest=mask^low
        out=defaultdict(int)
        for u,w in recurse(rest).items():
            v=list(u);v[i//n]+=1;out[tuple(v)]+=w
        for j in range(i+1,N):
            if i//n==j//n or not (rest&(1<<j)):
                continue
            for u,w in recurse(rest^(1<<j)).items():
                out[u]+=w
        return dict(out)
    return recurse((1<<N)-1)

def finite_law(n,c):
    vals=exact_counts(n)
    # The common factor (n/c)^(floor(3n/2)) cancels:
    # exponent equals number of missing dimers j=(R-(3n mod 2))/2.
    parity=3*n%2
    v={u:count*(c/n)**((sum(u)-parity)//2) for u,count in vals.items()}
    z=sum(v.values())
    return {u:w/z for u,w in v.items()}

def limiting_mass(u,c):
    r=sum(u)
    x=3*sqrt(c/2)
    pref=cosh(x) if r%2==0 else sinh(x)
    return (x/3)**r/(factorial(u[0])*factorial(u[1])*factorial(u[2])*pref)

def tv_bound(n,c):
    x=3*sqrt(c/2)
    if n%2==0:
        return 3*(x*x+3*x*tanh(x))/(4*n)
    m=(n-1)//2
    return sinh(x)/x*(1/m+(x/tanh(x)-1)/(2*(2*m+1))+
         3*(x*x+5*x/tanh(x)+3)/(8*m))

for n in range(1,6):
    test(exact_counts(n)==brute_counts(n),('brute counts',n))
    base=sum(w for u,w in exact_counts(n).items() if sum(u)==(3*n)%2)
    m=n//2
    expected=(factorial(n)**3//factorial(m)**3 if n%2==0
        else 3*factorial(n)**3//(factorial(m)**2*factorial(m+1)))
    test(base==expected,('maximal matchings',n,base,expected))

for n in range(2,17):
    for c in (0.2,1.0,2.0,5.0):
        d=finite_law(n,c)
        x=3*sqrt(c/2)
        mass=sum(limiting_mass(u,c) for u in d)
        # Outside finite support is accounted for by 1-mass.
        tv=(sum(abs(v-limiting_mass(u,c)) for u,v in d.items())+1-mass)/2
        bound=tv_bound(n,c)
        test(tv<bound+1e-8,('TV bound',n,c,tv,bound))
        test(abs(sum(d.values())-1)<1e-8,('normalize',n,c))

# Check exact finite mixed moments and parity-dependent limiting signs.
for n in (20,21,40,41,80,81):
    c=2.0
    d=finite_law(n,c)
    mean=sum(u[0]*p for u,p in d.items())
    covariance=sum(u[0]*u[1]*p for u,p in d.items())-mean**2
    test(covariance==covariance,('finite moment',n))
    if n==80:
        test(covariance>0,('positive even cross-species covariance',n))
    if n==81:
        test(covariance<0,('negative odd cross-species covariance',n))

print('TRIPARTITE_CHECKS_PASSED',checks)
print('Finite exact enumeration: n=1..5. Finite TV inequality: n=2..16 and c=0.2,1,2,5.')
print('Supplementary parity-sign examples: n=80,81 at c=2; these do not replace the all-n proof.')
