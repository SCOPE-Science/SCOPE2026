"""lane-1196 target audit: pure-stdlib, exact integer arithmetic throughout.
Curve as literally stated: E: y^2+y = x^3-x^2-10x+20, [a1,a2,a3,a4,a6]=[0,-1,1,-10,20].
Compares against Cremona 11a1 candidate [0,-1,1,-10,-20] and LMFDB newform 11.2.a.a.
"""
from fractions import Fraction

def disc_c4(a1, a2, a3, a4, a6):
    a1, a2, a3, a4, a6 = map(Fraction, (a1, a2, a3, a4, a6))
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    D = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    c4 = b2*b2 - 24*b4
    assert D.denominator == 1 and c4.denominator == 1
    return int(D), int(c4)

def factorint(n):
    n = abs(n); out = {}; d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l-1)//2, l) == 1 else -1

def count_E(F, l):
    """F(x)=x^3-x^2-10x+c. Count E(F_l) by brute force (incl. infinity)."""
    N = 1
    for x in range(l):
        rhs = (x**3 - x**2 - 10*x + F) % l
        for y in range(l):
            if (y*y + y) % l == rhs:
                N += 1
    return N

def ap_legendre(F, l):
    return -sum(legendre((1 + 4*(x**3 - x**2 - 10*x + F)) % l, l) for x in range(l))

def kronecker(a, n):
    """Kronecker (a/n), n>0, elementary."""
    assert n > 0
    if n == 1:
        return 1
    fac = factorint(n)
    r = 1
    for p, e in fac.items():
        if p == 2:
            if a % 2 == 0:
                return 0
            v = 1 if a % 8 in (1, 7) else -1
            r *= v ** e
        else:
            r *= legendre(a, p) ** e
    return r

print("=== (1) discriminant / conductor audit ===")
for name, m in [("as-stated(+20)", (0,-1,1,-10,20)), ("sign-flip(-20)", (0,-1,1,-10,-20))]:
    D, c4 = disc_c4(*m)
    print(f"{name}: Delta={D} {factorint(D)}  c4={c4} {factorint(c4)}")

print("=== (2) traces vs LMFDB newform 11.2.a.a (a2=-2,a3=-1,a5=1,a7=-2) ===")
newform = {2: -2, 3: -1, 5: 1, 7: -2}
for name, F in [("as-stated(+20)", 20), ("sign-flip(-20)", -20)]:
    row = {}
    for l in [2, 3, 5, 7]:
        a = (3 - count_E(F, l)) if l == 2 else ap_legendre(F, l)
        # cross-check brute force for odd l
        assert l == 2 or a == (l + 1 - count_E(F, l)), (name, l)
        row[l] = a
    print(f"{name}: {row}  match-11.2.a.a: {all(row[l] == newform[l] for l in row)}")

print("=== (3) P=(0,4) on as-stated curve has infinite order ===")
F = 20
assert (4*4 + 4) == (0 - 0 - 0 + 20)  # on curve
D, _ = disc_c4(0, -1, 1, -10, 20)
assert D % 2 != 0 and D % 3 != 0, "need good reduction at 2,3"
N2, N3 = count_E(F, 2), count_E(F, 3)
P2 = (0 % 2, 4 % 2); P3 = (0 % 3, 4 % 3)
print(f"#E(F2)={N2} (prime) so ord(P mod 2)=5 divides ord(P); P mod 2 = {P2} affine nonzero")
print(f"#E(F3)={N3} so prime-to-3 part of ord(P) divides 2; P mod 3 = {P3}")
print("If ord(P)=N: 5|N from mod 2; mod-3 kernel is a 3-group so 5|(prime-to-3 part of N)|2, absurd. Hence infinite order.")

print("=== (4) preliminary gate on as-stated curve ===")
N17 = count_E(20, 17); a17 = 18 - N17
print(f"N(E/F17)={N17}, a17={a17}, good (17 nmid cond 11*4721), ordinary (a17 not = 0 mod 17): {a17 % 17 != 0}")
print(f"kron(-19,11)={kronecker(-19,11)} (11 splits), kron(-19,17)={kronecker(-19,17)} (17 splits)")
print("mod-17 Borel witnesses: S_l = {{x + l*x^-1}} subset F17; reducible => a_l in S_l")
def borel_set(l):
    lm = l % 17
    return sorted({(x + lm*pow(x, -1, 17)) % 17 for x in range(1, 17)})
als = {l: ((3 - count_E(20, l)) if l == 2 else ap_legendre(20, l)) for l in [2,3,5,7,13,19,23,29,31]}
for l, a in als.items():
    S = borel_set(l)
    print(f"l={l}: a_l={a} (mod17: {a % 17}), in S_l={S}: {(a % 17) in S}")

print("=== (5) Heegner hypothesis at LITERAL level N=51931=11*4721 ===")
print(f"kron(-19,4721)={kronecker(-19,4721)}")

print("=== (6) bounded O_K-point search, K=Q(sqrt(-19)), w=(1+sqrt(-19))/2 ===")
# Represent a+b*w with integer pairs; N(a+bw)=a^2+ab+5b^2. E: y^2+y=f(x), test directly in Z[w].
def add(p, q): return (p[0]+q[0], p[1]+q[1])
def mul(p, q):
    a, b = p; c, d = q
    return (a*c - 5*b*d, a*d + b*c + b*d)  # w^2 = w-5... check: w=(1+s)/2, w^2-w+5=0 so w^2=w-5
assert mul((0,1),(0,1)) == (-5,1)
def neg(p): return (-p[0], -p[1])
def sub(p, q): return add(p, neg(q))
def is_one(p): return p == (1, 0)
def pow3(p): return mul(p, mul(p, p))
def fOK(x):
    return add(sub(sub(pow3(x), mul(x, x)), mul((10,0), x)), (20,0))
def on_curve(x, y):
    return add(mul(y, y), y) == fOK(x)
B = 4
vals = [(a, b) for a in range(-B, B+1) for b in range(-B, B+1)]
pts = []
for x in vals:
    rhs = fOK(x)
    for y in vals:
        if on_curve(x, y):
            pts.append((x, y))
print(f"box |a|,|b|<={B}: {len(pts)} O_K-points: {pts}")
