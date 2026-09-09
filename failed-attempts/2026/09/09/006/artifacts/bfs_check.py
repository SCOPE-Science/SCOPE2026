#!/usr/bin/env python3
"""Lane-278 BFS cross-check: Tits reflection representation over QQ.
alpha_i = e_i; B(e_i,e_j) = -cos(pi/m) (0 for m=inf). sigma_i(v) = v - 2B(v,a_i)a_i.
Represent v in basis e: column coords; B-matrix G with G_ii=1, G_ij=-cos(pi/m).
sigma_i acts on coordinate column x as x -> x - 2 (row_i(G) . x) e_i.
cos(pi/m) for m in {2,3,4,5}: 0, 1/2, sqrt2/2, (1+sqrt5)/4. Work in:
  m in {2,3,4,inf}: QQ(sqrt2); m=5: QQ(sqrt2,sqrt5) biquadratic (a+b s2+c s5+d s25).
Separate exact classes per needed field. BFS on (reduced) words with canonical
keys; compare |S(n)| (new words at length n) with series a_n for n<=12.
"""
import json, math
from fractions import Fraction

class Q2:
    __slots__ = ("a","b")  # a + b*sqrt2
    def __init__(s, a=0, b=0): s.a, s.b = Fraction(a), Fraction(b)
    def __add__(s, o):
        if isinstance(o, Q2): return Q2(s.a+o.a, s.b+o.b)
        return Q2(s.a+Fraction(o), s.b)
    __radd__ = __add__
    def __neg__(s): return Q2(-s.a, -s.b)
    def __sub__(s, o): return s + (-o)
    def __mul__(s, o):
        if isinstance(o, Q2): return Q2(s.a*o.a + 2*s.b*o.b, s.a*o.b + s.b*o.a)
        return Q2(s.a*Fraction(o), s.b*Fraction(o))
    __rmul__ = __mul__
    def __eq__(s, o): return isinstance(o, Q2) and s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"({s.a}+{s.b}r2)"

class QB:
    __slots__ = ("a","b","c","d")  # a + b s2 + c s5 + d s2s5
    def __init__(s, a=0, b=0, c=0, d=0):
        s.a, s.b, s.c, s.d = Fraction(a), Fraction(b), Fraction(c), Fraction(d)
    def __add__(s, o):
        if isinstance(o, QB): return QB(s.a+o.a, s.b+o.b, s.c+o.c, s.d+o.d)
        return QB(s.a+Fraction(o), s.b, s.c, s.d)
    __radd__ = __add__
    def __neg__(s): return QB(-s.a, -s.b, -s.c, -s.d)
    def __sub__(s, o): return s + (-o)
    def __mul__(s, o):
        if not isinstance(o, QB): return QB(s.a*Fraction(o), s.b*Fraction(o), s.c*Fraction(o), s.d*Fraction(o))
        # s2^2=2, s5^2=5, (s2s5)^2=10
        a = s.a*o.a + 2*s.b*o.b + 5*s.c*o.c + 10*s.d*o.d
        b = s.a*o.b + s.b*o.a + 5*s.c*o.d + 5*s.d*o.c
        c = s.a*o.c + s.c*o.a + 2*s.b*o.d + 2*s.d*o.b
        d = s.a*o.d + s.d*o.a + s.b*o.c + s.c*o.b
        return QB(a, b, c, d)
    __rmul__ = __mul__
    def __eq__(s, o): return isinstance(o, QB) and (s.a,s.b,s.c,s.d)==(o.a,o.b,o.c,o.d)
    def __hash__(s): return hash((s.a, s.b, s.c, s.d))

def make_field(M):
    ms = {M[i][j] for i in range(len(M)) for j in range(len(M)) if i != j}
    if 5 in ms:
        Z, H = QB(0), QB(1)
        def C(m):
            if m == 0: return QB(0)
            if m == 2: return QB(0)
            if m == 3: return QB(Fraction(1,2))
            if m == 4: return QB(0, Fraction(1,2))
            if m == 5: return QB(Fraction(1,4), 0, Fraction(1,4), 0)  # (1+sqrt5)/4
            raise ValueError(m)
        return "QB", Z, H, C, QB
    Z, H = Q2(0), Q2(1)
    def C(m):
        if m in (0, 2): return Q2(0)
        if m == 3: return Q2(Fraction(1,2))
        if m == 4: return Q2(0, Fraction(1,2))
        raise ValueError(m)
    return "Q2", Z, H, C, Q2

def bfs_counts(M, L=12):
    r = len(M)
    _, Z, H, C, K = make_field(M)
    G = [[(H if i == j else ((Z-H) if M[i][j]==0 else -C(M[i][j]))) for j in range(r)] for i in range(r)]
    def key(cols):
        return tuple(x for col in cols for x in col)
    ident = [[H if i == j else Z for j in range(r)] for i in range(r)]
    seen = {key(ident)}
    frontier = [ident]
    new_counts = [1]
    for _ in range(1, L+1):
        nxt = []
        for mat in frontier:
            for i in range(r):
                # row i of G times mat: y_j = sum_k G[i][k]*mat[k][j]
                y = [Z]*r
                for j in range(r):
                    s = Z
                    for k in range(r):
                        s = s + G[i][k]*mat[k][j]
                    y[j] = s
                # newmat = mat - 2 e_i y^T
                nmat = [row[:] for row in mat]
                for j in range(r):
                    nmat[i][j] = nmat[i][j] - 2*y[j]
                k = key(nmat)
                if k not in seen:
                    seen.add(k); nxt.append(nmat)
        frontier = nxt
        new_counts.append(len(nxt))
    return new_counts

def main():
    data = json.load(open("output/artifacts/series.json"))
    ok = True
    for name, S in data["systems"].items():
        M = S["M"]
        got = bfs_counts(M, 12)
        exp = S["series_0_14"][:13]
        match = (got == exp)
        ok &= match
        print(f"{name}: BFS {'OK' if match else 'MISMATCH'} got={got} exp={exp}", flush=True)
    assert ok, "BFS mismatch"
    print("all BFS sphere counts agree to length 12")

if __name__ == "__main__":
    main()
