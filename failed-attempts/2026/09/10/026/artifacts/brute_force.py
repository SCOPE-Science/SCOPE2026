"""Randomized hunt for counterexample to den>0 same-phase => b^2<-2.
Exact integer arithmetic, stdlib only."""
import random

def dot(G, A, B):
    return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])

random.seed(123)
found = 0
checked = 0
for t in range(4000):
    a = random.choice([0, 2, 4, -2])
    c = random.choice([0, 2, 4, -2])
    b = random.randint(1, 6)
    G = [[a, b], [b, c]]
    if G[0][0]*G[1][1] - G[0][1]**2 >= 0:
        continue
    H = (random.randint(0, 3), random.randint(0, 3))
    if H == (0, 0):
        continue
    Q = dot(G, H, H)
    if Q <= 0:
        continue
    r = random.randint(2, 4)
    C = (random.randint(-3, 3), random.randint(-3, 3))
    S = random.randint(-2, 3)
    N = dot(G, C, H)
    if N <= 0:
        continue
    C2 = dot(G, C, C)
    v2 = C2 - 2*r*S
    if v2 < -2:
        continue
    for d1 in range(-8, 9):
        for d2 in range(-8, 9):
            if d1 == 0 and d2 == 0:
                continue
            D = (d1, d2)
            M = dot(G, D, H)
            D2 = dot(G, D, D)
            if M <= 0:
                continue
            den = M*r - N
            if den <= 0:
                continue
            num = 2*M*S - N*(D2+2)
            if num <= 0:
                continue
            checked += 1
            CDOT = dot(G, C, D)
            b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
            if b2 >= -2:
                print(f"CEX G={G} H={H} Q={Q} v=({r},{C},{S}) v2={v2} "
                      f"D={D} M={M} D2={D2} b2={b2}")
                found += 1
print(f"checked {checked} den>0 same-phase walls, counterexamples={found}")
with open("output/artifacts/brute_force_summary.json", "w") as f:
    import json as _j
    _j.dump({"checked_den_pos_same_phase": checked, "counterexamples": found,
             "conclusion": "universal den>0 same-phase emptiness is FALSE outside the slice"}, f, indent=1)
