#!/usr/bin/env python3
"""Independent conflict-graph/2-SAT enumeration of binary-team obstructions."""
from collections import Counter

atoms = [((i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1) for i in range(16)]
red_conflicts = [(i, j) for i in range(16) for j in range(i + 1, 16)
                 if atoms[i][0] == atoms[j][0] and atoms[i][1] != atoms[j][1]]
blue_conflicts = [(i, j) for i in range(16) for j in range(i + 1, 16)
                  if atoms[i][2] == atoms[j][2] and atoms[i][3] != atoms[j][3]]

def is_satisfiable(team):
    # Literal vertex 2*i is true if assignment i belongs to blue; 2*i+1 its negation.
    adj = [[] for _ in range(32)]
    for pairs, polarity in ((red_conflicts, 0), (blue_conflicts, 1)):
        for i, j in pairs:
            if (team & (1 << i)) and (team & (1 << j)):
                a, b = 2 * i + polarity, 2 * j + polarity
                adj[a ^ 1].append(b)
                adj[b ^ 1].append(a)
    # A 2-CNF is unsatisfiable exactly when some variable and its
    # negation belong to the same strongly connected component.
    def reaches(start, target):
        seen = {start}
        stack = [start]
        while stack:
            for nxt in adj[stack.pop()]:
                if nxt == target:
                    return True
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return False
    for i in range(16):
        if (team >> i) & 1:
            if reaches(2*i, 2*i+1) and reaches(2*i+1, 2*i):
                return False
    return True

model = [is_satisfiable(t) for t in range(1 << 16)]
minimal = [t for t in range(1 << 16) if not model[t]
           and all(model[t & ~(1 << i)] for i in range(16) if t & (1 << i))]
print('2-SAT satisfying count', sum(model))
print('2-SAT inclusion-minimal obstructions', Counter(t.bit_count() for t in minimal))
assert sum(model) == 32377
assert Counter(t.bit_count() for t in minimal) == {4:12,5:16,6:96,8:8}
print('VERIFIED')
