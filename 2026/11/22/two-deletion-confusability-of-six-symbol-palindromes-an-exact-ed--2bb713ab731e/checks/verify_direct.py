#!/usr/bin/env python3
"""Independent direct deletion-shadow check of the palindrome-conflict law."""
from collections import defaultdict
from itertools import combinations, product

def shadow(t):
    return {tuple(t[j] for j in range(6) if j not in pair)
            for pair in combinations(range(6),2)}

def typ(t):
    a,b,c=t
    if a==b==c:return 'aaa'
    if a==b:return 'aab'
    if a==c:return 'aba'
    if b==c:return 'abb'
    return 'abc'

def degree_formula(label,q):
    return {'aaa':3*q-3,'aab':6*q-6,'aba':9*q-12,
            'abb':6*q-7,'abc':9*q-11}[label]

def run():
    for q in range(1,8):
        triples=list(product(range(q),repeat=3))
        D=[shadow(t+t[::-1]) for t in triples]
        degree=[0]*len(triples)
        E=0
        for i in range(len(triples)):
            for j in range(i+1,len(triples)):
                if not D[i].isdisjoint(D[j]):
                    E+=1;degree[i]+=1;degree[j]+=1
        assert 2*E==q*q*(q-1)*(9*q-8), (q,E)
        for t,d in zip(triples,degree):
            assert d==degree_formula(typ(t),q), (q,t,d)
        print(f'q={q} vertices={q**3} edges={E} degree_table=OK')
    # An explicit constructive independent family: greedy pair-disjoint triples.
    for q in range(3,31):
        used=set();family=[]
        for t in combinations(range(q),3):
            pairs=set(combinations(t,2))
            if used.isdisjoint(pairs):
                used.update(pairs);family.append(t)
        assert len(family)*18 >= q*(q-1) # maximal triple-packing bound
        for i,t in enumerate(family):
            for s in family[i+1:]:
                assert len(set(t)&set(s))<=1
        # Each chosen triple creates the even palindrome t+reversed(t).
        if q<=10:
            d=[shadow(t+t[::-1]) for t in family]
            assert all(d[i].isdisjoint(d[j]) for i in range(len(d)) for j in range(i+1,len(d)))
    print('DIRECT_OK, greedy pair-packing constructive bound through q=30')

if __name__=='__main__':run()
