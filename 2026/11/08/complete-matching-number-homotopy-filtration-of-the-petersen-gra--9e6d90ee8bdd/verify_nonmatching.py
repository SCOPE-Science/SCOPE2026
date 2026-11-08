"""Exact finite CW verification for nonmatching complexes of the Petersen graph.

Uses Python standard library only. The graph is GP(5,2): outer pentagon,
inner pentagram, and five spokes. All chain coefficients are integers.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import gcd

EDGES = sorted({tuple(sorted(e)) for e in (
    [(i, (i + 1) % 5) for i in range(5)]
    + [(i, i + 5) for i in range(5)]
    + [(i + 5, (i + 2) % 5 + 5) for i in range(5)]
)})
assert len(EDGES) == 15


def forbidden(k):
    return [sum(1 << i for i in inds)
            for inds in combinations(range(15), k)
            if len({v for i in inds for v in EDGES[i]}) == 2*k]


def enumerate_faces(k):
    F = forbidden(k)
    return [f for f in range(1 << 15) if all(f & m != m for m in F)]


def oriented_boundary(simplex):
    return [(simplex ^ (1 << b), (-1) ** j)
            for j, b in enumerate(i for i in range(15) if simplex & (1 << i))]


def matching(faces):
    remaining = set(faces) - {0}
    pairs = []
    for v in range(15):
        bit = 1 << v
        for lo in sorted(f for f in remaining if not f & bit and f | bit in remaining):
            if lo in remaining and (lo | bit) in remaining:
                remaining.remove(lo)
                remaining.remove(lo | bit)
                pairs.append((lo, lo | bit))
    assert 2*len(pairs) + len(remaining) + 1 == len(faces)
    paired = dict(pairs)
    indeg = {f: 0 for f in faces}
    outgoing = defaultdict(list)
    incidences = 0
    for upper in faces:
        for lower, _ in oriented_boundary(upper):
            a, b = (lower, upper) if paired.get(lower) == upper else (upper, lower)
            outgoing[a].append(b)
            indeg[b] += 1
            incidences += 1
    q = deque(f for f in faces if not indeg[f])
    seen = 0
    while q:
        f = q.popleft()
        seen += 1
        for t in outgoing[f]:
            indeg[t] -= 1
            if indeg[t] == 0:
                q.append(t)
    assert seen == len(faces), 'matching must have no gradient cycle'
    return remaining, pairs, incidences


def morse_matrix(critical, pairs, d):
    low = sorted(f for f in critical if f.bit_count() == d)
    high = sorted(f for f in critical if f.bit_count() == d + 1)
    lo_to_hi = dict(pairs)
    low_set = set(low)

    @lru_cache(None)
    def image(f):
        if f in low_set:
            return {f: 1}
        upper = lo_to_hi.get(f)
        if upper is None or upper.bit_count() != d+1:
            return {}
        bdy = oriented_boundary(upper)
        pivot = dict(bdy)[f]
        out = Counter()
        for x, coeff in bdy:
            if x != f:
                for dest, c in image(x).items():
                    out[dest] -= coeff * pivot * c
        return {dest: c for dest, c in out.items() if c}

    matrix = []  # columns
    for f in high:
        out = Counter()
        for x, coeff in oriented_boundary(f):
            for dest, c in image(x).items():
                out[dest] += coeff*c
        matrix.append([out[x] for x in low])
    return matrix


def det_integer(rows):
    """Fraction-free exact integer determinant."""
    n = len(rows)
    if n == 0:
        return 1
    a = [list(r) for r in rows]
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            r = next((r for r in range(k+1, n) if a[r][k]), None)
            if r is None: return 0
            a[k], a[r] = a[r], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1,n):
                numer = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numer % prev == 0
                a[i][j] = numer//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[n-1][n-1]


def unit_minor(columns, order):
    if order == 0: return ((), ())
    ncol = len(columns)
    nrow = len(columns[0]) if columns else 0
    for cis in combinations(range(ncol), order):
        for ris in combinations(range(nrow),order):
            mat = [[columns[c][r] for c in cis] for r in ris]
            if abs(det_integer(mat)) == 1:
                return (ris,cis)
    return None


def rank_over_Q(columns):
    """Exact rational rank through small Sylvester minors."""
    if not columns: return 0
    ncol, nrow = len(columns),len(columns[0])
    for k in range(min(ncol,nrow),0,-1):
        for cis in combinations(range(ncol),k):
            for ris in combinations(range(nrow),k):
                if det_integer([[columns[c][r] for c in cis] for r in ris]):
                    return k
    return 0


def run():
    for k, expected in [(2, {0:1,1:6}), (3,{0:1,3:10,4:1}),
                        (4,{0:1,5:8,6:5,7:1}), (5,{0:1,9:6,10:1})]:
        faces = enumerate_faces(k)
        critical,pairs,incidences = matching(faces)
        vec = dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))
        cv = dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
        assert cv == expected,(k,cv)
        boundary = {d:morse_matrix(critical,pairs,d) for d in sorted(cv) if d>0}
        print('k',k,'faces',len(faces),'f_vector',vec,'matches',len(pairs),
              'critical',cv,'incidences',incidences)
        if k == 2:
            assert len(boundary[1]) == 6 and all(v==[0] for v in boundary[1])
        if k == 3:
            d4=boundary[4]
            assert len(d4)==1 and len(d4[0])==10 and 1 in [abs(z) for z in d4[0]]
            print('d4_columns',d4)
        if k == 4:
            d7,d6=boundary[7],boundary[6]
            assert len(d7)==1 and len(d7[0])==5
            assert len(d6)==5 and len(d6[0])==8
            assert rank_over_Q(d6)==4 and unit_minor(d6,4) is not None
            assert any(abs(z)==1 for z in d7[0])
            assert [sum(d6[j][i]*d7[0][j] for j in range(5)) for i in range(8)] == [0]*8
            print('d6_columns',d6,'d7_columns',d7,'unit_minor',unit_minor(d6,4))
        if k == 5:
            d10=boundary[10]
            assert len(d10)==1 and len(d10[0])==6 and 1 in [abs(z) for z in d10[0]]
            print('d10_columns',d10)
    assert len(enumerate_faces(6)) == 32768
    print('INTEGRAL_MORSE_CHECKS_PASS')


if __name__ == '__main__':
    run()
