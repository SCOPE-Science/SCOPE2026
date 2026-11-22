"""Exact rational-function certificate for two-site vertex RSA on Petersen."""
from functools import lru_cache
from itertools import combinations
import sympy as sp

X, Y = sp.symbols('X Y', positive=True)
V = list(combinations(range(5), 2))
assert len(V) == 10
closed = []
for i, a in enumerate(V):
    mask = 1 << i
    for j, b in enumerate(V):
        if i != j and set(a).isdisjoint(b):
            mask |= 1 << j
    closed.append(mask)

for second, coefficient in [(7, 4), (1, -2)]:
    assert bool(closed[0] & (1 << second)) == (coefficient == 4)
    @lru_cache(None)
    def F(mask):
        if mask == 0:
            return sp.Integer(0)
        vertices = [i for i in range(10) if mask & (1 << i)]
        rates = [X if i == 0 else (Y if i == second else sp.Integer(1)) for i in vertices]
        total_rate = sum(rates)
        answer = sum(w * (1 + F(mask & ~closed[i])) for i, w in zip(vertices, rates))
        return sp.cancel(answer / total_rate)
    exact = F((1 << 10) - 1)
    guess = sp.Rational(11, 3) + coefficient * (X-1)*(Y-1) / (3*(X+2)*(Y+2)*(X+Y+1)*(X+Y+8))
    assert sp.cancel(exact - guess) == 0
    assert len(F.cache_info().__repr__()) > 0
    print(('adjacent' if coefficient == 4 else 'nonadjacent'), 'reachable_states', F.cache_info().currsize, 'PASS')
print('EXACT SYMBOLIC CERTIFICATE PASS')
