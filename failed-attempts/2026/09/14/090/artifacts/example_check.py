"""Verify the illustrating example for the TARGET theorem (no bound assumed).

Example: p=13, E: y^2 = x^3 + x + 4 over F_13, ell=3.
Checks:
 1. E is supersingular (trace 0) and j(E) = 5 (not 0, 1728 mod 13).
 2. Old hypothesis p > 4*q_j*ell^2 fails for EVERY q_j >= 1 (36 > 13).
 3. Rational 3-kernels: # = #{roots of psi_3 in F_p} = 0, matching 1 + Legendre(-p/ell).
 4. Geometric kernels: ell+1 = 4 left O-ideals of norm ell (M2(F_ell) count).
"""
p = 13
a, b = 1, 4
ell = 3

def npoints(a, b, p):
    n = 1
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        n += sum(1 for y in range(p) if (y*y) % p == rhs)
    return n

N = npoints(a, b, p)
t = p + 1 - N
D = (4*a**3 + 27*b**2) % p
j = (1728*4*a**3*pow(D, p-2, p)) % p
print("N =", N, "trace =", t, "supersingular:", t == 0)
print("j =", j, "| 1728 mod p =", 1728 % p)

# Old bound: p > 4*q*ell^2 with q >= 1 minimal
print("old bound needs p >", 4*1*ell**2, ": fails since p =", p)

# Division polynomial psi_3(x) = 3x^4 + 6a x^2 + 12b x - a^2
def psi3(x):
    return (3*x**4 + 6*a*x**2 + 12*b*x - a*a) % p
roots = [x for x in range(p) if psi3(x) == 0]
print("psi_3 F_p-roots:", roots, "-> rational 3-kernels:", len(roots))

# Legendre (-p/ell): -13 mod 3 = 2; (2/3) = -1
from math import gcd
lp = pow((-p) % ell, (ell-1)//2, ell)
leg = lp if lp == 1 else -1
print("1 + (-p/ell) =", 1 + leg)

# Separability of psi_3 (distinct geometric kernels): gcd with derivative
def poly_gcd_mod(f, g, p):
    f = list(f); g = list(g)
    while any(c % p for c in g):
        _, r = poly_divmod(f, g, p)
        f, g = g, r
    return f
def poly_divmod(f, g, p):
    f = [c % p for c in f]
    while len(f) > 1 and f[0] == 0: f.pop(0)
    while len(g) > 1 and g[0] == 0: g.pop(0)
    if len(f) < len(g): return ([0], f)
    inv = pow(g[0], p-2, p)
    q = [0]*(len(f)-len(g)+1)
    r = list(f)
    for i in range(len(q)):
        c = r[i]*inv % p
        q[i] = c
        for k in range(len(g)):
            r[i+k] = (r[i+k] - c*g[k]) % p
    return (q, r)
f = [3, 0, 6*a % p, 12*b % p, (-a*a) % p]   # psi_3 coeffs desc
fp = [(3*4) % p, 0, (12*a) % p, (12*b) % p]  # derivative
g = poly_gcd_mod(f, fp, p)
print("gcd(psi3, psi3') =", g, "(constant => 4 distinct geometric x-coords)")
print("geometric 3-subgroups = ell+1 =", ell+1)
