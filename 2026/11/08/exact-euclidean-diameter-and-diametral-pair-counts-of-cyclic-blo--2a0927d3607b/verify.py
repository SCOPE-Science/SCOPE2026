#!/usr/bin/env python3
"""Exact finite checks for cyclic-block Euclidean diameter and pair enumeration.
All distances are squared using coordinates multiplied by two; no rounding.
This verifier is supplementary to the all-parameter proof.
"""
from itertools import combinations, product
from math import comb

def independent_masks(m):
    for bits in range(1 << m):
        if all(not ((bits >> i) & 1 and (bits >> ((i+1)%m)) & 1) for i in range(m)):
            yield bits

def vertices(m, a):
    result=[]
    for bits in independent_masks(m):
        blocks=[i for i in range(m) if bits & (1 << i)]
        for labels in product(range(a),repeat=len(blocks)):
            v=[0]*(m*a)
            for i,j in zip(blocks,labels):
                v[i*a+j]=2
            result.append(tuple(v))
    if m%2:
        for labels in product(range(a),repeat=m):
            v=[0]*(m*a)
            for i,j in enumerate(labels):
                v[i*a+j]=1
            result.append(tuple(v))
    assert len(result)==len(set(result))
    for v in result:
        assert all(z>=0 for z in v)
        r=[sum(v[i*a:(i+1)*a]) for i in range(m)]
        assert all(r[i]+r[(i+1)%m]<=2 for i in range(m))
    return result

def predicted_count(m,a):
    r=m//2
    if m%2==0:
        return a**(2*r) + (a*(a-1))**r
    return m*sum(a**(2*r-t)*(a-1)**t for t in range(r))+(m*(a*(a-1))**r)//2

def run():
    cases=0
    pair_tests=0
    checked=0
    for m in range(4,10):
        for a in range(1,4):
            v=vertices(m,a)
            if len(v)>1500: continue
            cases+=1
            mx=-1; count=0
            for ix,x in enumerate(v):
                for y in v[ix+1:]:
                    ds=sum((p-q)**2 for p,q in zip(x,y))
                    pair_tests+=1
                    if ds>mx:
                        mx=ds;count=1
                    elif ds==mx:
                        count+=1
            assert mx==8*(m//2), ('diameter',m,a,mx)
            assert count==predicted_count(m,a),('pairs',m,a,count,predicted_count(m,a))
            checked+=1
            print(f'm={m} a={a} vertices={len(v)} max_distance_squared={mx}/4 diametral_pairs={count}')
    # Independent block-mask overlap enumeration (distinct masks and same masks)
    for m in range(4,23):
        r=m//2
        M=[x for x in independent_masks(m) if x.bit_count()==r]
        assert len(M)==(2 if m%2==0 else m)
        for a in (1,2,3,4,5):
            q=0
            for ix,s in enumerate(M):
                q+=(a*(a-1))**r//2 if ((a*(a-1))**r)%2==0 else 0
                # a(a-1) always even, fine
                for t in M[ix+1:]:
                    o=(s&t).bit_count()
                    q+=a**(2*r-o)*(a-1)**o
            assert q==predicted_count(m,a),(m,a,q,predicted_count(m,a))
            checked+=1
    print('PASS',cases,'direct cyclic cases;',pair_tests,'exact squared pair distances;',checked,'model checks')
if __name__=='__main__':run()
