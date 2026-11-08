"""Exact subtree enumeration and coefficient checks for complete bipartite graphs.

Uses only the Python standard library. The asymptotic proof is in RESULT.md;
finite checks are corroborating evidence and not replacements for that proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, exp

checks = 0

def check(condition, name):
    global checks
    if not condition:
        raise AssertionError(name)
    checks += 1

def tau(a, b):
    if a < 0 or b < 0:
        return 0
    if a + b == 1:
        return 1
    if a == 0 or b == 0:
        return 0
    return a ** (b - 1) * b ** (a - 1)

def nsubtrees(a, b, k):
    """Number of subtrees omitting k vertices, including one-vertex subtrees."""
    return sum(comb(a, i) * comb(b, k-i) * tau(a-i, b-k+i)
               for i in range(max(0, k-b), min(a, k)+1))

def brute_counts(a,b):
    n = a+b
    edges = [(i,a+j) for i in range(a) for j in range(b)]
    counts = [0]*(n+1)
    counts[1] = n
    for e in range(1, n):
        for es in combinations(edges,e):
            parent = list(range(n))
            def find(x):
                while parent[x]!=x:
                    x=parent[x]
                return x
            used=set()
            valid=True
            for u,v in es:
                used.add(u);used.add(v)
                ru,rv=find(u),find(v)
                if ru==rv:
                    valid=False;break
                parent[ru]=rv
            if valid and len(used)==e+1 and len({find(u) for u in used})==1:
                counts[e+1]+=1
    return counts

# Finite-graph enumeration is independent of the Kirchhoff formula.
for a,b in [(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)]:
    counts=brute_counts(a,b)
    for k in range(a+b):
        check(counts[a+b-k] == nsubtrees(a,b,k),f'brute {a,b,k}')
    check(counts[a+b]==tau(a,b),f'trees {a,b}')

for a in range(2,12):
    for b in range(2,12):
        den=tau(a,b)
        beta=Fraction(nsubtrees(a,b,1),den)
        r2=Fraction(nsubtrees(a,b,2),den)
        A=Fraction(a,b)*Fraction(a-1,a)**(b-1)
        B=Fraction(b,a)*Fraction(b-1,b)**(a-1)
        check(beta==A+B,f'beta {a,b}')
        two_A=Fraction(a*(a-1),2*b*b)*Fraction(a-2,a)**(b-1)
        two_B=Fraction(b*(b-1),2*a*a)*Fraction(b-2,b)**(a-1)
        two_AB=Fraction(a-1,a)**(b-2)*Fraction(b-1,b)**(a-2)
        check(r2==two_A+two_AB+two_B,f'R2 {a,b}')

for m in range(2,28):
    beta=Fraction(2)*Fraction(m-1,m)**(m-1)
    R2=Fraction(m-1,m)*Fraction(m-2,m)**(m-1)+Fraction(m-1,m)**(2*m-4)
    check(beta == Fraction(nsubtrees(m,m,1),tau(m,m)),f'balanced beta {m}')
    check(R2 == Fraction(nsubtrees(m,m,2),tau(m,m)),f'balanced R2 {m}')

# Exact rational tail formula and two independent numerical asymptotic limits.
for m in [40,80,160,320,640]:
    x=Fraction(1,m)
    f=(1-x)**(m-1)
    r2=(1-x)*(1-2*x)**(m-1)+(1-x)**(2*m-4)
    scaled=float((r2-2*f*f)*m*m)
    expected=7/(2*exp(2))
    check(abs(scaled-expected)<(4.0/m),f'balanced asymptotic {m}')

for a,b in [(30,70),(60,140),(120,280),(210,90),(420,180)]:
    den=tau(a,b)
    beta=float(Fraction(nsubtrees(a,b,1),den))
    r2=float(Fraction(nsubtrees(a,b,2),den))
    alpha=a/(a+b);gamma=b/(a+b)
    prediction=-0.5*(exp(-gamma/alpha)/gamma-exp(-alpha/gamma)/alpha)**2
    observed=(a+b)*(r2-beta**2/2)
    check(abs(observed-prediction)<20/(a+b),f'unbalanced asymptotic {a,b}')

print(f'VERIFY_OK {checks} finite and asymptotic checks')
