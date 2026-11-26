#!/usr/bin/env python3
"""Direct finite-field checks for the exterior-square tangent condition.
The theorem is proved algebraically; these finite-field ranks are checks, not its proof.
Run: python3 verify.py
"""
from itertools import combinations, product


def field_rank(rows, width, p):
    pivots = {}
    for rr in rows:
        r = [x % p for x in rr]
        while True:
            j = next((i for i, x in enumerate(r) if x), None)
            if j is None:
                break
            if j not in pivots:
                inv = pow(r[j], -1, p)
                pivots[j] = [(x * inv) % p for x in r]
                break
            u = pivots[j]
            c = r[j]
            for i in range(j, width):
                r[i] = (r[i] - c * u[i]) % p
    return len(pivots)


def bivectors(n, p):
    for i, j in combinations(range(n), 2):
        # Unique 2D planes via their reduced-row-echelon basis.
        fs = [(r, c) for r in (0, 1) for c in range(n)
              if c > (i if r == 0 else j) and c not in (i, j)]
        for v in product(range(p), repeat=len(fs)):
            basis = [[0] * n for _ in range(2)]
            basis[0][i] = basis[1][j] = 1
            for (r, c), val in zip(fs, v):
                basis[r][c] = val
            u, w = basis
            yield tuple((u[a] * w[b] - u[b] * w[a]) % p
                        for a, b in combinations(range(n), 2))


def wedge_sign(coords):
    return -1 if sum(coords[i] > coords[j]
                     for i in range(len(coords))
                     for j in range(i + 1, len(coords))) % 2 else 1


def constraints(n, p):
    pairs = list(combinations(range(n), 2))
    m = len(pairs)
    forms = list(combinations(range(n), 4))
    for z in bivectors(n, p):
        for quad in forms:
            row = [0] * (m*m)
            for a, (i, j) in enumerate(pairs):
                if not z[a] or i not in quad or j not in quad:
                    continue
                for c, (k, l) in enumerate(pairs):
                    if k not in quad or l not in quad or len({i,j,k,l}) != 4:
                        continue
                    sign = wedge_sign((i, j, k, l))
                    for b in range(m):
                        row[c*m+b] += sign * z[a] * z[b]
            if any(x % p for x in row):
                yield row


def wedge_rep_basis(n, p):
    pairs = list(combinations(range(n), 2))
    m = len(pairs)
    index = {ij: i for i, ij in enumerate(pairs)}
    for s in range(n):
        for t in range(n):
            flat = [0] * (m*m)
            for col, (i, j) in enumerate(pairs):
                terms = []
                if i == t:
                    terms.append((s,j,1))
                if j == t:
                    terms.append((i,s,1))
                for a, b, scale in terms:
                    if a == b:
                        continue
                    sign = 1 if a < b else -1
                    row = index[tuple(sorted((a,b)))]
                    flat[row*m+col] += sign * scale
            yield flat


def run(n,p):
    m=n*(n-1)//2
    image = list(wedge_rep_basis(n,p))
    image_rank = field_rank(image, m*m, p)
    assert image_rank == n*n, (n,p,image_rank)
    all_z = list(bivectors(n,p))
    rows = list(constraints(n,p))
    for r in rows:
        assert all(sum(a*b for a,b in zip(r, e))%p==0 for e in image)
    constraint_rank = field_rank(rows,m*m,p)
    assert m*m-constraint_rank==n*n, (n,p,m*m-constraint_rank,n*n)
    print('CHECK',f'n={n}',f'p={p}',f'planes={len(all_z)}',f'constraints={len(rows)}',
          f'constraint_rank={constraint_rank}',f'nullity={m*m-constraint_rank}',
          f'exterior_rep_rank={image_rank}')

if __name__=='__main__':
    for n,p in ((4,3),(4,5),(5,3)):
        run(n,p)
    print('VERIFY_OK')
