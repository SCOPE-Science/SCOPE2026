#!/usr/bin/env python3
"""Exhaustive lex shape-position stratification over the complete sparse box U.

U = unordered pairs {f,g} of DISTINCT signed polynomials in Q[x,y], each of
total degree exactly 2, with 2-3 nonzero terms, coefficients in {+1,-1}.
Stdlib only (fractions). Outputs stratification.csv + summary.json.
"""
import itertools
import csv
import json
import math
import sys
import time
from fractions import Fraction

MONS = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0)]
MSTR = {(2, 0): 'x^2', (1, 1): 'xy', (0, 2): 'y^2', (1, 0): 'x',
        (0, 1): 'y', (0, 0): '1'}
QUADS = {(2, 0), (1, 1), (0, 2)}


def enum_polys():
    polys = []
    for k in (2, 3):
        for supp in itertools.combinations(range(6), k):
            if not any(MONS[m] in QUADS for m in supp):
                continue
            for signs in itertools.product((1, -1), repeat=k):
                d = {}
                for mi, s in zip(supp, signs):
                    d[MONS[mi]] = Fraction(s)
                polys.append(d)
    polys.sort(key=lambda d: (tuple(sorted(d.keys())),
                              tuple(d[m] for m in sorted(d.keys()))))
    return polys


def pstr(d):
    parts = []
    for m in MONS:
        if m in d:
            c = d[m]
            s = MSTR[m]
            if s == '1':
                parts.append('+1' if c > 0 else '-1')
            else:
                parts.append('+' + s if c > 0 else '-' + s)
    t = ''.join(parts)
    return t[1:] if t.startswith('+') else t


def KEY(order):
    if order == 'lex_xy':
        return lambda e: (e[0], e[1])
    if order == 'lex_yx':
        return lambda e: (e[1], e[0])
    if order == 'grlex':
        return lambda e: (e[0] + e[1], e[0], e[1])
    raise ValueError(order)


def LT(p, key):
    return max(p.keys(), key=key)


class CapError(Exception):
    pass


def psub(a, b):
    r = dict(a)
    for k, v in b.items():
        nv = r.get(k, Fraction(0)) - v
        if nv == 0:
            r.pop(k, None)
        else:
            r[k] = nv
    return r


def pmul_monom(p, t, c):
    return {(k[0] + t[0], k[1] + t[1]): v * c for k, v in p.items()}


def mreduce(p, blt, key):
    r = dict(p)
    rem = {}
    while r:
        e = max(r.keys(), key=key)
        c = r[e]
        hit = False
        for eb, cb, b in blt:
            if eb[0] <= e[0] and eb[1] <= e[1]:
                q = c / cb
                t = (e[0] - eb[0], e[1] - eb[1])
                del r[e]
                for k2, v2 in b.items():
                    k3 = (k2[0] + t[0], k2[1] + t[1])
                    nv = r.get(k3, Fraction(0)) - q * v2
                    if nv == 0:
                        r.pop(k3, None)
                    else:
                        r[k3] = nv
                hit = True
                break
        if not hit:
            rem[e] = c
            del r[e]
    return rem


def spoly(f, g, key):
    ef = LT(f, key)
    eg = LT(g, key)
    L = (max(ef[0], eg[0]), max(ef[1], eg[1]))
    t1 = (L[0] - ef[0], L[1] - ef[1])
    t2 = (L[0] - eg[0], L[1] - eg[1])
    return psub(pmul_monom(f, t1, Fraction(1) / f[ef]),
                pmul_monom(g, t2, Fraction(1) / g[eg]))


def buchberger(f, g, order, cap=300):
    key = KEY(order)
    B = [dict(f), dict(g)]
    blt = [(LT(b, key), b[LT(b, key)], b) for b in B]
    from collections import deque
    pairs = deque([(0, 1)])
    while pairs:
        i, j = pairs.popleft()
        s = spoly(B[i], B[j], key)
        r = mreduce(s, blt, key)
        if r:
            if len(B) >= cap:
                raise CapError(order)
            B.append(r)
            n = len(B) - 1
            blt.append((LT(r, key), r[LT(r, key)], r))
            for k in range(n):
                pairs.append((k, n))
    return B


