"""Exact-cover recurrence for strong odd optimal coloring partitions of S(K_5).
No external libraries. Run: python3 exact_cover_dp.py
"""
from itertools import combinations
from collections import Counter

V = tuple(range(5))
E = tuple(combinations(V, 2))
edge_index = {e: i for i, e in enumerate(E)}
ALL = (1 << len(E)) - 1


def allowable_classes(omitted_vertex):
    """All edge sets of K_4 on V-minus-{omitted_vertex} with degrees 0 or odd."""
    others = [v for v in V if v != omitted_vertex]
    candidate = [e for e in E if omitted_vertex not in e]
    answer = []
    for subset in range(1 << len(candidate)):
        chosen = [candidate[j] for j in range(len(candidate)) if subset >> j & 1]
        deg = Counter(v for e in chosen for v in e)
        if all(x % 2 for x in deg.values()):
            mask = sum(1 << edge_index[e] for e in chosen)
            answer.append((mask, max(deg.values(), default=0) <= 1))
    assert len(answer) == 15
    assert Counter(int(mask.bit_count()) for mask, sq in answer) == {0: 1, 1: 6, 2: 3, 3: 4, 6: 1}
    return answer


def count(all_square=False):
    # States are masks of already covered edges; each of the five colors is processed once.
    state = {0: 1}
    for color in V:
        next_state = {}
        for occupied, ways in state.items():
            for chosen, is_square in allowable_classes(color):
                if (not all_square or is_square) and occupied & chosen == 0:
                    m = occupied | chosen
                    next_state[m] = next_state.get(m, 0) + ways
        state = next_state
    return state.get(ALL, 0)


if __name__ == '__main__':
    print('K5 root edges:', E)
    print('Admissible class sizes: 0:1, 1:6, 2:3, 3:4, 6:1 (per color)')
    print('All strong odd minimum-color partitions:', count(False))
    print('Square-coloring partitions among those:', count(True))
    assert count(False) == 201
    assert count(True) == 6
