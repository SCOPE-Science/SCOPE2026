#!/usr/bin/env python3
"""Finite exact checks for Mayer path chains of a monotone directed ladder.

Uses prime fields with roots of the prescribed orders. The proof for arbitrary
ladder length and root order is mathematical; finite checks are corroboration.
"""
from itertools import product

PARAMETERS = [(2, 7, 6), (3, 7, 2), (4, 5, 2), (5, 11, 3), (6, 7, 3)]


def rank_mod(rows, number_columns, prime):
    matrix = [list(map(lambda x: x % prime, r)) for r in rows]
    rank = 0
    for column in range(number_columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(inverse*x) % prime for x in matrix[rank]]
        for i in range(rank + 1, len(matrix)):
            if matrix[i][column]:
                f = matrix[i][column]
                matrix[i] = [(x - f*y) % prime for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def directed_ladder(m):
    # Bottom vertices are 0,...,m-1; upper vertices m,...,2m-1.
    edges = ([(i,i+1) for i in range(m-1)]
             + [(m+i,m+i+1) for i in range(m-1)]
             + [(i,m+i) for i in range(m)])
    adjacency = {i: [] for i in range(2*m)}
    for x,y in edges:
        adjacency[x].append(y)
    paths = {0: [(i,) for i in range(2*m)]}
    for degree in range(1,m+1):
        paths[degree] = [a+(v,) for a in paths[degree-1]
                         for v in adjacency[a[-1]]]
    assert not any(adjacency[a[-1]] for a in paths[m])
    return edges, paths


def check_case(N, prime, zeta, m):
    assert pow(zeta, N, prime) == 1
    assert all(pow(zeta, k, prime) != 1 for k in range(1,N))
    edges, paths = directed_ladder(m)
    vcount, ecount, scount = 2*m, 3*m-2, m-1
    assert len(edges) == ecount
    # Directly construct the 'not-allowed' part of the one-step boundary
    # of *every* allowed path, without assuming a description of Omega.
    for degree in range(2,m+1):
        allowed = set(paths[degree-1])
        nonallowed = {}
        for col, path in enumerate(paths[degree]):
            for j in range(degree+1):
                face = path[:j]+path[j+1:]
                if face not in allowed:
                    row = nonallowed.setdefault(face,[0]*len(paths[degree]))
                    row[col] = (row[col] + pow(zeta,j,prime)) % prime
        r = rank_mod(nonallowed.values(),len(paths[degree]),prime)
        expected = scount if degree==2 else 0
        assert len(paths[degree])-r == expected, (N,m,degree,r)
    # Basis of Omega_2: two route differences around every square.
    two = {path:j for j,path in enumerate(paths[2])}
    one = set(paths[1])
    edge_index = {path:j for j,path in enumerate(edges)}
    B1 = [[0]*ecount for _ in range(vcount)]
    for col,(a,b) in enumerate(edges):
        B1[a][col] = zeta
        B1[b][col] = 1
    B2 = [[0]*scount for _ in range(ecount)]
    for col in range(scount):
        path1=(col,col+1,m+col+1)
        path2=(col,m+col,m+col+1)
        assert path1 in two and path2 in two
        for sign, path in [(1,path1),(-1,path2)]:
            for j in range(3):
                face = path[:j]+path[j+1:]
                if face in one:
                    B2[edge_index[face]][col] = (B2[edge_index[face]][col]
                                          + sign*pow(zeta,j,prime))%prime
                else:
                    assert j==1
    B12 = [[sum(B1[i][k]*B2[k][j] for k in range(ecount))%prime
             for j in range(scount)] for i in range(vcount)]
    r1=rank_mod(B1,ecount,prime)
    r2=rank_mod(B2,scount,prime)
    r12=rank_mod(B12,scount,prime)
    assert (r1,r2,r12)==(vcount-1,scount,0 if N==2 else scount)
    # Verify the *actual* degree-zero composition coefficient and support.
    for i in range(vcount):
        for j in range(scount):
            expected=0
            if N!=2:
                if i==j+1: expected=zeta+zeta*zeta
                if i==m+j: expected=-(zeta+zeta*zeta)
            assert B12[i][j] == expected % prime, (N,m,i,j)
    if N==2:
        expected_by_q={1:(1,0,0)}
    else:
        expected_by_q={}
        for q in range(1,N):
            beta0=(1 if q==N-1 else m+1 if q==N-2 else 2*m)
            beta1=(m-1 if q==1 else 2*m-1 if q==N-1 else 3*m-2)
            beta2=m-1 if q>=3 else 0
            expected_by_q[q]=(beta0,beta1,beta2)
    for q,expected in expected_by_q.items():
        # With Omega_n=0 beyond degree two, direct kernel-minus-image ranks.
        ranks=[0,r1,r2,r12]
        dimensions=[vcount,ecount,scount]
        def power_rank(n,power):
            if n-power<0: return 0
            if power==1: return {1:r1,2:r2}.get(n,0)
            if power==2: return r12 if n==2 else 0
            return 0
        actual=tuple(dimensions[n]-power_rank(n,q)
                   -power_rank(n+N-q,N-q) for n in range(3))
        assert actual==expected,(N,m,q,actual,expected)
    return sum(map(len,paths.values()))


def main():
    cases=0; path_instances=0
    for N,p,z in PARAMETERS:
        for m in range(2,9):
            path_instances+=check_case(N,p,z,m)
            cases+=1
    print(f'ALL_VERIFY_OK cases={cases} ladder_columns=2..8 '
          f'orders=2,3,4,5,6 allowed_path_instances={path_instances}')

if __name__=='__main__': main()
