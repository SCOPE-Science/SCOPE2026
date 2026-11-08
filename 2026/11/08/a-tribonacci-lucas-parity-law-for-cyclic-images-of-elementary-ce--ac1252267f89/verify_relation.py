"""Exact all-length certificate for cyclic one-step images of ECA 172 and 184.
Only Python standard library is required; all arithmetic is integral.
"""
from collections import deque


def matrices(rule):
    by_label = [0, 0]
    for left in (0, 1):
        for center in (0, 1):
            for right in (0, 1):
                source = 2 * left + center
                target = 2 * center + right
                bit = (rule >> (4 * left + 2 * center + right)) & 1
                by_label[bit] |= 1 << (4 * source + target)
    return by_label


def compose(x, y):
    result = 0
    for i in range(4):
        for j in range(4):
            if (x >> (4 * i + j)) & 1:
                result |= ((y >> (4 * j)) & 15) << (4 * i)
    return result


def automaton(rule):
    label = matrices(rule)
    identity = sum(1 << (5 * i) for i in range(4))
    states = [identity]
    lookup = {identity: 0}
    transitions = []
    for s in states:
        destinations = []
        for b in (0, 1):
            nxt = compose(s, label[b])
            if nxt not in lookup:
                lookup[nxt] = len(states)
                states.append(nxt)
            destinations.append(lookup[nxt])
        transitions.append(tuple(destinations))
    accept = [(s & identity) != 0 for s in states]
    return states, transitions, accept


def sequence(rule, stop):
    states, transitions, accept = automaton(rule)
    count = [0] * len(states)
    count[0] = 1
    values = []
    for n in range(stop + 1):
        values.append(sum(c for c, final in zip(count, accept) if final))
        next_count = [0] * len(states)
        for i, c in enumerate(count):
            if c:
                to0, to1 = transitions[i]
                next_count[to0] += c
                next_count[to1] += c
        count = next_count
    return len(states), values


def check_rule(rule, expected_states, first_four, coefficients):
    # q(T) = T^4 + coefficients[3] T^3 + ... + coefficients[0] I.
    states, values = sequence(rule, expected_states + 4)
    assert states == expected_states, (rule, states)
    assert values[1:5] == first_four
    for j in range(1, states + 1):
        residual = values[j + 4] + sum(
            coefficients[k] * values[j + k] for k in range(4)
        )
        assert residual == 0, (rule, j, residual)
    # Cayley-Hamilton on the state transition matrix gives the same
    # identity for every j>=1, since the first states equations vanish.
    return values


def main():
    a = check_rule(172, 83, [2, 2, 8, 10], [-1, -2, -2, 0])
    b = check_rule(184, 34, [2, 4, 8, 12], [1, 0, 0, -2])
    assert all(b[n] - a[n] == (2 if n % 2 == 0 else 0)
               for n in range(1, min(len(a), len(b))))
    print('PASS: reachable state counts 83 and 34')
    print('PASS: 83 and 34 exact scalar recurrence equations')
    print('PASS: image-count parity identity through common computed range')
    print('Rule 172 first 16:', a[1:17])
    print('Rule 184 first 16:', b[1:17])


if __name__ == '__main__':
    main()
