"""Exact finite certificate replay for ternary multiset two-deletion optima.

Usage: python3 s3_check.py s3_cert.json
Only Python's standard library is required. This is a finite mathematical certificate.
"""
import json
import sys
from fractions import Fraction
from itertools import combinations


def dist(u,v):
    return sum(abs(a-b) for a,b in zip(u,v))//2


def valid(u,n):
    return len(u)==3 and all(type(z) is int and z>=0 for z in u) and sum(u)==n


def check(path):
    obj=json.load(open(path,encoding='utf-8'))
    rows=obj['records']
    assert [r['n'] for r in rows]==list(range(6,21))
    for rec in rows:
        n=rec['n'];val=rec['optimum']
        universe=[(a,b,n-a-b) for a in range(n+1) for b in range(n+1-a)]
        cover={u:Fraction(0) for u in universe}
        witness=[tuple(u) for u in rec['witness']]
        assert len(witness)==val and len(set(witness))==len(witness)
        assert all(valid(u,n) for u in witness)
        assert all(dist(u,v)>=3 for u,v in combinations(witness,2))
        cost=Fraction(0)
        for raw_clique,raw_weight in rec['dual_cliques']:
            clique=[tuple(u) for u in raw_clique]
            weight=Fraction(raw_weight)
            assert weight>0 and len(set(clique))==len(clique)
            assert all(u in cover for u in clique)
            assert all(dist(u,v)<=2 for u,v in combinations(clique,2))
            cost+=weight
            for u in clique: cover[u]+=weight
        assert all(cover[u]>=1 for u in universe)
        assert cost==Fraction(rec['dual_cost']) and cost<val+1
        residues=[0]*7
        for a,b,c in universe: residues[(a+3*b)%7]+=1
        assert rec['cyclic_sizes']==residues and rec['cyclic_max']==max(residues)
        print(f'n={n:2d} size={val:2d} lower= {val:2d} upper=floor({cost})={cost.numerator//cost.denominator} dual_cliques={len(rec["dual_cliques"]):3d}')
    print('CERTIFICATE VERIFIED: 15 length values, exact rational upper bounds and explicit lower witnesses')


if __name__=='__main__':
    check(sys.argv[1] if len(sys.argv)>1 else 's3_cert.json')
