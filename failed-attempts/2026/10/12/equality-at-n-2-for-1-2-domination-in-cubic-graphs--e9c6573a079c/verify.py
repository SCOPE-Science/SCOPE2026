#!/usr/bin/env python3
import itertools

def all_graphs(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1<<len(edges)):
        deg=[0]*n
        adj=[set() for _ in range(n)]
        ok=True
        for b,(u,v) in enumerate(edges):
            if mask>>b & 1:
                deg[u]+=1; deg[v]+=1
                if deg[u]>3 or deg[v]>3:
                    ok=False; break
                adj[u].add(v); adj[v].add(u)
        if ok and all(d==3 for d in deg):
            seen={0}; stack=[0]
            while stack:
                u=stack.pop()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v); stack.append(v)
            if len(seen)==n:
                yield adj

def is_12_dom(adj,D):
    D=set(D)
    for v,N in enumerate(adj):
        inside=sum(u in D for u in N)
        if v in D:
            if inside<2: return False
        else:
            if inside<1: return False
    return True

def is_pm_cut(adj,A):
    A=set(A); n=len(adj)
    if not A or len(A)==n: return False
    for v,N in enumerate(adj):
        cross=sum((u in A)!=(v in A) for u in N)
        if cross!=1: return False
    return True

def gamma12(adj):
    n=len(adj)
    for k in range(n+1):
        sols=[]
        for D in itertools.combinations(range(n),k):
            if is_12_dom(adj,D): sols.append(D)
        if sols: return k,sols
    raise AssertionError

def main():
    graphs=0; equality_graphs=0; equality_sets=0; pmcut_graphs=0
    for n in (4,6):
        for adj in all_graphs(n):
            graphs+=1
            g,mins=gamma12(adj)
            has_pm=any(is_pm_cut(adj,A) for k in range(1,n) for A in itertools.combinations(range(n),k))
            if has_pm: pmcut_graphs+=1
            assert (g*2==n)==has_pm
            if g*2==n:
                equality_graphs+=1
                for D in mins:
                    equality_sets+=1
                    assert is_pm_cut(adj,D)
                    R=set(range(n))-set(D)
                    assert all(sum(u in D for u in adj[v])==2 for v in D)
                    assert all(sum(u in R for u in adj[v])==2 for v in R)
    print(f"ALL CHECKS PASSED; connected_labeled_cubic_graphs={graphs}; equality_graphs={equality_graphs}; perfect_matching_cut_graphs={pmcut_graphs}; half_order_minimum_sets={equality_sets}; orders=4,6")
if __name__=='__main__': main()
