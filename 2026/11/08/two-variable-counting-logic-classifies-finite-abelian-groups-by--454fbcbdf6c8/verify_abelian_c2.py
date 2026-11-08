#!/usr/bin/env python3
"""Reproduce complete small-order C2 checks for finite abelian groups.

Language: equality, a named zero, and ternary R(x,y,z) iff x+y=z.
The refinement below includes all 27 substitutions of x, y, and zero
into the three argument positions, not merely selected multiplication tests.
All operations are deterministic and use Python's standard library.
"""
from collections import Counter
from itertools import product
from math import prod


def partitions(n, low=1):
    if n == 0:
        yield ()
    for k in range(low, n+1):
        for rest in partitions(n-k, k):
            yield (k,) + rest


def group_types(n):
    factors=[]
    d=n
    p=2
    while p*p<=d:
        if d%p == 0:
            e=0
            while d%p == 0:
                d//=p; e+=1
            factors.append((p,e))
        p+=1
    if d>1:
        factors.append((d,1))
    if not factors:
        return [()]
    return [tuple(sorted(sum((tuple(p**k for k in a) for (p,_),a in zip(factors,choice)), ())))
            for choice in product(*(tuple(partitions(e)) for p,e in factors))]


def invariant(factors):
    power2=tuple(sorted(k for k in factors if k%2==0))
    odd_size=prod(k for k in factors if k%2==1)
    odd_3torsion=3**sum(1 for k in factors if k%3==0)
    return power2,odd_size,odd_3torsion


def multiplication(factors):
    els=list(product(*(range(k) for k in factors))) if factors else [()]
    ids={x:i for i,x in enumerate(els)}
    table=[[ids[tuple((a+b)%k for a,b,k in zip(x,y,factors))]
            for y in els] for x in els]
    n=len(els)
    zero=ids[(0,)*len(factors)]
    assert zero==0
    return table


def compact_type(squares,inverses,a,b):
    return (a==b, a==0, b==0, squares[a]==0, squares[b]==0,
            squares[a]==b, squares[b]==a, inverses[a]==b)


def full_type(table,a,b):
    labels=(a,b,0)
    return ((a==b,a==0,b==0),
            tuple(table[labels[i]][labels[j]]==labels[k]
                  for i,j,k in product(range(3),repeat=3)))


def c2_equivalent(table_a,table_b):
    tables=(table_a,table_b)
    nums=[len(t) for t in tables]
    squares=[[t[i][i] for i in range(n)] for t,n in zip(tables,nums)]
    inverses=[[next(j for j in range(n) if t[i][j]==0) for i in range(n)]
              for t,n in zip(tables,nums)]
    atoms=[[[compact_type(squares[u],inverses[u],i,j)
             for j in range(nums[u])] for i in range(nums[u])]
           for u in (0,1)]
    def relabel(keys):
        lookup={key:i for i,key in enumerate(sorted(set(keys.values())))}
        return {c:lookup[key] for c,key in keys.items()}
    colors=relabel({(u,i):atoms[u][i][i] for u in (0,1) for i in range(nums[u])})
    rounds=0
    while True:
        rounds+=1
        keys={}
        for u in (0,1):
            for i in range(nums[u]):
                histogram=Counter((atoms[u][i][j],colors[u,j]) for j in range(nums[u]))
                keys[u,i]=(colors[u,i],tuple(sorted(histogram.items())))
        newer=relabel(keys)
        if len(set(newer.values()))==len(set(colors.values())):
            colors=newer
            break
        assert rounds<=sum(nums)
        colors=newer
    return (Counter(colors[0,i] for i in range(nums[0]))
            ==Counter(colors[1,i] for i in range(nums[1]))),rounds


def test_atomic_normalization():
    # Exhaustively verify that the compact signature encodes every atomic
    # substitution of x, y, zero for a broad collection of group types.
    mapping={}
    for n in range(1,37):
        for factors in group_types(n):
            t=multiplication(factors); sq=[t[i][i] for i in range(n)]
            inv=[next(j for j in range(n) if t[i][j]==0) for i in range(n)]
            for i in range(n):
                for j in range(n):
                    compact=compact_type(sq,inv,i,j)
                    full=full_type(t,i,j)
                    if compact in mapping: assert mapping[compact]==full
                    else: mapping[compact]=full
    print('ATOMIC_NORMALIZATION_OK','distinct_compact_types',len(mapping))


def run():
    test_atomic_normalization()
    groups=0; compared=0
    print('COMPLETE_FINITE_CHECK max_order=128')
    for order in range(1,129):
        kinds=group_types(order)
        groups+=len(kinds)
        tables={k:multiplication(k) for k in kinds}
        for i,x in enumerate(kinds):
            for y in kinds[i+1:]:
                actual,_=c2_equivalent(tables[x],tables[y])
                assert actual==(invariant(x)==invariant(y)),(order,x,y,actual)
                compared+=1
        if order in (8,16,36,50,64,81,100,108,125,128):
            print('ORDER',order,'abelian_types',len(kinds),'theory_types',len(set(map(invariant,kinds))))
    print('COMPLETE_OK', 'group_types', groups, 'pairs',compared)

    examples=[((2,25),(2,5,5),True),
              ((2,3,3,3),(2,3,9),False),
              ((4,9,9),(4,3,27),True),
              ((2,3,25),(2,3,5,5),True),
              ((2,2,9,9),(4,9,9),False)]
    for a,b,want in examples:
        actual,rounds=c2_equivalent(multiplication(a),multiplication(b))
        assert actual==want,(a,b,actual,want)
        print('PAIR_OK',a,b,'equivalent',actual,'rounds',rounds)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
