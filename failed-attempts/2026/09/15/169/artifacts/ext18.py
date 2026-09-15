#!/usr/bin/env python3
"""Attempted Route 1 for target: machine-checkable Adams E_2 page in stems <= 18.

Builds the minimal free resolution of F_2 over the mod-2 Steenrod algebra,
truncated to internal degree TMAX, by a fully explicit finite algorithm
(admissible (Serre-Cartan) basis, Adem relations, degree-by-degree kernels and
decomposable quotients). Every step is finite F_2-linear algebra, hence in
principle proof-assistant checkable; the script records the E_2 table that a
Lean/Coq certification would have to reproduce, and validates it against
textbook facts (binary-partition dims of A, the h_i classes, h_0 h_1 = 0).

Pure Python, no dependencies. All arithmetic over F_2 (bitmask vectors).
"""

from functools import lru_cache

TMAX = 26
SMAX = 8
STEM_MAX = 20

# ---------------------------------------------------------------- basis of A
def binom_mod2(n, k):
    if k < 0 or k > n:
        return 0
    return 1 if (k & ~n) == 0 else 0

def admissible_monomials(maxdeg):
    res = []
    def rec(seq, maxnext, deg):
        res.append(seq)
        for a in range(1, min(maxnext, maxdeg - deg) + 1):
            rec(seq + (a,), a // 2, deg + a)
    rec((), maxdeg, 0)
    return res

ADM = admissible_monomials(TMAX)
print(f"dim A_{{<={TMAX}}} = {len(ADM)}")

# self-check: dim A_n == partitions of n into parts 2^k - 1 (dual: A_* = F2[xi_k], |xi_k|=2^k-1)
def milnor_partitions(n):
    parts = []
    m = 1
    while m <= n:
        parts.append(m)
        m = 2 * m + 1
    p = [0] * (n + 1)
    p[0] = 1
    for coin in parts:
        for j in range(coin, n + 1):
            p[j] += p[j - coin]
    return p[n]

cnt = {}
for M in ADM:
    cnt[sum(M)] = cnt.get(sum(M), 0) + 1
for n in range(0, 21):
    assert cnt.get(n, 0) == milnor_partitions(n), f"A_{n}: {cnt.get(n,0)} vs {milnor_partitions(n)}"
print("basis self-check OK (dims of A_n match Milnor polynomial dims for n<=20)")

@lru_cache(maxsize=None)
def mul_gen(a, I):
    """Sq^a * Sq^I as a tuple of admissible monomials (each once), deg<=TMAX."""
    if a == 0:
        return (I,) if sum(I) <= TMAX else ()
    if not I:
        return ((a,),) if a <= TMAX else ()
    b, R = I[0], I[1:]
    if a >= 2 * b:
        M = (a,) + I
        return (M,) if sum(M) <= TMAX else ()
    out = set()
    def tog(K):
        if K in out:
            out.remove(K)
        else:
            out.add(K)
    for c in range(0, a // 2 + 1):
        if binom_mod2(b - c - 1, a - 2 * c):
            for J in mul_gen(c, R):
                for K in mul_gen(a + b - c, J):
                    tog(K)
    return tuple(sorted(out))

# generic product of admissible monomials: fold single generators from the RIGHT
# (mul_gen(a, M) = Sq^a left-multiplied onto the admissible monomial M)
@lru_cache(maxsize=None)
def mon_prod(A, B):
    cur = {(): 1}
    for a in reversed(A + B):
        nxt = set()
        for M in cur:
            for K in mul_gen(a, M):
                if K in nxt:
                    nxt.remove(K)
                else:
                    nxt.add(K)
        cur = nxt
    return tuple(sorted(cur))

# sanity (left-to-right action convention): Sq^1 Sq^1 = 0 ; Sq^2 Sq^1 = Sq^{2,1} (admissible) ;
# Sq^2 Sq^2 = Sq^3 Sq^1 ; Sq^1 Sq^2 = Sq^3 ; Sq^2 Sq^3 = Sq^5 + Sq^{4,1}
assert mon_prod((1,), (1,)) == ()
assert mon_prod((2,), (1,)) == ((2, 1),)
assert mon_prod((2,), (2,)) == ((3, 1),)
assert mon_prod((1,), (2,)) == ((3,),)
assert tuple(sorted(mon_prod((2,), (3,)))) == ((4, 1), (5,))
print("Adem self-checks OK")

# ---------------------------------------------------------------- F2 linear algebra (bitmask vectors)
class Echelon:
    def __init__(self):
        self.piv = {}
    def reduce(self, v):
        while v:
            b = v.bit_length() - 1
            if b in self.piv:
                v ^= self.piv[b]
            else:
                return v
        return 0
    def add(self, v):
        r = self.reduce(v)
        if r:
            self.piv[r.bit_length() - 1] = r
            return True
        return False
    def rank(self):
        return len(self.piv)

def rref_kernel(rows, ncols):
    """Kernel of matrix given as row bitmasks (len(rows) x ncols). Returns list of col-coord masks."""
    rows = list(rows)
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(rows)):
            if (rows[i] >> c) & 1:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        pivots.append(c)
        r += 1
    pivset = set(pivots)
    free = [c for c in range(ncols) if c not in pivset]
    ker = []
    for f in free:
        v = (1 << f)
        for idx, p in enumerate(pivots):
            if (rows[idx] >> f) & 1:
                v |= (1 << p)
        ker.append(v)
    return ker

# ---------------------------------------------------------------- free modules
class FreeMod:
    def __init__(self):
        self.gens = []   # degrees
        self.basis = []  # (g, M)
        self.bpos = {}
        self.bydeg = {}
        self._sqcache = {}
    def add_gen(self, d):
        g = len(self.gens)
        self.gens.append(d)
        for M in ADM:
            if d + sum(M) <= TMAX:
                i = len(self.basis)
                self.basis.append((g, M))
                self.bpos[(g, M)] = i
                self.bydeg.setdefault(d + sum(M), []).append(i)
        return g
    def sq_images(self, a, dfrom):
        """{basis idx of deg dfrom : ambient mask of Sq^a image (deg dfrom+a)}."""
        key = (a, dfrom)
        if key in self._sqcache:
            return self._sqcache[key]
        out = {}
        for j in self.bydeg.get(dfrom, []):
            g, M = self.basis[j]
            v = 0
            for K in mul_gen(a, M):
                i = self.bpos.get((g, K))
                if i is not None:
                    v ^= (1 << i)
            if v:
                out[j] = v
        self._sqcache[key] = out
        return out

def apply_sq(images, v):
    r = 0
    while v:
        b = (v & -v).bit_length() - 1 if False else None
        lsb = v & (-v)
        j = lsb.bit_length() - 1
        if j in images:
            r ^= images[j]
        v ^= lsb
    return r

def apply_mon(mod, M, v):
    for a in M:
        if v == 0:
            return 0
        dfrom = None
        # degree of v: find from lowest set bit's basis element
        lsb = v & (-v)
        j = lsb.bit_length() - 1
        g, N = mod.basis[j]
        dfrom = mod.gens[g] + sum(N)
        v = apply_sq(mod.sq_images(a, dfrom), v)
    return v

# ---------------------------------------------------------------- resolution
mods = []       # FreeMod per homological degree
dimg = []       # dimg[s][g] = ambient mask in mods[s-1]
kervecs = []    # kervecs[s][t] = list of ambient masks in mods[s]

F0 = FreeMod(); F0.add_gen(0)
mods.append(F0); dimg.append([]); kervecs.append({})
# ker(d_0): augmentation ideal
for t in range(TMAX + 1):
    cols = F0.bydeg.get(t, [])
    if t == 0:
        kervecs[0][t] = []
    else:
        kervecs[0][t] = [(1 << bi) for bi in cols]

ext = {}  # (s,t) -> dim
ext[(0, 0)] = 1

for s in range(1, SMAX + 1):
    F = FreeMod()
    dimgs = []
    Fk = {}
    for t in range(TMAX + 1):
        C = kervecs[s - 1].get(t, [])
        ech = Echelon()
        # decomposables first
        for a in range(1, t + 1):
            imgs = mods[s - 1].sq_images(a, t - a)
            for y in kervecs[s - 1].get(t - a, []):
                w = apply_sq(imgs, y)
                if w:
                    ech.add(w)
        n0 = ech.rank()
        reps = []
        for c in C:
            if ech.add(c):
                reps.append(c)
        Fk[t] = list(C)
        for rep in reps:
            g = F.add_gen(t)
            dimgs.append(rep)
            assert g == len(dimgs) - 1
        if reps:
            ext[(s, t)] = len(reps)
    mods.append(F); dimg.append(dimgs); kervecs.append({})
    # kernel of d_s per degree
    for t in range(TMAX + 1):
        cols = F.bydeg.get(t, [])
        prows = mods[s - 1].bydeg.get(t, [])
        if not cols:
            Fk[t] = []
            continue
        m = {bi: k for k, bi in enumerate(prows)}
        rows = [0] * len(prows)
        for k, j in enumerate(cols):
            g, M = F.basis[j]
            w = apply_mon(mods[s - 1], M, dimgs[g])
            ww = w
            while ww:
                lsb = ww & (-ww)
                bi = lsb.bit_length() - 1
                if bi in m:
                    rows[m[bi]] |= (1 << k)
                ww ^= lsb
        ker = rref_kernel(rows, len(cols))
        out = []
        for v in ker:
            amb = 0
            vv = v
            while vv:
                lsb = vv & (-vv)
                k = lsb.bit_length() - 1
                amb |= (1 << cols[k])
                vv ^= lsb
            out.append(amb)
        Fk[t] = out
    kervecs[s] = Fk
    ng = len(F.gens)
    print(f"s={s}: {ng} generators (deg<={TMAX}), dim F_{s} = {len(F.basis)}", flush=True)

# ---------------------------------------------------------------- reports
print("\nExt^{1,t}: " + str(sorted(t for (s, t) in ext if s == 1)))
assert sorted(t for (s, t) in ext if s == 1) == [1, 2, 4, 8, 16], "h_i check failed"
print("h_i check OK: Ext^1 nontrivial in degrees 1,2,4,8,16 (32 beyond TMAX)")
assert ext.get((2, 3), 0) == 0, "h0 h1 should vanish"
assert ext.get((2, 4), 0) >= 1, "h1^2 should be nonzero"
print("product checks OK: h0h1=0, Ext^{2,4}!=0 (contains h1^2)")

print("\nAdams E_2 (s, stem, dim) for stems <= %d:" % STEM_MAX)
for stem in range(STEM_MAX + 1):
    row = []
    for s in range(SMAX + 1):
        d = ext.get((s, stem + s), 0)
        if d:
            row.append(f"s={s}:{d}")
    print(f"stem {stem:3d}: " + ("  ".join(row) if row else "-"))
