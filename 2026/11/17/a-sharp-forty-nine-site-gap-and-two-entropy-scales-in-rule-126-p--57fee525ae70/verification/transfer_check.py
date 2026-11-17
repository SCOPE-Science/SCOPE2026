#!/usr/bin/env python3
"""Exact finite-state certificates for periodic Rule 126; standard library only."""
from collections import Counter


def build(height):
    q = 1 << height
    adjacency = {a*q+b: [] for a in range(q) for b in range(q)}
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if all((126 >> (4*((a>>i)&1) + 2*((b>>i)&1) + ((c>>i)&1))) & 1
                       == ((b>>((i+1)%height)) & 1) for i in range(height)):
                    adjacency[a*q+b].append(b*q+c)
    return adjacency


def tarjan(adj):
    index=0; indices={};low={};stack=[]; on=set(); comps=[]
    def visit(v):
        nonlocal index
        indices[v]=low[v]=index; index+=1;stack.append(v);on.add(v)
        for w in adj[v]:
            if w not in indices:
                visit(w);low[v]=min(low[v],low[w])
            elif w in on:
                low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v:break
            comps.append(sorted(comp))
    for v in adj:
        if v not in indices:visit(v)
    return comps


def simple_cycles(adj,component):
    allowed=set(component); cycles=[]
    for base in component:
        def walk(v,path,seen):
            for w in adj[v]:
                if w==base:
                    cycles.append(tuple(path))
                elif w>base and w in allowed and w not in seen:
                    walk(w,path+[w],seen|{w})
        walk(base,[base],{base})
    return cycles


def components(height):
    adj=build(height)
    out=[]
    for comp in tarjan(adj):
        if len(comp)>1 or comp[0] in adj[comp[0]]:
            cyc=simple_cycles(adj,comp)
            out.append((comp,cyc))
    return sorted(out,key=lambda c:(-len(c[0]),c[0][0]))


def trace_renewal(lengths,maximum):
    # With all simple cycles incident to one vertex, closed-word generating
    # function is -z P'(z)/P(z), P=1-sum_{cycles} z^{length}.
    f=[0]*(maximum+1);trace=[0]*(maximum+1);f[0]=1
    for n in range(1,maximum+1):
        f[n]=sum(m*f[n-k] for k,m in lengths.items() if n>=k)
        trace[n]=sum(k*m*f[n-k] for k,m in lengths.items() if n>=k)
    return trace


def walk_trace(adj,n):
    # Independent path-count implementation, used for short lengths.
    total=0
    for v in adj:
        cur={v:1}
        for _ in range(n):
            nxt={}
            for u,wgt in cur.items():
                for w in adj[u]:nxt[w]=nxt.get(w,0)+wgt
            cur=nxt
        total+=cur.get(v,0)
    return total


def run():
    expected={1:[(1,Counter({1:1}))],
              2:[(6,Counter({4:1,5:2,6:1})),(1,Counter({1:1}))],
              3:[(1,Counter({1:1}))],
              4:[(12,Counter({10:1,11:2,12:1})),
                 (12,Counter({10:1,11:2,12:1})),
                 (6,Counter({4:1,5:2,6:1})),
                 (1,Counter({1:1}))]}
    for h in (1,2,3,4):
        sccs=components(h)
        stats=[]
        for comp,cycles in sccs:
            freq=Counter(map(len,cycles))
            common=set.intersection(*(set(c) for c in cycles))
            assert common, (h,comp)
            stats.append((len(comp),freq))
        assert stats==expected[h],(h,stats)
        print(f'height {h}: recurrent SCCs '+str([(n,dict(c)) for n,c in stats]))
    maximum=125
    t2=trace_renewal({4:1,5:2,6:1},maximum)
    t4=trace_renewal({10:1,11:2,12:1},maximum)
    for n in range(1,maximum+1):
        assert t2[n]%2==0 and t4[n]%2==0,(n,t2[n],t4[n])
        if n>=3:
            assert (t4[n]>0)==(n>=50 or any(10*k<=n<=12*k for k in range(1,5)))
    for h,arr in ((2,t2),(4,t4)):
        adj=build(h)
        for n in range(3,13):
            target=(1+t2[n]) if h==2 else (1+t2[n]+2*t4[n])
            got=walk_trace(adj,n)
            assert target==got,(h,n,target,got)
        print(f'height {h}: independent transfer traces agree through n=12')
    print('least four-cycle circumference 10; largest excluded circumference 49; every n>=50 has cycles')
    print('circumference,primitive-two-orbits,primitive-four-orbits')
    for n in list(range(3,21))+[24,30,40,49,50,51,60]:
        print(n,t2[n]//2,t4[n]//2,sep=',')
    print('PASS')

if __name__=='__main__':run()
