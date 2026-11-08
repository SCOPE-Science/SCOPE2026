#!/usr/bin/env python3
"""Independent finite examples for graph-vs-walk evolution algebras.

The rank checks enumerate finite-field vectors, while positive cases check
specified real diagonal algebra isomorphisms. These finite checks are not a
proof of the general theorem.
"""
from fractions import Fraction
from itertools import product
from math import isclose


def adjacency(name):
    if name.startswith('K'):
        n = int(name[1:]); return [[int(i != j) for j in range(n)] for i in range(n)]
    if name.startswith('P'):
        n = int(name[1:]); return [[int(abs(i-j) == 1) for j in range(n)] for i in range(n)]
    if name.startswith('C'):
        n = int(name[1:]); return [[int((i-j) % n in (1, n-1)) for j in range(n)] for i in range(n)]
    raise ValueError(name)


def matrix_rank(matrix, p=None):
    if not matrix: return 0
    mat = [[(x % p if p else Fraction(x)) for x in row] for row in matrix]
    n, k = len(mat), len(mat[0]); row = 0
    for col in range(k):
        piv = next((i for i in range(row, n) if mat[i][col]), None)
        if piv is None: continue
        mat[row], mat[piv] = mat[piv], mat[row]
        inv = pow(int(mat[row][col]), -1, p) if p else 1 / mat[row][col]
        for j in range(col, k): mat[row][j] = (mat[row][j] * inv) % p if p else mat[row][j] * inv
        for i in range(row + 1, n):
            c = mat[i][col]
            if not c: continue
            for j in range(col, k): mat[i][j] = (mat[i][j] - c * mat[row][j]) % p if p else mat[i][j] - c * mat[row][j]
        row += 1
        if row == n: break
    return row


def blowup(base, sizes):
    partition = [i for i,m in enumerate(sizes) for _ in range(m)]
    adj = [[base[partition[u]][partition[v]] for v in range(len(partition))] for u in range(len(partition))]
    deg = [sum(row) for row in adj]
    return partition, adj, deg


def is_bipartite(base):
    color = [None] * len(base); color[0] = 0
    queue = [0]
    for i in queue:
        for j, b in enumerate(base[i]):
            if not b: continue
            if color[j] is None: color[j] = 1-color[i];queue.append(j)
            else: assert color[j] != color[i] or return_false()
    return color


def return_false():
    raise NotBipartite

class NotBipartite(Exception): pass


def positive_witness(base, bag_ids, deg):
    if len(set(deg)) == 1:
        scale = [float(deg[0])] * len(deg)
    else:
        colors = is_bipartite(base)
        gcolors = [colors[i] for i in bag_ids]
        D = [next(deg[v] for v in range(len(deg)) if gcolors[v] == c) for c in (0,1)]
        assert all(deg[v] == D[gcolors[v]] for v in range(len(deg)))
        S = [(D[0]**2 * D[1])**(1/3), (D[0]*D[1]**2)**(1/3)]
        scale = [S[c] for c in gcolors]
    for v, dv in enumerate(deg):
        for w in range(len(deg)):
            if base[bag_ids[v]][bag_ids[w]]:
                assert isclose(scale[v]**2 / dv, scale[w], abs_tol=1e-10, rel_tol=1e-10)
    return scale


def exhaustive_rank_check(bag_ids, adj, p=5):
    n = len(bag_ids)
    w = {i:[adj[next(v for v,b in enumerate(bag_ids) if b == i)][k] for k in range(n)] for i in set(bag_ids)}
    count = 0
    for x in product(range(p), repeat=n):
        if not any(x): continue
        # The map y -> xy has columns x_v times the adjacency neighbor vector of v.
        op = [[(x[v]*w[bag_ids[v]][row]) % p for v in range(n)] for row in range(n)]
        expected = len({bag_ids[v] for v in range(n) if x[v]})
        assert matrix_rank(op, p) == expected, (x, expected)
        count += 1
    return count


def run():
    cases = [
        ('K2',(2,3),'biregular'),
        ('K3',(2,2,2),'regular'),
        ('K3',(2,1,1),'obstructed'),
        ('K3',(1,1,1),'regular'),
        ('P4',(2,1,2,1),'obstructed'),
        ('C6',(2,3,2,3,2,3),'biregular'),
        ('K4',(2,1,1,1),'obstructed'),
    ]
    rank_vectors=0; positive=0; blocked=0
    for name, sizes, expected in cases:
        base = adjacency(name)
        assert matrix_rank(base) == len(base), name
        bags, graph, degrees = blowup(base,sizes)
        assert min(degrees)>0
        bipartite = False
        try: colors=is_bipartite(base);bipartite=True
        except NotBipartite: pass
        if len(set(degrees))==1: classification='regular'
        elif bipartite and all(len(set(degrees[v] for v in range(len(degrees)) if colors[bags[v]]==c))==1 for c in (0,1)):
            classification='biregular'
        else: classification='obstructed'
        assert expected == classification, (name,sizes,expected,classification)
        if classification != 'obstructed':
            positive_witness(base,bags,degrees);positive+=1
        else: blocked+=1
        if len(bags)<=6: rank_vectors+=exhaustive_rank_check(bags,graph)
    print(f'VERIFY_OK cases={len(cases)} positive_real_isomorphisms={positive} obstructed_degree_profiles={blocked} exhaustive_rank_vectors_F5={rank_vectors} base_adjacency_full_rank=all')

if __name__=='__main__': run()
