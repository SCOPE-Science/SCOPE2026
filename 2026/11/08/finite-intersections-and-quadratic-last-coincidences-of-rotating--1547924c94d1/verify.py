#!/usr/bin/env python3
"""Exact independent recurrence checks of cross-period RM-Fibonacci coincidence theorem."""
from math import floor

def rm(k, limit):
    seq = [0,1]
    for n in range(2,limit+1):
        seq.append(sum(seq[n-j] for j in range(1,2+n%k+1) if n-j>=0))
    return seq

def count_c(k,n):
    return max(0, n//k-(1 if k in (2,3) else 0))

def formula(k,n):
    if n==0:return 0
    if n==1:return 1
    c=count_c(k,n)
    assert n-2-2*c>=0
    return (2**(n-2-2*c))*(3**c)

def theoretical(k,l):
    if k==2:
        return {3:2,4:4,5:3}.get(l,2)
    if k==3:
        return {4:13,5:8,6:7,7:6,8:5}.get(l,4)
    d=l-k
    q=(k-1)//d
    return k-2 + q*k-d*q*(q+1)//2

def main():
    maxk=42
    bound=maxk*(maxk+3)+8
    ss={k:rm(k,bound) for k in range(2,maxk+1)}
    checked=0
    for k in range(2,maxk+1):
        for n in range(bound+1):
            if ss[k][n]!=formula(k,n):raise AssertionError(('formula',k,n,ss[k][n],formula(k,n)))
            checked+=1
    pairs=0
    for k in range(2,maxk+1):
        for l in range(k+1,maxk+1):
            s,t=ss[k],ss[l]
            a=set(s)
            b=set(t)
            common=a&b
            # R0=0 shared. For positive terms, 1 at indices 1 and 2.
            pred={s[n] for n in range(2,bound+1) if count_c(k,n)==count_c(l,n)}|{0}
            assert common==pred,('sets',k,l)
            assert len(common)-1==theoretical(k,l),('count',k,l,len(common)-1,theoretical(k,l))
            # Strong index-rigidity for all common values >1, checked by dictionaries.
            da={v:i for i,v in enumerate(s) if i>=2}
            db={v:i for i,v in enumerate(t) if i>=2}
            assert all(da[v]==db[v] for v in common if v>1),('indices',k,l)
            pairs+=1
    print('VERIFY_OK periods=2..%d recurrence_terms=%d period_pairs=%d exact_common_value_sets=yes exact_intersection_counts=yes index_rigidity=yes'%(maxk,checked,pairs))
    for k,l in [(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),(5,6),(7,8),(7,10)]:
        print('PAIR k=%d ell=%d positive_shared=%d'%(k,l,theoretical(k,l)))

if __name__=='__main__':main()
