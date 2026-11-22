"""Exact rational certificate for small cyclic TV-ball projection face norms.

Run with Python 3, no external dependencies. The proof reduces the
infinite-dimensional input search to this finite exhaustive enumeration.
"""
from fractions import Fraction as F
from itertools import combinations, product


def tv(v):
    return sum(abs(v[(i+1)%len(v)]-v[i]) for i in range(len(v)))


def components(n, boundary_edges):
    """Blocks connected by zero-difference edges on the cycle."""
    groups = [set([i]) for i in range(n)]
    for i in range(n):
        if i in boundary_edges:
            continue
        j = (i+1) % n
        a = next(k for k,g in enumerate(groups) if i in g)
        b = next(k for k,g in enumerate(groups) if j in g)
        if a != b:
            groups[a] |= groups[b]
            groups.pop(b)
    return groups


def Qv(v, blocks):
    out = list(v)
    for block in blocks:
        m = sum((v[j] for j in block), F(0)) / len(block)
        for j in block:
            out[j] = m
    return out


def arc_vectors(n):
    # The 2n-choose-2 extremal edges in the zero-sum l1 gradient ball;
    # opposite indicators are redundant because constants are annihilated.
    seen = set()
    for a in range(n):
        for k in range(1,n):
            v = tuple(F(int((j-a)%n < k)) for j in range(n))
            code = min(v, tuple(1-x for x in v))
            if code in seen: continue
            seen.add(code)
            yield v


def check(n):
    worst_by_r = {}
    configs_by_r = {}
    arcs = list(arc_vectors(n))
    assert len(arcs) == n*(n-1)//2, (n,len(arcs))
    for r in range(2,n+1):
        for edges_tuple in combinations(range(n),r):
            edges = set(edges_tuple)
            blocks = components(n,edges)
            assert len(blocks)==r, (n,r,edges,blocks)
            for suffix in product((-1,1),repeat=r-1):
                signs = (1,)+suffix # global sign reversal doesn't change J
                if 1 not in signs or -1 not in signs: continue
                s = [F(0) for i in range(n)]
                for i,si in zip(edges_tuple,signs):s[i]=F(si)
                bts = [s[(j-1)%n]-s[j] for j in range(n)]
                g = Qv(bts,blocks)
                gg = sum(t*t for t in g)
                assert gg>0
                configs_by_r[r] = configs_by_r.get(r,0)+1
                for v in arcs:
                    z=Qv(v,blocks)
                    gv = sum(g[j]*v[j] for j in range(n))
                    out=[z[j]-g[j]*gv/gg for j in range(n)]
                    val=tv(out)/tv(v)
                    worst_by_r[r] = max(worst_by_r.get(r,F(0)),val)
    return worst_by_r, configs_by_r


if __name__=='__main__':
    goal={3:F(1),4:F(1),5:F(3,2)}
    for n in (3,4,5):
        rows,counts=check(n)
        maximum=max([F(1)]+list(rows.values()))
        print('n=',n,'face_counts=',counts,'face_maxima=',{k:str(v) for k,v in rows.items()},'with_interior=',maximum)
        assert maximum==goal[n]
    print('EXACT_COMPLETE_SMALL_CYCLE_FACE_CERTIFICATE_PASS')
