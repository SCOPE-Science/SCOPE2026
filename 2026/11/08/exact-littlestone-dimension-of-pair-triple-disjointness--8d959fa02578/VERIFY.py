"""Verification of pair-center/triple-query disjointness mistake trees.

Python >=3.9, standard library only. Uses independent membership checks and
an optional exact minimax recurrence for small ground sets.
"""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def verify_certificate(cert):
    n = cert['ground_size']
    d = cert['depth']
    leaves = []
    def walk(node, remaining, depth):
        if depth == 0:
            assert set(node) == {'witness'}
            witness = tuple(node['witness'])
            assert len(witness) == 2 and witness in remaining
            leaves.append(witness)
            return
        assert set(node) == {'query', 'no', 'yes'}
        q = tuple(node['query'])
        assert len(q) == 3 and len(set(q)) == 3 and all(1 <= x <= n for x in q)
        no = tuple(pair for pair in remaining if set(pair) & set(q))
        yes = tuple(pair for pair in remaining if not(set(pair) & set(q)))
        assert no and yes
        walk(node['no'], no, depth - 1)
        walk(node['yes'], yes, depth - 1)
    pairs = tuple(combinations(range(1, n+1), 2))
    walk(cert['tree'], pairs, d)
    assert len(leaves) == 2**d and len(set(leaves)) == 2**d
    return n, d, len(leaves)


def exact_dimension(n):
    hypotheses = tuple(combinations(range(1, n+1), 2))
    queries = tuple(combinations(range(1, n+1), 3))
    masks = tuple(sum(1 << i for i, pair in enumerate(hypotheses) if not set(pair) & set(query)) for query in queries)
    universe = (1 << len(hypotheses)) - 1
    @lru_cache(None)
    def rank(space):
        best = 0
        for mask in masks:
            pos = space & mask
            neg = space & (universe ^ mask)
            if pos and neg:
                best = max(best, 1 + min(rank(pos), rank(neg)))
        return best
    answer = rank(universe)
    return answer, rank.cache_info().currsize


def main():
    data = json.loads((HERE/'TREES.json').read_text(encoding='utf-8'))
    expected_certificates = [(5,1),(6,2),(7,3),(8,4),(10,5)]
    actual = [verify_certificate(c) for c in data['certificates']]
    assert [c[:2] for c in actual] == expected_certificates
    print('ALL_PAIR_TRIPLE_TREE_CERTIFICATES_PASS', actual)
    results=[]
    for n in range(3, 9):
        got, states = exact_dimension(n)
        expected={3:0,4:0,5:1,6:2,7:3,8:4}[n]
        assert got == expected, (n,got,expected)
        results.append((n,got,states))
    print('INDEPENDENT_EXACT_RECURRENCE_PASS', results)
    print('PAIR_TRIPLE_ALL_CHECKS_PASS')

if __name__=='__main__':main()
