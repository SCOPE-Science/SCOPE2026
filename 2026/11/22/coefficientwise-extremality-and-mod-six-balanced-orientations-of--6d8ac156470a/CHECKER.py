"""Independent finite checks for ternary-triangle-free oriented one-point spectra."""
from itertools import product
from math import comb, factorial
from collections import Counter

COLS = tuple(product((0, 1), repeat=3))
ALLOWED_R = (1, 6, 3, 14, 3, 6)

def add(x, y):
    return tuple((x[i] if i < len(x) else 0) + (y[i] if i < len(y) else 0)
                 for i in range(max(len(x), len(y))))

def graded_by_rectangles(cols):
    b = len(cols)
    ans = [0] * (b + 4)
    # Supports entirely inside a shore: two choices of direction per chosen vertex.
    for i in range(4):
        ans[i] += comb(3, i) * (2 ** i)
    for i in range(b + 1):
        ans[i] += comb(b, i) * (2 ** i)
    ans[0] -= 1
    for row_mask in range(1, 8):
        k = row_mask.bit_count()
        for color in (0, 1):
            m = sum(all(col[j] == color for j in range(3) if (row_mask >> j) & 1)
                    for col in cols)
            for j in range(1, m + 1):
                ans[k + j] += comb(m, j)
    return tuple(ans)

def graded_by_types(cols):
    b = len(cols)
    out = [0] * (b + 4)
    # state 0: no relation; state 1: x -> old; state 2: old -> x
    for states in product((0, 1, 2), repeat=b + 3):
        ok = True
        for j, col in enumerate(cols):
            for i in range(3):
                a, v = states[i], states[3 + j]
                if a == 0 or v == 0:
                    continue
                # Old edge i -> (3+j) for color 0. Only the cyclic triangle is permitted.
                if col[i] == 0:
                    if not (a == 1 and v == 2): ok = False
                else:
                    if not (a == 2 and v == 1): ok = False
                if not ok: break
            if not ok: break
        if ok:
            out[sum(s != 0 for s in states)] += 1
    return tuple(out)

def poly_min(b):
    lo, hi = b // 2, (b + 1) // 2
    q, r = divmod(b, 6)
    out = [0] * (b + 4)
    for k in range(4): out[k] += comb(3, k) * 2**k
    for k in range(b + 1): out[k] += comb(b, k) * 2**k
    out[0] -= 1
    for m in (lo, hi):
        for j in range(1, m + 1): out[1 + j] += 3 * comb(m, j)
    for m, mult in ((q, 6 - r), (q + 1, r)):
        for j in range(1, m + 1): out[2 + j] += mult * comb(m, j)
    return tuple(out)

def poly_max(b):
    out = [0] * (b + 4)
    for i in range(4): out[i] += comb(3, i) * 2**i
    for j in range(b + 1): out[j] += comb(b, j) * 2**j
    out[0] -= 1
    for i in range(1, 4):
        for j in range(1, b + 1):
            out[i + j] += comb(3, i) * comb(b, j)
    return tuple(out)

def min_histogram(cols):
    b = len(cols)
    q, r = divmod(b, 6)
    ct = Counter(cols)
    if ct[(0,0,0)] or ct[(1,1,1)]:return False
    other = [p for p in COLS if p not in ((0,0,0), (1,1,1))]
    if sorted(ct[p] for p in other) != [q] * (6-r) + [q+1] * r:return False
    for i in range(3):
        ones = sum(col[i] for col in cols)
        if ones not in (b//2,(b+1)//2):return False
    return True

def run():
    cases=0
    for b in range(1,7):
        lo,hi=poly_min(b),poly_max(b)
        mins=maxs=0
        for cols in product(COLS, repeat=b):
            got=graded_by_rectangles(cols)
            assert len(got)==len(lo)
            assert all(x<=y<=z for x,y,z in zip(lo,got,hi)), (b,cols,lo,got,hi)
            if got==lo:
                mins+=1
                assert min_histogram(cols), (b,cols)
            if got==hi:
                maxs+=1
                assert len(set(v for c in cols for v in c))==1, (b,cols)
            if b<=3:
                assert got==graded_by_types(cols), (b,cols,got,graded_by_types(cols))
            cases+=1
        q,r=divmod(b,6)
        expected_min=ALLOWED_R[r]*factorial(b)//(factorial(q)**(6-r)*factorial(q+1)**r)
        assert mins==expected_min,(b,mins,expected_min)
        assert maxs==2,(b,maxs)
        print(f'b={b}: min={sum(lo)}, max={sum(hi)}, minimizing orientations={mins}, maximizing orientations={maxs}; all {8**b} orientations verified')
    print(f'VERIFY_OK; checked {cases} orientation matrices, including all direct ternary extensions for b<=3')

if __name__=='__main__': run()
