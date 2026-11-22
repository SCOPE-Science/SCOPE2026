#!/usr/bin/env python3
"""Reproduce all finite checks for a weight-resolved constrained deletion graph."""
from collections import defaultdict
from itertools import product
from math import comb

def words(n):
    return [''.join(v) for v in product('01', repeat=n) if all(not(v[i]=='1' and v[i+1]=='1') for i in range(n-1))]

def deletions(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def count_formula(n, k):
    a = (n-2*k+1)*comb(n-k+1,k-1) if k>=1 and n>=2*k else 0
    b = (n-2*k)*comb(n-k,k-1) if k>=1 and n>=2*k+1 else 0
    return a,b

def enumerate_edges(n):
    vv=words(n)
    ds={x: deletions(x) for x in vv}
    a=defaultdict(int); b=defaultdict(int)
    adj={x:set() for x in vv}
    for i,x in enumerate(vv):
        for y in vv[i+1:]:
            if len(ds[x]&ds[y]) >=2:
                wx=x.count('1'); wy=y.count('1')
                assert abs(wx-wy)<=1, (n,x,y)
                if wx==wy: a[wx]+=1
                else: b[min(wx,wy)]+=1
                adj[x].add(y);adj[y].add(x)
    return a,b,adj

def components(adj):
    seen=set();comp=[]
    for x in adj:
        if x in seen:continue
        todo=[x];seen.add(x);c=0
        while todo:
            y=todo.pop();c+=1
            for z in adj[y]:
                if z not in seen:seen.add(z);todo.append(z)
        comp.append(c)
    return sorted(comp)

def coef_P2(length, ones):
    if length<2*ones or ones<0:return 0
    a=length-2*ones;b=ones
    return (a+b+1)*comb(a+b,b)

def rational_coefficient(n,k,cross=False):
    # Coefficient of uz^(2+cross) P^2 / (1-uz^2).
    return sum(coef_P2(n-2*t-int(cross), k-t) for t in range(1,k+1))

def main():
    for n in range(2,13):
        a,b,adj=enumerate_edges(n)
        for k in range(1,(n+1)//2+1):
            fa,fb=count_formula(n,k)
            assert a[k]==fa,(n,k,'same',a[k],fa)
            assert b[k]==fb,(n,k,'cross',b[k],fb)
        assert adj['0'*n]==set()
        assert components(adj)==[1,len(adj)-1]
    for n in range(0,46):
        for k in range(1,(n+1)//2+2):
            fa,fb=count_formula(n,k)
            assert fa==rational_coefficient(n,k,False)
            assert fb==rational_coefficient(n,k,True)
            assert fb==count_formula(n-1,k)[0]
    print('PASS: direct deletion-spectrum graph counts and components for n=2..12')
    print('PASS: rational bivariate generating functions and shift for n=0..45')
if __name__=='__main__':main()
