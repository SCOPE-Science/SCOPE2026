"""Span-size and coarse-dimension check for the fixed-field-span construction.

Finite-field facts verified here:
1. GF(4)/GF(2) trace-kernel identity: ker(Tr) = im(sigma - id) = {0,1}, sizes match.
2. Actual k-ranks and F-ranks of X = {1/(x-y) : x in F} for representative
   parameters, including a capped case with an explicit dependent-subset
   certificate (null-vector coefficients), not just the min(q/n,1) printout.
3. Coarse-dimension table: weak hypothesis m/n -> 0 does NOT imply strong q/n -> 0.
   Conditional exact formula (proved only under [F(y):F] >= q, see DRAFT.md):
     |Y_i| = p_i^min(q_i,n_i), delta = lim min(q_i/n_i,1) (prime span),
     and analogously min(m_i q_i/n_i,1) for the F-span.
   Sequence deltas below are conditional on maximal-degree approximants
   (y of degree >= q over F); uniform cross-p L_sigma-definability of the span
   and positive transformal degree of the ultraproduct span element remain open.
Run: python3 span_delta.py
"""
import math
from itertools import product


# ---------- generic GF(p^n) via polynomial basis mod a monic irreducible ----------

def _poly_add(a, b, p):
    n = max(len(a), len(b))
    return [( (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) ) % p
            for i in range(n)]

def _poly_mul(a, b, p):
    if not a or not b:
        return [0]
    c = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            c[i + j] = (c[i + j] + ca * cb) % p
    return c

def _poly_deg(a):
    d = len(a) - 1
    while d > 0 and a[d] == 0:
        d -= 1
    return d

def _poly_mod(a, mod, p):
    a = list(a)
    dm = _poly_deg(mod)
    lc = mod[dm] % p
    linv = pow(lc, -1, p)
    while True:
        da = _poly_deg(a)
        if da < dm:
            break
        coeff = (a[da] * linv) % p
        shift = da - dm
        for i in range(dm + 1):
            a[shift + i] = (a[shift + i] - coeff * mod[i]) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def _poly_divides(d, a, p):
    return all(c % p == 0 for c in _poly_mod(a, d, p))

def _all_monic(deg, p):
    if deg == 0:
        yield [1]
        return
    for rest in product(range(p), repeat=deg):
        yield list(rest) + [1]

def _is_irreducible(mod, p):
    n = _poly_deg(mod)
    if n <= 0:
        return False
    # no monic factor of degree <= n//2
    for d in range(1, n // 2 + 1):
        for f in _all_monic(d, p):
            if _poly_divides(list(f), mod, p):
                return False
    return True

def find_irreducible(p, n):
    for coeffs in product(range(p), repeat=n):
        mod = list(coeffs) + [1]
        if _is_irreducible(mod, p):
            return mod
    raise ValueError(f'no irreducible found for p={p} n={n}')


class GF:
    def __init__(self, p, n, mod=None):
        self.p = p
        self.n = n
        self.mod = mod or find_irreducible(p, n)
        self.size = p ** n
        self.zero = (0,) * n
        self.one = (1,) + (0,) * (n - 1)

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        c = _poly_mul(list(a), list(b), self.p)
        c = _poly_mod(c, self.mod, self.p)
        c = c + [0] * (self.n - len(c))
        return tuple(c[:self.n])

    def pow(self, a, e):
        r = self.one
        while e:
            if e & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            e >>= 1
        return r

    def inv(self, a):
        assert a != self.zero, 'division by zero'
        for b in self.elems():
            if self.mul(a, b) == self.one:
                return b
        raise AssertionError('no inverse')

    def elems(self):
        return product(range(self.p), repeat=self.n)

    def frob(self, a):
        return self.pow(a, self.p)


def gf4_check():
    # GF(4) = F2[w]/(w^2+w+1); sigma = Frobenius squaring; Tr(x)=x+x^2.
    # Represent as pairs over F2: 0=(0,0),1=(1,0),w=(0,1),w2=(1,1); add=xor.
    add = lambda a, b: (a[0] ^ b[0], a[1] ^ b[1])
    els = {'0': (0, 0), '1': (1, 0), 'w': (0, 1), 'w2': (1, 1)}
    sigma = {'0': '0', '1': '1', 'w': 'w2', 'w2': 'w'}  # squaring swaps w,w2
    ker, im = [], []
    for k, v in els.items():
        sv = els[sigma[k]]
        tr = add(v, sv)  # Tr(x) = x + sigma(x), lands in {(0,0),(1,0)}
        if tr == (0, 0):
            ker.append(k)
        d = add(sv, v)  # sigma(x)-x = sigma(x)+x in char 2
        im.append(d)
    im_set = sorted(set(im))
    assert sorted(ker) == ['0', '1'], ker
    assert im_set == [(0, 0), (1, 0)], im_set
    print('GF(4)/F2 check: ker(Tr)={0,1} (size 2 = q), im(sigma-id)={(0,0),(1,0)} (size 2). MATCH.')


# ---------- actual rank computations ----------

def fixed_field(K, q):
    return [a for a in K.elems() if K.pow(a, q) == a]

def deg_over_F(K, y, Fset, q):
    # degree of y over F = least d>=1 with y^{q^d} = y; 0 for y... (y always satisfies for some d | [K:F])
    z = y
    for d in range(1, 60):
        z = K.pow(z, q)
        if z == y:
            return d
    raise AssertionError('degree not found')

def rank_over_k(K, vecs):
    # vecs: list of K elements; coordinates = base-p digits; Gaussian elim over GF(p)
    p, n = K.p, K.n
    rows = [list(v) for v in vecs]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % p != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c] % p, -1, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p != 0:
                f = rows[i][c] % p
                rows[i] = [(x - f * y) % p for x, y in zip(rows[i], rows[r])]
        r += 1
    return r

