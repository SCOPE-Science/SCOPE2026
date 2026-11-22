#!/usr/bin/env python3
"""Independent exact census for binary six-mer decycling sets.

Run: python3 verify_independent.py
Uses recursive depth-first cycle checks and a different permutation of necklace orbits.
"""
from collections import Counter

K = 6
N = 1 << K
NEXT = tuple(((u << 1) & (N - 1), ((u << 1) & (N - 1)) | 1) for u in range(N))

def necklace_orbits():
    orbits = []
    unseen = set(range(N))
    while unseen:
        u = min(unseen)
        orbit = []
        while u in unseen:
            unseen.remove(u)
            orbit.append(u)
            u = ((u & 31) << 1) | (u >> 5)
        orbits.append(orbit)
    return orbits

ORBS = sorted(necklace_orbits(), key=lambda o: (-len(o), -min(o)))

def dfs_topology(alive):
    """Return a longest path if acyclic, otherwise None; entirely DFS-based."""
    color = bytearray(N)
    memo = [0] * N

    def dfs(u):
        if color[u] == 1:
            raise ValueError("cycle")
        if color[u] == 2:
            return memo[u]
        color[u] = 1
        best = 1
        for v in NEXT[u]:
            if alive >> v & 1:
                best = max(best, 1 + dfs(v))
        color[u] = 2
        memo[u] = best
        return best

    try:
        longest = 0
        for u in range(N):
            if alive >> u & 1 and not color[u]:
                longest = max(longest, dfs(u))
        return longest
    except ValueError:
        return None

hist = Counter()
accepted = 0
nodes = 0
examples = {}
best_masks = set()

def run(i, alive):
    global accepted, nodes
    nodes += 1
    if i == len(ORBS):
        longest = dfs_topology(alive)
        if longest is None:
            raise AssertionError("partial DAG pruning failed")
        hist[longest] += 1
        accepted += 1
        if longest not in examples:
            examples[longest] = ((1 << N) - 1) ^ alive
        if longest == 13:
            best_masks.add(((1 << N) - 1) ^ alive)
        return
    allbits = sum(1 << u for u in ORBS[i])
    for removed in ORBS[i]:
        added = allbits ^ (1 << removed)
        extended = alive | added
        if dfs_topology(extended) is not None:
            run(i + 1, extended)

def complement_set(mask):
    return sum(1 << (u ^ 63) for u in range(N) if (mask >> u) & 1)

def reversal_set(mask):
    def rev(x):
        y = 0
        for _ in range(K):
            y = (y << 1) | (x & 1)
            x >>= 1
        return y
    return sum(1 << rev(u) for u in range(N) if (mask >> u) & 1)

if __name__ == "__main__":
    run(0,0)
    print("TOTAL", accepted)
    print("SEARCH_NODES", nodes)
    for k in sorted(hist):
        print("PATH", k, hist[k])
    assert accepted == 68288
    assert sum(hist.values()) == accepted
    assert min(hist) == 13 and max(hist) == 26
    seen = set()
    orbit_size_counts = Counter()
    for mask in best_masks:
        if mask in seen:
            continue
        transforms = {mask, complement_set(mask), reversal_set(mask), complement_set(reversal_set(mask))}
        assert transforms <= best_masks
        seen.update(transforms)
        orbit_size_counts[len(transforms)] += 1
    print("OPTIMAL_COUNT", len(best_masks))
    print("OPTIMAL_DIHEDRAL_ORBITS", sorted(orbit_size_counts.items()))
    print("EXAMPLE_OPTIMAL_SET", ",".join(format(u,"06b") for u in range(N) if (examples[13] >> u) & 1))
