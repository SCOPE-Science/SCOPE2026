"""Bounded recovery test: (a,b) reachability under mixed C / Cbar steps.

Model: state = (a, b) where a = 1 iff |B(+M)| > 0, b = 1 iff |B(-M)| > 0.
A C_{Delta=0} step preserves a; a Cbar_{Delta=0} step preserves b
(Ladu Prop 3.2(b) + Lemma 3.3, assuming b^+/b^- >= 2 throughout).
Start (X0): (1, 0). End (X1): (0, 1).
Question: reachable by mixed steps? Result: yes in 2 steps via (1,1) or (0,0).
Hence zero/nonzero cardinalities alone cannot obstruct the union.
"""
from collections import deque

start = (1, 0)
goal = (0, 1)

def neighbors(state):
    a, b = state
    # C-step: keep a, flip-or-keep b arbitrarily (adversarial change allowed)
    # Cbar-step: keep b, change a arbitrarily
    out = set()
    for nb in (0, 1):
        out.add((a, nb))   # C-step
        out.add((nb, b))   # Cbar-step
    return out

def bfs(limit=4):
    seen = {start: 0}
    q = deque([start])
    paths = {start: [start]}
    while q:
        s = q.popleft()
        if seen[s] >= limit:
            continue
        for t in neighbors(s):
            if t not in seen:
                seen[t] = seen[s] + 1
                paths[t] = paths[s] + [t]
                q.append(t)
    return seen, paths

seen, paths = bfs()
print("start:", start, "goal:", goal)
print("distance to goal:", seen.get(goal))
print("path:", paths.get(goal))
print("2-step witnesses: via (1,1):", [(1, 0), (1, 1), (0, 1)],
      "via (0,0):", [(1, 0), (0, 0), (0, 1)])
assert seen.get(goal) == 2
print("CONCLUSION: no elementary cardinality contradiction for mixed sequences.")
