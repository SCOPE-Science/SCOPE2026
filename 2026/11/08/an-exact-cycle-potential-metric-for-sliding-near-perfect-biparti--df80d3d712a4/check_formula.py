"""Independent breadth-first validation of the cyclic-distance potential.
This program is scientific verification code for matchings of balanced bicliques.
"""
from collections import Counter, deque
from math import factorial

def potential(state):
    n = len(state)
    root = n - 1
    hole = state.index(-1)
    missing = (set(range(n)) - set(state)).pop()
    perm = list(state)
    perm[hole] = missing
    seen = set()
    score = 0
    for v in range(n):
        if v in seen:
            continue
        cyc = []
        w = v
        while w not in seen:
            seen.add(w)
            cyc.append(w)
            w = perm[w]
        if len(cyc) > 1:
            score += len(cyc) - 1 + (0 if root in cyc else 2)
    if hole != root and perm[hole] == hole:
        score += 2
    return score

def neighbours(state):
    n = len(state)
    hole = state.index(-1)
    missing = (set(range(n)) - set(state)).pop()
    for row, col in enumerate(state):
        if col == -1:
            continue
        nxt = list(state)
        nxt[hole] = col
        nxt[row] = -1
        yield tuple(nxt)
        nxt = list(state)
        nxt[row] = missing
        yield tuple(nxt)

def main():
    for n in range(2, 9):
        start = tuple(range(n - 1)) + (-1,)
        distances = {start: 0}
        q = deque([start])
        spectrum = Counter()
        while q:
            state = q.popleft()
            d = distances[state]
            assert potential(state) == d, (n, state, potential(state), d)
            spectrum[d] += 1
            nb = list(neighbours(state))
            assert len(nb) == 2 * (n - 1) and len(set(nb)) == len(nb)
            for next_state in nb:
                assert abs(potential(next_state) - d) == 1
                if next_state not in distances:
                    distances[next_state] = d + 1
                    q.append(next_state)
        assert len(distances) == n * n * factorial(n - 1)
        assert max(spectrum) == 3 * n // 2 - 1
        print(f'PASS n={n} states={len(distances)} diameter={max(spectrum)} layers={dict(sorted(spectrum.items()))}', flush=True)

if __name__ == '__main__':
    main()
