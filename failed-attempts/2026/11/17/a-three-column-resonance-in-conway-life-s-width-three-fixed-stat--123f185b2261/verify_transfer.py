"""Exact occupancy-transfer verification for B3/S23 on a 3 by n Moore torus.
Run: python verify_transfer.py  (requires sympy)."""
from math import comb
import sympy as s


def allowed(a, b, c):
    t = a + c
    return (t != 3 if b == 0 else t == 3 if b == 1
            else t == 2 if b == 2 else t <= 1)


def matrix():
    M = s.zeros(16)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if allowed(a, b, c):
                    M[4*a+b, 4*b+c] = comb(3, b)
    return M


def sccs(M):
    graph = {i: [j for j in range(16) if M[i,j]] for i in range(16)}
    reach = {}
    for v in range(16):
        seen = {v}; todo = [v]
        while todo:
            for w in graph[todo.pop()]:
                if w not in seen:
                    seen.add(w); todo.append(w)
        reach[v] = seen
    remaining = set(range(16)); components = []
    while remaining:
        v = min(remaining)
        C = {w for w in remaining if w in reach[v] and v in reach[w]}
        components.append(sorted(C)); remaining -= C
    return sorted(components,key=lambda x:(-len(x),x))

M = matrix()
components = sccs(M)
print('components',components)
# Explicit recurrent blocks and transient states
recurrent_10 = [0,1,2,3,4,7,8,10,12,13]
recurrent_3 = [5, 6, 9]
assert components[0] == recurrent_10 and components[1] == recurrent_3
assert all(len(C)==1 for C in components[2:])
B = M.extract(recurrent_10,recurrent_10)
C = M.extract(recurrent_3,recurrent_3)
x = s.Symbol('x')
f = x**10-x**9-x**8-14*x**7+6*x**6+63*x**4-63*x**3-81*x+243
assert s.expand(B.charpoly(x).as_expr()-f)==0
assert s.expand(C.charpoly(x).as_expr()-(x**3-27))==0
assert s.expand(M.charpoly(x).as_expr()-x**3*(x**3-27)*f)==0
print('characteristic',s.factor(M.charpoly(x).as_expr()))
# A positive rational super-eigenvector certifies that the primitive block has rho < 3.
v = s.Matrix([740,261,1000,456,539,235,812,901,635,598])
assert all(s.Rational(27,10)*v[i] < (B*v)[i] < s.Rational(271,100)*v[i] for i in range(10))
assert s.Poly(f,x).count_roots(s.Rational(27,10),s.Rational(271,100)) == 1
assert all(v[i] > 0 for i in range(10))
print('positive_eigenvector_bounds',list(v),'2.70 < Perron < 2.71')
N = s.eye(16)
for n in range(1,17):
    N = N*M
    whole = int(s.trace(N))
    # Contribution from the 3-cycle block is 3**(n+1) when 3 divides n.
    contribution = 3**(n+1) if n % 3 == 0 else 0
    base = int(s.trace(B**n))
    assert whole == base + contribution
    if n >= 3:print('n',n,'total',whole,'base',base,'resonant',contribution)
print('PASS: transfer, characteristic polynomial, SCC and exact traces')
