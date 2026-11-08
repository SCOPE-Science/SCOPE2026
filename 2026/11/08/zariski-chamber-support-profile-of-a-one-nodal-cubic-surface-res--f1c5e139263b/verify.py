#!/usr/bin/env python3
"""Exact Zariski-support enumeration for a one-node weak cubic surface.

Run: python3 verify.py
Only standard-library integer arithmetic is used.
"""
from functools import lru_cache
from collections import Counter


def vec(d, coeff):
    """d*H - sum coeff_i*E_i; exceptional E_i has coefficient -1."""
    return (d,) + tuple(coeff)


def exc(i):
    return vec(0, [-int(j == i) for j in range(1, 7)])


def line(i, j):
    return vec(1, [int(h in (i, j)) for h in range(1, 7)])


def conic(i):
    return vec(2, [int(h != i) for h in range(1, 7)])


def intersection(x, y):
    return x[0]*y[0] - sum(a*b for a,b in zip(x[1:], y[1:]))


def curve_data(nodal):
    points = range(1, 7)
    cs = [(f'E{i}',exc(i)) for i in points]
    cs += [(f'L{i}{j}', line(i,j)) for i in points for j in points if i<j
           and (not nodal or not ({i,j} <= {1,2,3}))]
    cs += [(f'Q{i}',conic(i)) for i in points if not nodal or i in (1,2,3)]
    return cs


def graph(cs):
    n=len(cs)
    neighbors=[0]*n
    for i,(_,x) in enumerate(cs):
        assert intersection(x,x)==-1
        for j,(_,y) in enumerate(cs):
            if j==i: continue
            z=intersection(x,y)
            assert z in (0,1)
            if z: neighbors[i] |= 1<<j
    return neighbors


def independent_polynomial(neighbors, extra=None):
    """Memoized exact deletion/closed-neighborhood recurrence.

    A coefficient of (degree,contacts) counts pairwise disjoint (-1)-sets.
    """
    n=len(neighbors)
    if extra is None: extra=[0]*n
    @lru_cache(None)
    def calculate(mask):
        if not mask: return (((0,0),1),)
        bit=mask&-mask
        i=bit.bit_length()-1
        skip=dict(calculate(mask^bit))
        include=dict(calculate((mask^bit)&~neighbors[i]))
        out=Counter(skip)
        for (degree,contacts), multiplicity in include.items():
            out[(degree+1,contacts+extra[i])] += multiplicity
        return tuple(sorted(out.items()))
    return dict(calculate((1<<n)-1))


def independent_bruteforce(neighbors, contacts):
    """Independent 2^21-state subset dynamic program."""
    n=len(neighbors)
    flags=bytearray(1<<n)
    flags[0]=1
    normal=Counter(); withroot=Counter()
    contactmask=sum(1<<i for i,c in enumerate(contacts) if c)
    for mask in range(1<<n):
        if mask:
            bit=mask&-mask
            i=bit.bit_length()-1
            smaller=mask^bit
            flags[mask]=int(flags[smaller] and not (neighbors[i]&smaller))
        if flags[mask]:
            size=mask.bit_count()
            normal[size]+=1
            if (mask&contactmask).bit_count()<2:
                withroot[size+1]+=1
    return normal,withroot


def as_tuple(data, length=7):
    return tuple(data.get(i,0) for i in range(length))


def main():
    nodal=curve_data(True)
    assert len(nodal)==21
    root=vec(1, (1,1,1,0,0,0))
    assert intersection(root,root)==-2
    contacts=[intersection(root,c) for _,c in nodal]
    assert contacts.count(1)==6 and set(contacts)=={0,1}
    assert [name for (name,_),hit in zip(nodal,contacts) if hit] == [
        'E1','E2','E3','L45','L46','L56']
    neighbors=graph(nodal)
    rec=independent_polynomial(neighbors,contacts)
    nonroot=Counter(); rootincluded=Counter()
    for (degree,hits),multiplicity in rec.items():
        nonroot[degree]+=multiplicity
        if hits<2: rootincluded[degree+1]+=multiplicity
    brute0,brute1=independent_bruteforce(neighbors,contacts)
    assert nonroot==brute0 and rootincluded==brute1
    full=nonroot+rootincluded
    assert as_tuple(nonroot)==(1,21,135,370,465,237,21)
    assert as_tuple(rootincluded)==(0,1,21,120,260,210,36)
    assert as_tuple(full)==(1,22,156,490,725,447,57)
    assert sum(full.values())==1898
    smooth=curve_data(False)
    assert len(smooth)==27
    smoothed=independent_polynomial(graph(smooth))
    baseline=Counter()
    for (size,_),multiplicity in smoothed.items(): baseline[size]+=multiplicity
    assert as_tuple(baseline)==(1,27,216,720,1080,648,72)
    assert sum(baseline.values())==2764
    print('negative_curves=21; unique_minus_two_root=1')
    print('root_contacts=E1,E2,E3,L45,L46,L56')
    print('nonroot_support_profile='+str(as_tuple(nonroot)))
    print('root_support_profile='+str(as_tuple(rootincluded)))
    print('combined_support_profile='+str(as_tuple(full)))
    print('chambers_total='+str(sum(full.values())))
    print('smooth_cubic_profile='+str(as_tuple(baseline)))
    print('smooth_cubic_total='+str(sum(baseline.values())))
    print('independent_enumeration_agrees=True')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
