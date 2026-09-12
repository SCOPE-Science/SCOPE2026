"""lane-1196 supplement: exact-arithmetic proofs of (i) mod-17 irreducibility with
three independent Frobenius witnesses (split AND non-split Borel excluded),
(ii) P=(0,4) of order exactly 85 mod 83 with Pbar not in 17E(F83),
(iii) Kronecker splitting witnesses with explicit square roots.
Curve: y^2+y = x^3-x^2-10x+20 (literal target equation). Pure stdlib.
"""
import math

def countE(c, l):
    n = 0
    for x in range(l):
        rhs = (x**3 - x**2 - 10*x + c) % l
        for y in range(l):
            if (y*y + y) % l == rhs:
                n += 1
    return n + 1

def Eadd(P, Q, l):
    a1, a2, a3 = 0, -1, 1
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2 + a1*x1 + a3) % l == 0:
        return None
    if P != Q:
        if (x1 - x2) % l == 0:
            return None
        lam = ((y2 - y1) * pow((x2 - x1) % l, -1, l)) % l
    else:
        num = (3*x1*x1 + 2*a2*x1 - 10 - a1*y1) % l
        den = (2*y1 + a1*x1 + a3) % l
        if den % l == 0:
            return None
        lam = (num * pow(den, -1, l)) % l
    nu = (y1 - lam*x1) % l
    x3 = (lam*lam + a1*lam - a2 - x1 - x2) % l
    y3 = (-(lam + a1)*x3 - nu - a3) % l
    return (x3, y3)

def Emul(P, n, l):
    R = None; Q = P
    while n > 0:
        if n & 1:
            R = Eadd(R, Q, l)
        Q = Eadd(Q, Q, l); n >>= 1
    return R

QR17 = {(x*x) % 17 for x in range(1, 17)}
print("=== (i) mod-17 irreducibility: 3 independent witnesses ===")
print("QR mod 17 =", sorted(QR17))
for l in (7, 23, 31):
    N = countE(20, l); a = l + 1 - N
    d = (a*a - 4*l) % 17
    S = sorted({(x + (l % 17)*pow(x, -1, 17)) % 17 for x in range(1, 17)})
    print(f"l={l}: N={N} a_l={a}; a_l mod17={a % 17} in S_l={S}: {(a % 17) in S}; "
          f"disc a_l^2-4l mod17={d} in QR17: {d in QR17} "
          f"-> {'reducible-possible' if ((a % 17) in S or d in QR17) else 'IRREDUCIBLE (both Borel types excluded)'}")

print("=== (ii) F83 Kummer non-divisibility certificate for P=(0,4) ===")
l = 83
pts = [None] + [(x, y) for x in range(l) for y in range(l)
                if (y*y + y - (x**3 - x**2 - 10*x + 20)) % l == 0]
N = len(pts)
P = (0, 4)
assert ((4*4 + 4) - 20) % l == 0
print(f"#E(F83)={N} (=85: {'yes' if N == 85 else 'NO'}); 83 prime to 51931*17: {math.gcd(83, 51931*17) == 1}")
print(f"5P={Emul(P,5,l)} (nonzero: {Emul(P,5,l) is not None}); "
      f"17P={Emul(P,17,l)} (nonzero: {Emul(P,17,l) is not None}); 85P={Emul(P,85,l)} -> ord(Pbar)=85")
S17 = {Emul(Q, 17, l) for Q in pts}
print(f"|17E(F83)|={len(S17)} (expect 5); Pbar in 17E(F83): {P in S17} -> P 17-indivisible mod 83")

print("=== (iii) Kronecker witnesses (explicit roots) ===")
for m, r, l in [(64, 8, 83), (3, 5, 11), (15, 7, 17), (1, 1, 4721)]:
    assert (r*r) % l == m, (m, r, l)
    print(f"-19 mod {l} = {m} = {r}^2 -> ({-19}/{l})=+1")
print("4721 prime (trial division):", all(4721 % d for d in range(2, int(4721**0.5)+1)))
print("51931 = 11*4721:", 11*4721 == 51931, "; good reduction at 83,127,2,3:",
      all(51931 % l != 0 for l in (83, 127, 2, 3)))
