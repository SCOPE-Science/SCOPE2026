#!/usr/bin/env python3
"""Exact finite checks for a family of five-term Lucas-Niven runs."""
from collections import defaultdict


def lucas_values(n):
    vals = [2, 1]
    for _ in range(2, n + 1):
        vals.append(vals[-1] + vals[-2])
    return vals


def greedy_digits(n, vals):
    assert n >= 0
    indices = []
    for i in sorted(range(len(vals)), key=lambda k: vals[k], reverse=True):
        if vals[i] <= n:
            indices.append(i)
            n -= vals[i]
    assert n == 0
    return indices


def legal(indices):
    ss = set(indices)
    return (not (0 in ss and 2 in ss)) and all(abs(i - j) > 1 for i in ss for j in ss if i != j)


def independent_low_enumeration(vals, max_index=17):
    by_value = defaultdict(list)
    def visit(i, prev, selected, total):
        if i > max_index:
            by_value[total].append(tuple(selected))
            return
        visit(i + 1, False, selected, total)
        if not prev and not (i == 2 and 0 in selected):
            selected.append(i)
            visit(i + 1, True, selected, total + vals[i])
            selected.pop()
    visit(0, False, [], 0)
    assert all(len(w) == 1 for w in by_value.values()), "Lucas representation uniqueness failed"
    size = sum(1 for n in range(vals[max_index+1]) if n in by_value)
    assert size == vals[max_index + 1], "Lucas representation completeness failed"
    for n in range(1, min(10001, vals[max_index + 1])):
        assert tuple(sorted(greedy_digits(n, vals))) == by_value[n][0]
    return len(by_value)


def check():
    vals = lucas_values(350)
    assert vals[:9] == [2, 1, 3, 4, 7, 11, 18, 29, 47]
    assert vals[24] % 12 == 2 and vals[25] % 12 == 1
    residues = [i for i in range(24) if vals[i] % 12 == 5]
    assert residues == [7, 13], residues
    low = [[6, 3, 1], [6, 4], [6, 4, 0], [7], [7, 0]]
    low_offsets = [23, 25, 27, 29, 31]
    assert [sum(vals[i] for i in row) for row in low] == low_offsets
    assert [len(row) for row in low] == [3, 2, 3, 1, 2]
    assert all(legal(row) for row in low)
    low_neighbors = [[6, 2], [7, 3]]
    assert [sum(vals[i] for i in row) for row in low_neighbors] == [21, 33]
    assert all(legal(row) for row in low_neighbors)
    independent_size = independent_low_enumeration(vals)
    nclasses = [0, 0]
    for J in range(9, 301):
        H = vals[J]
        observed = [greedy_digits(H + v, vals) for v in [21, *low_offsets, 33]]
        expected = [[J] + row for row in [low_neighbors[0], *low, low_neighbors[1]]]
        assert all(legal(row) for row in expected)
        assert [set(o) for o in observed] == [set(e) for e in expected], J
        checks = [(H + x) % k == 0 for x, k in zip(low_offsets, [4,3,4,2,3])]
        good = J % 24 in [7,13]
        assert all(checks) == good, J
        if good:
            nclasses[0] += 1
            assert (H + 21) % 3 and (H + 33) % 3
        else:
            nclasses[1] += 1
    assert vals[13] + 23 == 544
    assert [vals[13] + x for x in low_offsets] == [544, 546, 548, 550, 552]
    print('VERIFY_OK')
    print('lucas_period_12=24; qualifying_indices_mod_24=[7,13]')
    print('independent_unique_canonical_low_representations', independent_size)
    print('candidate_indices_9_through_300', nclasses[0], 'other_indices', nclasses[1])
    print('first_constructed_run', [544, 546, 548, 550, 552])
    print('classification_for_all_indices_is_proved_by_recurrence_not_finite_checks')

if __name__ == '__main__':
    check()
