#!/usr/bin/env python3
"""Exhaustive independent checks for up-step relocation and one-symbol relocation on Dyck words."""
from collections import deque,defaultdict
from math import comb
import argparse

def dyck(n):
    out=[]
    def rec(s,up,down):
        if up==down==n:
            out.append(s);return
        if up<n:rec(s+'1',up+1,down)
        if down<up:rec(s+'0',up,down+1)
    rec('',0,0)
    assert len(out)==comb(2*n,n)//(n+1)
    return out

def gap(w):
    g=[0]*w.count('0');z=0
    for c in w:
        if c=='0':z+=1
        else:g[z]+=1
    return tuple(g)

def legal(w):
    s=0
    for c in w:
        s+=1 if c=='1' else -1
        if s<0:return False
    return s==0

def adjacency(words,up_only=False):
    lookup={w:i for i,w in enumerate(words)}
    adj=[set() for _ in words]
    for i,w in enumerate(words):
        for cut,c in enumerate(w):
            if up_only and c!='1':continue
            rem=w[:cut]+w[cut+1:]
            for ins in range(len(w)):
                nw=rem[:ins]+c+rem[ins:]
                if nw!=w and nw in lookup:
                    j=lookup[nw];adj[i].add(j)
        assert i not in adj[i]
    for i,a in enumerate(adj):
        assert all(i in adj[j] for j in a)
    return adj

def bfs(adj,src):
    d=[-1]*len(adj);d[src]=0;q=deque([src])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    assert -1 not in d
    return d

def main(max_n=7):
    for n in range(1,max_n+1):
        W=dyck(n);G=[gap(w) for w in W];A1=adjacency(W,True);A=adjacency(W)
        max_d=0;full_checks=0;one_checks=0
        for i in range(len(W)):
            d1=bfs(A1,i);d=bfs(A,i)
            for j in range(len(W)):
                prediction=n-sum(min(a,b) for a,b in zip(G[i],G[j]))
                assert d1[j]==prediction,(n,W[i],W[j],d1[j],prediction)
                assert d[j]<=n-1 or n==1,(n,W[i],W[j],d[j])
                one_checks+=1;full_checks+=1
                max_d=max(max_d,d[j])
        assert max_d==n-1 if n>1 else max_d==0
        print('n=%d words=%d 1-type_edges=%d all_edges=%d all_diameter=%d checked_pairs=%d' % (n,len(W),sum(map(len,A1))//2,sum(map(len,A))//2,max_d,full_checks),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-n',type=int,default=7)
    args=p.parse_args();main(args.max_n)
