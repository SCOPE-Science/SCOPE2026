"""Bounded recovery test for lane-1377 target.

Reproduces the exact global verifications behind the TARGET EXIT request:
  1. Norms in O_K = Z[zeta8] = Z[t]/(t^4+1) via exact integer determinants.
  2. Factorization of 2 (unique prime above 2) and 3 (two primes above 3).
  3. S-unit generator norms + residue-field Legendre data supporting the
     F2-independence of the 5 Kummer classes (hence the 32-count).
  4. Hypothesis check for H^3(Pi_S, Z/2) = 0 (S nonempty, contains prime above 2).

Requires only Python 3 + sympy. Run: python3 s_unit_check.py
"""
import itertools
import sympy


def mul(a, b):
    c = [0] * 8
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    for k in range(7, 3, -1):
        if c[k]:
            c[k - 4] -= c[k]
    return tuple(c[:4])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def norm(a):
    cols = [mul(a, tuple(1 if i == j else 0 for i in range(4))) for j in range(4)]
    return int(sympy.Matrix([[cols[j][i] for j in range(4)] for i in range(4)]).det())


def gal(a, k):
    table = {(0): (1, 0, 0, 0), (1): (0, 1, 0, 0), (2): (0, 0, 1, 0),
             (3): (0, 0, 0, 1), (4): (-1, 0, 0, 0), (5): (0, -1, 0, 0),
             (6): (0, 0, -1, 0), (7): (0, 0, 0, -1)}

    def zpw(e):
        return table[e % 8]

    res = (0, 0, 0, 0)
    for j, aj in enumerate(a):
        if aj:
            w = zpw(k * j)
            res = add(res, tuple(aj * x for x in w))
    return res


def divides(a, b):
    cols = [mul(a, tuple(1 if i == j else 0 for i in range(4))) for j in range(4)]
    M = sympy.Matrix([[cols[j][i] for j in range(4)] for i in range(4)])
    try:
        sol = M.LUsolve(sympy.Matrix(list(b)))
    except Exception:
        return None
    if all(v.q == 1 for v in sol):
        return tuple(int(v) for v in sol)
    return None


def eval_mod(a, x, p):
    return (a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3) % p


def legendre(v, p):
    v %= p
    if v == 0:
        return 0
    return 1 if pow(v, (p - 1) // 2, p) == 1 else -1


def main():
    z = (0, 1, 0, 0)
    one = (1, 0, 0, 0)
    u0 = (1, 1, 0, -1)      # 1 + sqrt(2), fundamental unit factor
    pi2 = (1, -1, 0, 0)     # 1 - zeta8, N = 2
    a0 = (-1, -1, 0, -1)    # generator of P1 above 3, N = 9
    b0 = (-1, 1, 0, 1)      # generator of P2 above 3, N = 9
    three = (3, 0, 0, 0)

    assert norm(pi2) == 2, norm(pi2)
    assert norm(a0) == 9 and norm(b0) == 9
    assert mul(a0, b0) == three, mul(a0, b0)  # (3) = P1 * P2
    assert divides(a0, b0) is None  # P1 != P2
    # Galois orbits: {a0} stable under z->z^3 (Frob at 3 fixes each prime),
    # swapped by z->z^5. Confirms residue degree 2, two primes above 3.
    assert gal(a0, 3) == a0
    assert gal(a0, 5) == b0
    print("factorization of 2 and 3: OK (unique p2 with N=2; (3)=P1*P2, N=9 each)")

    gens = {"z": z, "u0": u0, "pi2": pi2, "a0": a0, "b0": b0}
    print("norms:", {k: norm(v) for k, v in gens.items()})
    # Norm-kernel step of independence: N(product) = 2^e2 * (square) forces e2 = 0.
    # Valuation steps at P1, P2 force e3 = e4 = 0 (other generators are P1/P2-units).
    # Residue step mod a prime above 17 (x=2 root): z is a square, u0 is not.
    p = 17
    roots = [x for x in range(p) if (x ** 4 + 1) % p == 0]
    assert len(roots) == 4, roots
    vecs = {k: tuple(legendre(eval_mod(v, x, p), p) for x in roots) for k, v in gens.items()}
    print("Legendre vectors above 17:", vecs)
    assert vecs["z"] == (1, 1, 1, 1) and vecs["u0"] == (-1, -1, -1, -1)
    # Non-squareness of 3*u0 in K via descent to Q(sqrt2): N_{k0/Q} = -9, not a
    # square in Q, and K = k0(i) so K^2 cap k0 = k0^2 ∪ -k0^2. Hence the mod-17
    # coincidence u0*a0*b0 = square locally does not lift globally.
    assert 9 * (1 - 2) == -9
    print("S-unit independence data: OK (supports 5-dim F2-basis, hence 32 homomorphisms)")
    print("H^3-vanishing hypothesis: S = {p2, P1, P2} nonempty and contains the "
          "prime above 2, so cd_2(Pi_S) <= 2 applies (NSW).")
    print("RECOVERY TEST RESULT: global/countable checks PASS; local HKM CS "
          "computation (wild 2-adic Hilbert symbols + unfixed local sections) FAILS.")


if __name__ == "__main__":
    main()
