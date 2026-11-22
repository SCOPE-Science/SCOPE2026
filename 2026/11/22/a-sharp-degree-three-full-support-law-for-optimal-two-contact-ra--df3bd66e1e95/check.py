"""Exact checks of the two-contact graph-averaging support theorem.

Uses only Python's standard library. Run: python check.py
The universal theorem is established by the proof, not by these finite tests.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(A, b):
    n = len(A)
    tab = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(A)]
    for k in range(n):
        pivot = next((r for r in range(k, n) if tab[r][k]), None)
        assert pivot is not None
        tab[k], tab[pivot] = tab[pivot], tab[k]
        t = tab[k][k]
        tab[k] = [x / t for x in tab[k]]
        for i in range(n):
            if i != k:
                c = tab[i][k]
                if c:
                    tab[i] = [x-c*y for x,y in zip(tab[i],tab[k])]
    return [row[-1] for row in tab]


def connected(n, edges):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for a,b in edges:
            v=b if a==u else a if b==u else None
            if v is not None and v not in seen:
                seen.add(v);stack.append(v)
    return len(seen)==n


def evaluate(n, edges):
    m=len(edges)
    deg=[0]*n
    for u,v in edges: deg[u]+=1;deg[v]+=1
    Q=[[0]*n for _ in range(n)]
    for i in range(n):Q[i][i]=2+deg[i]
    for u,v in edges:Q[u][v]+=1;Q[v][u]+=1
    w=solve(Q,[1]*n)
    sums=[w[u]+w[v] for u,v in edges]
    if min(sums)<=0: return (w,None,None)
    p=[s/sum(sums) for s in sums]
    A=[[F(1) if i==j else F(1,4) if len(set(edges[i]) & set(edges[j]))==1 else F(0) for j in range(m)] for i in range(m)]
    Ap=[sum(A[i][j]*p[j] for j in range(m)) for i in range(m)]
    return w,p,Ap


def double_star(m):
    # hub vertices 0,1; each has m private leaves
    return [(0,2+i) for i in range(m)]+[(1,2+m+i) for i in range(m)]+[(0,1)]


def main():
    checked=0
    for n in range(2,6):
        pool=list(combinations(range(n),2))
        for mask in range(1,1<<len(pool)):
            edges=[e for i,e in enumerate(pool) if mask>>i&1]
            degrees=[sum(v in e for e in edges) for v in range(n)]
            if max(degrees)>3 or not connected(n,edges):continue
            w,p,Ap=evaluate(n,edges)
            assert all(0<=v<=F(1,3) for v in w)
            assert all(w[a]+w[b]>=F(1,9) for a,b in edges)
            assert all(x>=F(1,6*len(edges)) for x in p)
            assert sum(p)==1 and all(x>0 for x in p)
            assert len(set(Ap))==1
            checked+=1
    # Nontrivial subcubic graphs beyond the exhaustive small cases
    extra=[(8,[(i,(i+1)%4) for i in range(4)]+[(i+4,(i+1)%4+4) for i in range(4)]+[(i,i+4) for i in range(4)]),
           (6,[(i,j) for i in range(3) for j in range(3,6)]),
           (10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,(i+2)%5+5) for i in range(5)])]
    for n,edges in extra:
        w,p,Ap=evaluate(n,edges)
        assert all(F(0)<=v<=F(1,3) for v in w)
        assert all(p[i]>=F(1,6*len(edges)) for i in range(len(edges)))
        assert len(set(Ap))==1
        checked+=1
    # Double-stars (m=3 is the sharp first loss of support).
    for m in range(1,9):
        edges=double_star(m)
        a=F(3,5*m+3) if m<=2 else F(1,2*m)
        b=F(3-m,5*m+3) if m<=2 else F(0)
        probs=[a]*(2*m)+[b]
        assert sum(probs)==1 and min(probs)>=0
        M=len(edges)
        A=[[F(1) if i==j else F(1,4) if set(edges[i])&set(edges[j]) else F(0) for j in range(M)] for i in range(M)]
        Ap=[sum(A[i][j]*probs[j] for j in range(M)) for i in range(M)]
        lam=Ap[0]
        assert all(v==lam for v in Ap[:2*m])
        assert Ap[-1]>=lam and (Ap[-1]==lam if m<=3 else Ap[-1]>lam)
        if m>=3:assert b==0
        checked+=1
    # Previously derived four-vertex path benchmark.
    n=4;edges=[(0,1),(1,2),(2,3)]
    w,p,Ap=evaluate(n,edges)
    assert p==[F(3,8),F(1,4),F(3,8)]
    print('PASS:',checked,'exact graph cases, including all labeled connected subcubic graphs with 2--5 vertices')
    print('PASS: sharp degree-four support-loss example and exact KKT tests for eight double stars')
    print('PASS: normalized resolvent weights, global positive lower bounds, and stationarity')

if __name__=='__main__':main()
