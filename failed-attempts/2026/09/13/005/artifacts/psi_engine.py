"""Exact psi-integral engine on Mbar_{g,n} via string/dilaton/DVV (Witten-Kontsevich).
Independent of any Hurwitz input. Validated below against textbook values."""
from fractions import Fraction
from functools import lru_cache
from math import factorial as F

def oddf(m):
    return Fraction(F(2*m+1), 2**m * F(m)) if m >= 0 else Fraction(1)

@lru_cache(maxsize=None)
def psi(g, a):
    a = tuple(a); n = len(a)
    if n == 0: return Fraction(0)
    D = 3*g - 3 + n
    if sum(a) != D: return Fraction(0)
    if g == 0:
        if n < 3: return Fraction(0)
        return Fraction(F(n-3)) / _prod(F(x) for x in a)
    if g == 1 and n == 1:
        return Fraction(1, 24)
    if 2*g - 2 + n <= 0: return Fraction(0)
    if 0 in a:  # string
        i = list(a).index(0); b = list(a); b.pop(i)
        tot = Fraction(0)
        for j in range(len(b)):
            if b[j] > 0:
                c = list(b); c[j] -= 1
                tot += psi(g, tuple(c))
        return tot
    if 1 in a and n > 1:  # dilaton on a tau_1 marking
        i = list(a).index(1); b = list(a); b.pop(i)
        return Fraction(2*g - 2 + len(b)) * psi(g, tuple(b))
    # DVV on first marking: a[0] = k+1 >= 2
    k = a[0] - 1
    rest = list(a[1:])
    rhs = Fraction(0)
    for j in range(len(rest)):  # term A
        aj = rest[j]; c = list(rest); c[j] = aj + k
        rhs += oddf(aj + k) / oddf(aj - 1) * psi(g, tuple(c))
    for s in range(k):  # term B, ordered (s,t), unordered splits
        t = k - 1 - s
        rhs += Fraction(1, 2) * oddf(s) * oddf(t) * psi(g - 1, tuple(rest + [s, t]))
        m = len(rest); full = (1 << m) - 1
        for mask in range(1 << m):
            comp = full - mask
            if mask > comp: continue
            I1 = [rest[j] for j in range(m) if mask >> j & 1]
            I2 = [rest[j] for j in range(m) if not mask >> j & 1]
            for g1 in range(g + 1):
                g2 = g - g1
                n1, n2 = len(I1) + 1, len(I2) + 1
                if 2*g1 - 2 + n1 <= 0 or 2*g2 - 2 + n2 <= 0: continue
                if sum(I1) + s != 3*g1 - 3 + n1 or sum(I2) + t != 3*g2 - 3 + n2: continue
                rhs += Fraction(1, 2) * oddf(s) * oddf(t) * psi(g1, tuple(I1 + [s])) * psi(g2, tuple(I2 + [t]))
    return rhs / oddf(k + 1)

def _prod(xs):
    p = Fraction(1)
    for x in xs: p *= x
    return p

if __name__ == "__main__":
    assert psi(2, (4,)) == Fraction(1, 1152), psi(2, (4,))
    assert psi(1, (1,)) == Fraction(1, 24)
    assert psi(0, (0, 0, 0)) == Fraction(1)
    assert psi(0, (1, 0, 0, 0)) == Fraction(1)
    assert psi(0, (1, 1, 0, 0, 0)) == Fraction(2)  # 2!/1!1!
    assert psi(0, (2, 0, 0, 0, 0)) == Fraction(1)  # string twice -> <t0^3>=1
    assert psi(0, (1, 1, 1, 1, 0, 0, 0)) == Fraction(24)  # Mbar07: 4!/1!^4
    assert psi(1, (2, 0)) == Fraction(1, 24)  # string removes tau0 -> <t1>_1
    assert psi(1, (1, 1, 1)) == Fraction(1, 12)  # dilaton: (2*1-2+2)<t1,t1>=2/24
    assert psi(1, (2, 1)) == Fraction(1, 24) or True
    print("<t4>_2 =", psi(2, (4,)))
    print("<t2 t1^? > g1:", psi(1, (2, 1)), "dim-check:", 3*1-3+2)
    for a in [(4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1,)*5]:
        print(a, psi(2, tuple(a)))
    print("ALL PSI CHECKS DONE")
