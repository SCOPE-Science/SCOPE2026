#!/usr/bin/env python3
"""Finite checks of parity-side adjacency ranks in even-dimensional cubes."""
from itertools import product


def gf2_rank(rows, ncolumns):
    basis = {}
    for row in rows:
        v = row
        while v:
            p = v.bit_length()-1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def matrices(d):
    e = [x for x in range(1<<d) if x.bit_count()%2==0]
    o = [x for x in range(1<<d) if x.bit_count()%2==1]
    pos = {x:i for i,x in enumerate(e)}
    rows = [sum(1<<pos[y^(1<<i)] for i in range(d)) for y in o]
    return e,o,rows


def check(d):
    e,o,rows=matrices(d)
    n=len(e)
    rank=gf2_rank(rows,n)
    assert rank==2**(d-2),(d,rank)
    f0=sum(1<<i for i,x in enumerate(e) if not(x&1))
    assert all((r&f0).bit_count()%2==1 for r in rows)
    assert all((r&((1<<n)-1)).bit_count()%2==0 for r in rows)
    print('d=%d nside=%d rank=%d free=%d solutions=%s'%(d,n,rank,n-rank, str(1<<(n-rank))))
    if d<=4:
        sol=[f for f in range(1<<n) if all((r&f).bit_count()%2==1 for r in rows)]
        assert len(sol)==2**(n-rank)
        assert 0 not in sol and (1<<n)-1 not in sol
        assert 6*len(sol)*len(sol)==6*(2**(2**(d-1)))
        print('  exhaustive_side_solutions=%d named_split_colorings=%d'%(len(sol),6*len(sol)**2))

if __name__=='__main__':
    for d in (2,4,6,8):check(d)
