#!/usr/bin/env python3
"""Exact finite decision-tree check for comparison concepts of total orders.

No external dependencies. Run: python3 permutation_comparison_verify.py
If witness_tree.json is beside this file, its 2,047 internal queries are also checked.
The two decision procedures use separate mathematical representations:
sets of total orders (bit masks) and transitively closed strict partial orders.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import json


def mask_solver(n):
    orders = list(permutations(range(n)))
    queries = list(combinations(range(n), 2))
    patterns = []
    for i, j in queries:
        mask = 0
        for t, p in enumerate(orders):
            # p is the order from least to greatest; compare positions.
            if p.index(i) < p.index(j):
                mask |= 1 << t
        patterns.append(mask)
    universe = (1 << len(orders)) - 1
    states = Counter()

    @lru_cache(None)
    def depth_possible(mask, depth):
        states[depth] += 1
        if depth == 0:
            return mask != 0
        if mask.bit_count() < (1 << depth):
            return False
        for query in patterns:
            yes = mask & query
            no = mask & (universe ^ query)
            if min(yes.bit_count(), no.bit_count()) < (1 << (depth - 1)):
                continue
            if depth_possible(yes, depth - 1) and depth_possible(no, depth - 1):
                return True
        return False

    return depth_possible, states, universe, patterns, queries, orders


def poset_solver(n):
    full = (1 << n) - 1
    states = Counter()
    strategy = {}

    def add_comparison(reach, left, right):
        """Insert left<right; reach is already transitively closed.

        All predecessors of left gain right and all successors of right.
        Only called for incomparable left,right.
        """
        reach = list(reach)
        successors = reach[right] | (1 << right)
        for x in range(n):
            if x == left or ((reach[x] >> left) & 1):
                reach[x] |= successors
        return tuple(reach)

    @lru_cache(None)
    def extensions(reach):
        predecessor = [0] * n
        for x in range(n):
            for y in range(n):
                if (reach[x] >> y) & 1:
                    predecessor[y] |= 1 << x

        @lru_cache(None)
        def count(placed):
            if placed == full:
                return 1
            total = 0
            for x in range(n):
                if not (placed >> x) & 1 and not (predecessor[x] & ~placed):
                    total += count(placed | (1 << x))
            return total
        return count(0)

    @lru_cache(None)
    def depth_possible(reach, depth):
        states[depth] += 1
        if depth == 0:
            return extensions(reach) > 0
        if extensions(reach) < (1 << depth):
            return False
        for i in range(n):
            for j in range(i + 1, n):
                if ((reach[i] >> j) & 1) or ((reach[j] >> i) & 1):
                    continue
                low = add_comparison(reach, i, j)
                high = add_comparison(reach, j, i)
                if min(extensions(low), extensions(high)) < (1 << (depth - 1)):
                    continue
                if depth_possible(low, depth - 1) and depth_possible(high, depth - 1):
                    strategy[(reach, depth)] = (i, j)
                    return True
        return False

    return depth_possible, states, (0,) * n, add_comparison, extensions, strategy


def build_witness():
    possible, _, root, add, _, strategy = poset_solver(7)
    assert possible(root, 11)
    # Breadth-first full binary tree of depth 11, query at every internal node.
    level = [root]
    output = []
    for depth in range(11, 0, -1):
        next_level = []
        for state in level:
            i, j = strategy[(state, depth)]
            output.append([i + 1, j + 1])
            next_level += [add(state, j, i), add(state, i, j)]
        level = next_level
    assert len(output) == 2047
    assert all(possible(state, 0) for state in level)
    return {'n': 7, 'depth': 11, 'query_pairs_breadth_first': output}


def check_witness(w):
    assert set(w) == {'n', 'depth', 'query_pairs_breadth_first'}
    assert w['n'] == 7 and w['depth'] == 11
    tree = w['query_pairs_breadth_first']
    assert len(tree) == 2047
    orders = list(permutations(range(1, 8)))
    allmask = (1 << len(orders)) - 1
    query_mask = {}
    for i, j in combinations(range(1, 8), 2):
        mask = 0
        for t, order in enumerate(orders):
            if order.index(i) < order.index(j):
                mask |= 1 << t
        query_mask[(i, j)] = mask
    level = [allmask]
    index = 0
    for depth in range(11):
        next_level = []
        for valid_orders in level:
            i, j = tree[index]
            assert i < j and 1 <= i <= 7 and 1 <= j <= 7
            index += 1
            query = query_mask[(i, j)]
            next_level += [valid_orders & (allmask ^ query), valid_orders & query]
        level = next_level
        assert all(level), ('unrealized branch', depth)
    assert index == 2047 and len(level) == 2048
    return len(level), min(x.bit_count() for x in level)


def main():
    # Independent decision procedures and their exact yes/no depth tests.
    desired = [0, 1, 2, 4, 6, 9, 11]
    for n in range(1, 8):
        mask_yes, mask_states, universe, queries_mask, _, _ = mask_solver(n)
        poset_yes, poset_states, root, add, count, _ = poset_solver(n)
        d = desired[n - 1]
        assert mask_yes(universe, d)
        assert not mask_yes(universe, d + 1)
        assert poset_yes(root, d)
        assert not poset_yes(root, d + 1)
        print('n=', n, 'Ldim=', d, 'entropy_upper=', len(list(permutations(range(n)))).bit_length() - 1,
              'mask_states=', sum(mask_states.values()), 'poset_states=', sum(poset_states.values()))
        if n == 7:
            child = add(root, 0, 1)
            assert count(child) == 2520
            assert poset_yes(child, 10) and not poset_yes(child, 11)
            assert mask_yes(universe & queries_mask[0], 10)
            assert not mask_yes(universe & queries_mask[0], 11)
            print('comparison_1_before_2: 2520 linear extensions; rank exactly 10')
    path = Path(__file__).with_name('permutation_comparison_witness.json')
    assert path.exists(), 'The standalone witness must be present beside this checker.'
    w = json.loads(path.read_text(encoding='utf-8'))
    leaves, min_weight = check_witness(w)
    print('PERMUTATION_COMPARISON_7_PASS', 'complete_tree_leaves=', leaves,
          'minimum_number_of_witnessing_permutations=', min_weight)

if __name__ == '__main__':
    main()
