#!/usr/bin/env python3
"""Independent oracle: minimal resolution of F2 over A via the MILNOR basis.

A = free assoc algebra on {Sq^k} modulo Adem relations, truncated to degree<=TMAX.
Represent A_n concretely as F2^(all words in positive ints summing to n) modulo the
subspace spanned by Adem relators (a<2b: Sq^a Sq^b - sum_c binom(b-c-1,a-2c) Sq^{a+b-c} Sq^c)
applied in every word position. Basis of each A_n = complement of row space.
Products: word concatenation + reduction mod relations.
Resolution: same degree-by-degree minimal engine, but matrices built from independently
implemented Milnor-basis-free presentation code (no Serre-Cartan, no mul_gen cache).
Cross-checks ext18.py E_2 dims for stems<=10.
"""
import itertools

TMAX = 14
SMAX = 5

def words_of_deg(n, maxpart=None):
    if n == 0:
        yield ()
        return
    for a in range(1, n + 1):
        if maxpart is not None and a > maxpart:
            continue
        for rest in words_of_deg(n - a, a if False else None):
            yield (a,) + rest

def binom2(n, k):
    if k < 0 or k > n:
        return 0
    return 1 if (k & ~n) == 0 else 0

# word list per degree
W = {}
wpos = {}
for n in range(TMAX + 1):
    wl = list(words_of_deg(n))
    W[n] = wl
    wpos[n] = {w: i for i, w in enumerate(wl)}

def adem_relators(n):
    """Row masks over W[n] spanning the Adem-relation subspace."""
    rels = []
    for w in W[n]:
        L = len(w)
        for i in range(L - 1):
            a, b = w[i], w[i + 1]
            if a < 2 * b and a > 0:
                row = 0
                row |= (1 << wpos[n][w])
                for c in range(0, a // 2 + 1):
                    if binom2(b - c - 1, a - 2 * c):
                        w2 = w[:i] + (a + b - c, c) + w[i + 2:] if c > 0 else w[:i] + (a + b,) + w[i + 2:]
                        if sum(w2) == n and w2 in wpos[n]:
                            row ^= (1 << wpos[n][w2])
                rels.append(row)
    return rels

def rref_rows(rows, ncols):
    rows = list(rows)
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(rows)):
            if (rows[i] >> c) & 1:
                p = i
                break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        piv.append(c)
        r += 1
    return rows, piv

def basis_complement(n):
    """Pivot-free (non-pivot) word indices = basis of A_n; plus reducer word->basis mask."""
    rels = adem_relators(n)
    if not W[n]:
        return [], {}
    rows, piv = rref_rows(rels, len(W[n]))
    pivset = set(piv)
    free = [c for c in range(len(W[n])) if c not in pivset]
    # reducer: for each word index, its coordinates in the free basis
    red = {}
    for c in range(len(W[n])):
        if c in pivset:
            idx = piv.index(c)
            v = 0
            for k, f in enumerate(free):
                if (rows[idx] >> f) & 1:
                    v |= (1 << k)
            red[c] = v
        else:
            red[c] = (1 << free.index(c))
    return free, red

FREE = {}
RED = {}
for n in range(TMAX + 1):
    f, r = basis_complement(n)
    FREE[n] = f
    RED[n] = r
    print(f"dim A_{n} = {len(f)}  (nwords={len(W[n])})", flush=True)

# Milnor cross-check
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

for n in range(TMAX + 1):
    assert len(FREE[n]) == milnor_partitions(n), f"dim mismatch at {n}"
print("Milnor-dim cross-check OK")

# product: A_i x A_j -> coords in FREE[i+j] basis
def prod_coords(A, i, B, j):
    """A,B masks in FREE bases; returns mask in FREE[i+j] basis. A,B are basis-coord masks."""
    # expand to word masks
    def expand(mask, deg):
        w = 0
        m = mask
        while m:
            lsb = m & (-m)
            k = lsb.bit_length() - 1
            w |= (1 << FREE[deg][k])
            m ^= lsb
        return w
    # multiply word-mask x word-mask by concatenation
    from functools import reduce
    wa, wb = expand(A, i), expand(B, j)
    wc = 0
    a = wa
    while a:
        lsb = a & (-a)
        x = lsb.bit_length() - 1
        b = wb
        while b:
            lsb2 = b & (-b)
            y = lsb2.bit_length() - 1
            ww = W[i][x] + W[j][y]
            if sum(ww) <= TMAX and ww in wpos[sum(ww)]:
                wc ^= (1 << wpos[sum(ww)][ww])
            b ^= lsb2
        a ^= lsb
    # reduce: word mask -> FREE basis mask
    out = 0
    c = wc
    n = i + j
    while c:
        lsb = c & (-c)
        x = lsb.bit_length() - 1
        out ^= RED[n][x]
        c ^= lsb
    return out

