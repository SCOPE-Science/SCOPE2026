"""Recompute finite DNA-code bounds and check explicit codebooks.

Requires Python 3.11+, NumPy, SciPy (HiGHS MILP), and NetworkX.
Run: python verify.py
"""
from itertools import product
from pathlib import Path
import numpy as np
import networkx as nx
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

BASE = Path(__file__).resolve().parent
ALPHABET = "ATCG"
COMPLEMENT = str.maketrans("ATCG", "TAGC")


def reverse_complement(word):
    return word[::-1].translate(COMPLEMENT)


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def permitted(n):
    return [s for t in product(ALPHABET, repeat=n)
            if (s := ''.join(t)) and sum(c in 'CG' for c in s) == n // 2
            and all(s[i] != s[i+1] for i in range(n-1))
            and hamming(s, reverse_complement(s)) >= 3]


def conflict(a, b):
    return hamming(a, b) < 3 or hamming(a, reverse_complement(b)) < 3


def read_code(filename, n):
    code = (BASE / filename).read_text(encoding='utf-8').splitlines()
    assert len(set(code)) == len(code) and all(len(s) == n for s in code)
    allowed = set(permitted(n))
    assert all(s in allowed for s in code)
    assert all(not conflict(a,b) for i,a in enumerate(code) for b in code[i+1:])
    return code


def graph(n):
    words = permitted(n)
    g = nx.Graph()
    g.add_nodes_from(words)
    for i, a in enumerate(words):
        for b in words[i+1:]:
            if conflict(a,b):
                g.add_edge(a,b)
    return words,g


def run_binary_milp(matrix, num_words):
    r = milp(-np.ones(num_words),
             integrality=np.ones(num_words, dtype=np.int32),
             bounds=Bounds(0,1),
             constraints=LinearConstraint(matrix,0,1),
             options={"mip_rel_gap":0.0, "time_limit":55})
    assert r.status == 0, r.message
    # Both an integral feasible witness and a certified branch-and-bound
    # dual bound are required. An absolute margin of 0.01 is safely below
    # the full unit separation between possible integer optima.
    assert abs(r.fun + 27) < 0.01, (r.fun,r.mip_dual_bound)
    assert r.mip_dual_bound > -27.01, r.mip_dual_bound
    assert np.all(np.abs(r.x - np.round(r.x)) < 1.e-6)
    assert np.all(matrix @ r.x <= 1.000001)
    assert round(sum(r.x)) == 27
    return r


def main():
    assert len(permitted(2)) == 0
    words4,g4=graph(4)
    assert (len(words4), g4.number_of_edges()) == (40,468)
    maxima = [c for c in nx.find_cliques(nx.complement(g4)) if len(c) == 4]
    # max_clique=4 is also checked by not finding larger cliques.
    maximal = list(nx.find_cliques(nx.complement(g4)))
    assert max(map(len,maximal)) == 4 and len(maxima) == 64
    words,g=graph(6)
    assert len(words) == 344 and g.number_of_edges() == 7804
    c6=read_code('code6.txt',6)
    assert len(c6)==27
    idx={w:i for i,w in enumerate(words)}
    # Formulation 1: all maximal incompatibility cliques (a different
    # constraint-generation route from individual pairs).
    cliques=list(nx.find_cliques(g))
    assert len(cliques)==980
    rows=[j for j,C in enumerate(cliques) for w in C]
    cols=[idx[w] for C in cliques for w in C]
    M=coo_matrix((np.ones(len(rows)),(rows,cols)),
                 shape=(len(cliques),len(words))).tocsr()
    r1=run_binary_milp(M,len(words))
    # Formulation 2: all pairwise incompatibilities, constructed afresh.
    pairs=[(i,j) for i,a in enumerate(words) for j in range(i+1,len(words))
           if hamming(a,words[j])<3 or hamming(a,reverse_complement(words[j]))<3]
    assert len(pairs)==7804
    rr=np.repeat(np.arange(len(pairs)),2)
    cc=np.fromiter((v for ij in pairs for v in ij),dtype=np.int32)
    M2=coo_matrix((np.ones(len(cc)),(rr,cc)),shape=(len(pairs),len(words))).tocsr()
    r2=run_binary_milp(M2,len(words))
    c8=read_code('code8.txt',8)
    assert len(c8)==136
    print('VERIFY_OK n2=0 n4=4,64-optima n6=27 n8>=136')
    print('N6 certificates: maximal-clique rows=',len(cliques), 'B&B nodes=',r1.mip_node_count,
          '; pairwise rows=',len(pairs),'B&B nodes=',r2.mip_node_count)
    print('N6 certified MILP dual bounds:',r1.mip_dual_bound,r2.mip_dual_bound)


if __name__=='__main__':
    main()
