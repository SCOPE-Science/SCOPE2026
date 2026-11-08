#!/usr/bin/env python3
"""Exact finite certificate verifier for five-nucleotide near-GC-balanced DNA deletion codes."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

BASES = "ACGT"
COMPLEMENT = dict(zip("ATCG", "TAGC"))

def reverse_complement(word):
    return "".join(COMPLEMENT[x] for x in reversed(word))

def deletions(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}

def candidate_pairs():
    words = ("".join(w) for w in itertools.product(BASES, repeat=5))
    eligible = [w for w in words if sum(x in "CG" for x in w) in (2, 3)]
    paired = sorted({tuple(sorted((w, reverse_complement(w)))) for w in eligible})
    assert len(eligible) == 640 and len(paired) == 320
    candidates = [pair for pair in paired if pair[0] != pair[1] and deletions(pair[0]).isdisjoint(deletions(pair[1]))]
    assert len(candidates) == 260
    return candidates

def graph(candidates):
    shadow = [set().union(*(deletions(w) for w in pair)) for pair in candidates]
    adjacent = [set() for _ in candidates]
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            if not shadow[i].isdisjoint(shadow[j]):
                adjacent[i].add(j)
                adjacent[j].add(i)
    assert sum(map(len, adjacent)) == 9896
    return adjacent

def verify_certificate(cert, candidates, adjacency):
    n = len(candidates)
    assert cert['format'] == 'clique_dual_branch_v1' and cert['n_vertices'] == n
    cliques = cert['cliques']
    for clique in cliques:
        assert clique and len(clique) == len(set(clique))
        assert all(isinstance(i, int) and 0 <= i < n for i in clique)
        assert all(j in adjacency[i] for i, j in itertools.combinations(clique, 2))
    reached = []
    def visit(node, path):
        if 'leaf' not in node:
            vertex = node['variable']
            assert isinstance(vertex, int) and 0 <= vertex < n
            assert vertex not in [k for k, _ in path]
            visit(node['one'], path + [(vertex, 1)])
            visit(node['zero'], path + [(vertex, 0)])
            return
        leaf = node['leaf']
        assert leaf['path'] == [[k, v] for k, v in path]
        ones = {i for i, v in path if v == 1}
        zeros = {i for i, v in path if v == 0}
        conflict = any(j in adjacency[i] for i in ones for j in ones if i != j)
        if leaf['kind'] == 'conflicting_selected':
            assert conflict
            reached.append('conflicting')
            return
        assert leaf['kind'] == 'dual' and not conflict
        unavailable = ones | zeros | set().union(*(adjacency[i] for i in ones))
        remaining = set(range(n)) - unavailable
        coverage = {i: Fraction(0) for i in remaining}
        total = Fraction(len(ones))
        for index, rational in leaf['weights']:
            assert isinstance(index, int) and 0 <= index < len(cliques)
            weight = Fraction(rational)
            assert weight >= 0
            total += weight
            for i in cliques[index]:
                if i in coverage:
                    coverage[i] += weight
        assert all(value >= 1 for value in coverage.values())
        assert total == Fraction(leaf['bound'])
        assert total < 23, (path, total)
        assert leaf['remaining'] == len(remaining)
        reached.append(str(total))
    visit(cert['root'], [])
    assert len(reached) == len(cert['leaves']) == 4
    return reached

def verify_lower_example(candidates, adjacency, words):
    assert len(words) == 22 and len(set(words)) == 22
    to_index = {tuple(pair): i for i, pair in enumerate(candidates)}
    selected = []
    for text in words:
        pair = tuple(text.split('/'))
        assert len(pair) == 2 and pair == tuple(sorted(pair))
        assert reverse_complement(pair[0]) == pair[1]
        selected.append(to_index[pair])
    assert len(set(selected)) == 22
    assert all(j not in adjacency[i] for i, j in itertools.combinations(selected, 2))
    all_words = [w for i in selected for w in candidates[i]]
    seen = {}
    for word in all_words:
        assert sum(x in 'CG' for x in word) in (2, 3)
        for output in deletions(word):
            assert output not in seen, (output, seen.get(output), word)
            seen[output] = word
    assert len(all_words) == 44 and len(set(all_words)) == 44
    return len(seen)

def main():
    folder = Path(__file__).resolve().parent
    candidates = candidate_pairs()
    adjacency = graph(candidates)
    cert = json.loads((folder / 'certificate.json').read_text(encoding='utf-8'))
    example = (folder / 'example_code.txt').read_text(encoding='utf-8').splitlines()
    observed = verify_lower_example(candidates, adjacency, example)
    bounds = verify_certificate(cert, candidates, adjacency)
    print(f'EXACT_CERTIFICATE_OK candidates={len(candidates)} conflicts={sum(map(len, adjacency))//2} pairs=22 words=44 deletion_outputs={observed} leaves={len(bounds)}')
    print('leaf_bounds=' + ','.join(bounds))
if __name__ == '__main__':
    main()
