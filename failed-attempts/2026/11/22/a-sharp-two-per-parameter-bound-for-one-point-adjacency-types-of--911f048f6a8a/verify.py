#!/usr/bin/env python3
"""Independent finite checks for the cograph neighbourhood-type theorem.

All tests operate on undirected simple graphs and do not rely on third-party modules.
"""
from itertools import combinations
from random import Random


def is_cograph(adj):
    n=len(adj)
    for vs in combinations(range(n),4):
        deg=[sum(bool(adj[v] & (1<<w)) for w in vs) for v in vs]
        if sorted(deg)==[1,1,2,2] and sum(deg)==6:
            return False
    return True


def trace(adj, A, external=False):
    # Return masks relative to increasing parameter order.
    q=list(A); covered=set(q)
    return {sum((1<<j) for j,a in enumerate(q) if adj[v]>>a & 1)
            for v in range(len(adj)) if not external or v not in covered}


def add_edge(adj,u,v):
    adj[u]|=1<<v;adj[v]|=1<<u


def make_witness(m):
    """m parameters, 2m outside vertices, all 2m outside patterns."""
    adj=[]
    def new():
        adj.append(0);return len(adj)-1
    def rec(a,b):
        if b-a==1:
            p=new();q=new();add_edge(adj,p,q)
            return [p,q],[p]
        mid=(a+b)//2
        left,A1=rec(a,mid);right,A2=rec(mid,b)
        apex=new()
        for u in left+right:add_edge(adj,apex,u)
        return left+right+[apex],A1+A2
    nodes,A=rec(0,m)
    isolated=new()
    assert len(adj)==3*m
    return adj,A


def exhaustive(max_n=6):
    tested=0;graphs=0
    for n in range(1,max_n+1):
        pairs=list(combinations(range(n),2))
        for bits in range(1<<len(pairs)):
            adj=[0]*n
            for j,(u,v) in enumerate(pairs):
                if bits>>j&1:add_edge(adj,u,v)
            if not is_cograph(adj):continue
            graphs+=1
            for mask in range(1,1<<n):
                A=[i for i in range(n) if mask>>i &1]
                T=trace(adj,A)
                full=(1<<len(A))-1
                assert len(T)+(0 not in T)+(full not in T)<=2*len(A),(n,bits,A,T)
                assert len(trace(adj,A,True))<=2*len(A)
                tested+=1
    return graphs,tested


def sample_cotrees(samples=500):
    random=Random(271828)
    checks=0
    for _ in range(samples):
        n=random.randrange(2,90)
        adj=[0]*n;blocks=[[v] for v in range(n)]
        while len(blocks)>1:
            i=random.randrange(len(blocks));left=blocks.pop(i)
            j=random.randrange(len(blocks));right=blocks.pop(j)
            if random.randrange(2):
                for v in left:
                    for w in right:add_edge(adj,v,w)
            blocks.append(left+right)
        for _ in range(10):
            size=random.randrange(1,n+1)
            A=sorted(random.sample(range(n),size))
            T=trace(adj,A)
            assert len(T)+(0 not in T)+((1<<len(A))-1 not in T)<=2*len(A)
            checks+=1
    return checks


def witness_checks():
    checks=0
    for m in range(1,13):
        adj,A=make_witness(m)
        T=trace(adj,A,True)
        assert len(T)==2*m,(m,T)
        assert len(adj)==3*m
        # A direct check of all induced 4-vertex subgraphs.
        assert is_cograph(adj),(m,adj)
        checks+=1
    return checks


if __name__=='__main__':
    g,e=exhaustive()
    w=witness_checks()
    r=sample_cotrees()
    print(f'VERIFY_OK exhaustive_cographs={g} exhaustive_parameter_cases={e} extremal_witnesses={w} randomized_cotree_cases={r}')
