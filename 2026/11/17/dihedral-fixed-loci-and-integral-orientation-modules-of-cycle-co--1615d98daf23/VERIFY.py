#!/usr/bin/env python3
"""Exact finite test of dihedral chamber actions and fixed-locus Euler values.
Only finite testing; the all-n theorem uses a separate relative-homology proof.
"""
from math import gcd
from collections import Counter


def sign_perm(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def vertex_map(n,k,reflect):
    if reflect:
        return tuple((k-i)%n for i in range(n))
    return tuple((k+i)%n for i in range(n))


def action_bits(n,bits,k,reflect):
    new=0
    for i in range(n):
        if not reflect:
            j=(i+k)%n
            v=(bits>>i)&1
        else:
            j=(k-i-1)%n
            v=1-((bits>>i)&1)
        new |= v<<j
    return new


def formula_count(n,k,reflect):
    if not reflect:
        return 2**gcd(n,k)-2
    if n%2 or k%2:
        return 0
    return 2**(n//2)


def formula_trace(n,k,reflect):
    if not reflect:
        d=gcd(n,k)
        return (-1)**(n-d)*(2**d-3)
    if n%2:
        return (-1)**((n+1)//2)
    if k%2:
        return (-1)**(n//2+1)
    return (-1)**((n-2)//2)*(2**(n//2)-1)


def vertex_orbits(p):
    n=len(p)
    seen=set(); out=[]
    for i in range(n):
        if i not in seen:
            orb=[]; j=i
            while j not in seen:
                seen.add(j);orb.append(j);j=p[j]
            out.append(orb)
    return out


def acyclic_orientation_count(m,edge_set):
    edges=sorted(edge_set)
    out=0
    for mask in range(1<<len(edges)):
        adj=[[] for _ in range(m)]
        for j,(a,b) in enumerate(edges):
            if mask>>j&1: a,b=b,a
            adj[a].append(b)
        state=[0]*m
        def dfs(u):
            state[u]=1
            for v in adj[u]:
                if state[v]==1 or (state[v]==0 and not dfs(v)):
                    return False
            state[u]=2
            return True
        if all(state[v] or dfs(v) for v in range(m)):out+=1
    return out


def fixed_euler(n,p):
    orbits=vertex_orbits(p); m=len(orbits)
    if m==1:return 0
    label={v:i for i,o in enumerate(orbits) for v in o}
    es=set(); has_loop=False
    for v in range(n):
        a,b=label[v],label[(v+1)%n]
        if a==b:has_loop=True
        else:es.add(tuple(sorted((a,b))))
    if has_loop: return 1+(-1)**(m-2)
    a=acyclic_orientation_count(m,es)
    return 1+(-1)**(m-3)*(a-1)


def run():
    total=0
    for n in range(3,13):
        distribution=Counter()
        invariant_numer=0
        for reflect in (False,True):
            for k in range(n):
                p=vertex_map(n,k,reflect)
                s=sign_perm(p)
                got=sum(1 for b in range(1,2**n-1) if action_bits(n,b,k,reflect)==b)
                want=formula_count(n,k,reflect)
                assert got==want,(n,k,reflect,got,want)
                tr=s*(got-1)
                target=formula_trace(n,k,reflect)
                assert tr==target,(n,k,reflect,tr,target)
                euler=fixed_euler(n,p)
                trace_euler=1+(-1)**(n-3)*tr
                assert euler==trace_euler,(n,k,reflect,euler,trace_euler)
                invariant_numer+=tr
                distribution[tr]+=1
                total+=1
        assert invariant_numer % (2*n)==0,(n,invariant_numer)
        inv=invariant_numer//(2*n)
        assert inv>=0,(n,inv)
        print('n=%d: top_rank=%d, full_D_invariant_rank=%d, classes=%s'%(n,2**n-3,inv,dict(sorted(distribution.items()))))
    print('CYCLE_COLORING_DIHEDRAL_EXACT_CHECK_PASS elements=%d'%total)
if __name__=='__main__':run()
