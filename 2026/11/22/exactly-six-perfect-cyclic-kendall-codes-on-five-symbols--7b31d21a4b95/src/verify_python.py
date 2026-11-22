#!/usr/bin/env python3
"""Exact certificate for perfect cyclic-adjacent-swap codes on five symbols.

Only the Python standard library is needed.  Full search, not sampling.
"""
from itertools import permutations
from collections import Counter

U = tuple(permutations(range(5)))
position = {w: i for i, w in enumerate(U)}
assert len(U) == 120

# Construct each closed radius-one ball by performing each possible swap.
ball = []
incidence = [[] for _ in U]
for i, word in enumerate(U):
    recipients = {i}
    for j in range(5):
        changed = list(word)
        changed[j], changed[(j + 1) % 5] = changed[(j + 1) % 5], changed[j]
        recipients.add(position[tuple(changed)])
    assert len(recipients) == 6
    mask = sum(1 << j for j in recipients)
    ball.append(mask)
    for j in recipients:
        incidence[j].append(i)
assert all(len(candidates) == 6 for candidates in incidence)

# Select identity as one center.  Every solution can be relabeled to do this.
all_vertices = (1 << 120) - 1
visited_by_depth = Counter()
dead_ends = 0
solutions = []

def exact_cover(covered, centers):
    global dead_ends
    visited_by_depth[len(centers)] += 1
    if covered == all_vertices:
        assert len(centers) == 20
        solutions.append(frozenset(centers))
        return
    eligible = None
    # Choose the first uncovered vertex with the fewest compatible centers.
    for v in range(120):
        if (covered >> v) & 1:
            continue
        opts = [j for j in incidence[v] if ball[j] & covered == 0]
        if not opts:
            dead_ends += 1
            return
        if eligible is None or len(opts) < len(eligible):
            eligible = opts
            if len(opts) == 1:
                break
    assert eligible is not None
    for j in eligible:
        exact_cover(covered | ball[j], centers + (j,))

exact_cover(ball[position[(0, 1, 2, 3, 4)]], (position[(0, 1, 2, 3, 4)],))
assert sum(visited_by_depth.values()) == 41
assert dead_ends == 4
assert len(solutions) == 1
assert visited_by_depth[20] == 1

# Identify the only normalized solution as the order-20 affine subgroup.
H = frozenset(tuple((a * x + b) % 5 for x in range(5))
              for a in range(1, 5) for b in range(5))
assert len(H) == 20
assert frozenset(U[i] for i in solutions[0]) == H

# Check all cosets via all permutations of symbol values, independently
# verifying disjoint balls and exhaustion for each labeled codebook.
cosets = set()
for f in U:
    C = frozenset(tuple(f[w[i]] for i in range(5)) for w in H)
    cosets.add(C)
assert len(cosets) == 6
for C in cosets:
    assert len(C) == 20
    masks = [ball[position[w]] for w in C]
    occupied = 0
    for mask in masks:
        assert not (occupied & mask)
        occupied |= mask
    assert occupied == all_vertices
assert sum((0, 1, 2, 3, 4) in C for C in cosets) == 1

print('n_permutations=120; ball_size=6')
print('normalized_exact_cover_nodes=41; dead_ends=4; normalized_solutions=1')
print('all_codebooks=6; each_is_a_20_word_affine_coset; PASS')
print('depth_node_counts=', sorted(visited_by_depth.items()))
