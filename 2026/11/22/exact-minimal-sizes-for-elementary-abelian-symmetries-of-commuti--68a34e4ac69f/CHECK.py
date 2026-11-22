"""Finite checks for commuting-permutation braid-solution constructions."""
from itertools import permutations
from math import factorial


def build(p, rank):
    if p == 2:
        if rank == 1:
            specs = [(1, 0)]
            free = False
            fixed = 0
        else:
            specs = [(1, 0), (0, 1), (1, 1)][:min(rank, 3)]
            free = rank in (5, 6)
            fixed = 2 if rank in (4, 6) else 0
    else:
        assert 1 <= rank <= p + 3
        specs = [(1, t) for t in range(p)] + [(0, 1)]
        if rank <= p + 1:
            specs = specs[:rank]
            free = False
        else:
            specs = specs[:rank - 2]
            free = True
        fixed = 0
    f, g = [], []
    for a, b in specs:
        base = len(f)
        f.extend(base + (t + a) % p for t in range(p))
        g.extend(base + (t + b) % p for t in range(p))
    if free:
        base = len(f)
        for u in range(p):
            for v in range(p):
                f.append(base + ((u + 1) % p) * p + v)
                g.append(base + u * p + ((v + 1) % p))
    for i in range(fixed):
        f.append(len(f))
        g.append(len(g))
    return tuple(f), tuple(g)


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def test():
    for p in (2, 3, 5):
        limit = 6 if p == 2 else p + 3
        for rank in range(1, limit + 1):
            f, g = build(p, rank)
            n = len(f)
            assert sorted(f) == list(range(n)) and sorted(g) == list(range(n))
            assert compose(f, g) == compose(g, f)
            # For R(x,y) = (f(y),g(x)), braid equation follows from fg=gf.
            for x in range(n):
                for y in range(n):
                    for z in range(n):
                        def R12(t):
                            a, b, c = t
                            return f[b], g[a], c
                        def R23(t):
                            a, b, c = t
                            return a, f[c], g[b]
                        assert R12(R23(R12((x,y,z)))) == R23(R12(R23((x,y,z))))
            if n <= 8:
                centralizer = [h for h in permutations(range(n)) if compose(h, f) == compose(f,h) and compose(h,g)==compose(g,h)]
                assert len(centralizer) == p**rank, (p,rank,n,len(centralizer))
                ident = tuple(range(n))
                assert all((lambda h: __import__('functools').reduce(lambda s,_: compose(s,h), range(p),ident) == ident)(h) for h in centralizer)
            print(f'p={p},rank={rank},n={n},expected_centralizer={p**rank}')
    print('COMMUTING_PERMUTATION_BRAID_CENTRALIZERS_OK')

if __name__ == '__main__':
    test()
