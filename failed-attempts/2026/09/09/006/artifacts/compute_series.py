#!/usr/bin/env python3
"""Lane-278: committed window + exact Steinberg data + Sturm brackets.

CORRECT Steinberg form (checked vs C2^3 and infinite dihedral):
  g(t) = sum_{T sph} (-1)^|T| t^{l_T} / W_T(t) = 1/W(t) as formal power series,
l_T = longest-element length of W_T (0 for empty). g(0)=1 always.
W(t) = D(t)/Q(t) ordinary rational; omega = 1/R, R = min-modulus zero of Q.
This script: builds g, reduces, series coefficients (exact recurrence),
Sturm-bracketed smallest positive zero r in [a,b] (omega >= 1/b rigorous).
Upper bounds via Routh-Hurwitz in routh.py.
"""
import json, itertools
from fractions import Fraction
from sympy import symbols, Poly, Rational
from sympy import S as SYMS
from sympy import sturm as sym_sturm, together, fraction, gcd as sym_gcd

t = symbols('t')

SYSTEMS = {
    "A": {"rank": 3, "M": [[1,3,4],[3,1,3],[4,3,1]],
          "desc": "triangle [3,3,4] compact hyperbolic"},
    "B": {"rank": 3, "M": [[1,3,5],[3,1,3],[5,3,1]],
          "desc": "triangle [3,3,5] compact hyperbolic"},
    "C": {"rank": 3, "M": [[1,3,4],[3,1,4],[4,4,1]],
          "desc": "triangle [3,4,4] compact hyperbolic"},
    "D": {"rank": 3, "M": [[1,3,0],[3,1,3],[0,3,1]],
          "desc": "triangle [3,3,inf]"},
    "E": {"rank": 3, "M": [[1,2,0],[2,1,4],[0,4,1]],
          "desc": "triangle [2,4,inf] (right-angled vertex + m=4 edge)"},
    "F": {"rank": 4, "M": [[1,3,4,2],[3,1,3,2],[4,3,1,3],[2,2,3,1]],
          "desc": "rank-4: hyperbolic triangle [3,3,4] on {0,1,2} + pendant m=3 at node 2"},
    "G": {"rank": 4, "M": [[1,3,2,2],[3,1,4,2],[2,4,1,0],[2,2,0,1]],
          "desc": "rank-4 path [3,4,inf]"},
}

RANK3_FINITE_PATHS = {(3,3): "A3", (3,4): "B3", (3,5): "H3"}
DEGREES = {"A1": (2,), "A3": (2,3,4), "B3": (2,4,6), "H3": (2,6,10)}

def comp_data(c):
    """(poincare poly degrees list, longest length l). I2(m): degs (2,m), l=m."""
    if c[0] == "A1":
        return ([2], 1)
    if c[0] == "I2":
        return ([2, c[1]], c[1])
    return (list(DEGREES[c[0]]), sum(d-1 for d in DEGREES[c[0]]))

def classify(nodes, M):
    nodes = tuple(nodes)
    if len(nodes) == 0:
        return []
    sub = {(a,b): M[a][b] for a in nodes for b in nodes if a < b}
    if any(m == 0 for m in sub.values()):
        return None
    if len(nodes) == 1:
        return [("A1",)]
    if len(nodes) == 2:
        i, j = nodes
        m = M[i][j]
        if m == 2:
            return [("A1",), ("A1",)]
        return [("I2", m)]
    if len(nodes) == 3:
        edges = [(a,b,m) for (a,b),m in sub.items() if m > 2]
        if len(edges) == 0:
            return [("A1",), ("A1",), ("A1",)]
        if len(edges) == 1:
            return [("I2", edges[0][2]), ("A1",)]
        if len(edges) == 2:
            labs = tuple(sorted(m for _,_,m in edges))
            if labs in RANK3_FINITE_PATHS:
                return [(RANK3_FINITE_PATHS[labs],)]
            return None
        return None
    assert len(nodes) == 4
    return None

def connected_full(M):
    r = len(M); seen = {0}; stack = [0]
    while stack:
        i = stack.pop()
        for j in range(r):
            if j != i and M[i][j] != 2 and j not in seen:
                seen.add(j); stack.append(j)
    return len(seen) == r

def bracket(k):
    return sum(t**i for i in range(k))

def term_expr(comps):
    p = SYMS.One; l = 0
    for c in comps:
        degs, ll = comp_data(c)
        l += ll
        for d in degs:
            p *= bracket(d)
    return t**l, p

