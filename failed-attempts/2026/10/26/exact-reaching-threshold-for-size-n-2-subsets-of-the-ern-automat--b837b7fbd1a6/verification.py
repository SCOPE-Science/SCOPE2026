"""Finite corroboration for the symbolic reaching-threshold proof.

Uses only the Python standard library. It checks all subset images for n=3..10;
this finite check is not the proof for arbitrary n.
"""
from collections import deque
from itertools import combinations


def image(mask, n, letter):
    full = (1 << n) - 1
    if letter == "a":
        return ((mask << 1) & full) | (mask >> (n - 1))
    # b fixes 0,...,n-2 and maps n-1 to 0.
    out = mask & ~(1 << (n - 1))
    if mask & (1 << (n - 1)):
        out |= 1
    return out


def distances(n):
    start = (1 << n) - 1
    dist = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for letter in ("a", "b"):
            nxt = image(state, n, letter)
            if nxt not in dist:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)
    return dist


def check():
    for n in range(3, 11):
        d = distances(n)
        full = (1 << n) - 1
        targets = {}
        for i, j in combinations(range(n), 2):
            target = full & ~(1 << i) & ~(1 << j)
            assert target in d, (n, i, j, "unreachable")
            targets[(i, j)] = d[target]
        maximum = max(targets.values())
        extremizers = [pair for pair, value in targets.items() if value == maximum]
        assert maximum == 2 * n, (n, maximum)
        assert extremizers == [(n - 3, n - 2)], (n, extremizers)
        # The explicit witness b a^(n-1) b a^(n-1) has length 2n.
        state = full
        state = image(state, n, "b")
        for _ in range(n - 1):
            state = image(state, n, "a")
        state = image(state, n, "b")
        for _ in range(n - 1):
            state = image(state, n, "a")
        expected = full & ~(1 << (n - 3)) & ~(1 << (n - 2))
        assert state == expected, (n, state, expected)
    print("VERIFY_OK: exact BFS agrees for n=3..10; symbolic proof covers all n>=3")


if __name__ == "__main__":
    check()
