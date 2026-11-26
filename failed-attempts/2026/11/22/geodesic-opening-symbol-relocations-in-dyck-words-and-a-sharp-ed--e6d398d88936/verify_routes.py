#!/usr/bin/env python3
"""Construct monotone shortest Dyck routes using only relocations of an opening symbol."""
import argparse

def dyck(n):
    out=[]
    def rec(s,u,d):
        if d==n:out.append(s);return
        if u<n:rec(s+'1',u+1,d)
        if d<u:rec(s+'0',u,d+1)
    rec('',0,0);return out

def gap(w):
    g=[0]*w.count('0'); j=0
    for c in w:
        if c=='0':j+=1
        else:g[j]+=1
    return g

def word(g):return ''.join('1'*q+'0' for q in g)

def legal(g):return all(sum(g[:j])>=j for j in range(1,len(g)+1))

def route(a,b):
    g=gap(a);h=gap(b);supply={i:g[i]-h[i] for i in range(len(g)) if g[i]>h[i]};need={i:h[i]-g[i] for i in range(len(g)) if h[i]>g[i]};plan=[]
    for i in supply:
        for j in list(need):
            k=min(supply[i],need[j]);
            if k:plan.extend([(i,j)]*k);supply[i]-=k;need[j]-=k
            if need[j]==0:del need[j]
            if supply[i]==0:break
    assert not need and all(v==0 for v in supply.values())
    plan=sorted(plan,key=lambda p:p[0]<p[1])  # leftward transfers before rightward
    history=[a]
    for i,j in plan:
        assert g[i]>0
        g[i]-=1;g[j]+=1
        assert legal(g),(a,b,i,j,g)
        history.append(word(g))
    assert history[-1]==b
    assert len(plan)==len(gap(a))-sum(min(x,y) for x,y in zip(gap(a),gap(b)))
    return history

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--max-n',type=int,default=7)
 args=parser.parse_args()
 for n in range(1,args.max_n+1):
    W=dyck(n)
    for a in W:
        for b in W:
            H=route(a,b)
            for u,v in zip(H,H[1:]):
                assert u!=v and len(u)==len(v)
    print(f'n={n} states={len(W)} ordered_pairs={len(W)**2} all constructive routes valid',flush=True)
