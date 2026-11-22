"""Direct finite-field enumeration of characteristic ideals of truncated coordinate crosses."""
from itertools import combinations, product
from math import floor
from collections import Counter


def canonical(rows, p, d):
    a = [[v % p for v in row] for row in rows if any(v % p for v in row)]
    pivot_row = 0
    for col in range(d):
        ix = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if ix is None:
            continue
        a[pivot_row], a[ix] = a[ix], a[pivot_row]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(inv*v) % p for v in a[pivot_row]]
        for j in range(len(a)):
            if j != pivot_row:
                z = a[j][col]
                if z:
                    a[j] = [(u-z*v) % p for u, v in zip(a[j], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return tuple(tuple(row) for row in a[:pivot_row])


def all_subspaces(d, p):
    yield ()
    for r in range(1, d+1):
        for pivots in combinations(range(d), r):
            slots = [(i, j) for i in range(r) for j in range(pivots[i]+1, d) if j not in pivots]
            for values in product(range(p), repeat=len(slots)):
                rows = [[0]*d for _ in range(r)]
                for i, j in enumerate(pivots):
                    rows[i][j] = 1
                for (i, j), v in zip(slots, values):
                    rows[i][j] = v
                yield tuple(tuple(row) for row in rows)


def in_span(v, rows, p, d):
    return len(canonical((*rows, v), p, d)) == len(rows)


def multiply_basis(m, n, branch, index):
    # basis x,x^2,...,x^(m-1),y,y^2,...,y^(n-1)
    d = m+n-2
    w = [0]*d
    if branch == 'x' and 0 <= index < m-2:
        w[index+1] = 1
    if branch == 'y' and m-1 <= index < d-1:
        w[index+1] = 1
    return tuple(w)


def mat_transform(m, n, p, kind):
    d = m+n-2
    cols = [[0]*d for _ in range(d)]
    for j in range(d):
        cols[j][j] = 1
    if kind == 'x_socle':
        cols[0][d-1] += 1
    if kind == 'y_socle':
        cols[m-1][m-2] += 1
    if kind == 'x_jet':
        # x -> x+x^2; x^j -> (x+x²)^j truncated
        from math import comb
        for j in range(1, m):
            col = [0]*d
            for k in range(j+1):
                exponent = j+k
                if exponent < m:
                    col[exponent-1] += comb(j,k)
            cols[j-1] = col
    if kind == 'y_jet':
        from math import comb
        for j in range(1, n):
            col = [0]*d
            for k in range(j+1):
                exponent = j+k
                if exponent < n:
                    col[m-2+exponent] += comb(j,k)
            cols[m-2+j] = col
    if kind == 'x_scale':
        for j in range(1,m):
            cols[j-1][j-1] = pow(next(a for a in range(1,p) if len({pow(a,k,p) for k in range(1,p)}) == p-1),j,p)
    if kind == 'y_scale':
        for j in range(1,n):
            cols[m-2+j][m-2+j] = pow(next(a for a in range(1,p) if len({pow(a,k,p) for k in range(1,p)}) == p-1),j,p)
    return cols


def apply(v, cols, p):
    d = len(cols)
    return tuple(sum(v[i]*cols[i][j] for i in range(d)) % p for j in range(d))


def count_actual(m,n,p):
    d = m+n-2
    nx = [multiply_basis(m,n,'x',j) for j in range(d)]
    ny = [multiply_basis(m,n,'y',j) for j in range(d)]
    generators = [mat_transform(m,n,p,k) for k in ('x_socle','y_socle','x_jet','y_jet','x_scale','y_scale')]
    ideals = fixed = inspected = 0
    hist = Counter()
    for rows in all_subspaces(d,p):
        inspected += 1
        if all(in_span(tuple(sum(row[i]*nx[i][j] for i in range(d)) % p for j in range(d)), rows,p,d) and
               in_span(tuple(sum(row[i]*ny[i][j] for i in range(d)) % p for j in range(d)), rows,p,d)
               for row in rows):
            ideals += 1
            if all(in_span(apply(row,cols,p),rows,p,d) for cols in generators for row in rows):
                fixed += 1
                hist[len(rows)] += 1
    fixed += 1  # unit ideal
    hist[d+1] += 1
    return inspected, ideals+1, fixed, dict(sorted(hist.items()))


def expected_hist(m,n,q):
    t=q-1
    counts=Counter({m+n-1:1})
    for a in range(1,m+1):
        for b in range(1,n+1):
            if (a,b) not in ((1,n),(m,1)):
                counts[m+n-a-b] += 1
    for u in range(t,m,t):
        for v in range(t,n,t):
            if q==2 and (u,v) in ((1,n-1),(m-1,1)):
                continue
            counts[m+n-u-v-1] += t
    return dict(sorted(counts.items()))

def expected(m,n,q):
    t=q-1
    return m*n - 1 + t*( (m-1)//t )*( (n-1)//t ) - (2 if q==2 else 0)

if __name__ == '__main__':
    for m,n,q in [(3,4,2),(3,4,3),(3,4,5),(3,5,2),(3,5,3),(4,5,2)]:
        actual=count_actual(m,n,q)
        predicted=expected(m,n,q)
        print(f'm={m},n={n},q={q}: inspected={actual[0]}, ideals={actual[1]}, fixed={actual[2]}, predicted={predicted}')
        assert actual[2] == predicted
        assert actual[3] == expected_hist(m,n,q), (actual[3],expected_hist(m,n,q))
        print(f'  dimension_histogram={actual[3]}')
    print('CHARACTERISTIC_IDEAL_ENUMERATION_VERIFIED')
