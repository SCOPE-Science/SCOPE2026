#!/usr/bin/env python3
"""Exact tests for matching-polytope Euclidean ball identities.

Only Python's standard library is required.  All linear algebra is rational.
The infinite-dimensional theorem is established by the accompanying proof,
not by this finite test suite.
"""
from fractions import Fraction as F
from itertools import permutations


def inverse(A):
    n=len(A)
    M=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        k=next((k for k in range(i,n) if M[k][i]),None)
        assert k is not None, 'incidence rank deficient'
        M[i],M[k]=M[k],M[i]
        fac=M[i][i]
        M[i]=[v/fac for v in M[i]]
        for j in range(n):
            if i!=j and M[j][i]:
                fac=M[j][i]
                M[j]=[a-fac*b for a,b in zip(M[j],M[i])]
    return [row[n:] for row in M]


def graph_complete(n):
    return [(i,j) for i in range(n) for j in range(n)]


def graph_crown(n):
    return [(i,j) for i in range(n) for j in range(n) if i!=j]


def graph_cycle(n):
    return [(i,j) for i in range(n) for j in (i,(i+1)%n)]


def graph_cube(d):
    left=[i for i in range(1<<d) if i.bit_count()%2==0]
    right=[i for i in range(1<<d) if i.bit_count()%2==1]
    li={v:i for i,v in enumerate(left)}
    ri={v:i for i,v in enumerate(right)}
    return [(li[x],ri[x^(1<<k)]) for x in left for k in range(d)]


def one_perfect_matching(edges,n):
    adj=[[j for i,j in edges if i==row] for row in range(n)]
    def backtrack(row,used,partial):
        if row==n: return partial[:]
        for j in adj[row]:
            if j not in used:
                partial.append((row,j))
                answer=backtrack(row+1,used|{j},partial)
                if answer is not None:return answer
                partial.pop()
        return None
    return backtrack(0,set(),[])


def verify_graph(label,n,degree,edges,enumerate_matchings=False):
    edges=list(edges); m=len(edges); dim=m-2*n+1
    assert len(set(edges))==m==n*degree and dim>0
    for i in range(n):
        assert sum(x==i for x,y in edges)==degree
        assert sum(y==i for x,y in edges)==degree
    B=[]
    for v in range(n): B.append([int(e[0]==v) for e in edges])
    for v in range(n-1): B.append([int(e[1]==v) for e in edges])
    N=len(B)
    gram=[[sum(B[i][e]*B[j][e] for e in range(m)) for j in range(N)] for i in range(N)]
    Gi=inverse(gram)
    # Orthogonal projector onto the zero-margins cycle space.
    P=[[F(int(e==f))-sum(F(B[i][e])*Gi[i][j]*B[j][f] for i in range(N) for j in range(N)) for f in range(m)] for e in range(m)]
    s2=F(dim,m)
    assert all(P[e][e]==s2 for e in range(m)),(label,[P[e][e] for e in range(m)])
    assert all(sum(P[e][f] for f in range(m))==0 for e in range(m))
    assert all(P[e][f]==P[f][e] for e in range(m) for f in range(m))
    assert all(sum(P[e][k]*P[k][f] for k in range(m))==P[e][f] for e in range(m) for f in range(m))
    # John's contact vectors u_e = -P e_e/s, weights c_e=dim/m.
    # Their first moment vanishes, second moment is identity on the cycle space.
    assert all(sum(P[e][f] for e in range(m))==0 for f in range(m))
    # For a contact point x=U-rPe/s, all coordinates satisfy x_f>=0 by Cauchy-Schwarz.
    assert all(P[e][f]<=s2 for e in range(m) for f in range(m))
    r2=F(n,degree*dim)
    R2=F(n*(degree-1),degree)
    ratio2=F((degree-1)*dim)
    assert R2/r2==ratio2
    # Edge-decompose the regular bipartite graph into exactly degree perfect matchings.
    rest=set(edges); decomposition=[]
    for step in range(degree):
        M=one_perfect_matching(rest,n)
        assert M is not None and len(M)==n
        decomposition.append(M)
        rest-=set(M)
    assert not rest
    assert all(sum((e in M) for M in decomposition)==1 for e in edges)
    for M in decomposition:
        assert sum((F(int(e in M))-F(1,degree))**2 for e in edges)==R2
    if enumerate_matchings:
        mat=set(edges)
        matchings=[[(i,p[i]) for i in range(n)] for p in permutations(range(n)) if all((i,p[i]) in mat for i in range(n))]
        assert matchings
        assert all(sum((F(int(e in M))-F(1,degree))**2 for e in edges)==R2 for M in matchings)
    print(f'{label}: n={n}, d={degree}, m={m}, D={dim}, r^2={r2}, R^2={R2}, (R/r)^2={ratio2}; PASS')


def run():
    for n in range(2,6):
        verify_graph(f'K_{n},{n}',n,n,graph_complete(n),True)
    for n in range(3,7):
        verify_graph(f'crown_{n}',n,n-1,graph_crown(n),n<=5)
    for n in range(2,7):
        verify_graph(f'cycle_{2*n}',n,2,graph_cycle(n),n<=5)
    for d in (3,4):
        n=2**(d-1)
        verify_graph(f'cube_Q{d}',n,d,graph_cube(d),d==3)
    print('ALL EXACT TESTS PASSED: 15 graph instances')
if __name__=='__main__': run()
