#!/usr/bin/env python3
"""Exact independently replayable checks for the rank-two evolution-algebra graph theorem.
Integer vector arithmetic, rational Cheeger values, and exhaustive graph cuts.
"""
from fractions import Fraction
from itertools import combinations

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def cheeger(edges,n):
    vals=[]
    for size in range(1,n//2+1):
        for W in combinations(range(n),size):
            cut=set(W)
            vals.append(Fraction(sum((i in cut)!=(j in cut) for i,j in edges), size))
    return min(vals)
def graph_from_natural_basis(F):
    n=len(F)
    e1=[1]+[0]*(n-1)
    z=[1]*n
    # e1^2=z+e1, ei^2=z for i>=2.
    def mult(u,v): return [dot(u,v)*z[k]+u[0]*v[0]*e1[k] for k in range(n)]
    # Prove naturalness and independence by explicit dot orthogonality.
    for i in range(n):
        for j in range(n):
            if i!=j: assert mult(F[i],F[j])==[0]*n
    # Express squares using rational Gaussian elimination in the orthogonal block.
    # F[0]=e1, F[1:] have first coordinate zero and are mutually orthogonal.
    assert F[0]==e1
    assert all(f[0]==0 for f in F[1:])
    assert all(dot(f,f)>0 for f in F)
    def coord(v,j):
        return Fraction(v[0]) if j==0 else Fraction(dot(v,F[j]),dot(F[j],F[j]))
    M=[[coord(mult(F[i],F[i]),j) for j in range(n)] for i in range(n)]
    assert all([sum(M[i][j]*F[j][k] for j in range(n)) for k in range(n)]==mult(F[i],F[i]) for i in range(n))
    edges={(i,j) for i in range(n) for j in range(i+1,n) if M[i][j]!=0 or M[j][i]!=0}
    return edges,M

def test(n):
    e=[[int(i==j) for j in range(n)] for i in range(n)]
    # Same elementary integral orthogonal transform on the last n-1 coordinates.
    F=[e[0], [0]+[1]*(n-1)]
    for t in range(1,n-1):
        F.append([0]+[1 if j<t else -t if j==t else 0 for j in range(n-1)])
    for i in range(1,n):
        for j in range(1,n):
            assert (dot(F[i],F[j])==0)==(i!=j)
    edge_full,_=graph_from_natural_basis(e)
    edge_min,_=graph_from_natural_basis(F)
    complete={(i,j) for i in range(n) for j in range(i+1,n)}
    split={(i,j) for i in range(n) for j in range(i+1,n) if i<2 or j<2}
    assert edge_full==complete and edge_min==split
    target_min=Fraction(2) if n%2 else Fraction(2)-Fraction(2,n)
    assert cheeger(edge_min,n)==target_min
    assert cheeger(edge_full,n)==Fraction((n+1)//2)
    # Verify all intervening complete-split graph Cheeger constants are nondecreasing.
    vals=[]
    for k in range(2,n+1):
        E={(i,j) for i in range(n) for j in range(i+1,n) if i<k or j<k}
        h=cheeger(E,n)
        predicted=Fraction((n+1)//2)-Fraction(((n-k)**2)//4,n//2)
        assert h==predicted, (n,k,h,predicted)
        vals.append(h)
    assert vals[0]==target_min and vals[-1]==Fraction((n+1)//2)
    assert vals==sorted(vals)

if __name__=='__main__':
    for n in range(3,11): test(n)
    print('VERIFY_OK rank_two_evolution_algebras dimensions=3..10 natural_bases=16 exact_multiplications=yes all_cuts=yes parity_extrema=yes all_split_graph_cheeger_formula=yes')
