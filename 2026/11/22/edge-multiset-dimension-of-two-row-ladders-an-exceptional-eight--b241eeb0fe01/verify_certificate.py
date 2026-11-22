#!/usr/bin/env python3
"""Independently check exhaustive obstruction pairs by coordinate distance.
The certificate is complete because each case's ordered record follows the
lexicographic itertools.combinations ordering, with an entry for every subset.
"""
import json,sys
from itertools import combinations

def edges(n):
    return [(2*i,2*i+1) for i in range(n)]+[(2*i+j,2*(i+1)+j) for i in range(n-1) for j in (0,1)]
def edge_distance(v,e):
    def dd(x,y): return abs(x//2-y//2)+(x%2!=y%2)
    return min(dd(v,e[0]),dd(v,e[1]))
def sig(e,S): return sorted(edge_distance(v,e) for v in S)
def main():
    fname=sys.argv[1] if len(sys.argv)>1 else 'finite_obstructions.json'
    dat=json.load(open(fname))
    assert dat['schema_version']==1
    observed=set()
    for case in dat['cases']:
        n,k=case['n'],case['k'];E=edges(n);pairs=case['pairs'];ct=0
        assert (n<=4 and 0<=k<=2*n) or (n in (5,6,8) and k==3)
        assert (n,k) not in observed;observed.add((n,k))
        it=combinations(range(2*n),k)
        for S,pair in zip(it,pairs):
            a,b=pair
            assert isinstance(a,int) and isinstance(b,int) and 0<=a<b<len(E)
            assert sig(E[a],S)==sig(E[b],S),(n,k,S,pair)
            ct+=1
        assert ct==len(pairs) and next(it,None) is None,(n,k,ct)
    assert observed=={(n,k) for n in (2,3,4) for k in range(2*n+1)}|{(n,3) for n in (5,6,8)}
    print('FINITE_OBSTRUCTION_CERTIFICATE_OK',len(observed),'cases')
if __name__=='__main__':main()
