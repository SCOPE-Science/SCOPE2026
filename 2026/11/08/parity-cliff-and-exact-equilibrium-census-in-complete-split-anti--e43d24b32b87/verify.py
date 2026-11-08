#!/usr/bin/env python3
"""Exact finite checks for the complete-split anti-coordination theorem.
Run: python3 verify.py (Python standard library only).
This finite computation supports, but does not replace, the all-size proof.
"""
from math import comb

def cut(c,m,k,l):
    return k*(c-k)+k*(m-l)+(c-k)*l

def predicted_profiles(c,m):
    assert c>=1 and m>=1
    for k in range(c+1):
        for l in range(m+1):
            if k<c/2 and l != m: continue
            if k>c/2 and l != 0: continue
            if k == c/2 and abs(2*l-m)>1: continue
            if 0<k and 2*(k+l)>c+m+1: continue
            if k<c and 2*(k+l)<c+m-1: continue
            yield k,l

def predicted_total(c,m):
    # Two orientation choices for each noncentral minority-clique occupation.
    subtotal = 0
    for k in range((c-1)//2+1):
        if (k == 0 and m>=c-1) or (k>0 and c-1<=2*k+m<=c+1):
            subtotal += comb(c,k)
    ans = 2*subtotal
    if c%2==0:
        r=c//2
        ans += comb(c,r)*sum(comb(m,l) for l in range(m+1) if abs(2*l-m)<=1)
    return ans

def opt_formula(c,m):
    d=max(c-m,0)
    return c*m+(d*d)//4

def worst_formula(c,m):
    if c%2: return opt_formula(c,m)
    return c*c//4+c*m//2

def explicit_profile(c,m,mask):
    vals=[(mask>>i)&1 for i in range(c+m)]
    edges=[(u,v) for u in range(c) for v in range(u+1,c)] + [(u,v) for u in range(c) for v in range(c,c+m)]
    cutnum=sum(vals[u]!=vals[v] for (u,v) in edges)
    is_ne=True
    for u in range(c+m):
        current=sum(vals[u]!=vals[v] for x,v in edges if x==u)+sum(vals[u]!=vals[x] for x,v in edges if v==u)
        degree=sum(1 for x,v in edges if x==u or v==u)
        if current < degree-current: is_ne=False
    return vals[:c].count(1),vals[c:].count(1),cutnum,is_ne

labeled=0
for c in range(1,9):
    for m in range(1,9):
        seen={}
        n=c+m
        all_cuts=[]; nash=[]
        for mask in range(1<<n):
            k,l,w,ok=explicit_profile(c,m,mask)
            assert w==cut(c,m,k,l)
            assert ok==((k,l) in set(predicted_profiles(c,m))), (c,m,k,l)
            all_cuts.append(w)
            if ok:nash.append(w)
        assert len(nash)==predicted_total(c,m),(c,m,len(nash),predicted_total(c,m))
        assert max(all_cuts)==opt_formula(c,m)
        assert min(nash)==worst_formula(c,m)
        labeled+=1<<n
compressed=0
for c in range(1,71):
    for m in range(1,71):
        ps=list(predicted_profiles(c,m))
        total=sum(comb(c,k)*comb(m,l) for k,l in ps)
        assert total==predicted_total(c,m)
        worst=min(cut(c,m,k,l) for k,l in ps)
        best=max(cut(c,m,k,l) for k in range(c+1) for l in (0,m))
        assert worst==worst_formula(c,m) and best==opt_formula(c,m)
        compressed+=1
print('VERIFY_OK labeled_masks=%d compressed_pairs=%d' % (labeled,compressed))
