#!/usr/bin/env python3
"""Independent exact-rational test of pair-leader inverse traces on crown graphs."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def crown_laplacian(m):
    n=2*m
    L=[[0]*n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            if i != j:
                u=i;v=m+j
                L[u][u]+=1;L[v][v]+=1
                L[u][v]-=1;L[v][u]-=1
    return L

def inverse_trace(A):
    n=len(A)
    E=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)]
       for i,row in enumerate(A)]
    for j in range(n):
        p=next((i for i in range(j,n) if E[i][j]),None)
        if p is None:
            raise ArithmeticError('singular grounded matrix')
        E[j],E[p]=E[p],E[j]
        r=E[j][j]
        E[j]=[x/r for x in E[j]]
        for i in range(n):
            if i!=j and E[i][j]:
                t=E[i][j]
                E[i]=[a-t*b for a,b in zip(E[i],E[j])]
    return sum((E[i][n+i] for i in range(n)),F(0))

def objective(L,leaders):
    rem=[j for j in range(len(L)) if j not in leaders]
    return inverse_trace([[L[i][j] for j in rem] for i in rem])

def classes_and_formulas(m):
    matched=F(6*(m-1)**2,m*(2*m-3))
    same=F(3*m*m-4*m+3,m*(m-1))
    adjacent=F(2*(m-1)*(3*m*m-5*m+3),m*(m-2)*(2*m-1))
    return matched,same,adjacent

def classification(m, pair):
    a,b=sorted(pair)
    if a<m and b>=m:
        return "matched" if a==b-m else "adjacent"
    return "same"

def main():
    exhaustive=0;representatives=0;symbolic_identity=0
    for m in range(3,9):
        L=crown_laplacian(m)
        vals=classes_and_formulas(m)
        expect=dict(zip(("matched","same","adjacent"),vals))
        assert vals[0]<vals[1]<vals[2]
        counter={key:0 for key in expect}
        for pair in combinations(range(2*m),2):
            kind=classification(m,pair)
            actual=objective(L,set(pair))
            assert actual==expect[kind],(m,pair,kind,actual,expect[kind])
            counter[kind]+=1
            exhaustive+=1
        assert counter=={"matched":m,"same":m*(m-1),"adjacent":m*(m-1)}
        assert sum(counter.values())==comb(2*m,2)
    for m in (9,10,12):
        L=crown_laplacian(m)
        for pair in ((0,m),(0,1),(0,m+1)):
            kind=classification(m,pair)
            assert objective(L,set(pair))==dict(zip(
                ("matched","same","adjacent"), classes_and_formulas(m)))[kind]
            representatives+=1
    for m in range(3,151):
        CM,CS,CA=classes_and_formulas(m)
        assert CS-CM==F(m*m-3,m*(m-1)*(2*m-3))
        assert CA-CS==F(m*m+1,(m-2)*(m-1)*(2*m-1))
        symbolic_identity+=1
    print("PASS exhaustive_2sets",exhaustive,
          "representative_larger",representatives,
          "exact_gap_identities",symbolic_identity,
          "m_range", "3..8")
if __name__=="__main__":
    main()
