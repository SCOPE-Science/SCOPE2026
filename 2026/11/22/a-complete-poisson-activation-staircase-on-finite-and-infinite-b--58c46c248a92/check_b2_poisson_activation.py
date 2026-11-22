"""Exact finite diagnostics for the weighted B2 Poisson fourth-moment theorem.

Run: python check_b2_poisson_activation.py
All arithmetic tests below use fractions; numerical threshold tests are separate.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import isclose

checks = 0

def demand(condition):
    global checks
    assert condition
    checks += 1

def is_b2(exponents):
    sums = [exponents[i] + exponents[j]
            for i in range(len(exponents)) for j in range(i, len(exponents))]
    return len(sums) == len(set(sums))

def sharp(weights):
    # Exact solution to the threshold equation on a finite B2 spectrum.
    n = len(weights)
    solutions = []
    for k in range(1, n + 1):
        t = (Fraction(k) - Fraction(1, 2)) / sum((1 / x for x in weights[:k]), Fraction())
        if weights[k-1] > t and (k == n or weights[k] <= t):
            solutions.append((k, t))
    demand(len(solutions) == 1)
    k, t = solutions[0]
    D = sum(((w-t) / w**2 for w in weights if w>t), Fraction())
    p = [(w-t) / (w**2 * D) if w > t else Fraction(0) for w in weights]
    S = sum((w*x for w,x in zip(weights,p)), Fraction())
    F = 2*S*S - sum((w*w*x*x for w,x in zip(weights,p)), Fraction())
    demand(sum(p) == 1)
    demand(F == t/D)
    demand(S == Fraction(1,2)/D)
    demand(all((w>t) == (x>0) for w,x in zip(weights,p)))
    return p,F,k,t

def l4_by_convolution(exponents, coefficients, rho):
    v = [c*rho**n for n,c in zip(exponents, coefficients)]
    conv = defaultdict(Fraction)
    for i,x in enumerate(v):
        for j,y in enumerate(v):
            conv[exponents[i]+exponents[j]] += x*y
    return sum((z*z for z in conv.values()), Fraction())

for q in (3, 4, 5):
    for n in range(2, 9):
        exponents = [0] + [q**j for j in range(n-1)]
        demand(is_b2(exponents))
        for rho in (Fraction(1, 2), Fraction(3, 4), Fraction(9,10), Fraction(49,50)):
            weights = [rho**(2*m) for m in exponents]
            p,F,k,t = sharp(weights)
            # Exact global upper bound diagnostic for several rational coefficient vectors.
            for case in range(4):
                c = [Fraction((j*7+case*3)%13-6, j+case+3) for j in range(n)]
                if not any(c):
                    continue
                v = l4_by_convolution(exponents,c,rho)
                a = sum((x*x for x in c),Fraction())
                baseline = 2*sum((w*x*x for w,x in zip(weights,c)),Fraction())**2 - sum((w*w*x**4 for w,x in zip(weights,c)),Fraction())
                demand(v == baseline)
                demand(v <= F*a*a)

# Verify exact onsets for one rich example: each k enters only once.
exponents = [0,1,3,9,27]
def g(r,k):
    return sum(r**(2*(exponents[k]-exponents[i])) for i in range(k))-(k-.5)
roots=[]
for k in range(1,len(exponents)):
    lo,hi=0.,1.
    for _ in range(90):
        mid=(lo+hi)/2
        if g(mid,k)<0:lo=mid
        else:hi=mid
    root=(lo+hi)/2
    demand(abs(g(root,k))<1e-12)
    roots.append(root)
demand(all(a<b for a,b in zip(roots,roots[1:])))
for k in range(1,len(exponents)):
    r=(roots[k-2]+roots[k-1])/2 if k>1 else roots[0]/2
    weights=[Fraction.from_float(r).limit_denominator(1000000)**(2*m) for m in exponents]
    _,_,active,_=sharp(weights)
    demand(active==k)
weights=[Fraction(999999,1000000)**(2*m) for m in exponents]
_,_,active,_=sharp(weights)
demand(active==len(exponents))
print('EXACT_B2_WATERLINE_CHECKS_PASS',checks)
print('FIVE_FREQUENCY_ONSETS', ' '.join(f'{r:.12f}' for r in roots))
