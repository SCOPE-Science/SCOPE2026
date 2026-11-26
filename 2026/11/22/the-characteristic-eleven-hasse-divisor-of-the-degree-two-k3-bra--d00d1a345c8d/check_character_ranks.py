"""Exact checks for the characteristic-eleven marked sextic Frobenius maps."""

from itertools import combinations
from sympy import Poly, symbols

x, y, z, t = symbols('x y z t')
p = 11
def univariate(f):
    return Poly(f, t, modulus=p)

def power(f, gens, n):
    factor = Poly(f, *gens, modulus=p)
    ans = Poly(1, *gens, modulus=p)
    for _ in range(n):
        ans *= factor
    return ans

def twist(f, n):
    return univariate(sum(int(c)*t**(d*p**n) for (d,), c in f.terms()))

def equivalent(pair1, pair2):
    return any(all((a-b-d)%6 == 0 for a,b in zip(pair1,pair2))
               for d in (0,2,4))

basis = [(u+1,v+1,4-u-v) for u in range(4) for v in range(4-u)]
assert all(not equivalent(a[:2],b[:2]) for a,b in combinations(basis,2))
permutation = [next(j for j,b in enumerate(basis)
                    if equivalent(tuple(p*a for a in A[:2]), b[:2])) for A in basis]
assert permutation == [0,8,7,3,6,5,4,2,1,9]

sextic = x**6 + y**6 + z**6 + t*x**2*y**2*z**2
expanded = power(sextic, (x,y,z,t), p-1)
groups = {}
for (a,b,c,d), coeff in expanded.terms():
    groups[a,b,c] = groups.get((a,b,c),0) + int(coeff)*t**d
coefficients = []
A = univariate(t**2*(1-t**3))
B = univariate(2*t*(2*t**3+1))
C = univariate(t*(t**3-1)*(t**3+2)*(t**3+4))
assert (A*B*C).degree() == 19
for i,u in enumerate(basis):
    line = [univariate(groups.get(tuple(p*a-b for a,b in zip(u,v)),0))
            for v in basis]
    h = A if i in (0,3,9) else C if i==5 else B
    assert [j for j,f in enumerate(line) if not f.is_zero] == [permutation[i]]
    assert line[permutation[i]] == h
    coefficients.append(h)

index = list(range(10)); factors = [univariate(1) for _ in index]; s = 0
for n in (1,2,3):
    s += p**(n-1)
    factors = [coefficients[j]*twist(f,1) for j,f in zip(index,factors)]
    index = [permutation[j] for j in index]
    assert index == (permutation if n%2 else list(range(10)))
    assert all(f == power(h.as_expr(),(t,),s) for f,h in zip(factors,coefficients))

def order_along(f, g):
    ans = 0
    while f.rem(g).is_zero:
        f = f.exquo(g); ans += 1
    return ans

for g, expected in [(t,[1]*7+[2]*3),(t**3-1,[0]*6+[1]*4),
                    (t**3-5,[0]*4+[1]*6),(t**3-7,[0]*9+[1]),
                    (t**3-9,[0]*9+[1]),(t**3-6,[0]*10)]:
    g = univariate(g)
    assert g.gcd(g.diff()).degree()==0
    # For these factors, no proper subfactor occurs to a different order.
    orders = [order_along(h,g) for h in coefficients]
    assert all(h.exquo(g**o).gcd(g).degree()==0 for h,o in zip(coefficients,orders))
    assert sorted(orders)==expected
    for r in range(10):
        assert min(map(sum,combinations(orders,r+1)))==sum(expected[:r+1])

b = t**3+27
models = [x**3+3*(t+6)*x**2+3*(t+3)*(t+12)*x+27*(t+3)**2,
          x**3-27*t**2*x**2+216*t*b*x-432*b**2,
          x**3+2*t*x**2+t**2*x-4,
          x**3-48*t**2*x**2+768*t*b*x-4096*b**2]
elliptic = [univariate(sum(int(c)*t**n for (m,n),c in power(f,(x,t),5).terms() if m==10))
            for f in models]
assert elliptic == [-B,C,A,B]
print('PASS: character lines, three exact twists, all local minor orders, prior elliptic factor comparison')
