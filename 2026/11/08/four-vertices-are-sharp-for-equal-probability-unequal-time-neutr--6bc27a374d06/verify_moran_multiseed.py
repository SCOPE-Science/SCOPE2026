#!/usr/bin/env python3
"""Exact neutral birth-death fixation-probability/time classification through four sites.
Standard-library only. Execute: python3 verify_moran_multiseed.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial

def graphs(n):
    pairs=list(combinations(range(n),2))
    for code in range(1<<len(pairs)):
        edges=[pairs[i] for i in range(len(pairs)) if code>>i&1]
        adj=[set() for _ in range(n)]
        for u,v in edges:adj[u].add(v);adj[v].add(u)
        reached={0};todo=[0]
        while todo:
            for j in adj[todo.pop()]:
                if j not in reached:reached.add(j);todo.append(j)
        if len(reached)==n:yield edges,adj

def canon(n,edges):
    e=set(tuple(sorted(x)) for x in edges)
    return min(tuple(sorted(tuple(sorted((p[u],p[v]))) for u,v in e)) for p in permutations(range(n)))

def solve(a,b):
    n=len(b);A=[list(a[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=next(i for i in range(k,n) if A[i][k]);A[k],A[j]=A[j],A[k]
        den=A[k][k];A[k]=[z/den for z in A[k]]
        for i in range(n):
            if i==k:continue
            c=A[i][k]
            if c:
                for v in range(k,n+1): A[i][v]-=c*A[k][v]
    return [A[i][n] for i in range(n)]

def markov(adj):
    n=len(adj); full=(1<<n)-1;states=list(range(1,full));ind={m:i for i,m in enumerate(states)}
    degree=[len(s) for s in adj]
    z=sum((F(1,d) for d in degree),F())
    prob={m:sum((F(1,degree[i]) for i in range(n) if m>>i&1),F())/z for m in states}
    M=[[F(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    # M=I-Q, with all no-change probability in Q. Construct directly from total change rate.
    M=[[F() for j in states] for i in states]
    for m in states:
        i=ind[m]
        for u in range(n):
            for v in adj[u]:
                if bool(m>>u&1)==bool(m>>v&1):continue
                rate=F(1,n*degree[u]);m2=(m|(1<<v)) if m>>u&1 else (m&~(1<<v))
                M[i][i]+=rate
                if m2 not in (0,full):M[i][ind[m2]]-=rate
    # Assert formula for fixation probability is harmonic, including absorption.
    for m in states:
        left=sum((M[ind[m]][j]*prob[mm] for j,mm in enumerate(states)),F())
        right=sum((F(1,n*degree[u]) for u in range(n) for v in adj[u] if (m>>u&1) and not(m>>v&1) and m|(1<<v)==full),F())
        assert left==right,(m,left,right)
    moment=solve(M,[prob[m] for m in states]);return prob,{m:moment[ind[m]]/prob[m] for m in states},M,states

def verify_independent_doob(adj,prob,tau,M,states):
    # Independent derivation: conditional hitting time solves Doob-transform equation.
    m=len(states);B=[[M[i][j]*prob[states[j]]/prob[states[i]] for j in range(m)] for i in range(m)]
    u=solve(B,[F(1) for _ in states]);assert all(u[i]==tau[states[i]] for i in range(m))

if __name__=='__main__':
    reps={};labeled={};for_all=0
    for n in (2,3,4):
        saw={};discrepant=[];total=0
        for edges,adj in graphs(n):
            total+=1;prob,tau,M,states=markov(adj);key=canon(n,edges)
            grouped={}
            for m in states: grouped.setdefault((m.bit_count(),prob[m]),[]).append(m)
            diffs=[]
            for (k,p),masks in grouped.items():
                vals={tau[m] for m in masks}
                if len(vals)>1:diffs.append((k,p,masks,sorted(vals)))
            if diffs:discrepant.append((edges,diffs))
            saw.setdefault(key,(edges,diffs,adj,prob,tau,M,states))
        print('n',n,'connected labeled',total,'isomorphism classes',len(saw),'labeled divergent',len(discrepant))
        print('distinct divergent classes',[(v[0],[(x[0],str(x[1]),[str(w) for w in x[3]]) for x in v[1]]) for v in saw.values() if v[1]])
        if n<4:assert not discrepant
        else:
            assert total==38 and len(saw)==6
            assert len([v for v in saw.values() if v[1]])==2
            assert len(discrepant)==15
            for v in saw.values():
                if not v[1]:continue
                verify_independent_doob(v[2],v[3],v[4],v[5],v[6])
        for k,v in saw.items(): reps[(n,k)]=v
    # Independently check the two named networks in the exact labeled coordinates.
    for tag,n,edges,a,b,p_expect,t_expect_a,t_expect_b in [
        ('cycle',4,[(0,1),(1,2),(2,3),(3,0)],0b0011,0b0101,F(1,2),F(8),F(7)),
        ('path',4,[(0,1),(1,2),(2,3)],0b0011,0b0101,F(1,2),F(20),F(15))]:
        adj=[set() for _ in range(n)]
        for u,v in edges:adj[u].add(v);adj[v].add(u)
        p,t,M,states=markov(adj);verify_independent_doob(adj,p,t,M,states)
        assert p[a]==p[b]==p_expect and t[a]==t_expect_a and t[b]==t_expect_b
        print(tag,'sets',a,b,'fixation',p[a],'conditional_time',t[a],t[b],'difference',t[a]-t[b])
    print('PASS: exact exhaustive graph census, reproductive martingale, two rational moment equations and both witnesses')