def series_fromQD(Nq, Dq, n):
    assert Nq[0] == 1 and Dq[0] == 1
    a = [Fraction(0)]*(n+1)
    for m in range(n+1):
        nm = Fraction(Nq[m]) if m < len(Nq) else Fraction(0)
        a[m] = nm - sum(Fraction(Dq[k])*a[m-k] for k in range(1, min(m, len(Dq)-1)+1))
    assert all(x.denominator == 1 for x in a)
    return [int(x) for x in a]

def sturm_count(P, a, b):
    sq = sym_sturm(P)
    def V(x):
        s = []
        for q in sq:
            v = q.eval(x)
            if v > 0: s.append(1)
            elif v < 0: s.append(-1)
        return sum(1 for i in range(1,len(s)) if s[i] != s[i-1])
    return V(Rational(a.numerator,a.denominator)) - V(Rational(b.numerator,b.denominator))

def smallest_pos_root(Q):
    assert Q.eval(0) == 1
    N = 2000
    prev_x = Fraction(0)
    for j in range(1, N+1):
        x = Fraction(j, N)
        v = Q.eval(Rational(x.numerator, x.denominator))
        if v == 0:
            return (x, x)
        if v < 0:
            a, b = prev_x, x
            break
        prev_x = x
    else:
        raise ValueError("no sign change on (0,1]")
    assert sturm_count(Q, Fraction(0), a) == 0
    assert sturm_count(Q, a, b) == 1
    while b - a > Fraction(1, 10**12):
        m = (a+b)/2
        if sturm_count(Q, a, m) == 1:
            b = m
        else:
            assert sturm_count(Q, m, b) == 1
            a = m
    return (a, b)

def main():
    out = {"systems": {}}
    for name, SYS in SYSTEMS.items():
        M = SYS["M"]
        assert connected_full(M), name
        r = len(M)
        g = SYMS.Zero
        sph = []
        for s in range(0, r+1):
            for T in itertools.combinations(range(r), s):
                c = classify(T, M)
                if c is None:
                    continue
                sph.append((list(T), [list(x) for x in c]))
                tl, p = term_expr(c)
                g += SYMS((-1)**s) * tl / p
        g = together(g)
        num, den = fraction(g)
        PN = Poly(num, t, domain='ZZ'); PD = Poly(den, t, domain='ZZ')
        assert PN.eval(0) == 1 and PD.eval(0) == 1, (name, "g(0)!=1")
        # reduce common factor exactly
        u = symbols('u')
        from sympy import Poly as P2
        G = sym_gcd(PN, PD)
        if G.degree() > 0:
            Qr, _ = PN.div(G); Dr, _ = PD.div(G)
            PN = Poly(Qr.as_expr(), t, domain='ZZ'); PD = Poly(Dr.as_expr(), t, domain='ZZ')
            assert PN.eval(0) != 0 and PD.eval(0) != 0
            sgn = 1 if PN.eval(0) == 1 else -1
            assert abs(int(PN.eval(0))) == 1 and abs(int(PD.eval(0))) == 1
        else:
            sgn = 1
        Nq = [sgn*int(c) for c in PD.all_coeffs()[::-1]]  # W num = den of g
        Dq = [sgn*int(c) for c in PN.all_coeffs()[::-1]]  # W den = num of g
        assert Nq[0] == 1 and Dq[0] == 1, (name, Nq[0], Dq[0])
        coeffs = series_fromQD(Nq, Dq, 14)
        assert coeffs[0] == 1 and all(c >= 0 for c in coeffs), (name, coeffs)
        # growth check: exponential (last coeff >> 1)
        assert coeffs[14] > 50, (name, coeffs)
        (a, b) = smallest_pos_root(Poly(sum(c*t**i for i, c in enumerate(Dq)), t, domain='ZZ'))
        assert a > 0
        out["systems"][name] = {
            "desc": SYS["desc"], "M": M,
            "spherical_count": len(sph),
            "spherical": [[T, C] for T, C in sph],
            "gcd_degree": int(G.degree()),
            "Wnum_coeffs_asc": Nq, "Wden_coeffs_asc": Dq,
            "root_bracket": [str(a), str(b)],
            "omega_lower": str(Fraction(b.denominator, b.numerator)),
            "omega_lower_float": float(Fraction(b.denominator, b.numerator)),
            "series_0_14": coeffs,
        }
        print(f"{name} {SYS['desc']}: |sph|={len(sph)} gcddeg={int(G.degree())} "
              f"degQ={len(Dq)-1} r in [{float(a):.10f},{float(b):.10f}] "
              f"omega>={float(Fraction(b.denominator,b.numerator)):.6f} a14={coeffs[14]}", flush=True)
    with open("output/artifacts/series.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote output/artifacts/series.json")

if __name__ == "__main__":
    main()
