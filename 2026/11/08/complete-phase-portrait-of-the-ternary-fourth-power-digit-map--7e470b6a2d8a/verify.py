"""Deterministic arithmetic verification of a ternary digit-fourth-power phase portrait."""
from itertools import product

def T(n):
    assert n >= 1
    result = 0
    while n:
        n, digit = divmod(n, 3)
        result += digit ** 4
    return result

states = sorted({a + 16 * b for a in range(5) for b in range(5 - a) if a + b})
expected = {
    1: 1, 2: 16, 3: 1, 4: 2,
    16: 18, 17: 33, 18: 16, 19: 17,
    32: 18, 33: 17, 34: 18, 48: 18,
    49: 19, 64: 18,
}
assert len(states) == 14
assert states == sorted(expected)
assert {n: T(n) for n in states} == expected
assert set(expected.values()) <= set(states)
assert all(T(n) % 2 == n % 2 for n in range(1, 10001))

cycles = set()
for start in range(1, 81):
    history = []
    seen = {}
    n = start
    while n not in seen:
        seen[n] = len(history)
        history.append(n)
        n = T(n)
    cycle = history[seen[n]:]
    normalized = tuple(sorted(cycle))
    cycles.add(normalized)
    assert normalized in {(1,), (16, 18), (17, 33)}

assert cycles == {(1,), (16, 18), (17, 33)}
assert all(3 ** (k - 1) > 16 * k for k in range(5, 101))
print('VERIFIED: complete 14-state image closure and exact edge list')
print('states=' + ','.join(map(str, states)))
print('edges=' + ','.join(f'{x}:{expected[x]}' for x in states))
print('VERIFIED: all inputs 1..80 have only cycles [1], [16,18], [17,33]')
print('VERIFIED: parity on 1..10000 and descent bound 5..100 digits (supporting checks)')
print('INFINITE CLAIM: follows from strict digit-length descent and the 14 transitions, not from sample ranges')
