"""Finite checks for partition-preserving idempotent transformation counts.

Run with Python 3 standard library: python checker.py
These finite tests do not establish the stated asymptotic theorem.
"""
from itertools import product
from math import comb
from fractions import Fraction


def rooted_count(target_block_size, total_source_size):
    return sum(comb(target_block_size, r) * r ** (total_source_size - r)
               for r in range(1, target_block_size + 1))


def count_by_root_set(block_sizes):
    m = len(block_sizes)
    result = {}
    for phi in product(range(m), repeat=m):
        if any(phi[phi[i]] != phi[i] for i in range(m)):
            continue
        roots = tuple(sorted(set(phi)))
        multiplicity = 1
        for j in roots:
            mass = sum(block_sizes[i] for i in range(m) if phi[i] == j)
            multiplicity *= rooted_count(block_sizes[j], mass)
        result[roots] = result.get(roots, 0) + multiplicity
    return result


def direct_enumeration(block_sizes):
    blocks = []
    index_to_block = []
    offset = 0
    for j, s in enumerate(block_sizes):
        blocks.append(tuple(range(offset, offset + s)))
        index_to_block.extend([j] * s)
        offset += s
    m = len(block_sizes)
    result = {}
    for phi in product(range(m), repeat=m):
        choices = [blocks[phi[index_to_block[x]]] for x in range(offset)]
        for f in product(*choices):
            if any(f[f[x]] != f[x] for x in range(offset)):
                continue
            roots = tuple(sorted({index_to_block[f[x]] for x in range(offset)}))
            result[roots] = result.get(roots, 0) + 1
    return result


def run():
    cases = [(1, 1), (2, 1), (2, 2), (3, 2), (1, 1, 1), (2, 1, 1)]
    for sizes in cases:
        formula = count_by_root_set(sizes)
        direct = direct_enumeration(sizes)
        assert formula == direct, (sizes, formula, direct)
        assert sum(formula.values()) == sum(direct.values())
        print(f"PASS exact idempotent fibers: blocks={sizes}, total={sum(formula.values())}, roots={formula}")
    for s in range(2, 8):
        for N in range(s + 1, s + 6):
            h = rooted_count(s, N)
            hnext = rooted_count(s + 1, N)
            lhs = hnext - h
            rhs = (s + 1) ** (N - s - 1) + sum(
                Fraction(comb(s, r) * r ** (N - r) * r, s + 1 - r)
                for r in range(1, s + 1))
            assert Fraction(lhs, 1) == rhs
    print("PASS binomial step identity, including endpoint term, on 30 finite pairs")


if __name__ == "__main__":
    run()
