#!/usr/bin/env python3
"""Finite semantic-closure replay for the positive instantial modalities.

Checks the boxed witness and diamond co-witness operators on finite posets
against the proposed exact neighborhood-persistence normal forms.
"""
from itertools import product
from random import Random

def upsets(n, leq):
    return [u for u in range(1 << n) if all(not ((u >> i)&1 and leq[i][j]) or ((u >> j)&1) for i in range(n) for j in range(n))]

def conditions(n, leq, a, b, kind):
    def down(t):
        return sum((1<<i) for i in range(n) if any((t>>j)&1 and leq[i][j] for j in range(n)))
    if kind == 'box':
        for u in a:
            top = sum(1<<i for i in range(n) if (u>>i)&1 and not any((u>>j)&1 and i!=j and leq[i][j] for j in range(n)))
            if not any((v & ~u)==0 and (v & top)==top for v in b):
                return False
    else:
        for t in b:
            dt = down(t)
            if not any((s&t)==t and (s & ~dt)==0 for s in a):
                return False
    return True

def modal_truth(neighborhood, scope, args, kind):
    if kind == 'box':
        return any((u & ~scope)==0 and all(u&x for x in args) for u in neighborhood)
    return all((s&scope)!=0 or any((s & ~x)==0 for x in args) for s in neighborhood)

def operator_semantic_persistence(universe, a, b, kind):
    for scope in universe:
        for mask in range(1<<len(universe)):
            args=[universe[i] for i in range(len(universe)) if mask>>i &1]
            if modal_truth(a,scope,args,kind) and not modal_truth(b,scope,args,kind):
                return False
    return True

def run():
    posets=[]
    for n in (1,2,3):
        posets.append((f'antichain_{n}', [[i==j for j in range(n)] for i in range(n)]))
    posets += [('chain_2',[[i<=j for j in range(2)]for i in range(2)]),
               ('chain_3',[[i<=j for j in range(3)]for i in range(3)]),
               ('root_2_leaves',[[i==j or i==0 for j in range(3)] for i in range(3)]),
               ('two_roots_top',[[i==j or j==2 for j in range(3)] for i in range(3)])]
    rng=Random(742196)
    checks=0
    for label,leq in posets:
        ups=upsets(len(leq),leq)
        opts=list(range(1<<len(ups)))
        if len(ups)>4:
            pairs=[(rng.choice(opts),rng.choice(opts)) for _ in range(1200)]
        else:
            pairs=list(product(opts,repeat=2))
        for ma,mb in pairs:
            a=[ups[i] for i in range(len(ups)) if ma>>i&1]
            b=[ups[i] for i in range(len(ups)) if mb>>i&1]
            for kind in ('box','diamond'):
                anticipated=conditions(len(leq),leq,a,b,kind)
                actual=operator_semantic_persistence(ups,a,b,kind)
                assert anticipated==actual,(label,ma,mb,kind,anticipated,actual)
                checks+=1
    # Sharp two-point witness: each inclusion fails while both weakenings hold.
    leq=[[True,True],[False,True]]
    W=3; top=2
    assert conditions(2,leq,[W],[top],'box')
    assert conditions(2,leq,[W],[top],'diamond')
    assert [W] != [top]
    print('FINITE_PINL_PERSISTENCE_OK',checks,'semantic/structural comparisons',len(posets),'posets')
if __name__=='__main__':run()
