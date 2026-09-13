"""v2: bit-parallel exact cover for sigma-invariant STS(21). Row-conflict masks as Python ints (C-speed ops)."""
import sys, time, random

def sig(x):
    return x ^ 1 if x < 18 else x
FIXED = (18, 19, 20)

def is_fixed_pair(a, b):
    if a > b: a, b = b, a
    sa, sb = sig(a), sig(b)
    return (sa == a and sb == b) or (sa == b and sb == a)

def porb(a, b):
    if a > b: a, b = b, a
    c, d = sig(a), sig(b)
    if c > d: c, d = d, c
    return (a, b) if (a, b) <= (c, d) else (c, d)

col_index = {}
def get_col(key):
    if key not in col_index:
        col_index[key] = len(col_index)
    return col_index[key]

fixed_pairs = []
for a in range(21):
    for b in range(a+1, 21):
        if is_fixed_pair(a, b):
            fixed_pairs.append((a, b))
        else:
            get_col(porb(a, b))
use_col = [get_col(('use', i)) for i in range(9)]
NCOL = len(col_index)
print("NCOL", NCOL, flush=True)

from itertools import combinations
rows_cols = []
rows_descr = []
for i in range(9):
    a, b = 2*i, 2*i+1
    for f in FIXED:
        rows_cols.append([get_col(porb(f, a)), use_col[i]])
        rows_descr.append(('FIX', f, i))
seen = set()
for t in combinations(range(21), 3):
    a, b, c = t
    if is_fixed_pair(a, b) or is_fixed_pair(a, c) or is_fixed_pair(b, c):
        continue
    st = tuple(sorted((sig(a), sig(b), sig(c))))
    if st == t:
        print("UNEXPECTED fixed", t)
        continue
    key = min(t, st)
    if key in seen:
        continue
    seen.add(key)
    cl = [col_index[porb(a, b)], col_index[porb(a, c)], col_index[porb(b, c)]]
    if len(set(cl)) != 3:
        print("degenerate", t)
        continue
    rows_cols.append(cl)
    rows_descr.append(('ORB', key))
NR = len(rows_cols)
print("NROWS", NR, flush=True)

# col -> rows bitmask
colmask = [0]*NCOL
for ri, cl in enumerate(rows_cols):
    for c in cl:
        colmask[c] |= (1 << ri)
# row -> cols mask
rowmask = []
for cl in rows_cols:
    m = 0
    for c in cl:
        m |= (1 << c)
    rowmask.append(m)
# row conflict mask: rows sharing any column (including self)
confl = [0]*NR
for c in range(NCOL):
    cm = colmask[c]
    # for each row in col, add cm
    m = cm
    while m:
        lsb = m & (-m)
        ri = lsb.bit_length()-1
        confl[ri] |= cm
        m ^= lsb
print("conflict built", flush=True)

sys.setrecursionlimit(100000)
t0 = time.time()
tlim = float(sys.argv[1]) if len(sys.argv) > 1 else 15.0
maxsols = int(sys.argv[2]) if len(sys.argv) > 2 else 1
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
random.seed(seed)
nodes = [0]
sols = []
timed_out = [False]
# order rows randomly per column for diversification
col_rows = []
for c in range(NCOL):
    lst = []
    m = colmask[c]
    while m:
        lsb = m & (-m)
        lst.append(lsb.bit_length()-1)
        m ^= lsb
    random.shuffle(lst)
    col_rows.append(lst)

def pick_col(rem_mask, active):
    # rem_mask: int bitmask of remaining cols (NCOL bits)
    # MRV: iterate remaining cols, count (colmask[c] & active) popcount
    best = -1; bestn = 10**9; bestopts = 0
    r = rem_mask
    while r:
        lsb = r & (-r)
        c = lsb.bit_length()-1
        r ^= lsb
        n = bin(colmask[c] & active).count('1')
        if n == 0:
            return c, 0
        if n < bestn:
            bestn = n; best = c
            if n == 1:
                break
    return best, colmask[best] & active

def dfs(rem, active, chosen):
    nodes[0] += 1
    if (nodes[0] & 0xFFFFF) == 0:
        print(f"nodes={nodes[0]} depth={len(chosen)} t={time.time()-t0:.1f}", flush=True)
    if time.time()-t0 > tlim:
        timed_out[0] = True
        return True
    if rem == 0:
        sols.append(list(chosen))
        return len(sols) >= maxsols
    c, opts = pick_col(rem, active)
    if opts == 0:
        return False
    # iterate
    lst = [ri for ri in col_rows[c] if (opts >> ri) & 1]
    for ri in lst:
        chosen.append(ri)
        if dfs(rem & ~rowmask[ri], active & ~confl[ri], chosen):
            if len(sols) >= maxsols or timed_out[0]:
                return True
        chosen.pop()
    return False

FULL = (1 << NCOL) - 1
ALL = (1 << NR) - 1
dfs(FULL, ALL, [])
print(f"done nodes={nodes[0]} sols={len(sols)} t={time.time()-t0:.2f} timeout={timed_out[0]}", flush=True)
for s in sols:
    print([rows_descr[ri] for ri in s], flush=True)
