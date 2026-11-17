"""Exact finite orbit census for synchronous threshold-two cyclic dynamics on wheel graphs.
Standard Python 3, no third-party packages. Full state-space enumeration, not sampling.
"""
from collections import Counter
from itertools import product


def advance(state):
    n = len(state) - 1
    hub, rim = state[0], state[1:]
    neighbours = [tuple(range(1, n + 1))]
    for i in range(n):
        neighbours.append((0, 1 + ((i - 1) % n), 1 + ((i + 1) % n)))
    return tuple((state[v] + 1) % 3 if sum(state[w] == (state[v] + 1) % 3 for w in neighbours[v]) >= 2 else state[v] for v in range(n + 1))


def census(n):
    terminal_period = {}
    cycle_lengths = Counter()
    for seed in product(range(3), repeat=n + 1):
        if seed in terminal_period:
            continue
        path = []
        local_positions = {}
        state = seed
        while state not in local_positions and state not in terminal_period:
            local_positions[state] = len(path)
            path.append(state)
            state = advance(state)
        if state in local_positions:
            cycle_len = len(path) - local_positions[state]
            cycle_lengths[cycle_len] += 1
        else:
            cycle_len = terminal_period[state]
        for visited in path:
            terminal_period[visited] = cycle_len
    assert len(terminal_period) == 3 ** (n + 1)
    basin = Counter(terminal_period.values())
    assert cycle_lengths[1] == 3 * (n + 2)
    return cycle_lengths, basin


if __name__ == '__main__':
    for n in range(3, 8):
        cycles, basins = census(n)
        assert cycles == (Counter({1: 3 * (n + 2)}) if n <= 6 else Counter({1: 27, 21: 2})), (n, cycles)
        assert basins == (Counter({1: 3 ** (n + 1)}) if n <= 6 else Counter({1: 6393, 21: 168})), (n, basins)
        print('rim=%d total=%d cycles=%s basins=%s' % (n, 3 ** (n + 1), sorted(cycles.items()), sorted(basins.items())))
    print('FINITE_CENSUS_OK')