def reduced_gb(f, g, order):
    B = buchberger(f, g, order)
    key = KEY(order)
    lts = [LT(b, key) for b in B]
    keep = []
    for i, b in enumerate(B):
        drop = False
        for j in range(len(B)):
            if j == i:
                continue
            e2 = lts[j]
            ei = lts[i]
            if e2[0] <= ei[0] and e2[1] <= ei[1]:
                if e2 != ei or j < i:
                    drop = True
                    break
        if not drop:
            keep.append(b)
    R = []
    for i, b in enumerate(keep):
        others = keep[:i] + keep[i + 1:]
        blt = [(LT(o, key), o[LT(o, key)], o) for o in others]
        r = mreduce(dict(b), blt, key)
        if r:
            lc = r[LT(r, key)]
            r = {k: v / lc for k, v in r.items()}
            R.append(r)
    R.sort(key=lambda p: key(LT(p, key)))
    return R


def is_one_gb(R):
    return len(R) == 1 and set(R[0].keys()) == {(0, 0)}


# ---------------- univariate (ascending lists) ----------------
def unorm(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def udeg(p):
    p = unorm(p)
    return 0 if (len(p) == 1 and p[0] == 0) else len(p) - 1


def uis0(p):
    return all(c == 0 for c in p)


def umul(a, b):
    if uis0(a) or uis0(b):
        return [Fraction(0)]
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i + j] += ca * cb
    return unorm(r)


def umodrem(a, b):
    a = unorm(list(a))
    b = unorm(list(b))
    if uis0(b):
        raise ZeroDivisionError
    r = list(a)
    db = len(b) - 1
    cb = b[-1]
    while len(r) - 1 >= db and not uis0(r):
        dd = len(r) - 1 - db
        q = r[-1] / cb
        for i in range(len(b)):
            r[dd + i] -= q * b[i]
        r = unorm(r)
    return r


def uquo_exact(a, b):
    a = unorm(list(a))
    b = unorm(list(b))
    if uis0(b):
        raise ZeroDivisionError
    r = list(a)
    db = len(b) - 1
    cb = b[-1]
    q = [Fraction(0)] * max(len(r) - db, 0)
    while len(r) - 1 >= db and not uis0(r):
        dd = len(r) - 1 - db
        t = r[-1] / cb
        q[dd] = t
        for i in range(len(b)):
            r[dd + i] -= t * b[i]
        r = unorm(r)
    assert uis0(r), 'inexact division'
    return unorm(q)


def umonic(p):
    p = unorm(p)
    if uis0(p):
        return p
    return unorm([c / p[-1] for c in p])


def ugcd(a, b):
    a = unorm(a)
    b = unorm(b)
    while not uis0(b):
        a, b = b, umodrem(a, b)
    return umonic(a)


def uderiv(p):
    if len(p) <= 1:
        return [Fraction(0)]
    return unorm([i * p[i] for i in range(1, len(p))])


def usqfree(p):
    p = umonic(unorm(p))
    if udeg(p) == 0:
        return p
    g = ugcd(p, uderiv(p))
    return umonic(uquo_exact(p, g))


def udivides(a, b):
    if uis0(a):
        return False
    return uis0(umodrem(b, a))


# ---------------- shape tests / eliminants ----------------
def shape_xy(G):
    if len(G) != 2:
        return False
    uni = top = None
    for g in G:
        if all(e[0] == 0 for e in g):
            if uni is not None:
                return False
            uni = g
        else:
            if top is not None:
                return False
            top = g
    if uni is None or top is None:
        return False
    if (1, 0) not in top or top[(1, 0)] != 1:
        return False
    if any(e[0] not in (0, 1) for e in top):
        return False
    if sum(1 for e in top if e[0] == 1) != 1:
        return False
    return True