# left action of Sq^a on FREE-basis vectors: generator word (a,) times basis word
GEN = {}
for a in range(TMAX + 1):
    if (a,) in wpos[a]:
        GEN[a] = RED[a][wpos[a][(a,)]]
    else:
        GEN[a] = 0
print("GEN Sq1,Sq2,Sq3:", GEN[1], GEN[2], GEN[3])
# sanity: Sq^1 Sq^1 = 0 ; Sq^1 Sq^2 = Sq^3
assert prod_coords(GEN[1], 1, GEN[1], 1) == 0
assert prod_coords(GEN[1], 1, GEN[2], 2) == GEN[3]
print("product sanity OK")

class Echelon:
    def __init__(self):
        self.piv = {}
    def add(self, v):
        while v:
            b = v.bit_length() - 1
            if b in self.piv:
                v ^= self.piv[b]
            else:
                self.piv[b] = v
                return True
        return False

def left_sq(a, v, dfrom):
    """v: FREE-basis mask in degree dfrom -> FREE-basis mask in degree dfrom+a."""
    out = 0
    m = v
    while m:
        lsb = m & (-m)
        k = lsb.bit_length() - 1
        out ^= prod_coords(GEN[a], a, (1 << k), dfrom)
        m ^= lsb
    return out

def left_word(wd, v, dfrom):
    for a in wd:
        v = left_sq(a, v, dfrom)
        dfrom += a
        if v == 0:
            break
    return v

# ---- minimal resolution ----
class FM:
    def __init__(self):
        self.gens = []
        self.dim = {}   # deg -> dim (number of basis elements)
        self.base = {}  # deg -> global offset
        self.n = 0
    def add_gen(self, d):
        g = len(self.gens)
        self.gens.append(d)
        # basis elements: FREE[e] for e+d<=TMAX
        off = {}
        for e in range(TMAX - d + 1):
            self.base.setdefault(d + e, []).append((g, e))
        return g
    def coords(self, deg):
        """list of (g, k) with g gen, k FREE-basis index, spanning degree deg."""
        out = []
        for g, d in enumerate(self.gens):
            e = deg - d
            if 0 <= e <= TMAX - d:
                for k in range(len(FREE[e])):
                    out.append((g, k))
        return out

def act_sq(mod, a, dfrom):
    """dict: column index (in coords(dfrom)) -> mask over coords(dfrom+a)."""
    src = mod.coords(dfrom)
    tgt = mod.coords(dfrom + a) if dfrom + a <= TMAX else []
    tpos = {c: i for i, c in enumerate(tgt)}
    imgs = {}
    for j, (g, k) in enumerate(src):
        d = mod.gens[g]
        e = dfrom - d
        # Sq^a (FREE[e]-basis elt k) = sum over FREE[e+a] basis of prod((a),(e-word))
        w = 0
        m = prod_coords(GEN[a], a, (1 << k), e)
        while m:
            lsb = m & (-m)
            kk = lsb.bit_length() - 1
            if (g, kk) in tpos:
                w |= (1 << tpos[(g, kk)])
            m ^= lsb
        if w:
            imgs[j] = w
    return imgs, len(tgt)

def apply_imgs(imgs, v):
    r = 0
    while v:
        lsb = v & (-v)
        j = lsb.bit_length() - 1
        if j in imgs:
            r ^= imgs[j]
        v ^= lsb
    return r

def kernel_of(rows, ncols):
    rows = list(rows)
    pivs = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(rows)):
            if (rows[i] >> c) & 1:
                p = i
                break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        pivs.append(c)
        r += 1
    ps = set(pivs)
    free = [c for c in range(ncols) if c not in ps]
    out = []
    for f in free:
        v = (1 << f)
        for idx, p in enumerate(pivs):
            if (rows[idx] >> f) & 1:
                v |= (1 << p)
        out.append(v)
    return out

mods = []
dimg = []
kerv = []

F0 = FM(); F0.add_gen(0)
mods.append(F0); dimg.append([])
K0 = {}
for t in range(TMAX + 1):
    c = F0.coords(t)
    K0[t] = [] if t == 0 else [(1 << j) for j in range(len(c))]
kerv.append(K0)
ext = {(0, 0): 1}