def rank_over_F_bruteforce(K, vecs, Fset):
    # greedy F-rank by brute-force F-linear-relation search (small q only)
    F = list(Fset)
    indep = []
    for v in vecs:
        # check v in F-span(indep): try all coeff tuples
        found = True
        if not indep:
            found = (v == K.zero)
        else:
            found = False
            for coeffs in product(F, repeat=len(indep)):
                s = K.zero
                for c, u in zip(coeffs, indep):
                    s = K.add(s, K.mul(c, u))
                if s == v:
                    found = True
                    break
        if not found:
            indep.append(v)
    return len(indep)

def null_certificate_over_k(K, vecs):
    # find nonzero coeff tuple over GF(p) summing to zero (assumes dependence)
    p = K.p
    m = len(vecs)
    for coeffs in product(range(p), repeat=m):
        if all(c == 0 for c in coeffs):
            continue
        s = K.zero
        for c, v in zip(coeffs, vecs):
            for _ in range(c):
                s = K.add(s, v)
        if s == K.zero:
            return coeffs
    return None

def case_report(p, m, n, label):
    K = GF(p, n)
    q = p ** m
    Fset = fixed_field(K, q)
    assert len(Fset) == q, (label, len(Fset), q)
    assert (n % m) == 0, label
    extdeg = n // m
    # choose y in K\F of maximal F-degree
    best, bestd = None, -1
    for a in K.elems():
        if a in Fset:
            continue
        d = deg_over_F(K, a, Fset, q)
        if d > bestd:
            bestd, best = d, a
    y = best
    X = [K.inv(K.sub(x, y)) for x in Fset]
    assert len(set(X)) == q, (label, 'X not full size')
    kr = rank_over_k(K, X)
    fr = rank_over_F_bruteforce(K, X, Fset)
    cond = (bestd >= q)
    print(f'[{label}] p={p} m={m} n={n} q={q} [K:F]={extdeg} '
          f'maxdeg_F(y)={bestd} cond([F(y):F]>=q)={cond} '
          f'k-rank(X)={kr} (min(q,n)={min(q,n)}) F-rank(X)={fr} (min(q,[K:F])={min(q,extdeg)})')
    if kr < len(X):
        cert = null_certificate_over_k(K, X)
        assert cert is not None, label
        s = K.zero
        for c, v in zip(cert, X):
            for _ in range(c):
                s = K.add(s, v)
        assert s == K.zero, label
        print(f'   dependent-subset certificate over k=GF({p}): coeffs={cert} sum to 0.')
    else:
        print('   X is k-linearly independent (full independence, uncapped).')
    return {'label': label, 'p': p, 'm': m, 'n': n, 'q': q,
            'maxdeg': bestd, 'cond': cond, 'k_rank': kr, 'F_rank': fr}


def delta_table():
    print(f"{'p':>6} {'m':>3} {'n':>8} {'q=p^m':>8} {'m/n':>10} {'q/n':>10} {'delta~min(q/n,1)':>18}")
    for p, m, n in [(2,1,4),(3,1,9),(5,1,25),(11,1,121),(101,1,10201),(1009,1,1018081),
                    (5,2,50),(101,2,50),(1009,2,50),(1000003,2,50)]:
        q = p ** m
        print(f'{p:>6} {m:>3} {n:>8} {q:>8} {m/n:>10.6f} {q/n:>10.6f} {min(q/n,1):>18.6f}')

if __name__ == '__main__':
    gf4_check()
    print('--- actual ranks (maximal-degree y in each case) ---')
    r1 = case_report(2, 1, 4, 'A-like uncapped')
    assert r1['k_rank'] == 2 == min(2, 4) and r1['F_rank'] == 2
    assert r1['cond'] is True  # maxdeg 4 >= q=2
    r2 = case_report(2, 1, 2, 'B-like boundary')
    assert r2['k_rank'] == 2 == min(2, 2)
    assert r2['cond'] is True  # maxdeg 2 >= q=2
    r3 = case_report(3, 1, 2, 'capped (q>n)')
    assert r3['k_rank'] == 2 < 3  # capped: dependence certified above
    assert r3['cond'] is False  # maxdeg 2 < q=3: exact corollary hypothesis unsatisfiable here
    r4 = case_report(2, 2, 4, 'F-capped (q>[K:F])')
    assert r4['F_rank'] == 2 < 4  # F-span capped at [K:F]=2
    print('--- asymptotic table (conditional exact formula; sequence deltas conditional on maximal-degree approximants) ---')
    delta_table()
    print('CONCLUSION: weak m/n->0 holds in both families; strong q/n->0 (hence delta=0) holds only in the first.')
    print('Sequence deltas are conditional on maximal-degree approximants; capped case shows dependence when [F(y):F]<q.')
