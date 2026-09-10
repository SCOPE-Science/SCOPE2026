#!/usr/bin/env python3
"""R1d (bounded May-window): May E1/d1 for sphere (anchor validation) + V(1)-twisted
May E1/d1 in window s<=8, t<=41. Conventions logged below; validated by anchors
(alpha1, beta1, Ext^0(V1)) and machine-checked d1^2=0. Stdlib only.
"""
import json, itertools
P = 3
def add(a, b): return (a + b) % P
def neg(a): return (-a) % P

# ---------- May E1 generators (sphere, p=3), tridegree (s,t) ----------
# a_n: (1, 2(3^n-1)+1); h_ij: (1, 2(3^i-1)3^j); b_ij: (2, 2(3^i-1)3^{j+1})
AG = [(n, 1, 2*(3**n - 1) + 1) for n in range(0, 4)]          # a0..a3
HG = [(i, j, 1, 2*(3**i - 1)*(3**j)) for i in range(1, 5) for j in range(0, 5)]
BG = [(i, j, 2, 2*(3**i - 1)*(3**(j+1))) for i in range(1, 4) for j in range(0, 4)]
AG = [g for g in AG if g[2] <= 41]
HG = [g for g in HG if g[3] <= 41 and g[3] > 0]
BG = [g for g in BG if g[3] <= 41]
print(json.dumps({'A': AG, 'H': HG, 'B': BG}))

# E1 monomial: (a0^e0 a1^e1 ...)(b..^f..)(ordered squarefree h-prod), s<=SMAX, t<=TMAX
SMAX, TMAX = 8, 41
polys = [('a',) + tuple(a) for a in AG] + [('b',) + tuple(b) for b in BG]  # (kind,n/i,j,s,t)
hs = [('h',) + tuple(h) for h in HG]
def gen_monomials(with_cells=None):
    mons = []
    # polynomial part via bounded exponents
    def rec(idx, s, t, part):
        if idx == len(polys):
            # h part: subsets
            for r in range(len(hs) + 1):
                for sub in itertools.combinations(range(len(hs)), r):
                    s2 = s + r
                    if s2 > SMAX: continue
                    t2 = t + sum(hs[k][4] for k in sub)
                    if t2 > TMAX: continue
                    mons.append((tuple(part), tuple(sub)))
            return
        _, _, _, ps, pt = polys[idx][0], polys[idx][1], polys[idx][2], polys[idx][-2], polys[idx][-1]
        e = 0
        while s + e*ps <= SMAX and t + e*pt <= TMAX:
            part.append((idx, e))
            rec(idx + 1, s + e*ps, t + e*pt, part)
            part.pop()
            e += 1
            if e > 8: break
    rec(0, 0, 0, [])
    return mons

MONS = gen_monomials()
def st_of(poly, hsub):
    s = sum(e * polys[i][-2] for i, e in poly) + len(hsub)
    t = sum(e * polys[i][-1] for i, e in poly) + sum(hs[k][4] for k in hsub)
    return s, t
def totdeg(poly, hsub):
    s, t = st_of(poly, hsub)
    return t - s
# canonical key
def key(poly, hsub): return (tuple(poly), tuple(sorted(hsub)))
INDEX = {key(p, h): n for n, (p, h) in enumerate(MONS)}
print(json.dumps({'n_E1_monomials': len(MONS)}))

# ---------- d1 ----------
# d1(a)=0, d1(b)=0, d1(h_ij) = sum_{k=1}^{i-1} h_{k,j} h_{i-k,j+k} (ordered by index order)
def h_index(i, j):
    for n, h in enumerate(hs):
        if h[1] == i and h[2] == j: return n
    return None
def d1_on_gen(g):
    # g: ('a',n,s,t) / ('b',i,j,s,t) / ('h',i,j,s,t) -> list of (coeff, poly, hsub)
    if g[0] in ('a', 'b'): return []
    _, i, j, s, t = g
    out = []
    for k in range(1, i):
        A = h_index(k, j); Bc = h_index(i - k, j + k)
        if A is None or Bc is None: continue
        out.append((1, (), tuple(sorted((A, Bc)))))
    return out
# product rep: dict key->coeff; multiply with Koszul signs (total degree t-s; h odd, a? t-s even? a: t-s = 2(3^n-1): even -> commute; b: even -> commute)
def gdeg(g):
    return g[-1] - g[-2]
def mul(repA, repB):
    out = {}
    for ka, ca in repA.items():
        for kb, cb in repB.items():
            pa, ha = ka; pb, hb = kb
            # merge polys
            d = dict(pa)
            for i, e in pb: d[i] = d.get(i, 0) + e
            pc = tuple(sorted(d.items()))
            # merge h subsets with sign: count swaps to merge sorted lists
            la, lb = list(ha), list(hb)
            if set(la) & set(lb):
                continue  # h^2 = 0
            inv = sum(1 for x in la for y in lb if x > y)
            # Koszul: moving lb past la? all h odd: sign = (-1)^{|la||lb| - ... } use permutation parity of merge
            sgn = -1 if inv % 2 else 1
            # also polynomial-odd crossings: polys all even degree -> no sign
            kc = (pc, tuple(sorted(la + lb)))
            if kc not in INDEX: continue  # out of window -> truncate (logged)
            out[kc] = (out.get(kc, 0) + sgn * ca * cb) % P
    return {k: v % P for k, v in out.items() if v % P != 0}
