"""Separate exact verifier using erasure shadows and base-three integer states.

Usage: python3 alternate.py   (run beside cert5.json and cert7.json)
"""
import json
from pathlib import Path


def decode(v, n):
    x = []
    for j in range(n):
        x.append(v % 3)
        v //= 3
    return tuple(x)


def encode(word):
    return sum(int(symbol) * 3 ** i for i, symbol in enumerate(word))


def distinguishable(c):
    # Erasing one known coordinate gives one punctured signature per position.
    for i in range(len(c[0])):
        observed = [x[:i] + x[i + 1:] for x in c]
        assert len(set(observed)) == len(observed)


def check(n, max_size, cycle_count):
    f = Path(__file__).resolve().parent / ('cert%d.json' % n)
    d = json.loads(f.read_text(encoding='utf8'))
    all_states = {v for v in range(3 ** n) if all(
        decode(v, n)[j] != decode(v, n)[j + 1] for j in range(n - 1))}
    assert len(all_states) == 3 * 2 ** (n - 1)
    code = d['codewords']
    assert len(code) == max_size
    distinguishable(code)
    cyclic = [tuple(map(encode, c)) for c in d['odd_cycles']]
    assert len(cyclic) == cycle_count
    matched = [tuple(map(encode, e)) for e in d['paired_edges']]
    assert len(set(sum((list(c) for c in cyclic), []) + sum((list(e) for e in matched), []))) == len(all_states)
    seen = set()
    for cyc in cyclic:
        assert len(cyc) % 2 == 1
        for i, v in enumerate(cyc):
            w = cyc[(i + 1) % len(cyc)]
            assert sum(a != b for a, b in zip(decode(v, n), decode(w, n))) == 1
            assert v not in seen
            seen.add(v)
    for a, b in matched:
        assert a not in seen and b not in seen
        assert sum(x != y for x, y in zip(decode(a, n), decode(b, n))) == 1
        seen.add(a); seen.add(b)
    assert seen == all_states
    assert sum(len(c)//2 for c in cyclic) + len(matched) == max_size
    print('ERASURE_AND_COVER_OK', n, len(all_states), max_size)


if __name__ == '__main__':
    check(5, 23, 2)
    check(7, 92, 8)
    print('ALTERNATE_OK')
