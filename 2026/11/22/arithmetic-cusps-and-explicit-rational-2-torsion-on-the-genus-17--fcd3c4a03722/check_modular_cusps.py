"""Check the Tate invariants, level-five identities, and canonical cusp lifts."""
from collections import Counter
from math import gcd
import sympy as S

b, t = S.symbols('b t')
a1, a2, a3, a4, a6 = 1-b, -b, -b, 0, 0
b2 = a1**2+4*a2
b4 = a1*a3+2*a4
b6 = a3**2+4*a6
b8 = a1**2*a6+4*a2*a6-a1*a3*a4+a2*a3**2-a4**2
c4 = b2**2-24*b4
delta = -b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
Q = t**2+22*t+125
k = b-11-1/b
assert S.cancel(delta-b**6*k) == 0
assert S.cancel(c4-b**2*(k*k+10*k+5)) == 0
j = (t*t+250*t+3125)**3/t**5
assert S.cancel(j.subs(t,125/k)-c4**3/delta) == 0
assert S.expand(t**5*(j-1728)-(t*t-500*t-15625)**2*Q) == 0
assert S.cancel((((t/5)*(b+1/b))**2-5*Q).subs(t,125/k)) == 0
assert (5*Q).subs(t,0) == 625
assert S.limit(5*Q/t**2,t,S.oo) == 5

N = 4800
assert N*S.prod(1+S.Rational(1,p) for p in (2,3,5))/6 == 1920
assert 2743*7-4*N==1
base = Counter()
fields = {}
for d in map(int,S.divisors(N)):
    g = gcd(d,N//d)
    deg = int(S.totient(g))
    base[deg] += 1
    if d%5 == 0 and g%5 == 0:  # Infinity but sqrt(5) already in K_d
        fields[d] = (deg,deg)
    elif d%5 == 0:             # Infinity, and K_d is 2-power cyclotomic
        assert g & (g-1) == 0
        fields[d] = (2*deg,)
    else:                      # Zero: residual constant 625 is a square
        fields[d] = (deg,deg)

assert len(fields) == 42 and sum(k*v for k,v in base.items()) == 144
assert fields[1] == (1,1) and fields[25] == (2,)
counts = Counter(e for fiber in fields.values() for e in fiber)
assert sorted(counts.items()) == [(1,16),(2,16),(4,24),(8,10),(16,4)]
assert sum(counts.values()) == 70 and sum(k*v for k,v in counts.items()) == 288
print('PASS: canonical square class 5, denominator-wise cusp lifts, and degree spectrum')