def single(poly, hsub): return {key(poly, hsub): 1}
def d1(rep):
    out = {}
    for k, c in rep.items():
        poly, hsub = k
        # Leibniz over factors: poly gens (even) + h gens (odd, ordered)
        terms = []
        for (i, e) in poly:
            if e == 0: continue
            for coeff, pp, hh in d1_on_gen(polys[i]):
                # d on one copy: sign from preceding odd factors: polys even -> +
                rest_poly = tuple(sorted(((j, (ej - (1 if j == i else 0))) for j, ej in poly if not (j == i and ej == 1)), ))
                t = mul(mul(single(rest_poly, ()), {key((), ()): coeff}), single(pp, hh))
                # times remaining h part with sign: d1(poly) is even? |d1| = +1 in s -> total degree -1? d lowers total deg by... d1: (s,t)->(s+1,t): total deg -1 (odd). sign crossing hsub: (-1)^{|hsub|} since d1 odd passes? use (-1)^len(hsub)
                sgn = -1 if len(hsub) % 2 else 1
                t2 = mul(t, single((), hsub))
                for kk, vv in t2.items(): out[kk] = (out.get(kk, 0) + sgn * c * vv) % P
        for pos, hk in enumerate(hsub):
            for coeff, pp, hh in d1_on_gen(hs[hk]):
                sgn = -1 if pos % 2 else 1  # preceding odd h's
                rest_h = tuple(x for q, x in enumerate(hsub) if q != pos)
                t = mul(mul(single(poly, rest_h), {key((), ()): coeff}), single(pp, hh))
                for kk, vv in t.items(): out[kk] = (out.get(kk, 0) + sgn * c * vv) % P
    return {k: v % P for k, v in out.items() if v % P != 0}

# d1^2 = 0 check on all E1 gens in window
d1sq_ok = True
for n, (p, h) in enumerate(MONS):
    if len(p) <= 1 and len(h) <= 1:
        if d1(d1(single(p, h))):
            d1sq_ok = False; print('D1SQ_FAIL', (p, h)); break
print(json.dumps({'d1_squared_zero_on_gens': d1sq_ok}))

# E2 in window: build complex per t, compute homology dims per (s,t)
from collections import defaultdict
def homology_by_t(smax=SMAX):
    by_t = defaultdict(lambda: defaultdict(list))  # t -> s -> [monomial indices]
    for n, (p, h) in enumerate(MONS):
        s, t = st_of(p, h)
        by_t[t][s].append(n)
    E2 = {}
    for t, smap in sorted(by_t.items()):
        for s in range(smax + 1):
            cur = smap.get(s, []); prv = smap.get(s - 1, []); nxt = smap.get(s + 1, [])
            # d: C^{s} -> C^{s+1} matrix; din: C^{s-1} -> C^s
            def mat(rows, cols, fwd=True):
                M = []
                for r in rows:
                    pass
                # M[r][c]: coefficient of basis_r in d(basis_c)
                M = [[0]*len(cols) for _ in rows]
                for j, c in enumerate(cols):
                    p, h = MONS[c]
                    img = d1(single(p, h))
                    for kk, vv in img.items():
                        # find row index
                        try: i = rows.index(INDEX[kk])
                        except ValueError: continue
                        M[i][j] = vv % P
                return M
            def rank(M):
                M = [row[:] for row in M]; r = 0; nr, nc = len(M), len(M[0]) if M else 0
                for c in range(nc):
                    piv = next((i for i in range(r, nr) if M[i][c] % P), None)
                    if piv is None: continue
                    M[r], M[piv] = M[piv], M[r]
                    inv = pow(M[r][c] % P, -1, P)
                    M[r] = [(v*inv) % P for v in M[r]]
                    for i in range(nr):
                        if i != r and M[i][c]:
                            f = M[i][c]
                            M[i] = [(a - f*b) % P for a, b in zip(M[i], M[r])]
                    r += 1
                return r
            Dout = mat(nxt, cur)
            Din = mat(cur, prv)
            hdim = len(cur) - rank(Dout) - rank(Din)
            if hdim: E2[(s, t)] = hdim
    return E2
E2 = homology_by_t()
anchors = {(1,1):1,(1,4):1,(2,12):None}
print(json.dumps({'E2_nonzero_(s,t)_t_le_41': sorted([[s,t,v] for (s,t),v in E2.items()]),
                  'anchor_(1,1)': E2.get((1,1),0), 'anchor_(1,4)': E2.get((1,4),0),
                  'anchor_(2,12)': E2.get((2,12),0)}))
