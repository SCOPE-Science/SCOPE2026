#!/usr/bin/env python3
"""Exact finite-field controllability checks for odd chorded cycles.

This finite test supplements, but does not replace, the infinite-family proof.
Run: python3 chorded_cycle_verify.py
Requires only Python standard library.
"""

PRIME = 1000000007

def laplacian_adjacency(n):
    adjacency = [set() for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        adjacency[i].add(j)
        adjacency[j].add(i)
    adjacency[0].add(2)
    adjacency[2].add(0)
    return [tuple(sorted(x)) for x in adjacency]

def krylov(n, adj, leader, prime=PRIME):
    columns = []
    v = [int(i == leader) for i in range(n)]
    for _ in range(n):
        columns.append(v)
        v = [(len(adj[i])*v[i] - sum(v[k] for k in adj[i])) % prime for i in range(n)]
    return [[columns[k][i] for k in range(n)] for i in range(n)]

def rank_mod(A, p=PRIME):
    m = len(A); n = len(A[0]); row = 0
    for col in range(n):
        pivot = next((r for r in range(row, m) if A[r][col]%p), None)
        if pivot is None: continue
        A[row], A[pivot] = A[pivot], A[row]
        inv = pow(A[row][col], p-2, p)
        for r in range(row+1,m):
            coeff = A[r][col]*inv%p
            if coeff:
                for c in range(col+1,n):
                    A[r][c] = (A[r][c]-coeff*A[row][c])%p
                A[r][col]=0
        row += 1
        if row==m: break
    return row

def check():
    cases = 0
    counts = []
    for n in range(5,36,2):
        adj = laplacian_adjacency(n)
        full = 0
        for j in range(n):
            r = rank_mod(krylov(n,adj,j))
            if j==1:
                assert r == (n+1)//2, (n,j,'exception rank',r)
            else:
                assert r == n, (n,j,'full rank',r)
                full += 1
            cases+=1
        counts.append(f'{n}:{full}/{n-1}')
    print('PASS: exact modular Krylov ranks;', cases, 'single-vertex configurations')
    print('Admissible placements (n:count/expected):', ', '.join(counts))
    print('Modular full rank gives a rigorous nonzero integer minor/determinant;')
    print('non-full-rank at vertex 1 is separately established by reflection in the proof.')
if __name__=='__main__': check()
