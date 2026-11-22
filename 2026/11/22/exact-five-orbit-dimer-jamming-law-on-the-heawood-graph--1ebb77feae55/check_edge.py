#!/usr/bin/env python3
"""Independent exact-rational edge-conflict recurrence using binary-vector Fano lines."""
from fractions import Fraction
from functools import lru_cache

lines = sorted({tuple(sorted((a, b, a ^ b)))
                for a in range(1, 8) for b in range(a + 1, 8)})
assert len(lines) == 7
edges = sorted((p - 1, j + 7) for j, line in enumerate(lines) for p in line)
assert len(edges) == 21
conflict = [sum(1 << j for j, (x, y) in enumerate(edges)
                if x in (u, v) or y in (u, v)) for u, v in edges]
assert all(m.bit_count() == 5 for m in conflict)

@lru_cache(maxsize=None)
def go(available):
    if available == 0:
        return (Fraction(1),)
    out = {}
    total = available.bit_count()
    for i in range(21):
        if available >> i & 1:
            for k, p in enumerate(go(available & ~conflict[i])):
                out[k + 1] = out.get(k + 1, Fraction(0)) + p / total
    return tuple(out.get(k, Fraction(0)) for k in range(max(out) + 1))

result = {i: p for i, p in enumerate(go((1 << 21) - 1)) if p}
assert result == {5: Fraction(19, 330), 6: Fraction(497, 792),
                  7: Fraction(1247, 3960)}
assert sum(result.values()) == 1
print('PASS independent edge-conflict recurrence:', result,
      'states:', go.cache_info().currsize)
