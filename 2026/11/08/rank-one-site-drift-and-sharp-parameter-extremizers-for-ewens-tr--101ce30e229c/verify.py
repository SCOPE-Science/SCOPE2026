"""Reproducibility checks for the six local Ewens ordinal-pattern laws.

Run with Python 3.9 or newer: python verify.py
All comparisons are exact integers or rational numbers.
Finite enumeration corroborates, but does not replace, the all-size proof.
"""
from itertools import permutations
from fractions import Fraction
from math import comb

PATTERNS = ('123','132','213','231','312','321')
checks = 0

def test(ok, detail):
    global checks
    assert ok, detail
    checks += 1

def pattern(triple):
    return ''.join(str(1+sum(y<x for y in triple)) for x in triple)

def coefficients(n,i):
    b,h = comb(n-1,3),comb(n-2,2)
    return {
        '123':(b,h,n-3,1),
        '132':(b-(n-i-1),n*(n-3)//2,n-i,0),
        '213':(b-(i-2),n*(n-3)//2,i-1,0),
        '231':(b+(n-i-1),h+1,i-2,0),
        '312':(b+(i-2),h+1,n-i-1,0),
        '321':(b,n*(n-3)//2,1,0),
    }

def partial_cycles(sources, outputs):
    f = dict(zip(sources, outputs))
    total = 0
    for x in sources:
        trail = [x]
        y = f[x]
        while y in f and y not in trail:
            trail.append(y)
            y=f[y]
        if y==x and x==min(trail):
            total+=1
    return total

def complete_cycles(perm):
    n=len(perm); seen=set(); total=0
    for i in range(1,n+1):
        if i not in seen:
            total+=1; j=i
            while j not in seen:
                seen.add(j); j=perm[j-1]
    return total

def rising(theta,n):
    z=Fraction(1)
    for j in range(n):z *= theta+j
    return z

def evalpoly(cs,theta):
    return sum(Fraction(c)*theta**j for j,c in enumerate(cs))

# First calculation uses only 3-source partial injections, not full permutations.
for n in range(4,13):
    for i in range(2,n):
        counts={q:[0]*4 for q in PATTERNS}
        for v in permutations(range(1,n+1),3):
            q=pattern(v)
            counts[q][partial_cycles((i-1,i,i+1),v)]+=1
        for q in PATTERNS:
            test(tuple(counts[q])==coefficients(n,i)[q],('partial',n,i,q,counts[q],coefficients(n,i)[q]))
        d=(n-1)*(n-2)*(n-3)
        test(sum(counts[q][0] for q in PATTERNS)==d,('zero-cycle total',n,i))

# Independently enumerate complete permutations weighted by their global cycles.
# This does not rely on the partial injection calculation.
for n in range(4,9):
    hist = {(i,q):[0]*(n+1) for i in range(2,n) for q in PATTERNS}
    for pi in permutations(range(1,n+1)):
        k=complete_cycles(pi)
        for i in range(2,n):
            q=pattern(pi[i-2:i+1])
            hist[(i,q)][k]+=1
    for theta in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(5)):
        z=rising(theta,n)
        d=rising(theta+n-3,3)
        probs={}
        for i in range(2,n):
            for q in PATTERNS:
                brute=sum(Fraction(a)*theta**j for j,a in enumerate(hist[(i,q)]))/z
                rhs=evalpoly(coefficients(n,i)[q],theta)/d
                test(brute==rhs,('full Ewens',n,i,theta,q,brute,rhs))
                probs[(i,q)]=brute
            test(sum(probs[(i,q)] for q in PATTERNS)==1,('normalization',n,i,theta))
        for i in range(2,n):
            for j in range(i+1,n):
                tv=sum(abs(probs[(i,q)]-probs[(j,q)]) for q in PATTERNS)/2
                exact=2*(j-i)*abs(theta**2-1)/d
                test(tv==exact,('TV',n,i,j,theta,tv,exact))

# Algebraic checks for the phase transition at size five.
# The proof, not this finite check, establishes the all-size statement.
for n in range(5,101):
    m=n-5
    positivity=m**4+15*m**3+72*m*m+116*m+18
    test(positivity>0,('strict witness polynomial',n))
    at_theta_n=Fraction(n*n-1,(2*n-1)*(2*n-2)*(2*n-3))
    zero_limit=Fraction(1,(n-1)*(n-2)*(n-3))
    test(at_theta_n>zero_limit,('high theta dominates zero limit',n))

print('PASS',checks,'exact assertions')
