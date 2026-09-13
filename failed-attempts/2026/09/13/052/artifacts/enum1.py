"""Enumerate STS(21) invariant under sigma = 9 swaps + 3 fixed points.
Model: exact cover over pair-orbits. Quick smoke test: find first solutions."""
import sys, time

# points 0..20; sigma swaps (0 1),(2 3),...,(16 17); fixes 18,19,20
def sig(x):
    if x < 18:
        return x ^ 1
    return x

FIXED = (18, 19, 20)
NPAIR = 9  # transposition pairs i=0..8 -> points (2i,2i+1)

def pair_orbit_key(a, b):
    if a > b: a, b = b, a
    return (a, b)

# canonical pair-orbit id: min of (a,b) and (sig a, sig b) lexicographically
def porb(a, b):
    if a > b: a, b = b, a
    c, d = sig(a), sig(b)
    if c > d: c, d = d, c
    return (a, b) if (a, b) <= (c, d) else (c, d)

# fixed pairs (fixed by sigma as sets): fixed-fixed pairs and vertical pairs
def is_fixed_pair(a, b):
    if a > b: a, b = b, a
    sa, sb = sig(a), sig(b)
    return (sa == a and sb == b) or (sa == b and sb == a)

# Build columns: pair-orbits of non-fixed pairs
# mixed orbits (f,m): key (f, pair i); moved-moved: porb tuple
col_index = {}
cols = []
def get_col(key):
    if key not in col_index:
        col_index[key] = len(cols)
        cols.append(key)
    return col_index[key]

# enumerate all unordered pairs, classify
fixed_pairs = []
for a in range(21):
    for b in range(a+1, 21):
        if is_fixed_pair(a, b):
            fixed_pairs.append((a, b))
        else:
            get_col(porb(a, b))
print("num fixed pairs:", len(fixed_pairs), fixed_pairs)
print("num pair-orbit columns:", len(cols))
# usage columns: one per transposition pair i
use_col = []
for i in range(9):
    use_col.append(get_col(('use', i)))
NCOL = len(cols)
print("NCOL total:", NCOL)

from itertools import combinations

# fixed rows: {f, 2i, 2i+1} -> covers mixed orbit col + use col
rows = []          # list of (mask, descr)
row_triples = []   # for orbit rows: representative triple
for i in range(9):
    a, b = 2*i, 2*i+1
    for f in FIXED:
        m = (1 << get_col(porb(f, a))) | (1 << use_col[i])
        rows.append((m, ('FIX', f, a, b)))

seen = set()
norb = 0
for t in combinations(range(21), 3):
    a, b, c = t
    # skip if contains a fixed pair
    if is_fixed_pair(a, b) or is_fixed_pair(a, c) or is_fixed_pair(b, c):
        continue
    st = tuple(sorted((sig(a), sig(b), sig(c))))
    if st == t:
        # fixed triple (should have been skipped since it contains fixed pair... verify)
        print("UNEXPECTED fixed triple", t)
        continue
    key = min(t, st)
    if key in seen:
        continue
    seen.add(key)
    # columns covered: the 3 pair-orbits
    try:
        m = (1 << col_index[porb(a, b)]) | (1 << col_index[porb(a, c)]) | (1 << col_index[porb(b, c)])
    except KeyError as e:
        print("missing col for", t, e)
        continue
    # check distinctness: mask must have exactly 3 bits
    if bin(m).count('1') != 3:
        print("degenerate orbit", t, bin(m).count('1'))
        continue
    rows.append((m, ('ORB', key)))
    norb += 1

print("num rows:", len(rows), "orbit rows:", norb, "fixed rows:", 27)
FULL = (1 << NCOL) - 1
print("FULL bits:", bin(FULL).count('1'))

# column -> rows adjacency (row indices)
col_rows = [[] for _ in range(NCOL)]
for ri, (m, d) in enumerate(rows):
    mm = m
    while mm:
        lsb = mm & (-mm)
        c = lsb.bit_length() - 1
        col_rows[c].append(ri)
        mm ^= lsb

sys.setrecursionlimit(10000)
t0 = time.time()
sols = []
nodes = [0]
Tobreak = [False]

def choose_col(rem, activerows_set=None):
    # MRV over remaining columns; count compatible rows
    best = -1; bestopts = None; bestn = 10**9
    r = rem
    while r:
        lsb = r & (-r)
        c = lsb.bit_length() - 1
        r ^= lsb
        opts = [ri for ri in col_rows[c] if (rows[ri][0] & ~rem) == 0]
        n = len(opts)
        if n == 0:
            return c, []
        if n < bestn:
            bestn = n; best = c; bestopts = opts
            if n == 1:
                break
    return best, bestopts

def dfs(rem, chosen, tlim, maxsols):
    nodes[0] += 1
    if nodes[0] % 200000 == 0:
        print(f"nodes={nodes[0]} depth={len(chosen)} t={time.time()-t0:.1f}s", flush=True)
    if time.time() - t0 > tlim:
        Tobreak[0] = True
        return True
    if rem == 0:
        sols.append(list(chosen))
        return len(sols) >= maxsols
    c, opts = choose_col(rem)
    if not opts:
        return False
    for ri in opts:
        m = rows[ri][0]
        chosen.append(ri)
        if dfs(rem & ~m, chosen, tlim, maxsols):
            if len(sols) >= maxsols or Tobreak[0]:
                return True
        chosen.pop()
    return False

tlim = float(sys.argv[1]) if len(sys.argv) > 1 else 20.0
maxsols = int(sys.argv[2]) if len(sys.argv) > 2 else 3
dfs(FULL, [], tlim, maxsols)
print(f"done: nodes={nodes[0]} sols={len(sols)} t={time.time()-t0:.2f}s timeout={Tobreak[0]}")
for s in sols:
    print("SOL rows:", [rows[ri][1] for ri in s][:12], "... total", len(s))
