"""Extended exact verification for the C3 Weil-datum + torsion-free certificate.

Covers, stdlib only:
  (A) integer discriminant of F=4g+h^2 via Bareiss resultant(Sylvester 9x9),
      disc=89973248=2^9*17*10337 (trial-division factorisation), bad set {2,17,10337};
  (B) two-leg (general h(x)-model, completed-square) counts at p=7 -> (N1,N2)=(11,61),
      Weil data a=-3,b=10,#J(F7)=84;
  (C) generic completed-square counts at p in {5,11,13} -> #J in {52,138,133},
      tri-prime torsion lock: J(Q)_tors = 1;
  (D) stdlib distinct-degree factorisation types at {3,11,13,67};
  (E) logged F7 residue table.

Run: python3 output/artifacts/verify.py -> VERIFY_OK.
"""

# ---- (A) discriminant ----
FDESC = [4, -3, -6, 1, 8, 4]       # F descending x^5..x^0
FPDESC = [20, -12, -18, 2, 8]      # F' descending x^4..x^0
FASC = [4, 8, 1, -6, -3, 4]        # F ascending c0..c5
GASC = [1, 2, 0, -2, -1, 1]        # g ascending c0..c5


def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]


def discriminant_and_factors():
    rows = []
    for s in range(4):
        row = [0] * 9
        for i, c in enumerate(FDESC):
            row[s + i] = c
        rows.append(row)
    for s in range(5):
        row = [0] * 9
        for i, c in enumerate(FPDESC):
            row[s + i] = c
        rows.append(row)
    res = bareiss_det(rows)
    assert res % 4 == 0, res
    disc = res // 4
    assert disc == 89973248, disc
    n, fac, d = disc, {}, 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    assert fac == {2: 9, 17: 1, 10337: 1}, fac
    return disc


# ---- (B/C) point counts ----
P7 = 7
H = lambda x: x * x + x
G = lambda x: x**5 - x**4 - 2 * x**3 + 2 * x + 1


def add7(u, v):
    return ((u[0] + v[0]) % 7, (u[1] + v[1]) % 7)


def mul7(u, v):
    return ((u[0] * v[0] - u[1] * v[1]) % 7,
            (u[0] * v[1] + u[1] * v[0]) % 7)


def pw7(u, n):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul7(r, u)
        u = mul7(u, u)
        n >>= 1
    return r


def eval7(coeffs_asc, x):
    r = (0, 0)
    for k in reversed(coeffs_asc):
        r = mul7(r, x)
        r = ((r[0] + k) % 7, r[1])
    return r


def count_general_7():
    n1 = sum(1 for x in range(7) for y in range(7)
             if (y * y + (H(x) % 7) * y - (G(x) % 7)) % 7 == 0) + 1
    n2 = 0
    for a in range(7):
        for b in range(7):
            x = (a, b)
            hx = add7(mul7(x, x), x)
            gx = eval7(GASC, x)
            for c in range(7):
                for d in range(7):
                    y = (c, d)
                    if add7(mul7(y, y), mul7(hx, y)) == gx:
                        n2 += 1
    return n1, n2 + 1


def count_sq_7():
    n1 = sum(1 + (0 if (v := sum(FASC[k] * a**k
                                 for k in range(6)) % 7) == 0
                   else (1 if pow(v, 3, 7) == 1 else -1))
             for a in range(7)) + 1
    n2 = 0
    for a in range(7):
        for b in range(7):
            v = eval7(FASC, (a, b))
            if v == (0, 0):
                n2 += 1
            elif pw7(v, 24) == (1, 0):
                n2 += 2
    return n1, n2 + 1


