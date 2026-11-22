"""Independent finite checks for incoming-neighbor NOR on Kautz word digraphs.

Run: python3 kautz_verify.py
Only Python's standard library is required. Exhaustion is used only for
finite test instances; the all-size claims are established analytically.
"""
from collections import Counter
from itertools import product
from random import Random


def word_graph(q, d):
    assert q >= 2 and d >= 1
    alphabet = range(q + 1)
    words = [w for w in product(alphabet, repeat=d)
             if all(a != b for a, b in zip(w, w[1:]))]
    labels = {w: i for i, w in enumerate(words)}
    incoming = []
    for w in words:
        pre = [(a,) + w[:-1] for a in alphabet if a != w[0]]
        incoming.append(tuple(labels[u] for u in pre))
    assert len(words) == (q + 1) * q ** (d - 1)
    assert all(len(v) == q for v in incoming)
    return words, incoming


def step(mask, incoming):
    out = 0
    for i, pre in enumerate(incoming):
        if not any(mask & (1 << j) for j in pre):
            out |= 1 << i
    return out


def theoretical_cumulative(q, d, t):
    """Integer count of inputs reaching the recurrent set by update t."""
    assert 0 <= t <= d
    n = (q + 1) * q ** (d - 1)
    if t == d:
        return 1 << n
    b = 1  # one of two input values makes a depth-zero NOR tree output one
    s = 2
    for _ in range(t):
        b, s = (s - b) ** q, s ** q
    block = q ** (d - t - 1)
    nodes = (q + 1) * block
    return b ** nodes + (s - b) ** nodes + (q + 1) * (b ** block) * ((s - b) ** (q * block))


def theoretical_fixed_basin(q, d):
    b = 1
    s = 2
    for _ in range(d - 1):
        b, s = (s - b) ** q, s ** q
    return (q + 1) * b * (s - b) ** q


def verify_exhaustive(q, d):
    words, incoming = word_graph(q, d)
    n = len(words)
    shells = Counter()
    dest = Counter()
    fixed_states = set()
    cyc_states = set()
    for state in range(1 << n):
        x = state
        for t in range(d + 1):
            x1 = step(x, incoming)
            x2 = step(x1, incoming)
            if x2 == x:
                shells[t] += 1
                if x1 == x:
                    dest[1] += 1
                    fixed_states.add(x)
                else:
                    dest[2] += 1
                    cyc_states.add(x)
                break
            x = x1
        else:
            raise AssertionError('Bound failed: q=%d d=%d state=%d' % (q, d, state))
    assert len(fixed_states) == q + 1
    assert len(cyc_states) == 2
    assert sum(shells.values()) == 1 << n
    assert dest[1] == theoretical_fixed_basin(q, d)
    assert dest[2] == (1 << n) - dest[1]
    cumulative = 0
    for t in range(d + 1):
        cumulative += shells[t]
        assert cumulative == theoretical_cumulative(q, d, t), (q, d, t)
    assert shells[d] > 0  # sharp bound for these small test instances
    print('q=%d d=%d n=%d T_shells=%s fixed_basin=%d oscillator_basin=%d' %
          (q, d, n, [shells[i] for i in range(d + 1)], dest[1], dest[2]))


def verify_samples(q, d, samples=4000):
    words, incoming = word_graph(q, d)
    rng = Random(1729)
    for _ in range(samples):
        x = rng.getrandbits(len(words))
        for t in range(d + 1):
            y = step(x, incoming)
            if step(y, incoming) == x:
                break
            x = y
        else:
            raise AssertionError('Sample failed')
    print('q=%d d=%d random_samples=%d passed' % (q, d, samples))


def main():
    for q, d in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2)):
        verify_exhaustive(q, d)
    verify_samples(3, 3)
    print('all checks passed')


if __name__ == '__main__':
    main()
