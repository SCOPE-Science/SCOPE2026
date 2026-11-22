#!/usr/bin/env python3
"""Verify specific prescribed-subset synchronization distances by direct BFS."""
from collections import Counter, deque
from itertools import combinations

def images(mask, mapping):
    result = 0
    for i in range(8):
        if mask & (1 << i):
            result |= 1 << mapping[i]
    return result

def distance_and_word(b, initial):
    parents = {initial: (None, '')}
    queue = deque([initial])
    while queue:
        s = queue.popleft()
        if s & (s-1) == 0:
            chars = []
            while parents[s][0] is not None:
                old, ch = parents[s]
                chars.append(ch)
                s = old
            return len(chars), ''.join(reversed(chars))
        for ch, nxt in [('a', ((s << 1) & 255) | (s >> 7)),
                        ('b', images(s,b))]:
            if nxt not in parents:
                parents[nxt] = (s, ch)
                queue.append(nxt)
    return None, None

for label, digits in [('extremal', '11234567'),
                      ('fast_triples_reset28', '22634175'),
                      ('slow_triples_reset28', '11765432')]:
    b = [int(x) for x in digits]
    values = []
    for triple in combinations(range(8), 3):
        d,w = distance_and_word(b, sum(1 << x for x in triple))
        values.append((d, triple, w))
    m = max(d for d,_,_ in values)
    print(label, digits, 'worst_triple', m,
          'hardest', [(s,w) for d,s,w in values if d == m],
          'full_reset', distance_and_word(b,255)[0],
          'triple_distance_hist',sorted(Counter(d for d,_,_ in values).items()))
    if label=='extremal':assert m==37
    if label=='fast_triples_reset28':assert m==12
    if label=='slow_triples_reset28':assert m==24
print('WITNESS_OK')
