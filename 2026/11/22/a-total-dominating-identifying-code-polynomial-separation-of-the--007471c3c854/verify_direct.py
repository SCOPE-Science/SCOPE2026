"""Complete independent signature-based census of total dominating identifying codes."""
from collections import Counter
from hashlib import sha256
from itertools import combinations

EXPECTED = {
    "rook": {6: 1056, 7: 5520, 8: 10170, 9: 10800, 10: 7944,
             11: 4368, 12: 1820, 13: 560, 14: 120, 15: 16, 16: 1},
    "shrikhande": {6: 1040, 7: 5584, 8: 10206, 9: 10800, 10: 7944,
                   11: 4368, 12: 1820, 13: 560, 14: 120, 15: 16, 16: 1},
}

def graph(which):
    vertices = [(a, b) for a in range(4) for b in range(4)]
    differences = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    graph_neighbours = []
    for a, b in vertices:
        if which == "rook":
            near = {j for j, (c, d) in enumerate(vertices)
                    if (a, b) != (c, d) and (a == c or b == d)}
        else:
            near = {j for j, (c, d) in enumerate(vertices)
                    if ((c - a) % 4, (d - b) % 4) in differences}
        graph_neighbours.append(near)
    assert all(len(n) == 6 for n in graph_neighbours)
    assert all(len(graph_neighbours[u] & graph_neighbours[v]) == 2
               for u in range(16) for v in range(u + 1, 16))
    return graph_neighbours

def census(which):
    open_nbhd = graph(which)
    closed = [n | {v} for v, n in enumerate(open_nbhd)]
    good = bytearray(1 << 16)
    counts = Counter()
    for size in range(17):
        for chosen in combinations(range(16), size):
            selected = set(chosen)
            if any(not (selected & n) for n in open_nbhd):
                continue
            signatures = [frozenset(selected & n) for n in closed]
            if len(set(signatures)) != 16:
                continue
            mask = sum(1 << u for u in chosen)
            good[mask] = 1
            counts[size] += 1
    assert dict(counts) == EXPECTED[which], (which, counts)
    digest = sha256(good).hexdigest()
    print(which, "polynomial", sorted(counts.items()))
    print(which, "membership_bitmap_sha256", digest)
    return good, counts

if __name__ == "__main__":
    r, rc = census("rook")
    s, sc = census("shrikhande")
    assert len(r) == len(s) == 65536
    assert sum(sc.values()) - sum(rc.values()) == 84
    assert [rc[k] - sc[k] for k in range(6, 9)] == [16, -64, -36]
    assert all(rc[k] == sc[k] for k in range(9, 17))
    print("DIRECT_EXHAUSTIVE_PASS")
