import time, itertools
from sympy import symbols, QQ, groebner, Poly
x, y = symbols('x y')
M = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0)]
its = []
for k in (2, 3):
    for supp in itertools.combinations(range(6), k):
        if not any(sum(M[m]) == 2 for m in supp):
            continue
        for sg in itertools.product((1, -1), repeat=k):
            e = 0
            for mi, s in zip(supp, sg):
                a, b = M[mi]
                e = e + s * (x ** a) * (y ** b)
            its.append(e)
print('npolys', len(its), flush=True)
t = time.time()
N = 30
for k in range(N):
    groebner([its[k], its[k + 1]], x, y, order='lex', domain=QQ)
    groebner([its[k], its[k + 1]], y, x, order='lex', domain=QQ)
    groebner([its[k], its[k + 1]], x, y, order='grlex', domain=QQ)
    Poly(its[k], x, y).resultant(Poly(its[k + 1], x, y), x)
    Poly(its[k], x, y).resultant(Poly(its[k + 1], x, y), y)
dt = time.time() - t
print('full-per-pair ms:', round(dt / N * 1000, 1), flush=True)
print('est-total-min:', round(dt / N * 19900 / 60, 1), flush=True)
