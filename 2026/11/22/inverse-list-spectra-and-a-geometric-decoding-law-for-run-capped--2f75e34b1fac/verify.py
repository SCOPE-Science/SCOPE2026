#!/usr/bin/env python3
"""Exhaustive independent check of one-deletion run-capped inverse lists."""
from itertools import product
from collections import Counter

def runs(word):
    ans=[]
    for c in word:
        if ans and ans[-1][0]==c: ans[-1]=(c,ans[-1][1]+1)
        else: ans.append((c,1))
    return [r for _,r in ans]

def direct(y,h):
    parents=set()
    for i in range(len(y)+1):
        for bit in '01':
            w=y[:i]+bit+y[i:]
            if max(runs(w))<=h:parents.add(w)
    return len(parents)

def formula(y,h):
    rr=runs(y)
    bad=[r for r in rr if r>h]
    if not bad:return len(y)+2-rr.count(h)
    if len(bad)>1 or bad[0]>2*h:return 0
    return 2*h-bad[0]+1

def gf_poly(m,h):
    """Compute t^j coefficient by independent run compositions."""
    admiss=Counter()
    def visit(length,penalty):
        if length:admiss[length+2-penalty]+=2
        for a in range(1,h+1):
            if length+a<=m:visit(length+a,penalty+(a==h))
    # Count only exactly m words in run compositions, independently of input enumeration.
    admiss=Counter()
    def comp(left,penalty):
        if left==0:
            admiss[m+2-penalty]+=2
            return
        for a in range(1,min(h,left)+1):comp(left-a,penalty+(a==h))
    comp(m,0)
    long=Counter()
    for s in range(h+1,2*h+1):
        if s>m:break
        # g_h[k] = number of ordered compositions of k into 1..h
        g=[0]*(m-s+1);g[0]=1
        for v in range(1,m-s+1):g[v]=sum(g[v-a] for a in range(1,min(h,v)+1))
        long[2*h-s+1]+=2*sum(g[a]*g[m-s-a] for a in range(m-s+1))
    admiss.update(long)
    return admiss

cases=0;parents_seen=0
for h in range(1,6):
    for m in range(1,12):
        histogram=Counter()
        for bits in product('01',repeat=m):
            y=''.join(bits)
            actual=direct(y,h); expected=formula(y,h)
            assert actual==expected,(h,m,y,actual,expected)
            histogram[actual]+=1
            cases+=1; parents_seen+=actual
        poly=gf_poly(m,h)
        assert {j:v for j,v in histogram.items() if j>0} == dict(poly),(h,m,histogram,poly)
        assert histogram[0]+sum(poly.values())==2**m
        # Singleton series 2*z^(2h)/(1-sum(z^a for a=1..h))^2.
        if m>=2*h:
            b=m-2*h;g=[0]*(b+1);g[0]=1
            for i in range(1,b+1):g[i]=sum(g[i-a] for a in range(1,min(h,i)+1))
            u=2*sum(g[i]*g[b-i] for i in range(b+1))
        else:u=0
        assert histogram[1]==u,(h,m,histogram[1],u)
print('VERIFY_OK words=',cases,' compatible_parent_incidences=',parents_seen,' h=1..5, m=1..11')
