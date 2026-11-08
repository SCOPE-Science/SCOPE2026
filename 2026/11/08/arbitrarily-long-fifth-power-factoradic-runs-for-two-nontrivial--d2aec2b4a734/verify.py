#!/usr/bin/env python3
"""Exact verification of fifth-power factoradic attractors and synchronization witnesses.
All computations use Python integers; this program has no dependencies outside stdlib.
"""

BOUND = 40319
U = (1, 34, 35, 308, 309, 1058, 1059, 2114, 3401)
WITNESSES = ((1373, 34), (75004, 1058))
EXPECTED_CYCLES = ((1,), (34,), (35,), (308,), (309,),
                   (1058,), (1059,), (2114, 3401))


def F(n):
    """Read factoradic digits by successive Euclidean division."""
    assert n >= 0
    i, s = 1, 0
    while n:
        n, digit = divmod(n, i + 1)
        s += digit ** 5
        i += 1
    return s


def rotations_min(cyc):
    t = tuple(cyc)
    return min(t[j:] + t[:j] for j in range(len(t)))


def classify():
    vals = [F(i) for i in range(BOUND + 1)]
    assert all(0 < vals[i] <= 29008 for i in range(1, BOUND + 1))
    state = bytearray(BOUND + 1)  # 0=new; 1=in current path; 2=finished
    cycles = set()
    for start in range(1, BOUND + 1):
        if state[start]:
            continue
        path = []
        pos = {}
        cur = start
        while state[cur] == 0:
            pos[cur] = len(path)
            path.append(cur)
            state[cur] = 1
            cur = vals[cur]
        if state[cur] == 1:
            assert cur in pos
            cycles.add(rotations_min(path[pos[cur]:]))
        for x in path:
            state[x] = 2
    return tuple(sorted(cycles))


def orbit_to(n, target):
    values = [n]
    seen = {n}
    for _ in range(BOUND + 1):
        if n == target:
            return values
        n = F(n)
        if n in seen:
            raise AssertionError('orbit failed to hit target')
        values.append(n)
        seen.add(n)
    raise AssertionError('orbit exceeded bounded state count')


def main():
    actual = classify()
    assert actual == EXPECTED_CYCLES, (actual, EXPECTED_CYCLES)
    assert F(2114) == 3401 and F(3401) == 2114
    for off, target in WITNESSES:
        assert F(target) == target
        for u in U:
            chain = orbit_to(off + u, target)
            assert chain[-1] == target
            assert all(F(a) == b for a, b in zip(chain, chain[1:]))
            print(f'witness={off}, target={target}, u={u}, steps={len(chain)-1}, chain={",".join(map(str,chain))}')
    print('cycles=' + ';'.join(','.join(map(str,c)) for c in actual))
    print('checked_initial_states=40319')
    print('verification=PASS')


if __name__ == '__main__':
    main()