def shape_yx(G):
    if len(G) != 2:
        return False
    uni = top = None
    for g in G:
        if all(e[1] == 0 for e in g):
            if uni is not None:
                return False
            uni = g
        else:
            if top is not None:
                return False
            top = g
    if uni is None or top is None:
        return False
    if (0, 1) not in top or top[(0, 1)] != 1:
        return False
    if any(e[1] not in (0, 1) for e in top):
        return False
    if sum(1 for e in top if e[1] == 1) != 1:
        return False
    return True


def gb_uni_lists(G, var):
    out = []
    for g in G:
        if var == 'y' and all(e[0] == 0 for e in g):
            d = {}
            for e, v in g.items():
                d[e[1]] = v
            out.append(d)
        elif var == 'x' and all(e[1] == 0 for e in g):
            d = {}
            for e, v in g.items():
                d[e[0]] = v
            out.append(d)
    polys = []
    for d in out:
        n = max(d.keys())
        polys.append(unorm([d.get(i, Fraction(0)) for i in range(n + 1)]))
    return polys


def eliminant(G, var):
    unis = gb_uni_lists(G, var)
    if not unis:
        return None
    m = unis[0]
    for p in unis[1:]:
        m = ugcd(m, p)
    return umonic(m)


# ---------------- Sylvester resultant ----------------
def coeffs_in_x(p):
    dx = max(e[0] for e in p)
    out = []
    for i in range(dx + 1):
        d = {}
        for e, v in p.items():
            if e[0] == i:
                d[e[1]] = v
        n = max(d.keys()) if d else 0
        out.append(unorm([d.get(j, Fraction(0)) for j in range(n + 1)]))
    return unorm_lists(out)


def unorm_lists(out):
    while len(out) > 1 and uis0(out[-1]):
        out.pop()
    return out


def coeffs_in_y(p):
    dy = max(e[1] for e in p)
    out = []
    for j in range(dy + 1):
        d = {}
        for e, v in p.items():
            if e[1] == j:
                d[e[0]] = v
        n = max(d.keys()) if d else 0
        out.append(unorm([d.get(i, Fraction(0)) for i in range(n + 1)]))
    return unorm_lists(out)


def poly_det(M):
    n = len(M)
    if n == 0:
        return [Fraction(1)]
    if n == 1:
        return unorm(list(M[0][0]))
    A = [[unorm(list(c)) for c in row] for row in M]
    sign = 1
    prev = [Fraction(1)]
    for k in range(n - 1):
        if uis0(A[k][k]):
            sw = -1
            for i in range(k + 1, n):
                if not uis0(A[i][k]):
                    sw = i
                    break
            if sw == -1:
                return [Fraction(0)]
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        piv = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = uquo_exact(
                    umul_prev_sub(A[i][j], piv, A[i][k], A[k][j]), prev)
            for j in range(k + 1):
                A[i][j] = [Fraction(0)]
            A[k][i] = [Fraction(0)]
        prev = piv
    d = A[n - 1][n - 1]
    if sign == -1:
        d = [-c for c in d]
    return unorm(d)


def umul_prev_sub(aij, piv, aik, akj):
    r = umul(aij, piv)
    s = umul(aik, akj)
    n = max(len(r), len(s))
    r += [Fraction(0)] * (n - len(r))
    s += [Fraction(0)] * (n - len(s))
    return unorm([a - b for a, b in zip(r, s)])


def sylvester(fc, gc):
    m, n = len(fc) - 1, len(gc) - 1
    N = m + n
    M = []
    for i in range(n):
        M.append([[Fraction(0)]] * i + list(fc) +
                 [[Fraction(0)]] * (N - m - 1 - i))
    for i in range(m):
        M.append([[Fraction(0)]] * i + list(gc) +
                 [[Fraction(0)]] * (N - n - 1 - i))
    return poly_det(M)


def resultant_x(f, g):
    return unorm(sylvester(coeffs_in_x(f), coeffs_in_x(g)))


