#!/usr/bin/env python3
"""Exact state-transfer verification for period-three excitable colorings.

Uses only the Python standard library.  Triangles form an end-to-end
vertex-glued path, with distinguished connectors x_0,...,x_m and private
y_1,...,y_m.  Colors 0,1,2 advance when a successor-colored neighbor exists.
"""

def support(a, b, y):
    # Whether x_left, x_right, and y have a successor-colored neighbor.
    return ((b == (a + 1) % 3 or y == (a + 1) % 3),
            (a == (b + 1) % 3 or y == (b + 1) % 3),
            (a == (y + 1) % 3 or b == (y + 1) % 3))


def initial_counts():
    # Fix the right connector's color to zero by cyclic color symmetry.
    out = [0, 0]
    for a in range(3):
        for y in range(3):
            left_ok, right_ok, private_ok = support(a, 0, y)
            if left_ok and private_ok:
                out[int(right_ok)] += 1
    return out


def transition_counts():
    # Fix the incoming connector's color to zero by cyclic color symmetry.
    result = [[0, 0], [0, 0]]
    for incoming_ok in (0, 1):
        for b in range(3):
            for y in range(3):
                left_ok, right_ok, private_ok = support(0, b, y)
                if private_ok and (incoming_ok or left_ok):
                    result[incoming_ok][int(right_ok)] += 1
    return result


def rec(m):
    assert m >= 1
    a, b = 3, 6
    for _ in range(m - 1):
        a, b = a + 2*b, 2*a + 3*b
    return b


def dynamic(m):
    # Full six-state transfer, independent of the two-state reduction.
    states = [(c, flag) for c in range(3) for flag in (0, 1)]
    v = []
    for b, flag in states:
        n = 0
        for a in range(3):
            for y in range(3):
                left_ok, right_ok, private_ok = support(a, b, y)
                if left_ok and private_ok and int(right_ok) == flag:
                    n += 1
        v.append(n)
    for _ in range(m-1):
        nxt = [0]*len(states)
        for i, (a, old_flag) in enumerate(states):
            for j, (b, new_flag) in enumerate(states):
                n = 0
                for y in range(3):
                    left_ok, right_ok, private_ok = support(a, b, y)
                    if private_ok and (old_flag or left_ok) and int(right_ok)==new_flag:
                        n += 1
                nxt[j] += v[i]*n
        v=nxt
    return sum(v[i] for i, (_, flag) in enumerate(states) if flag)


def main():
    assert initial_counts() == [1, 2], initial_counts()
    assert transition_counts() == [[1, 2], [2, 3]], transition_counts()
    assert [rec(m) for m in range(1, 7)] == [6, 24, 102, 432, 1830, 7752]
    for m in range(1, 101):
        assert rec(m) == dynamic(m), m
        if m >= 3:
            assert rec(m) == 4*rec(m-1)+rec(m-2), m
        assert rec(m) % 3 == 0
    print('PASS: direct local transition enumeration, 6-state/2-state agreement through m=100, recurrence, orbit divisibility')
    print('counts m=1..10:', [rec(m) for m in range(1,11)])


if __name__ == '__main__':
    main()