def count_sq_generic(p):
    fc = [c % p for c in FASC]

    def fe(a):
        r = 0
        for k in reversed(fc):
            r = (r * a + k) % p
        return r

    n1 = sum(1 + (0 if fe(a) == 0
                  else (1 if pow(fe(a), (p - 1) // 2, p) == 1 else -1))
             for a in range(p)) + 1
    # F_{p^2} via t^2+1 if -1 non-residue else t^2+2
    def is_res(n):
        n %= p
        return True if n == 0 else pow(n, (p - 1) // 2, p) == 1
    c0 = 1 if not is_res(-1) else 2
    assert not is_res(-c0), (p, c0)

    def add(u, v):
        return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)

    def mul(u, v):
        return ((u[0] * v[0] - u[1] * v[1] * c0) % p,
                (u[0] * v[1] + u[1] * v[0]) % p)

    def pw(u, n):
        r = (1, 0)
        while n:
            if n & 1:
                r = mul(r, u)
            u = mul(u, u)
            n >>= 1
        return r

    def fe2(x):
        r = (0, 0)
        for k in reversed(fc):
            r = mul(r, x)
            r = ((r[0] + k) % p, r[1])
        return r

    q = p * p
    n2 = 0
    for a in range(p):
        for b in range(p):
            v = fe2((a, b))
            if v == (0, 0):
                n2 += 1
            elif pw(v, (q - 1) // 2) == (1, 0):
                n2 += 2
    return n1, n2 + 1


def weil(p, n1, n2):
    a = p + 1 - n1
    s = p * p + 1 - n2
    assert (a * a - s) % 2 == 0
    b = (a * a - s) // 2
    return a, b, 1 - a + b - a * p + p * p


# ---- (D) distinct-degree factorisation ----
def pnorm(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pdeg(a, p):
    a = pnorm(a, p)
    return -1 if len(a) == 1 and a[0] == 0 else len(a) - 1


def pmul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    return pnorm(r, p)


def psub(a, b, p):
    n = max(len(a), len(b))
    return pnorm([((a[i] if i < len(a) else 0)
                   - (b[i] if i < len(b) else 0)) % p for i in range(n)], p)


def pmod(a, b, p):
    a = pnorm(a, p)
    b = pnorm(b, p)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and pdeg(a, p) >= 0:
        c = a[-1] * inv % p
        d = len(a) - len(b)
        for i, x in enumerate(b):
            a[d + i] = (a[d + i] - c * x) % p
        a = pnorm(a, p)
    return a


def pgcd(a, b, p):
    a, b = pnorm(a, p), pnorm(b, p)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, pmod(a, b, p)
    return a


def pquo(a, b, p):
    a = pnorm(a, p)
    b = pnorm(b, p)
    inv = pow(b[-1], -1, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and pdeg(a, p) >= 0:
        c = a[-1] * inv % p
        d = len(a) - len(b)
        q[d] = c
        for i, x in enumerate(b):
            a[d + i] = (a[d + i] - c * x) % p
        a = pnorm(a, p)
    return pnorm(q, p)


def ppowmod(base, e, m, p):
    r, b = [1], pnorm(base, p)
    while e:
        if e & 1:
            r = pmod(pmul(r, b, p), m, p)
        b = pmod(pmul(b, b, p), m, p)
        e >>= 1
    return r


def factor_degrees(coeffs_asc, p):
    f = pnorm(coeffs_asc, p)
    assert pdeg(f, p) == 5, (p, f)
    fp = pnorm([(i * c) % p for i, c in enumerate(f)][1:] or [0], p)
    assert pdeg(pgcd(f, fp, p), p) == 0 or pgcd(f, fp, p) == [1], "singular"
    degs, rem = [], pnorm(f, p)
    for i in range(1, 6):
        xp = ppowmod([0, 1], p**i, rem, p)
        g = pgcd(psub(xp, [0, 1], p), rem, p)
        gd = pdeg(g, p)
        if gd > 0:
            assert gd % i == 0
            degs.extend([i] * (gd // i))
            rem = pquo(rem, g, p)
        if pdeg(rem, p) == 0:
            break
    return sorted(degs)


def modp_roots(coeffs_asc, p):
    return [a for a in range(p)
            if sum(c * a**k for k, c in enumerate(coeffs_asc)) % p == 0]


def main():
    disc = discriminant_and_factors()
    n1a, n2a = count_general_7()
    n1b, n2b = count_sq_7()
    assert (n1a, n2a) == (11, 61), (n1a, n2a)
    assert (n1b, n2b) == (11, 61), (n1b, n2b)
    a7, b7, J7 = weil(7, n1a, n2a)
    assert (a7, b7, J7, a7 * a7 - 4 * b7) == (-3, 10, 84, -31)
    assert abs(a7) <= 2 * 7 ** 0.5
    # logged F7 residue table
    tab = {}
    for x in range(7):
        tab[x] = sorted(y for y in range(7)
                        if (y * y + (H(x) % 7) * y - (G(x) % 7)) % 7 == 0)
    assert tab == {0: [1, 6], 1: [2, 3], 2: [4], 3: [3, 6],
                   4: [4], 5: [0, 5], 6: []}, tab
    # torsion lock at 5, 11, 13
    got = {}
    for p in (5, 11, 13):
        n1, n2 = count_sq_generic(p)
        got[p] = (n1, n2, weil(p, n1, n2))
    assert got[5][:2] == (9, 33) and got[5][2][2] == 52, got[5]
    assert got[11][:2] == (12, 154) and got[11][2][2] == 138, got[11]
    assert got[13][:2] == (11, 171) and got[13][2][2] == 133, got[13]
    # J(Q)_tors = 1: any prime l | #tors, l not in {7,11,13}, divides
    # gcd(84,138,133) = 1 (impossible); l in {7,11,13} killed by a prime
    # q not equal l whose J-order is coprime to l:
    #   7-part via q=11 (7 not | 138), 11-part via q=7 (11 not | 84),
    #   13-part via q=7 (13 not | 84); and 2,3-parts via q=13 (not | 133).
    import math
    assert math.gcd(math.gcd(84, 138), 133) == 1
    assert 84 % 11 != 0 and 84 % 13 != 0 and 138 % 7 != 0 and 133 % 2 != 0 and 133 % 3 != 0
    for q in (5, 7, 11, 13):
        assert disc % q != 0, q  # good reduction for the odd-degree model
    # Frobenius signatures
    assert factor_degrees(FASC, 7) == [1, 1, 3]  # also certifies separability mod 7
    assert factor_degrees(FASC, 3) == [2, 3]
    assert factor_degrees(FASC, 11) == [1, 4]
    assert factor_degrees(FASC, 13) == [5]
    assert factor_degrees(FASC, 67) == [1, 1, 1, 2]
    assert modp_roots(FASC, 13) == []
    assert modp_roots(FASC, 67) == [15, 28, 57]
    assert disc == 89973248
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
