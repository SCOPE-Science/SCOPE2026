"""Exact finite regression checks for the quartic Lucas-balancing five-adic law."""
from math import gcd

def v5(x):
    if x == 0: return 100000
    v=0
    while x % 5 == 0:
        x //= 5; v += 1
    return v

def companion_mod_terms(N, modulus=None):
    c = [1,3]
    for i in range(2,N):
        val = 6*c[-1]-c[-2]
        if modulus: val %= modulus
        c.append(val)
    return c

# Exact integer recurrence and its fifth-order quartic consequence.
from sympy import symbols, expand, Poly
x=symbols('x')
poly=Poly(expand((x-1)*(x*x-34*x+1)*(x*x-1154*x+1)),x)
coeff=[int(z) for z in poly.all_coeffs()]
assert coeff[0] == 1 and len(coeff)==6
C=companion_mod_terms(270)
F=[c**4 for c in C]
for n in range(250):
    assert sum(coeff[j]*F[n+5-j] for j in range(6)) == 0

# For every k, the window-sum recurrence is also fifth-order.
# Hence its gcd over all shifts equals the gcd of its first five terms.
checks=0
for k in range(1,180):
    sums = [sum(F[i+1:i+k+1]) for i in range(5)]
    g=0
    for value in sums: g=gcd(g,value)
    expected = (0 if k%5 else (v5(k) if k%3==0 else 1))
    assert v5(g) == expected, (k,v5(g),expected)
    checks += 1

for a in range(1,6):
    m=5**a
    P=1 if a==1 else 3*5**(a-1)
    # Find least period by checking all divisors of proposed P, then verify P.
    c=companion_mod_terms(P+20,m)
    f=[pow(v,4,m) for v in c]
    assert all(f[n+P]==f[n] for n in range(16))
    for d in range(1,P):
        if P%d==0:
            assert any(f[n+d]!=f[n] for n in range(16)), (a,d)
    checks+=1
for s in range(0,4):
    k=3*5**s
    modulus=5**(s+1)
    c=companion_mod_terms(k+15, modulus)
    f=[pow(v,4,modulus) for v in c]
    for n in range(8):
        assert sum(f[n+1:n+k+1])%modulus == (3*5**s)%modulus,(s,n)
        checks+=1
print('PASS quartic recurrence:',coeff,'; integer windows:',179,'; periods and means:',checks-179)
