"""Exact Markov-recursion verification for Q3 directional-rate growth.

Requires SymPy (tested with SymPy 1.13). Run: python verify_symbolic.py
"""
from functools import lru_cache
from sympy import Integer, Symbol, cancel, diff, simplify, together

z = Symbol('z', positive=True)
rates = (Integer(1), Integer(1), z)
# Coefficients listed in ascending powers.
N3 = (3616, 26912, 82162, 137585, 139614, 88714, 35054, 8229, 1035, 54)
N5 = (448, 1728, 3076, 3334, 2814, 2428, 1851, 890, 213, 18)
N7 = (16, 8, 1, 4, 16, 21, 9)
R = (25600, 150528, 423552, 752864, 919752, 785388, 461900, 180178, 43542, 5724, 297)

def polynomial(coefficients):
    return sum((Integer(c) * z**i for i, c in enumerate(coefficients)), Integer(0))

D = 8 * (z + 1)**2 * (z + 2)**3 * (z + 4)**2 * (3*z + 2)**2
expected = (polynomial(N3)/D, polynomial(N5)/D,
            polynomial(N7)*(z+2)/D)

@lru_cache(None)
def length_law(labels):
    if labels[7] >= 0:
        return tuple(Integer(labels[7] == length) for length in (3,5,7))
    infected = sum(1 << v for v, x in enumerate(labels) if x >= 0)
    cut = [(u, u^(1 << i), rates[i])
           for u in range(8) if (infected >> u) & 1
           for i in range(3) if not (infected >> (u^(1 << i))) & 1]
    total = sum((r for _,_,r in cut), Integer(0))
    numerators = [Integer(0), Integer(0), Integer(0)]
    for u, v, r in cut:
        following = list(labels)
        following[v] = labels[u] + 1
        child = length_law(tuple(following))
        for j in range(3):
            numerators[j] += r*child[j]
    return tuple(cancel(x/total) for x in numerators)

start = [-1]*8
start[0] = 0
actual = length_law(tuple(start))
assert len(length_law.cache_info().__repr__()) > 0
for result, target in zip(actual, expected):
    assert cancel(result-target) == 0
assert simplify(sum(actual)-1) == 0
assert tuple(cancel(x.subs(z,1)) for x in actual) == (Integer(6973)/7200, Integer(7)/225, Integer(1)/2400)
Dprime = 8*(z+1)**3*(z+2)**4*(z+4)**3*(3*z+2)**3
assert cancel(diff(actual[0],z) + (z-1)*polynomial(R)/Dprime) == 0
# Different state variable: only the set of geodesically infected vertices.
@lru_cache(None)
def geodesic_law(infected, good):
    if infected & (1 << 7):
        return Integer(bool(good & (1 << 7)))
    cut = [(u, u^(1 << i), rates[i])
           for u in range(8) if (infected >> u) & 1
           for i in range(3) if not (infected >> (u^(1 << i))) & 1]
    total = sum((r for _,_,r in cut), Integer(0))
    numerator = Integer(0)
    for u,v,r in cut:
        valid = ((good >> u) & 1) and (v.bit_count() == u.bit_count()+1)
        numerator += r*geodesic_law(infected | (1 << v),
                                    good | ((1 << v) if valid else 0))
    return cancel(numerator/total)
assert cancel(geodesic_law(1,1)-expected[0]) == 0
print('PASS: exact P3/P5/P7 for all z>0; derivative factorization; two state representations')
print('Full hop-label states:', length_law.cache_info().currsize)
print('Geodesic-bit states:', geodesic_law.cache_info().currsize)
