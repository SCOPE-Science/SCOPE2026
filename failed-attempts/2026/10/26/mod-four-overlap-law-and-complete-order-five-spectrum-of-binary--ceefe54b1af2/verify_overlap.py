"""Exact order-five binary de Bruijn pair-overlap verifier; Python stdlib only.

Independent full enumerations: 2^14 local wirings on the 32 edge set;
edge-simple Euler circuits rooted at the all-zero edge. Checks their labels,
all unordered pairs and the full distribution of common six-bit factors.
"""
from collections import Counter
from itertools import combinations

K = 5
NUM_EDGES = 1 << K
NUM_VERTICES = 1 << (K-1)


def next_edge(edge, mask):
    v = edge & (NUM_VERTICES - 1)
    inp = edge >> (K - 1)
    outgoing_bit = inp ^ ((mask >> v) & 1)
    return (v << 1) | outgoing_bit


def cycles_by_wiring():
    good = {}
    for free in range(1 << (NUM_VERTICES-2)):
        mask = 1 | (1 << (NUM_VERTICES-1)) | (free << 1)
        visited = 0
        edge = 0
        walk = []
        for _ in range(NUM_EDGES):
            if (visited >> edge) & 1:
                break
            visited |= 1 << edge
            walk.append(edge)
            edge = next_edge(edge, mask)
        if len(walk) == NUM_EDGES and edge == 0:
            good[mask] = tuple(walk)
    return good


def cycles_by_search():
    adj = [tuple(((v<<1)|bit) for bit in (0,1)) for v in range(NUM_VERTICES)]
    out = {}
    def walk(v, visited, path):
        if len(path) == NUM_EDGES:
            if v == 0:
                wiring = 0
                for a,b in zip(path, path[1:]+path[:1]):
                    vertex = a & (NUM_VERTICES-1)
                    assert b >> 1 == vertex
                    if (a >> (K-1)) != (b & 1):
                        wiring |= 1<<vertex
                assert wiring not in out
                out[wiring] = tuple(path)
            return
        for e in adj[v]:
            if not (visited >> e) & 1:
                walk(e&(NUM_VERTICES-1), visited | (1<<e), path+[e])
    walk(0, 1, [0])
    return out


def six_mers(edges):
    assert len(edges) == NUM_EDGES
    return frozenset((a<<1)|(b&1) for a,b in zip(edges,edges[1:]+edges[:1]))


def histogram_by_masks(masks):
    hist = Counter()
    for i,a in enumerate(masks):
        for b in masks[i+1:]:
            intersection = 2*(NUM_VERTICES-(a^b).bit_count())
            hist[intersection] += 1
    return hist


def histogram_by_words(sequences):
    sets = [six_mers(s) for s in sequences]
    hist = Counter()
    for i,a in enumerate(sets):
        for b in sets[i+1:]:
            hist[len(a.intersection(b))] += 1
    return hist

EXPECTED = {
    4:368, 8:27104, 12:254800, 16:710976,
    20:758800, 24:305376, 28:38704,
}
if __name__ == '__main__':
    wired = cycles_by_wiring()
    searched = cycles_by_search()
    assert len(wired) == len(searched) == 2048
    assert set(wired) == set(searched)
    # Independent DFS circuits are not assumed equal as rooted paths: compare directly.
    assert all(wired[m] == searched[m] for m in wired)
    ordered = sorted(wired)
    by_mask = histogram_by_masks(ordered)
    by_word = histogram_by_words([searched[m] for m in ordered])
    assert by_mask == by_word == Counter(EXPECTED)
    assert sum(by_mask.values()) == 2048*2047//2
    for mask, seq in wired.items():
        assert (mask & (1 << 0)) != 0 and (mask & (1 << 15)) != 0
        assert len(six_mers(seq)) == 32
    a,b = next((a,b) for a,b in combinations(ordered,2) if 2*(16-(a^b).bit_count())==4)
    print('PASS: independent Eulerian-wiring and rooted-Euler-DFS enumerations')
    print('Euler circuits modulo rotation: 2048; unordered pairs:', sum(by_mask.values()))
    print('Histogram:', dict(sorted(by_mask.items())))
    print('Witness masks:', hex(a), hex(b))
    print('Witness binary cycles:', ''.join(str(edge>>4) for edge in wired[a]), ''.join(str(edge>>4) for edge in wired[b]))
