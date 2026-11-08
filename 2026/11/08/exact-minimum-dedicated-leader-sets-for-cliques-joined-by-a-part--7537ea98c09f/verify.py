#!/usr/bin/env python3
"""Exact-matrix replay for matched-clique dedicated control.

Requires Python 3 and sympy. No network access or external data.
"""
import itertools
import sympy as sp

def graph_laplacian(m, k):
    n=2*m
    L=sp.zeros(n)
    for side in (0,m):
        for i in range(m):
            for j in range(i):
                a,b=side+i,side+j
                L[a,a]+=1; L[b,b]+=1
                L[a,b]-=1; L[b,a]-=1
    for i in range(k):
        a,b=i,m+i
        L[a,a]+=1;L[b,b]+=1
        L[a,b]-=1;L[b,a]-=1
    return L

def predicted(m,k,S):
    S=set(S)
    if k<m:
        if len(S)!=2*m-k-2: return False
        classes=[({i,m+i},"M") for i in range(k)]
        classes += [({i},"U") for i in range(k,m)]
        classes += [({m+i},"V") for i in range(k,m)]
        loads=[len(S & vertices) for vertices,_ in classes]
        omitted=[classes[i][1] for i,j in enumerate(loads) if j==0]
        return max(loads)<=1 and len(omitted)==2 and omitted[0]!=omitted[1]
    if len(S)!=m-1:return False
    return sum((int(i in S)+int(m+i in S))==1 for i in range(m))==m-1

def controllable_from_eigenspaces(eigenspaces,S):
    for value,basis in eigenspaces:
        B=sp.Matrix([[vec[u] for vec in basis] for u in S])
        if B.rank()!=len(basis):
            return False
    return True


def zero_forcing(L, S):
    n=L.rows
    neighbors=[{j for j in range(n) if i!=j and L[i,j]==-1} for i in range(n)]
    active=set(S)
    while True:
        newly=set()
        for i in active:
            remaining=neighbors[i]-active
            if len(remaining)==1:
                newly.update(remaining)
        if not newly:
            return len(active)==n
        active.update(newly)

def run():
    cases=0
    observed=0
    for m in (3,4,5):
        for k in range(2,m+1):
            L=graph_laplacian(m,k)
            d=2*m-k-2 if k<m else m-1
            es=[(z,basis) for z,mult,basis in L.eigenvects()]
            assert sum(len(basis) for _,basis in es)==2*m
            count=0
            for S in itertools.combinations(range(2*m),d):
                got=controllable_from_eigenspaces(es,S)
                want=predicted(m,k,S)
                assert got==want, (m,k,S,got,want)
                count+=int(got)
                cases+=1
            target=(2**k*m*(m-k)) if k<m else m*2**(m-1)
            assert count==target, (m,k,count,target)
            observed+=count
            print(f"m={m}, k={k}: exact minimum-size subsets, controllable={count}, expected={target}")
    # Explicit independent Kalman rank test, without eigenspace reuse,
    # for a nontrivial nonsymmetric leader pattern.
    m,k=4,2
    L=graph_laplacian(m,k)
    S=[0,1,2,6]
    assert predicted(m,k,S)
    B=sp.zeros(2*m,len(S))
    for col,row in enumerate(S):B[row,col]=1
    blocks=[B]
    for j in range(1,2*m):
        blocks.append(L*blocks[-1])
    assert sp.Matrix.hstack(*blocks).rank()==2*m
    # Distinguish fixed-Laplacian controllability from zero forcing.
    L6=graph_laplacian(3,2)
    leaders=[S for S in itertools.combinations(range(6),2) if predicted(3,2,S)]
    assert len(leaders)==12
    assert sum(zero_forcing(L6,S) for S in leaders)==4
    # boundary exception excluded from the theorem:
    L4=graph_laplacian(2,2)
    assert sorted([len(b) for _,_,b in L4.eigenvects()])==[1,1,2]
    print(f"PASS: {cases} exact eigenspace/subset comparisons; {observed} optimal sets; one full Kalman rank replay; zero-forcing separation 4/12; C4 resonance boundary.")

if __name__=="__main__":
    run()
