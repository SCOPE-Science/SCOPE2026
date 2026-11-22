#!/usr/bin/env python3
"""Independently enumerate direct local-color conditions on small Boolean cubes."""
from itertools import combinations


def side_subsets(d, side):
    vertices=[v for v in range(1<<d) if v.bit_count()%2==side]
    other=[v for v in range(1<<d) if v.bit_count()%2!=side]
    successful=[]
    for bits in range(1<<len(vertices)):
        chosen={v for j,v in enumerate(vertices) if (bits>>j)&1}
        if all(sum((v^(1<<k)) in chosen for k in range(d))%2 for v in other):
            successful.append(chosen)
    return vertices,successful


def is_strong_odd(d, color):
    for v in range(1<<d):
        neigh=[color[v^(1<<j)] for j in range(d)]
        if color[v] in neigh:return False
        for c in set(neigh):
            if neigh.count(c)%2!=1:return False
    return True


def check(d):
    e,es=side_subsets(d,0)
    o,os=side_subsets(d,1)
    assert len(es)==len(os)==2**(2**(d-2))
    total=0
    for a in es:
        for b in os:
            color={v:(0 if v in a else 1) for v in e}
            color.update({v:(2 if v in b else 3) for v in o})
            assert len(set(color.values()))==4
            assert is_strong_odd(d,color)
            total+=1
    assert total==2**(2**(d-1))
    print('d=%d E_choices=%d O_choices=%d fixed_palette_assignments=%d named= %d unlabelled=%d'%(d,len(es),len(os),total,6*total,total//4))

if __name__=='__main__':
    for d in (2,4):check(d)
