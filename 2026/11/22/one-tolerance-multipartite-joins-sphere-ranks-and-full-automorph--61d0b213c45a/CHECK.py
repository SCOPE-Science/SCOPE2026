"""Standalone exact checks for partition-matroid one-tolerance homotopy character.
Requires only Python 3 standard library; no data files or installed packages.
Finite checks support, but do not replace, the written all-size proof.
"""
from itertools import combinations, permutations, product
from math import comb, prod


def blocks(sizes):
    off = 0
    result = []
    for a in sizes:
        result.append(tuple(range(off, off + a)))
        off += a
    return result


def faces(sizes):
    bs = blocks(sizes)
    v = sum(sizes)
    for k in range(min(v, len(sizes)+1)+1):
        for s in combinations(range(v), k):
            if sum(max(0, len(set(s).intersection(b))-1) for b in bs) <= 1:
                yield s


def symmetry(sizes, p, local):
    bs = blocks(sizes)
    return tuple(bs[p[i]][local[i][j]] for i, sz in enumerate(sizes) for j in range(sz))


def chain_trace(sizes, g):
    val = 0
    for face in faces(sizes):
        image = [g[x] for x in face]
        if sorted(image) != list(face):
            continue
        parity = sum(image[i] > image[j] for i in range(len(image)) for j in range(i+1, len(image)))
        val += -1 if not face else (-1)**(len(face)-1+parity)
    return (-1)**len(sizes) * val


def formula(sizes, p, g):
    bs = blocks(sizes)
    seen = set()
    orbits = []
    for i in range(len(sizes)):
        if i in seen:
            continue
        j, orbit = i, []
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = p[j]
        def iterate(v, n):
            for _ in range(n):
                v = g[v]
            return v
        f = sum(iterate(v, len(orbit)) == v for v in bs[i])
        c = sum(iterate(v, 2) == v and g[v] != v for v in bs[i])//2 if len(orbit)==1 else 0
        orbits.append((len(orbit), f, c))
    total = prod(1-f for l, f, c in orbits)
    total += sum((comb(f, 2)-c)*prod(1-orbits[j][1] for j in range(len(orbits)) if j != i)
                 for i, (l, f, c) in enumerate(orbits) if l==1)
    return (-1)**(len(sizes)+1)*total


def mod_rank(columns, prime):
    # Sparse columns as dictionaries of row index -> coefficient modulo prime.
    pivots = {}
    rank = 0
    for v in columns:
        x = {k: val % prime for k, val in v.items() if val % prime}
        while x:
            lead = max(x)
            if lead not in pivots:
                inverse = pow(x[lead], -1, prime)
                pivots[lead] = {k: val*inverse % prime for k, val in x.items()}
                rank += 1
                break
            p = pivots[lead]
            scale = x[lead]
            for k, val in p.items():
                nv = (x.get(k, 0) - scale*val) % prime
                if nv:
                    x[k] = nv
                else:
                    x.pop(k, None)
    return rank


def betti(sizes, prime):
    fs = list(faces(sizes))
    by_dim = {}
    for f in fs:
        if f:
            by_dim.setdefault(len(f)-1, []).append(f)
    ranks = {}
    for k in range(1, len(sizes)+1):
        rows = {f:i for i, f in enumerate(by_dim.get(k-1, []))}
        cols = []
        for s in by_dim.get(k, []):
            cols.append({rows[s[:j]+s[j+1:]]:(-1)**j for j in range(len(s))})
        ranks[k] = mod_rank(cols, prime)
    ranks[0] = 0
    return [len(by_dim.get(k, [])) - ranks.get(k, 0) - ranks.get(k+1, 0)
            - (1 if k==0 else 0) for k in range(len(sizes)+1)]


def main():
    tested = 0
    for sizes in [(2,2,2),(2,2,2,2),(3,3,2),(3,3,3),(2,3,2,3)]:
        p_opts = [p for p in permutations(range(len(sizes))) if all(sizes[i]==sizes[p[i]] for i in range(len(sizes)))]
        locals_ = [list(permutations(range(a))) for a in sizes]
        cnt = 0
        for p in p_opts:
            for local in product(*locals_):
                g = symmetry(sizes, p, local)
                expected = formula(sizes, p, g)
                actual = chain_trace(sizes, g)
                assert actual == expected, (sizes, p, local, expected, actual)
                if all(a == 2 for a in sizes):
                    internal_parity = sum(local[i] != tuple(range(sizes[i])) for i in range(len(sizes)))
                    part_parity = sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))
                    special = (-1)**(internal_parity + part_parity) * (sum(p[i] == i for i in range(len(p)))-1)
                    assert actual == special, (sizes, p, local, actual, special)
                cnt += 1
        tested += cnt
        print('ALL WREATH ELEMENTS', sizes, cnt, 'PASS')
    for sizes in [(2,2),(2,2,2),(2,2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,2,2),(4,3,2)]:
        b = ((sum(sizes)-2)*prod(a-1 for a in sizes))//2
        assert (sum(sizes)-2)*prod(a-1 for a in sizes) == 2*b
        for prime in (2,3):
            actual = betti(sizes, prime)
            assert actual == [0]*len(sizes) + [b], (sizes, prime, actual, b)
            print('MODULAR REDUCED BETTI', sizes, 'prime', prime, 'PASS', actual)
    print('PASS', tested, 'signed wreath-character checks and all modular homology checks')


if __name__=='__main__':
    main()
