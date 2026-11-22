"""Exact finite witnesses for prime-count dynamics on labeled tournaments.
Code bit for pair i<j: 1 means i->j, 0 means j->i.
"""

def update(n, code, state):
    incoming = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if code & (1 << bit):
                incoming[j] |= 1 << i
            else:
                incoming[i] |= 1 << j
            bit += 1
    return sum(1 << j for j in range(n) if (incoming[j] & state).bit_count() in (2, 3, 5))


def orbit(n, code, seed):
    visited = {}
    states = []
    s = seed
    while s not in visited:
        visited[s] = len(states)
        states.append(s)
        s = update(n, code, s)
    return visited[s], states[visited[s]:], states


if __name__ == '__main__':
    witness_periods = {1: (0, 0), 2: (1080, 63), 3: (664, 31),
                       4: (1329, 59), 5: (1332, 55), 6: (1336, 15),
                       7: (9780, 7), 8: (1208, 23), 9: (9393, 15)}
    for period, (code, state) in witness_periods.items():
        prefix, cycle, _ = orbit(7, code, state)
        assert prefix == 0 and len(cycle) == period, (period, code, state, cycle)
    prefix, cycle, states = orbit(6, 344, 31)
    assert prefix == 0 and len(cycle) == 3 and cycle == [31, 47, 61]
    prefix, cycle, states = orbit(7, 1721, 86)
    assert prefix == 23 and len(cycle) == 1 and cycle == [0]
    assert states == [86, 46, 13, 3, 96, 28, 7, 98, 60, 15, 99, 124,
                      27, 110, 61, 31, 111, 127, 115, 118, 54, 14, 1, 0]
    print('All period witnesses and the 23-step transient verified exactly.')
