#!/usr/bin/env python3
"""Finite-state exact-rational tests for a partisan voter conservation theorem."""
from fractions import Fraction as F
from itertools import product

def edge_list(n, edges):
    assert n >= 2
    adj=[set() for _ in range(n)]
    for i,j in edges:
        assert 0<=i<n and 0<=j<n and i!=j
        adj[i].add(j);adj[j].add(i)
    assert all(adj)
    seen={0};stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    assert len(seen)==n
    return [sorted(x) for x in adj]

def transitions(adj, pref, eps, mask):
    n=len(adj); trans={}
    for i in range(n):
        bit=(mask>>i)&1
        for j in adj[i]:
            if bit==((mask>>j)&1):continue
            prob=(1 - eps*(2*bit-1)*pref[i])/2
            assert prob>0
            trans[mask^(1<<i)]=trans.get(mask^(1<<i),F(0))+prob/len(adj[i])
    return trans

def drift(adj,pref,eps,mask):
    d=[len(v) for v in adj];den=sum(d)
    m0=sum(d[i] for i in range(len(d)) if (mask>>i)&1)/F(den)
    actual=sum(rate*(sum(d[i] for i in range(len(d)) if (nxt>>i)&1)/F(den)-m0) for nxt,rate in transitions(adj,pref,eps,mask).items())
    edges=[(i,j) for i in range(len(d)) for j in adj[i] if i<j]
    predicted=eps/F(2*len(edges))*sum(F(pref[i]+pref[j],2) for i,j in edges if ((mask>>i)^(mask>>j))&1)
    # Equivalent eps/(4|E|) * sum (pref_i+pref_j) on discordant edges.
    assert actual==predicted,(actual,predicted,adj,pref,mask)
    return actual

def solve_linear(a,b):
    n=len(b); a=[list(row)+[x] for row,x in zip(a,b)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if a[i][k])
        a[k],a[pivot]=a[pivot],a[k]
        q=a[k][k]
        for j in range(k,n+1):a[k][j]/=q
        for i in range(n):
            if i==k:continue
            q=a[i][k]
            if q:
                for j in range(k,n+1):a[i][j]-=q*a[k][j]
    return [r[n] for r in a]

def fixation(adj,pref,eps):
    n=len(adj); full=(1<<n)-1
    states=list(range(1,full));idx={s:i for i,s in enumerate(states)}
    a=[[F(0) for _ in states] for _ in states]; b=[F(0) for _ in states]
    for s in states:
        r=idx[s]; tr=transitions(adj,pref,eps,s)
        a[r][r]=sum(tr.values())
        for t,v in tr.items():
            if t==full:b[r]+=v
            elif t!=0:a[r][idx[t]]-=v
    h=solve_linear(a,b)
    return {0:F(0),full:F(1),**dict(zip(states,h))}

def main():
    cases=[(2,[(0,1)]), (3,[(0,1),(1,2)]),
           (4,[(0,1),(1,2),(2,3)]),
           (4,[(0,1),(1,2),(2,3),(3,0)]),
           (5,[(0,1),(0,2),(0,3),(0,4)]),
           (3,[(0,1),(1,2),(2,0)])]
    algebra_cases=0;martingale_cases=0;fixation_cases=0;negative_cases=0
    for n,edges in cases:
        adj=edge_list(n,edges);deg=[len(s) for s in adj]
        for pref in product((-1,1),repeat=n):
            proper=all(pref[i]==-pref[j] for i,j in edges)
            for eps in (F(1,4),F(2,3)):
                values=[drift(adj,pref,eps,m) for m in range(1<<n)]
                algebra_cases+=1<<n
                assert (all(z==0 for z in values))==proper
                martingale_cases+=1
            if proper:
                for eps in (F(1,4),F(2,3)):
                    h=fixation(adj,pref,eps)
                    assert all(h[s]==sum(deg[i] for i in range(n) if (s>>i)&1)/F(sum(deg)) for s in h)
                    fixation_cases+=1
            else:negative_cases+=1
    # Exact contrast: 3-clique, all agents prefer +, initial one +, eps=1/2.
    adj=edge_list(3,[(0,1),(1,2),(2,0)])
    h=fixation(adj,(1,1,1),F(1,2))
    assert h[1]==F(9,13),h[1]
    # Source-preference initial state on star: half the degree mass lies at the hub.
    adj=edge_list(5,[(0,j) for j in (1,2,3,4)])
    h=fixation(adj,(1,-1,-1,-1,-1),F(2,3))
    assert h[1]==F(1,2)
    print('PASS exact directed-generator drift identities:',algebra_cases)
    print('PASS all-zero drift iff proper preference coloring:',martingale_cases,'graph/preference/bias pairs')
    print('PASS exact absorbing-chain fixation against degree-weighted law:',fixation_cases,'cases')
    print('PASS non-proper assignments considered:',negative_cases)
    print('PASS positive-bias 3-clique countercontrast: probability 9/13 versus neutral 1/3')
    print('PASS anti-preference 5-vertex star hub-only positive initial state: 1/2')

if __name__=='__main__': main()
