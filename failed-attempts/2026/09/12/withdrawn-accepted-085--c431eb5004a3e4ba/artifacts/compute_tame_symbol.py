"""Certified tame 4th-power symbol computation for K=Q(zeta_8) at primes above 7.

O_K/7 O_K = F7[x]/(x^4+1), x^4+1 = (x^2+3x+1)(x^2+4x+1) mod 7.
Reduction of (1-zeta_8) is u = 1-x. Tame 4th-power symbol of the pair
((1-zeta_8), pi7) at r7 is (up to inversion convention) u^((49-1)/4)=u^12.
We compute u^12 in each residue field F49 and its order.
Pure-Python integer arithmetic mod 7; no external libraries.
"""
MOD = 7

def add(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % MOD for i in range(n)]

def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i + j] = (r[i + j] + ca * cb) % MOD
    return r

def mod_poly(a, f):
    a = [c % MOD for c in a]
    while len(a) >= len(f):
        if a[-1] % MOD == 0:
            a.pop()
            continue
        c = a[-1]  # f monic
        k = len(a) - len(f)
        for i in range(len(f)):
            a[k + i] = (a[k + i] - c * f[i]) % MOD
        a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def pw(a, e, f):
    r = [1]
    b = mod_poly(a, f)
    while e:
        if e & 1:
            r = mod_poly(mul(r, b), f)
        b = mod_poly(mul(b, b), f)
        e >>= 1
    return r

def check_factor(f, g):
    # verify f*g == x^4+1 mod 7 (raw, no reduction)
    h = [c % MOD for c in mul(f, g)]
    assert h == [1, 0, 0, 0, 1], h
    print("factor check OK: (%s)(%s) = x^4+1 mod 7" % (f, g))

def disc_quad(a, b):
    # x^2 + a x + b discriminant a^2-4b
    return (a * a - 4 * b) % MOD

SQUARES = {(i * i) % MOD for i in range(MOD)}
print("squares mod 7:", sorted(SQUARES))

f1 = [1, 3, 1]
g1 = [1, 4, 1]
check_factor(f1, g1)
for f in (f1, g1):
    # leading coeff of x^2 is 1 -> quad a=f[1], b=f[0]
    d = disc_quad(f[1], f[0])
    print("factor", f, "disc =", d, "is square:", d in SQUARES, "-> irreducible:", d not in SQUARES)

for f in (f1, g1):
    u = [1, 6]  # 1 - x
    s12 = pw(u, 12, f)
    s24 = pw(u, 24, f)
    s48 = pw(u, 48, f)
    print("modulus", f, ": u^12 =", s12, " u^24 =", s24, " u^48 =", s48)
    assert s24 == [6], s24  # -1
    assert s48 == [1], s48
    assert s12 != [1] and s12 != [6], s12  # neither 1 nor -1
    print("  => u^12 has exact order 4 (primitive 4th root: squares to -1, not +-1 itself)")

print("CONCLUSION: tame symbol is primitive of order 4 for BOTH primes above 7.")
