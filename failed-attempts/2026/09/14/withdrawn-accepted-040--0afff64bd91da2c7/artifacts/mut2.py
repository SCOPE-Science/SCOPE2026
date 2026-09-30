"""Fixed wall-crossing pullback mutation + seed combinatorics for Bl2 seed."""
from collections import Counter
from math import comb


def div_by_1pm(N, m):
    import sympy as sp
    x, y = sp.symbols('x y')
    if not N:
        return None
    minx = min(k[0] for k in N)
    miny = min(k[1] for k in N)
    sx = -minx if minx < 0 else 0
    sy = -miny if miny < 0 else 0
    expr = sum(c * x ** (a + sx) * y ** (b + sy) for (a, b), c in N.items())
    div = 1 + x ** m[0] * y ** m[1]
    ox = -m[0] if m[0] < 0 else 0
    oy = -m[1] if m[1] < 0 else 0
    expr2 = sp.expand(expr * x ** ox * y ** oy)
    div2 = sp.expand(div * x ** ox * y ** oy)
    q, r = sp.Poly(expr2, x, y).div(sp.Poly(div2, x, y))
    if r.is_zero is not True:
        return None
    # N = q*div / (x^sx y^sy): quotient in Laurent ring is q/(x^sx y^sy)
    qexpr = q.as_expr() / (x ** sx * y ** sy)
    ex = sp.expand(qexpr)
    Q = Counter()
    for term in ex.as_ordered_terms():
        cc, mon = term.as_coeff_mul()
        a = b = 0
        for f in mon:
            if f == x:
                a += 1
            elif f == y:
                b += 1
            elif getattr(f, 'is_Pow', False) and f.base == x:
                a += int(f.exp)
            elif getattr(f, 'is_Pow', False) and f.base == y:
                b += int(f.exp)
            else:
                return None
        try:
            cci = int(cc)
        except Exception:
            return None
        Q[(a, b)] += cci
    return {k: v for k, v in Q.items() if v != 0}


def pullback_mutate(W, v):
    v1, v2 = v
    m = (v2, -v1)
    dots = {u: u[0] * v1 + u[1] * v2 for u in W}
    P = max(dots.values())
    if P <= 0:
        N2 = Counter()
        for u, c in W.items():
            k = -(u[0] * v1 + u[1] * v2)
            for j in range(k + 1):
                key = (u[0] + j * m[0], u[1] + j * m[1])
                N2[key] += c * comb(k, j)
        return {k: vv for k, vv in N2.items() if vv != 0}
    N = Counter()
    for u, c in W.items():
        e = P - (u[0] * v1 + u[1] * v2)
        for j in range(e + 1):
            key = (u[0] + j * m[0], u[1] + j * m[1])
            N[key] += c * comb(e, j)
    cur = dict(N)
    for _ in range(P):
        q = div_by_1pm(cur, m)
        if q is None:
            return None
        cur = q
    return {k: vv for k, vv in cur.items() if vv != 0}


def trop_mut(u, v):
    s = u[0] * v[1] - u[1] * v[0]
    mm = max(0, s)
    return (u[0] + mm * v[0], u[1] + mm * v[1])


def seed_mutate(W, Vs, j):
    vj = Vs[j]
    W2 = pullback_mutate(W, vj)
    if W2 is None:
        return None, None
    Vs2 = []
    for i, v in enumerate(Vs):
        if i == j:
            Vs2.append((-vj[0], -vj[1]))
        else:
            Vs2.append(trop_mut(v, vj))
    return W2, Vs2


def apply_mat(M, pt):
    return (M[0][0] * pt[0] + M[0][1] * pt[1], M[1][0] * pt[0] + M[1][1] * pt[1])


def sl_mats(bound):
    mats = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            for c in range(-bound, bound + 1):
                for d in range(-bound, bound + 1):
                    if a * d - b * c == 1:
                        mats.append(((a, b), (c, d)))
    return mats


def find_sl(Wa, Va, Wb, Vb, bound=10):
    """Find A in SL(2,Z) with entries in bound carrying (Wa,Va)->(Wb,Vb)."""
    for M in sl_mats(bound):
        if {apply_mat(M, p): c for p, c in Wa.items()} != dict(Wb):
            continue
        if Counter(apply_mat(M, v) for v in Va) == Counter(Vb):
            return M
    return None


def find_sl_W(Wa, Wb, bound=12):
    for M in sl_mats(bound):
        if {apply_mat(M, p): c for p, c in Wa.items()} == dict(Wb):
            return M
    return None


if __name__ == '__main__':
    # sanity: Example 4.11
    W = {(1, 0): 1, (0, 1): 1}
    print('Ex4.11 mu_(1,1)(x+y) =', pullback_mutate(W, (1, 1)))
    W0 = {(1, 0): 1, (0, 1): 1, (-1, 0): 1, (0, -1): 1, (-1, -1): 1}
    V0 = [(1, -1), (-1, 1), (-1, 0), (0, -1), (1, 1)]
    for j in range(5):
        W1, V1 = seed_mutate(W0, V0, j)
        print(f'j={j} v={V0[j]} Laurent={W1 is not None}')
        if W1 is not None:
            print('  W1:', sorted(W1.items()))
            print('  V1:', V1)
    # double mutation check
    for j in range(5):
        W1, V1 = seed_mutate(W0, V0, j)
        if W1 is None:
            print(f'double j={j}: first mutation failed')
            continue
        W2, V2 = seed_mutate(W1, V1, j)
        if W2 is None:
            print(f'double j={j}: second mutation NOT Laurent')
            continue
        M = find_sl(W0, V0, W2, V2, bound=10)
        MW = find_sl_W(W0, W2, bound=12)
        print(f'double j={j}: full SL-equiv={M}, W-only SL-equiv={MW}')
        if M is None:
            print('   W2:', sorted(W2.items()))
            print('   V2:', V2)
