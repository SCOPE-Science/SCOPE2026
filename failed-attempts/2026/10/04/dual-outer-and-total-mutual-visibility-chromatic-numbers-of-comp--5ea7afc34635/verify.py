#!/usr/bin/env python3
from itertools import combinations
from collections import deque

def parts(n,lo=1):
    if n==0:
        yield (); return
    for a in range(lo,n+1):
        for q in parts(n-a,a): yield (a,)+q

def graph(p):
    side=[]
    for i,s in enumerate(p): side += [i]*s
    n=len(side); a=[[False]*n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            a[u][v]=u!=v and side[u]!=side[v]
    return a

def visible(a,M,x,y):
    n=len(a)
    def d(block):
        q=deque([(x,0)]); seen={x}
        while q:
            v,z=q.popleft()
            if v==y:return z
            for w in range(n):
                if not a[v][w] or w in seen:continue
                if w not in (x,y) and w in block:continue
                seen.add(w); q.append((w,z+1))
        return None
    return d(set())==d(M)

def valid(a,mask,kind):
    n=len(a); M={i for i in range(n) if mask>>i&1}; C=set(range(n))-M
    if not M:return False
    if kind=='dual': pairs=list(combinations(M,2))+list(combinations(C,2))
    elif kind=='outer': pairs=list(combinations(M,2))+[(x,y) for x in M for y in C]
    else: pairs=list(combinations(range(n),2))
    return all(visible(a,M,x,y) for x,y in pairs)

def chi(a,kind):
    n=len(a); full=(1<<n)-1; ok=[False]*(1<<n)
    for m in range(1,1<<n):ok[m]=valid(a,m,kind)
    inf=n+1; dp=[inf]*(1<<n); dp[0]=0
    for m in range(1,1<<n):
        first=m&-m; s=m
        while s:
            if s&first and ok[s]:dp[m]=min(dp[m],dp[m^s]+1)
            s=(s-1)&m
    return None if dp[full]==inf else dp[full]

def formula(p,kind):
    if all(s==1 for s in p):return 1
    if kind=='outer':return 2
    if kind=='dual' and len(p)==2 and min(p)==1 and max(p)>=3:return None
    if kind=='total' and len(p)==2 and min(p)==1:return None
    return 2

def main():
    nt=nc=0
    for n in range(2,10):
        for p in parts(n):
            if len(p)<2:continue
            a=graph(p); nt+=1
            for kind in ('dual','outer','total'):
                got=chi(a,kind); want=formula(p,kind)
                if got!=want:raise AssertionError((p,kind,got,want))
                nc+=1
    print(f'ALL CHECKS PASSED; multipartite_types={nt}; invariant_cases={nc}; max_order=9')
if __name__=='__main__':main()
