#!/usr/bin/env python3
"""Exact finite permutation certificate for a genus-two Richelot-kernel Frobenius spectrum.

Only the 15 unordered perfect matchings of six labels and the 16 even
subsets modulo complement are used; no external packages are required.
"""
from itertools import combinations
from collections import Counter
from math import lcm
import json

PARTS = [(6,), (5,1), (4,2), (4,1,1), (3,3), (3,2,1),
         (3,1,1,1), (2,2,2), (2,2,1,1), (2,1,1,1,1), (1,1,1,1,1,1)]


def matching_partitions(labels):
    if not labels:
        yield ()
        return
    x = labels[0]
    for j in range(1, len(labels)):
        y = labels[j]
        for rest in matching_partitions(labels[1:j] + labels[j+1:]):
            yield tuple(sorted(((x, y),) + rest))

MATCHINGS = tuple(sorted(set(matching_partitions(tuple(range(6))))))
assert len(MATCHINGS) == 15


def permutation_from_partition(part):
    mapping = list(range(6))
    start = 0
    for n in part:
        for i in range(n):
            mapping[start + i] = start + (i+1) % n
        start += n
    assert start == 6
    return tuple(mapping)


def move_matching(t, permutation):
    return tuple(sorted(tuple(sorted((permutation[a], permutation[b])))
                        for a, b in t))


def canonical_even_subsets():
    universe = set(range(6))
    classes = set()
    for n in (0, 2, 4, 6):
        for combination in combinations(range(6), n):
            subset = set(combination)
            classes.add(min((tuple(sorted(subset)),
                             tuple(sorted(universe - subset)))))
    return tuple(sorted(classes))

EVEN_CLASSES = canonical_even_subsets()
assert len(EVEN_CLASSES) == 16


def move_even_class(t, permutation):
    image = set(permutation[i] for i in t)
    return min((tuple(sorted(image)), tuple(sorted(set(range(6)) - image))))


def cycles(items, action):
    unseen = set(items)
    result = []
    while unseen:
        start = min(unseen)
        item = start
        length = 0
        while item in unseen:
            unseen.remove(item)
            item = action(item)
            length += 1
        assert item == start
        result.append(length)
    return tuple(sorted(result))


def burnside_crosscheck(items, action, cycle_type):
    # Independent check using fixed points of each action power.
    order = lcm(*cycle_type)
    for exponent in range(1, order+1):
        fixed = 0
        for item in items:
            point = item
            for _ in range(exponent):
                point = action(point)
            fixed += (point == item)
        expected = sum(d for d in cycle_type if exponent % d == 0)
        assert fixed == expected, (exponent, fixed, expected)


def poly_trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def poly_rem(a,b,p):
    a=poly_trim([x%p for x in a]);b=poly_trim([x%p for x in b]); assert b!=[0]
    while a!=[0] and len(a)>=len(b):
        coeff=a[-1]*pow(b[-1],-1,p)%p
        shift=len(a)-len(b)
        for i,x in enumerate(b):a[i+shift]=(a[i+shift]-coeff*x)%p
        a=poly_trim(a)
    return a


def poly_mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return poly_trim(out)


def poly_gcd(a,b,p):
    while b!=[0]:a,b=b,poly_rem(a,b,p)
    return [x*pow(a[-1],-1,p)%p for x in a]


def check_examples():
    p=7
    q1=[1,0,1] # x^2+1
    q2=[2,0,1] # x^2+2
    roots=lambda arr:[[-r%p,1] for r in arr]
    for q, linear_roots, expected_type in [(q2,(0,1),(2,2,1,1)),
                                            (None,(0,1,2,3),(2,1,1,1,1))]:
        factors=[q1] + ([q] if q is not None else []) + roots(linear_roots)
        # irreducible quadratics (and distinct degree-one factors)
        for factor in factors:
            if len(factor)==3:
                assert all((factor[0]+factor[1]*a+a*a)%p for a in range(p))
        for i in range(len(factors)):
            for j in range(i+1,len(factors)):
                assert poly_gcd(factors[i], factors[j],p)==[1]
        f=[1]
        for factor in factors:f=poly_mul(f,factor,p)
        assert len(f)==7, (f,expected_type)
        # squarefreeness of f: gcd(f,f') = 1
        derivative=[(i*f[i])%p for i in range(1,len(f))]
        assert poly_gcd(f,derivative,p)==[1]


def main():
    output=[]
    for part in PARTS:
        perm=permutation_from_partition(part)
        match_cycles=cycles(MATCHINGS,lambda t:move_matching(t,perm))
        torsion_cycles=cycles(EVEN_CLASSES,lambda t:move_even_class(t,perm))
        burnside_crosscheck(MATCHINGS,lambda t:move_matching(t,perm),match_cycles)
        burnside_crosscheck(EVEN_CLASSES,lambda t:move_even_class(t,perm),torsion_cycles)
        output.append({"branch_partition":part,"kernel_cycles":match_cycles,
                       "rational_kernels":match_cycles.count(1),
                       "rational_two_torsion":torsion_cycles.count(1)})
    assert len({r['kernel_cycles'] for r in output})==9
    groups={}
    for r in output:groups.setdefault(r['kernel_cycles'],[]).append(r['branch_partition'])
    collisions=[tuple(z) for z in groups.values() if len(z)>1]
    assert collisions==[((4,2),(4,1,1)),((2,2,1,1),(2,1,1,1,1))],collisions
    assert {r['rational_kernels'] for r in output}=={0,1,3,7,15}
    assert {r['rational_two_torsion'] for r in output}=={1,2,4,8,16}
    paired={r['branch_partition']:r for r in output}
    assert paired[(2,2,1,1)]['kernel_cycles']==paired[(2,1,1,1,1)]['kernel_cycles']
    assert paired[(2,2,1,1)]['rational_two_torsion']==4
    assert paired[(2,1,1,1,1)]['rational_two_torsion']==8
    assert paired[(6,)]['rational_kernels']==1 and paired[(6,)]['rational_two_torsion']==1
    check_examples()
    print(json.dumps(output,separators=(',',':')))
    print('RICHELOT_FROBENIUS_NINE_KERNEL_SPECTRA_VERIFIED')

if __name__ == '__main__':main()
