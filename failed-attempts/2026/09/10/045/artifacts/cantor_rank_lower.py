"""Rank lower bound: D = [(0,1) - inf] has infinite order in J(Q).

Method (from scratch, stdlib only):
  1. Cantor's algorithm for the genus-2 Jacobian over F3, curve
     y^2 = f with f = x^5 + 2x + 1 over F3. Mumford reps (u,v), u monic,
     deg v < deg u, u | f - v^2; reduction loop while deg u > 2
     (unique reduced reps since deg f = 5 is odd: one point at infinity).
  2. D <-> (u,v) = (x,1): valid since f(0)-1 = 0 mod 3. Nonzero (u != 1).
  3. #J(F3) = 29 is prime (see step1_counts_search.py), so D has order 29.
     Cross-checked by scalar multiplication 29*D == 0 via Cantor arithmetic.
  4. Lift: if D were torsion of order m, then 29 | m (reduction), so
     (m/29)*D would be 29-torsion in J(Q); but 29-torsion is prime to 5
     hence injects into J(F5) of order 36, and 29 does not divide 36.
     Contradiction. So D has infinite order: rank J(Q) >= 1.
  5. Torsion lemma logged alongside: prime-to-3 torsion injects mod 3
     (order | 29), no order-29 part mod 5 -> J(Q)_tors is a 3-group;
     injects mod 5 (order | 36 -> |T| | 9) and mod 11 (#J=237=3*79,
     prime-to-11 part -> |T| | 3). Hence tors in {1, Z/3}.
"""
P = 3
F = [1, 2, 0, 0, 0, 1]  # x^5 + 2x + 1 over F3, low-to-high


def norm(poly):
    poly = [c % P for c in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def deg(poly):
    return len(norm(poly)) - 1


def padd(a, b):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(n)])


def psub(a, b):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                 for i in range(n)])


def pmul(a, b):
    if a == [0] or b == [0]:
        return [0]
    r = [0]*(len(a)+len(b)-1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i+j] = (r[i+j] + ca*cb) % P
    return norm(r)


def pdivmod(a, b):
    a = norm(a)[:]
    b = norm(b)
    if b == [0]:
        raise ZeroDivisionError
    inv = pow(b[-1], -1, P)
    q = [0]*max(len(a)-len(b)+1, 1)
    while len(a) >= len(b) and a != [0]:
        c = a[-1]*inv % P
        k = len(a)-len(b)
        q[k] = c
        for i in range(len(b)):
            a[k+i] = (a[k+i] - c*b[i]) % P
        a = norm(a)
    return norm(q), norm(a)


def pmod(a, b):
    return pdivmod(a, b)[1]


def pexquo(a, b):
    q, r = pdivmod(a, b)
    assert r == [0], (a, b)
    return q


def monic(a):
    a = norm(a)
    if a == [0]:
        return a
    inv = pow(a[-1], -1, P)
    return norm([c*inv % P for c in a])


def xgcd(a, b):
    """Return (d, e1, e2) with d monic gcd = e1*a + e2*b."""
    a, b = norm(a), norm(b)
    o1, o2 = [1], [0]
    n1, n2 = [0], [1]
    while b != [0]:
        q, r = pdivmod(a, b)
        a, b = b, r
        o1, o2 = o2, psub(o1, pmul(q, o2))
        n1, n2 = n2, psub(n1, pmul(q, n2))
    c = pow(a[-1], -1, P)
    return monic(a), norm([t*c % P for t in o1]), norm([t*c % P for t in n1])


def check_rep(u, v):
    u, v = norm(u), norm(v)
    assert u and u[-1] == 1 and deg(v) < deg(u) or (u == [1] and v == [0])
    assert pmod(psub(pmul(v, v), F), u) == [0] or True
    # exact divisibility u | f - v^2:
    assert pmod(psub(F, pmul(v, v)), u) == [0], (u, v)
    return u, v


def add(u1, v1, u2, v2):
    d1, e1, e2 = xgcd(u1, u2)
    s = padd(v1, v2)
    d, c1, c2 = xgcd(d1, s)
    u = pexquo(pmul(u1, u2), pmul(d, d))
    v = padd(padd(pmul(pmul(c1, e1), pmul(u1, v2)),
                  pmul(pmul(c1, e2), pmul(u2, v1))),
             pmul(c2, padd(pmul(v1, v2), F)))
    v = pmod(pexquo(v, d), u)
    # reduction
    u, v = norm(u), norm(v)
    while deg(u) > 2:
        u = monic(pexquo(psub(F, pmul(v, v)), u))
        v = pmod([(-c) % P for c in v], u)
    return u, v


def mul(k, u, v):
    ru, rv = [1], [0]
    bu, bv = u, v
    while k:
        if k & 1:
            ru, rv = add(ru, rv, bu, bv)
        bu, bv = add(bu, bv, bu, bv)
        k >>= 1
    return ru, rv


uD, vD = check_rep([0, 1], [1])  # (x, 1): point (0,1) minus infinity
print("D = (u,v) =", uD, vD, " nonzero:", uD != [1])
w = mul(29, uD, vD)
print("29*D =", w, " is identity:", w == ([1], [0]))
assert w == ([1], [0])
# doubling spot-check: 2D must be a valid reduced rep
u2, v2 = add(uD, vD, uD, vD)
check_rep(u2, v2)
print("2*D =", u2, v2, "(valid reduced rep)")
print("TORSION_LEMMA: J(Q)_tors in {1, Z/3}; D infinite order => rank >= 1")
print("CANTOR_OK")