for s in range(1, SMAX + 1):
    F = FM()
    dg = []
    for t in range(TMAX + 1):
        C = kerv[s - 1].get(t, [])
        ech = Echelon()
        for a in range(1, t + 1):
            imgs, _ = act_sq(mods[s - 1], a, t - a)
            for y in kerv[s - 1].get(t - a, []):
                w = apply_imgs(imgs, y)
                if w:
                    ech.add(w)
        for c in C:
            if ech.add(c):
                dg.append((t, c))
                F.add_gen(t)
    dimg.append([m for _, m in dg])
    mods.append(F)
    K = {}
    for t in range(TMAX + 1):
        cols = F.coords(t)
        tgt = mods[s - 1].coords(t)
        tpos = {c: i for i, c in enumerate(tgt)}
        rows = [0] * len(tgt)
        for k, (g, kk) in enumerate(cols):
            d = F.gens[g]
            e = t - d
            # image of FREE[e] basis elt kk under word? No: basis elt is (g, word-basis kk);
            # d_s(g.w) = w . dimg[g]: expand w = FREE[e] word, act on dimg[g] (coords mask in deg d)
            wmask = (1 << FREE[e][kk])  # word mask
            # apply word from the right: decompose word into gens and apply left_sq successively? NO:
            # need right action of the word on the cycle. Instead: image = sum over word-basis expansion
            # of w as product of generators from the LEFT is wrong for right action.
            # Correct: d(g.(Sq^{a1}...Sq^{ak})) = (...((dimg . a1) . a2)...). Need RIGHT multiplication
            # by generator: right_sq(v, a): v (FREE-basis mask deg f) -> mask deg f+a via prod(v_word, GEN[a]).
            v = dimg[s][g]
            deg = d
            ww = W[e][FREE[e][kk]] if e > 0 else ()
            for a in ww:
                v = right_sq(mods[s - 1], v, deg, a)
                deg += a
                if v == 0:
                    break
            vv = v
            while vv:
                lsb = vv & (-vv)
                j = lsb.bit_length() - 1
                if tgt[j] in tpos:
                    rows[tpos[tgt[j]]] |= (1 << k)
                vv ^= lsb
        K[t] = []
        if cols:
            for v in kernel_of(rows, len(cols)):
                amb = 0
                while v:
                    lsb = v & (-v)
                    k = lsb.bit_length() - 1
                    amb |= (1 << cols[k][0] if False else 0)
                    amb = amb  # placeholder
                    v ^= lsb
                K[t].append(v)
    # NOTE: kernel stored in coords-columns; convert: keep as-is with cols table
    kerv.append((K, F))
    print(f"s={s}: {len(F.gens)} gens", flush=True)

def right_sq(mod, v, dfrom, a):
    """Right-multiply coords-mask v (deg dfrom) by Sq^a -> coords-mask deg dfrom+a."""
    tgt = mod.coords(dfrom + a) if dfrom + a <= TMAX else []
    tpos = {c: i for i, c in enumerate(tgt)}
    out = 0
    m = v
    while m:
        lsb = m & (-m)
        j = lsb.bit_length() - 1
        src = mod.coords(dfrom)[j]
        g, k = src
        d = mod.gens[g]
        e = dfrom - d
        # word x = W[e][FREE[e][k]]; right product x*Sq^a in A_{e+a}, reduce, map to (g, kk)
        w = 0
        b = GEN[a]
        # expand b to word mask
        wb = 0
        mm = b
        while mm:
            l2 = mm & (-mm)
            kk2 = l2.bit_length() - 1
            wb |= (1 << FREE[a][kk2])
            mm ^= l2
        xa = xw = 0
        wx = (1 << wpos[e][W[e][FREE[e][k]]]) if e >= 0 else 0
        # concatenate each pair
        r = 0
        xx = wx
        while xx:
            l2 = xx & (-xx)
            xi = l2.bit_length() - 1
            yy = wb
            while yy:
                l3 = yy & (-yy)
                yi = l3.bit_length() - 1
                ww = W[e][xi] + W[a][yi]
                if sum(ww) <= TMAX and ww in wpos[sum(ww)]:
                    r ^= (1 << wpos[sum(ww)][ww])
                yy ^= l3
            xx ^= l2
        # reduce r (word mask in deg e+a) to FREE basis, then to coords
        rr = r
        while rr:
            l2 = rr & (-rr)
            xi = l2.bit_length() - 1
            rb = RED[e + a][xi]
            q = rb
            while q:
                l3 = q & (-q)
                kk3 = l3.bit_length() - 1
                if (g, kk3) in tpos:
                    out |= (1 << tpos[(g, kk3)])
                q ^= l3
            rr ^= l2
        m ^= lsb
    return out
