"""Finite exact-arithmetic sanity checks for torus-design extremal rigidity.

These tests do not replace the infinite-dimensional spectral proof.
Run with Python 3: python verify.py
"""
from fractions import Fraction
from itertools import combinations_with_replacement, product, permutations
from math import factorial, prod

checks = 0

def test(cond, message):
    global checks
    checks += 1
    assert cond, message

# Centered q-point grid has variance (q^2-1)/12, including q even.
for q in range(2, 10):
    a = [Fraction(2*r-q+1, 2) for r in range(q)]
    test(sum(a) == 0, ('center', q))
    test(sum(x*x for x in a)/q == Fraction(q*q-1, 12), ('variance', q))
    for d in range(1, 8):
        N = q**d
        Lsq = sum(q**(2*j) for j in range(d))
        test(Fraction(N*N-1, q*q-1) == Lsq, ('length identity',q,d))
        # Lowest eigenfrequency mean, with correct endpoint parity.
        if N > 500: continue
        if N % 2:
            k = [Fraction(j) for j in range(-(N-1)//2, (N-1)//2+1)]
        else:
            k = [Fraction(2*j-N+1, 2) for j in range(N)]
        test(sum(x*x for x in k)/N == Fraction(N*N-1, 12), ('spectrum',q,d))
        if N % 2 == 0:
            k_periodic = list(range(-N//2, N//2))
            test(Fraction(sum(x*x for x in k_periodic), N) == Fraction(N*N+2, 12), ('periodic strict gap',q,d))

# Complete small parameter census of all positive nondecreasing weight multisets
# with required total and base-q digit tiling property.
for q,d in [(2,1),(2,2),(2,3),(2,4),(2,5),
            (3,1),(3,2),(3,3),(3,4),
            (4,1),(4,2),(4,3),(5,2),(5,3)]:
    N=q**d
    total=(N-1)//(q-1)
    target=tuple(q**i for i in range(d))
    candidates=0
    successes=[]
    for tail in combinations_with_replacement(range(1,total+1),d-1):
        w=(1,)+tail
        if sum(w)!=total:
            continue
        candidates+=1
        values={sum(r*wj for r,wj in zip(digits,w)) for digits in product(range(q), repeat=d)}
        if values == set(range(N)):
            successes.append(w)
    test(successes == [target], ('digit tiling exhaustive',q,d,candidates,successes))
    test(candidates >= 1, ('nonempty census',q,d))

# Independence of all characters in the design frequency cube for the Korobov winding.
for q,d in [(2,1),(2,2),(2,3),(2,4),(2,5),
            (3,1),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3)]:
    vec=[q**j for j in range(d)]
    for m in product(range(1-q,q),repeat=d):
        if any(m):
            test(sum(x*y for x,y in zip(m,vec))!=0,('frequency annihilator',q,d,m))

# Small sign/permutation count, counting unoriented primitive winding vectors.
for q,d in [(2,1),(2,2),(2,3),(3,4)]:
    v=tuple(q**j for j in range(d))
    signs=list(product((-1,1),repeat=d))
    vectors={tuple(s*x for s,x in zip(sig,p)) for p in permutations(v) for sig in signs}
    test(len(vectors)==(2**d)*factorial(d), ('oriented count',q,d))
    unoriented={min(a,tuple(-b for b in a)) for a in vectors}
    test(len(unoriented)==(2**(d-1))*factorial(d), ('unoriented count',q,d))

print(f'PASS: {checks} exact finite assertions; analytic proof is required for all d,t and all rectifiable curves.')
