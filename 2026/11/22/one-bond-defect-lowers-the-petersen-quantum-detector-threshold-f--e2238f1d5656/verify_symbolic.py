"""Exact symbolic verification of weighted Petersen quantum capture."""
import itertools
import sympy as s

v = list(itertools.combinations(range(5), 2))
t, x = s.symbols('t x')
h = s.Matrix([[int(set(a).isdisjoint(b)) for b in v] for a in v])
assert v[0] == (0, 1) and v[7] == (2, 3)
assert h[0, 7] == h[7, 0] == 1
h[0, 7] = h[7, 0] = t
f = (x - 1)**3 * (x + 2)**2 * (x*x+t*x-2) * (x**3-(t+1)*x*x+(t-6)*x+4*t+2)
assert s.expand(h.charpoly(x).as_expr()-f) == 0
triple = [(0,1),(0,2),(0,8),(1,1),(1,2),(1,8),(2,1),(2,8),(3,1),(3,8)]
assert len(triple) == 10
power = [s.eye(10)]
for i in range(3): power.append(h*power[-1])
ct = s.Matrix.hstack(*(power[k][:,j] for k,j in triple))
assert s.factor(ct.det(method='domain-ge')) == -2*(t-1)**3
h1=h.subs(t,1)
assert s.factor(h1.charpoly(x).as_expr()) == (x-3)*(x-1)**5*(x+2)**4
assert s.Matrix.hstack(*(p.subs(t,1)[:,j] for p in power for j in (1,2,8))).rank() == 7
five = [(0,0),(0,1),(0,2),(0,4),(0,5),(1,0),(1,1),(1,2),(1,4),(2,0)]
power1 = [s.eye(10),h1,h1*h1]
c5 = s.Matrix.hstack(*(power1[k][:,j] for k,j in five))
assert c5.det() == -2
# At t=1 the 1-eigenspace dimension five makes every four sinks insufficient.
# At any t, the 1-eigenspace dimension is at least three: two sinks cannot suffice.
print('SYMBOLIC_PETERSEN_CERTIFICATE_PASSED: characteristic polynomial, minors, ranks')
