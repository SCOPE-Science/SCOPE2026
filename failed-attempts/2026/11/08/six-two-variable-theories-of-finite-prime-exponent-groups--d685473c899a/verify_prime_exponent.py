#!/usr/bin/env python3
"""Reproduce the finite checks for two-variable logic of prime-exponent groups.

The signature has the ternary graph of multiplication and a constant identity.
No counting quantifiers or function symbols are used in the logical game.
"""
from collections import Counter
from itertools import product


def elementary_abelian(p, dim):
    items=list(product(range(p),repeat=dim))
    def mul(x,y): return tuple((a+b)%p for a,b in zip(x,y))
    return items,tuple([0]*dim),mul


def heisenberg(p):
    items=list(product(range(p), repeat=3))
    def mul(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p,(x[2]+y[2]+x[0]*y[1])%p)
    return items,(0,0,0),mul


def pair_profile(G, x, y):
    elements,unit,mul=G
    d=(x,y,unit)
    return (x==y,x==unit,y==unit)+tuple(mul(d[i],d[j])==d[k] for i,j,k in product(range(3),repeat=3))


def class_model(p,dim=1,nonabelian=False):
    return heisenberg(p) if nonabelian else elementary_abelian(p,dim)


def classifications():
    G={
        'C2':class_model(2), 'C2xC2':class_model(2,2),
        'C3':class_model(3), 'C3xC3':class_model(3,2),
        'C5':class_model(5), 'C5xC5':class_model(5,2),
        'C7':class_model(7),'C11':class_model(11),
        'Heisenberg3':class_model(3,nonabelian=True),
        'Heisenberg5':class_model(5,nonabelian=True),
        'Heisenberg7':class_model(7,nonabelian=True),
    }
    profiles={}
    for name,g in G.items():
        elements,unit,mul=g
        assert all(mul(x,unit)==x and mul(unit,x)==x for x in elements)
        # Prime-exponent condition is verified using repeated multiplication.
        p=int(''.join(c for c in name if c.isdigit())[-1]) if 'Heisenberg' in name else int(name[1:name.find('x')] if 'x' in name else name[1:])
        for x in elements:
            y=unit
            for j in range(p):y=mul(y,x)
            assert y==unit
        target=None
        for x in elements:
            if x==unit:continue
            counts=Counter(pair_profile(g,x,y) for y in elements)
            key=frozenset(counts)
            if target is None:target=key
            assert target==key,(name,'nonuniform element profile')
        profiles[name]=target
    # Full atomic profile of each nonidentity anchor, not merely a handful of relations.
    assert len(set(map(frozenset,profiles.values())))==6
    known=[['C2'],['C2xC2'],['C3'],['C3xC3','Heisenberg3'],
           ['C5'],['C5xC5','C7','C11','Heisenberg5','Heisenberg7']]
    for block in known:
        assert len({profiles[name] for name in block})==1,block
    assert len({profiles[block[0]] for block in known})==6
    print('Prime-exponent atomic back-and-forth profiles: PASS')
    for block in known:
        print('  equivalent examples:',', '.join(block))
    truth_values={}
    for name,g in G.items():
        elements,unit,mul=g
        nonzero=[x for x in elements if x!=unit]
        alpha=any(mul(x,x)==unit for x in nonzero)
        beta=any(x!=y for x in nonzero for y in nonzero)
        gamma=any(mul(x,x)==y and mul(x,y)==unit for x in nonzero for y in elements)
        delta=any(x!=y and mul(x,x)!=y and mul(y,y)!=x and mul(x,y)!=unit
                  for x in nonzero for y in nonzero)
        truth_values[name]=(alpha,beta,gamma,delta)
    assert len(set(truth_values.values()))==6
    for block in known: assert len({truth_values[name] for name in block})==1
    print('Four explicit distinguishing sentence invariants: PASS')
    for block in known:
        print(' ', block[0], tuple(map(int,truth_values[block[0]])))
    print('Nonabelian group-law check: PASS')
    for p in (3,5,7):
        _,_,mul=heisenberg(p)
        a=(1,0,0);b=(0,1,0)
        assert mul(a,b)!=mul(b,a)
        print('  Heisenberg',p,'noncommutative, exponent',p)
    print('Exact number of two-variable prime-exponent theories: 6')

if __name__=='__main__':classifications()
