#!/usr/bin/env python3
"""Independent exhaustive combinatorial checks of interval-blob packing identities."""
from collections import Counter
from itertools import combinations
from math import comb

def compatible(x,y):
    a,b=x; c,d=y
    return b+1<c or d+1<a

def enumerated(n):
    vertices=[(a,b) for a in range(1,n+1) for b in range(a,n+1)]
    allsets=[]
    def go(start,selected):
        allsets.append(tuple(selected))
        for j in range(start,len(vertices)):
            if all(compatible(vertices[j],vertices[i]) for i in selected):
                selected.append(j); go(j+1,selected); selected.pop()
    go(0,[])
    maximal=[s for s in allsets if not any(j not in s and all(compatible(vertices[j],vertices[i]) for i in s) for j in range(len(vertices)))]
    return vertices,allsets,maximal

def predicted_max(n,k):
    if k<1 or 2*k-1>n:return 0
    q=n-2*k+1
    return sum(comb(k+1,j)*comb(k+q-j-1,k-1) for j in range(min(q,k+1)+1))

def omission_of_max_set(n,vertices,s):
    boundaries=[]
    for j in sorted(s,key=lambda j:vertices[j]):
        a,b=vertices[j]; boundaries.extend([a,b+1])
    missing=set(range(1,n+2))-set(boundaries)
    assert len(missing)==1, (n,s,missing)
    return next(iter(missing))

def main():
    total=0
    for n in range(1,13):
        vertices,allsets,maximal=enumerated(n)
        actual=Counter(map(len,allsets))
        expected={k:comb(n+1,2*k) for k in range((n+1)//2+1)}
        assert all(actual[k]==v for k,v in expected.items()), ('independent',n,actual,expected)
        assert sum(actual.values())==2**n
        mcounts=Counter(map(len,maximal))
        assert all(mcounts[k]==predicted_max(n,k) for k in range(1,(n+1)//2+1)), ('maximal',n,mcounts)
        alpha=(n+1)//2
        maxima=[s for s in maximal if len(s)==alpha]
        if n%2:
            assert len(maxima)==1, ('odd maxima',n,len(maxima))
        else:
            assert len(maxima)==n+1
            omits={omission_of_max_set(n,vertices,s):s for s in maxima}
            assert set(omits)==set(range(1,n+2))
            m=n//2
            expected_edges={tuple(sorted((r,t))) for i in range(1,m+1) for r,t in combinations((2*i-1,2*i,2*i+1),2)}
            true_edges={tuple(sorted((r,t))) for r,t in combinations(omits,2) if len(set(omits[r])&set(omits[t]))==m-1}
            assert expected_edges==true_edges,('reconfiguration',n,true_edges^expected_edges)
            assert len(true_edges)==3*m
        total+=len(allsets)
        print(f'n={n} independent={len(allsets)} maximal={len(maximal)} optimal={len(maxima)}')
    print('VERIFY_OK exhaustive_independent_sets=',total,' all_structure_tests=PASS')

if __name__=='__main__':main()
