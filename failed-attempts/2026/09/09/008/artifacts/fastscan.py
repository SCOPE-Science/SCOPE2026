import itertools, time
from sympy import symbols, QQ, Poly, groebner
x, y = symbols('x y')
M = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0)]
Q = {(2, 0), (1, 1), (0, 2)}
polys = []
for k in (2, 3):
    for supp in itertools.combinations(range(6), k):
        if not any(M[m] in Q for m in supp):
            continue
        for sg in itertools.product((1, -1), repeat=k):
            d = {}
            for mi, s in zip(supp, sg):
                d[M[mi]] = s
            polys.append(d)
polys.sort(key=lambda d: (tuple(sorted(d.keys())),
                          tuple(d[m] for m in sorted(d.keys()))))
exprs = []
for d in polys:
    e = 0
    for (a, b), c in d.items():
        e = e + c * (x ** a) * (y ** b)
    exprs.append(e)
print('NPOLYS', len(polys), flush=True)

def shape_xy(G):
    ps = [Poly(g, x, y, domain=QQ) for g in G.polys]
    if len(ps) != 2:
        return False
    uni = top = None
    for p in ps:
        t = p.as_dict()
        if all(a == 0 for (a, b) in t):
            if uni is not None: return False
            uni = t
        else:
            if top is not None: return False
            top = t
    if uni is None or top is None: return False
    if (1, 0) not in top or top[(1, 0)] != 1: return False
    if any(a not in (0, 1) for (a, b) in top): return False
    return sum(1 for (a, b) in top if a == 1) == 1

def shape_yx(G):
    ps = [Poly(g, x, y, domain=QQ) for g in G.polys]
    if len(ps) != 2:
        return False
    uni = top = None
    for p in ps:
        t = p.as_dict()
        if all(b == 0 for (a, b) in t):
            if uni is not None: return False
            uni = t
        else:
            if top is not None: return False
            top = t
    if uni is None or top is None: return False
    if (0, 1) not in top or top[(0, 1)] != 1: return False
    if any(b not in (0, 1) for (a, b) in top): return False
    return sum(1 for (a, b) in top if b == 1) == 1

hits = []
t = time.time()
N = len(exprs)
scanned = 0
for i in range(N):
    for j in range(i + 1, N):
        Gxy = groebner([exprs[i], exprs[j]], x, y, order='lex', domain=QQ)
        if list(Gxy) == [1]:
            scanned += 1
            continue
        Gyx = groebner([exprs[i], exprs[j]], y, x, order='lex', domain=QQ)
        sx = shape_xy(Gxy)
        sy = shape_yx(Gyx)
        if (not sx) and (not sy):
            Ix = Poly(exprs[i], x, y).resultant(Poly(exprs[j], x, y), x)[0]
            Iy = Poly(exprs[i], x, y).resultant(Poly(exprs[j], x, y), y)[0]
            if not (Ix.is_zero or Iy.is_zero):
                hits.append((i, j, sorted(str(g) for g in Gxy.polys),
                             sorted(str(g) for g in Gyx.polys)))
                if len(hits) >= 5:
                    break
        scanned += 1
    if len(hits) >= 5 or (time.time() - t) > 240:
        break
print('SCANNED', scanned, 'TIME', round(time.time() - t, 1), flush=True)
for h in hits:
    print('HIT', h[0], h[1], flush=True)
    print('  Gxy:', h[2], flush=True)
    print('  Gyx:', h[3], flush=True)