def resultant_y(f, g):
    return unorm(sylvester(coeffs_in_y(f), coeffs_in_y(g)))


# ---------------- staircase dimension ----------------
def staircase_dim(lts):
    xs = [a for (a, b) in lts if b == 0]
    ys = [b for (a, b) in lts if a == 0]
    if not xs or not ys:
        return None
    A, B = min(xs), min(ys)
    n = 0
    for a in range(A):
        for b in range(B):
            if not any(e[0] <= a and e[1] <= b for e in lts):
                n += 1
    return n


# ---------------- Q-factor orbits / fibers ----------------
def int_divisors(n):
    n = abs(int(n))
    if n == 0:
        return []
    s = set()
    r = int(n ** 0.5)
    for d in range(1, r + 1):
        if n % d == 0:
            s |= {d, -d, n // d, -(n // d)}
    return sorted(s)


def rat_root(p):
    p = unorm(p)
    if udeg(p) < 1:
        return None
    dens = 1
    for c in p:
        dens = dens * c.denominator // math.gcd(dens, c.denominator)
    ip = [int(c * dens) for c in p]
    while len(ip) > 1 and ip[-1] == 0:
        ip.pop()
    lead, const = ip[-1], ip[0]
    if const == 0:
        return Fraction(0)
    for a in int_divisors(const):
        for b in int_divisors(lead):
            r = Fraction(a, b)
            v = Fraction(0)
            for c in reversed(unorm(p)):
                v = v * r + c
            if v == 0:
                return r
    return None


def try_quad_split(P):
    P = umonic(unorm(P))
    S, U, T, P0 = P[3], P[2], P[1], P[0]
    if P0 == 0:
        return None
    cands = set()
    for a in int_divisors(P0.numerator):
        for b in int_divisors(P0.denominator):
            cands.add(Fraction(a, b))
    for b in sorted(cands, key=lambda x: (abs(x), x)):
        if b == 0:
            continue
        d = P0 / b
        det = d - b
        if det != 0:
            a = (T - b * S) / det
            c = S - a
        else:
            if b * S != T:
                continue
            D = S * S - 4 * (U - 2 * b)
            sq = isqrt_frac(D)
            if sq is None:
                continue
            a = (S + sq) / 2
            c = (S - sq) / 2
        if a * c + b + d == U and a * d + b * c == T and b * d == P0:
            return (umonic([b, a, Fraction(1)]), umonic([d, c, Fraction(1)]))
    return None


def isqrt_frac(D):
    if D < 0:
        return None
    n, d = D.numerator, D.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    if rn * rn == n and rd * rd == d:
        return Fraction(rn, rd)
    return None


def q_orbits(m):
    """Distinct monic Q-irreducible factors of squarefree monic m (deg<=4)."""
    facs = []
    p = umonic(unorm(m))
    while udeg(p) >= 1:
        r = rat_root(p)
        if r is None:
            break
        facs.append(umonic([-r, Fraction(1)]))
        p = umonic(uquo_exact(p, [-r, Fraction(1)]))
    d = udeg(p)
    if d == 0:
        return facs
    if d in (2, 3):
        return facs + [umonic(p)]
    if d == 4:
        s = try_quad_split(p)
        if s is None:
            return facs + [umonic(p)]
        return facs + [umonic(s[0]), umonic(s[1])]
    raise CapError('orbit-degree')


def sub_y(f, b):
    d = {}
    for e, v in f.items():
        d[e[0]] = d.get(e[0], Fraction(0)) + v * (b ** e[1])
    n = max(d.keys())
    return unorm([d.get(i, Fraction(0)) for i in range(n + 1)])


# K = Q[t]/(q)
def kadd(a, b):
    n = max(len(a), len(b))
    return unorm([(a[i] if i < len(a) else Fraction(0)) +
                  (b[i] if i < len(b) else Fraction(0)) for i in range(n)])


def ksub(a, b):
    n = max(len(a), len(b))
    return unorm([(a[i] if i < len(a) else Fraction(0)) -
                  (b[i] if i < len(b) else Fraction(0)) for i in range(n)])


def kmul(a, b, q):
    return umodrem(umul(a, b), q)


def kextgcd(a, b):
    a = unorm(a)
    b = unorm(b)
    s0, s1 = [Fraction(1)], [Fraction(0)]
    t0, t1 = [Fraction(0)], [Fraction(1)]
    while not uis0(b):
        qq = uquo_exact(a, b) if False else None
        # polynomial long division quotient
        r = list(a)
        db = len(b) - 1
        cb = b[-1]
        qq = [Fraction(0)] * max(len(r) - db, 0)
        while len(r) - 1 >= db and not uis0(r):
            dd = len(r) - 1 - db
            t = r[-1] / cb
            qq[dd] = t
            for i in range(len(b)):
                r[dd + i] -= t * b[i]
            r = unorm(r)
        a, b = b, unorm(r)
        s0, s1 = s1, ksub_plain(s0, umul(qq, s1))
        t0, t1 = t1, ksub_plain(t0, umul(qq, t1))
    return a, s0, t0


def ksub_plain(a, b):
    n = max(len(a), len(b))
    return unorm([(a[i] if i < len(a) else Fraction(0)) -
                  (b[i] if i < len(b) else Fraction(0)) for i in range(n)])


def kinv(a, q):
    g, s, _ = kextgcd(a, q)
    if udeg(g) != 0:
        raise CapError('kinv')
    c = g[0]
    return unorm([x / c for x in umodrem(umul(a, s), q)] and
                 umodrem(s, q) and [x / c for x in umodrem(s, q)])


def kx_deg(P):
    d = -1
    for i, c in enumerate(P):
        if not uis0(unorm(c)):
            d = i
    return d


def kx_norm(P):
    d = kx_deg(P)
    if d == -1:
        return [[Fraction(0)]]
    return [unorm(c) for c in P[:d + 1]]


def kx_is0(P):
    return kx_deg(P) == -1


def kx_add(A, B):
    n = max(len(A), len(B))
    return kx_norm([kadd(A[i] if i < len(A) else [Fraction(0)],
                         B[i] if i < len(B) else [Fraction(0)])
                    for i in range(n)])


def kx_smul(A, s, q):
    return kx_norm([kmul(c, s, q) for c in A])


def kx_mul(A, B, q):
    if kx_is0(A) or kx_is0(B):
        return [[Fraction(0)]]
    R = [[Fraction(0)]] * (len(A) + len(B) - 1)
    for i, ca in enumerate(A):
        for j, cb in enumerate(B):
            R[i + j] = kadd(R[i + j], kmul(ca, cb, q))
    return kx_norm(R)


def kx_modrem(A, B, q):
    A = kx_norm(A)
    B = kx_norm(B)
    if kx_is0(B):
        raise ZeroDivisionError
    R = list(A)
    db = kx_deg(B)
    lc = B[db]
    inv = kinv(lc, q)
    while kx_deg(R) >= db and not kx_is0(R):
        dd = kx_deg(R) - db
        coeff = kmul(R[kx_deg(R)], inv, q)
        for i in range(len(B)):
            R[dd + i] = ksub(R[dd + i], kmul(coeff, B[i], q))
        R = kx_norm(R)
    return R


def kx_monic(A, q):
    A = kx_norm(A)
    if kx_is0(A):
        return A
    inv = kinv(A[-1], q)
    return kx_norm([kmul(c, inv, q) for c in A])


def kx_gcd(A, B, q):
    A = kx_norm(A)
    B = kx_norm(B)
    while not kx_is0(B):
        A, B = B, kx_modrem(A, B, q)
    return kx_monic(A, q)


def kx_deriv(A):
    if len(A) <= 1:
        return [[Fraction(0)]]
    return kx_norm([[c * i for c in A[i]] if False else
                    [x * i for x in A[i]] for i in range(1, len(A))])


def kx_sqfree_deg(G, q):
    G = kx_monic(kx_norm(G), q)
    if kx_deg(G) <= 0:
        return 0
    D = kx_deriv(G)
    if kx_is0(D):
        return 0
    H = kx_gcd(G, D, q)
    if kx_deg(H) <= 0:
        return kx_deg(G)
    Q, R = kx_divmod(G, H, q)
    assert kx_is0(R)
    return kx_deg(Q)


def kx_divmod(A, B, q):
    A = kx_norm(A)
    B = kx_norm(B)
    if kx_is0(B):
        raise ZeroDivisionError
    R = list(A)
    db = kx_deg(B)
    inv = kinv(B[db], q)
    Q = [[Fraction(0)]] * max(kx_deg(R) - db + 1, 0)
    while kx_deg(R) >= db and not kx_is0(R):
        dd = kx_deg(R) - db
        coeff = kmul(R[kx_deg(R)], inv, q)
        Q[dd] = coeff
        for i in range(len(B)):
            R[dd + i] = ksub(R[dd + i], kmul(coeff, B[i], q))
        R = kx_norm(R)
    return kx_norm(Q), R


def sub_yK(f, q):
    dq = udeg(q)
    t = unorm([Fraction(0), Fraction(1)])
    tpow = [[Fraction(1)]]
    for _ in range(4):
        tpow.append(kmul(tpow[-1], t, q))
    dx = max(e[0] for e in f)
    A = [[Fraction(0)]] * (dx + 1)
    for e, v in f.items():
        A[e[0]] = kadd(A[e[0]], kmul([v], tpow[e[1]], q))
    return kx_norm(A)


def fiber_distinct(f, g, m_sq):
    """Distinct affine points over C via fibers above sqfree eliminant."""
    total = 0
    for q in q_orbits(m_sq):
        if udeg(q) == 1:
            b = -q[0]
            A, B = sub_y(f, b), sub_y(g, b)
            G = ugcd(A, B)
            if udeg(G) <= 0:
                continue
            total += udeg(usqfree(G))
        else:
            d = udeg(q)
            A, B = sub_yK(f, q), sub_yK(g, q)
            G = kx_gcd(A, B, q)
            if kx_deg(G) <= 0:
                continue
            total += d * kx_sqfree_deg(G, q)
    return total


def main():
    t0 = time.time()
    polys = enum_polys()
    strs = [pstr(p) for p in polys]
    npairs = len(polys) * (len(polys) - 1) // 2
    print(f'polys={len(polys)} pairs={npairs}', flush=True)
    rows = []
    both_fail_bases = {}
    counts = {'consistent_zd': 0, 'inconsistent': 0, 'posdim': 0,
              'shape_xy': 0, 'shape_yx': 0, 'shape_either': 0,
              'shape_both': 0, 'both_fail': 0, 'caps': 0, 'res_zero': 0,
              'res_nodiv': 0, 'dim_mismatch': 0}
    first = {'Pstar': None}
    shape_sample_checked = 0
    n = 0
    for i in range(len(polys)):
        for j in range(i + 1, len(polys)):
            n += 1
            f, g = polys[i], polys[j]
            try:
                Gxy = reduced_gb(f, g, 'lex_xy')
                Gyx = reduced_gb(f, g, 'lex_yx')
                Ggr = reduced_gb(f, g, 'grlex')
            except CapError:
                counts['caps'] += 1
                rows.append((i, j, 'CAP', 0, 0, -1, -1, -1, 0, 0,
                             -1, -1, -1, -1, -1, -1, -1))
                continue
            if is_one_gb(Gxy):
                counts['inconsistent'] += 1
                rows.append((i, j, 'INC', len(Gxy), len(Gyx), len(Ggr),
                             0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 1))
                continue
            lts = [LT(h, KEY('grlex')) for h in Ggr]
            dim = staircase_dim(lts)
            lts_xy = [LT(h, KEY('lex_xy')) for h in Gxy]
            dim_xy = staircase_dim(lts_xy)
            if dim is None or dim_xy is None:
                counts['posdim'] += 1
                rows.append((i, j, 'POS', len(Gxy), len(Gyx), len(Ggr),
                             0, 0, -1, -1, -1, -1, -1, -1, -1, 0, 1))
                continue
            if dim != dim_xy:
                counts['dim_mismatch'] += 1
            counts['consistent_zd'] += 1
            sx = shape_xy(Gxy)
            sy = shape_yx(Gyx)
            my = eliminant(Gxy, 'y')
            mx = eliminant(Gyx, 'x')
            edy = udeg(my) if my is not None else -1
            edx = udeg(mx) if mx is not None else -1
            Ry = resultant_x(f, g)
            Rx = resultant_y(f, g)
            ryd = udeg(Ry)
            rxd = udeg(Rx)
            divok = 1
            if uis0(Ry) or uis0(Rx):
                counts['res_zero'] += 1
                divok = 0 if (my is not None and not uis0(Ry) and
                              not udivides(my, Ry)) else divok
            else:
                if my is None or not udivides(my, Ry):
                    counts['res_nodiv'] += 1
                    divok = 0
                if mx is None or not udivides(mx, Rx):
                    counts['res_nodiv'] += 1
                    divok = 0
            if sx:
                counts['shape_xy'] += 1
            if sy:
                counts['shape_yx'] += 1
            if sx or sy:
                counts['shape_either'] += 1
            if sx and sy:
                counts['shape_both'] += 1
            bf = (not sx) and (not sy)
            if bf:
                counts['both_fail'] += 1
            # variety counts
            if sx:
                nd = udeg(usqfree(my))
            else:
                nd = fiber_distinct(f, g, usqfree(my))
            nm = dim
            if sx and shape_sample_checked < 300:
                chk = fiber_distinct(f, g, usqfree(my))
                assert chk == nd, f'fiber mismatch {i},{j}'
                shape_sample_checked += 1
            if bf and first['Pstar'] is None:
                first['Pstar'] = {
                    'i': i, 'j': j, 'f': strs[i], 'g': strs[j],
                    'Gxy': [pstr(h) for h in Gxy],
                    'Gyx': [pstr(h) for h in Gyx],
                    'edy': edy, 'edx': edx, 'dim': dim,
                    'n_distinct': nd, 'n_mult': nm}
            if bf and len(both_fail_bases) < 60:
                both_fail_bases[f'{i},{j}'] = {
                    'f': strs[i], 'g': strs[j],
                    'Gxy': [pstr(h) for h in Gxy],
                    'Gyx': [pstr(h) for h in Gyx]}
            rows.append((i, j, 'ZD', len(Gxy), len(Gyx), len(Ggr),
                         int(sx), int(sy), edy, edx, ryd, rxd, dim, nd,
                         nm, int(bf), divok))
            if n % 4000 == 0:
                print(f'  {n}/{npairs} {time.time()-t0:.0f}s', flush=True)
    with open('output/artifacts/stratification.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['i', 'j', 'status', 'n_lex_xy', 'n_lex_yx', 'n_grevlex',
                    'shape_xy', 'shape_yx', 'elim_deg_y', 'elim_deg_x',
                    'res_y_deg', 'res_x_deg', 'staircase_dim', 'n_distinct',
                    'n_mult', 'both_fail', 'res_div_ok'])
        w.writerows(rows)
    summary = {'n_polys': len(polys), 'n_pairs': npairs,
               'counts': counts, 'Pstar': first['Pstar'],
               'seconds': round(time.time() - t0, 1)}
    with open('output/artifacts/summary.json', 'w') as fh:
        json.dump(summary, fh, indent=1)
    with open('output/artifacts/both_fail_bases.json', 'w') as fh:
        json.dump(both_fail_bases, fh, indent=1)
    print(json.dumps(summary, indent=1)[:2000])
    print(f'done {time.time()-t0:.0f}s both_fail_stored={len(both_fail_bases)}')


if __name__ == '__main__':
    main()
