#!/usr/bin/env python3
"""Exact finite Littlestone recursion and separate path-wise tree verification.

Usage: python3 verify_triangular.py --generate witness_trees.json
       python3 verify_triangular.py --check witness_trees.json
No external dependencies. Vertices are 0,...,n-1; queries and hypotheses are unordered edges.
"""
import argparse
import json
from functools import lru_cache
from itertools import combinations

EXPECTED = {2: 0, 3: 1, 4: 1, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 4, 11: 4}


def build(n):
    edges = list(combinations(range(n), 2))
    incidence = []
    for query in edges:
        row = 0
        for j, hyp in enumerate(edges):
            if (query[0] == hyp[0]) + (query[0] == hyp[1]) + (query[1] == hyp[0]) + (query[1] == hyp[1]) == 1:
                row |= 1 << j
        incidence.append(row)
    return edges, incidence


def exact_dimension(n):
    edges, rows = build(n)
    @lru_cache(None)
    def rank(version):
        if version == 0 or version & (version - 1) == 0:
            return 0
        best = 0
        for row in rows:
            yes = version & row
            no = version & ~row
            if yes and no:
                score = 1 + min(rank(yes), rank(no))
                if score > best:
                    best = score
        return best
    return rank, edges, rows


def certificate(n, depth):
    rank, edges, rows = exact_dimension(n)
    current = (1 << len(edges)) - 1
    assert rank(current) >= depth
    def rec(version, remaining):
        if remaining == 0:
            return {"witness_hypothesis": list(edges[(version & -version).bit_length() - 1])}
        for i, row in enumerate(rows):
            yes, no = version & row, version & ~row
            if yes and no and rank(yes) >= remaining - 1 and rank(no) >= remaining - 1:
                return {"query": list(edges[i]), "zero": rec(no, remaining - 1), "one": rec(yes, remaining - 1)}
        raise AssertionError("witness tree not found")
    return {"n": n, "depth": depth, "tree": rec(current, depth)}


def verify_tree(tree_record):
    n, depth = tree_record["n"], tree_record["depth"]
    edges = list(combinations(range(n), 2))
    def hit(e, q):
        return len(set(e).intersection(q)) == 1
    paths = 0
    def check(node, constraints, level):
        nonlocal paths
        possible = [e for e in edges if all(hit(e, q) == label for q, label in constraints)]
        assert possible, f"empty branch: {constraints}"
        if level == depth:
            assert "query" not in node
            hyp = tuple(node["witness_hypothesis"])
            assert hyp in possible, (hyp, constraints)
            paths += 1
            return
        assert "query" in node and "witness_hypothesis" not in node
        q = tuple(node["query"])
        assert q in edges
        check(node["zero"], constraints + [(q, False)], level+1)
        check(node["one"], constraints + [(q, True)], level+1)
    check(tree_record["tree"], [], 0)
    assert paths == 2**depth
    return paths


def main():
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--generate')
    group.add_argument('--check')
    args = p.parse_args()
    if args.generate:
        rows = [certificate(5, 3), certificate(7, 4)]
        with open(args.generate, 'w', encoding='utf8') as f:
            json.dump({"format": "triangular-open-neighborhood-tree-v1", "certificates": rows}, f, indent=2)
            f.write('\n')
        print('Generated depth-3 and depth-4 trees with', sum(verify_tree(r) for r in rows), 'nonempty leaf paths.')
    else:
        with open(args.check, encoding='utf8') as f:
            cert = json.load(f)
        assert cert['format'] == 'triangular-open-neighborhood-tree-v1'
        for row in cert['certificates']:
            print('Tree:', row['n'], 'depth', row['depth'], 'verified paths', verify_tree(row))
        for n, expected in EXPECTED.items():
            dim, edges, _ = exact_dimension(n)
            actual = dim((1 << len(edges)) - 1)
            assert actual == expected, (n, actual, expected)
            print('Exact recurrence: n=', n, 'Ldim=', actual, 'hypotheses=', len(edges), 'states=', dim.cache_info().currsize)
        print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
