"""Vertices of edge-only relaxation Q0(C5) = {x>=0, x_i+x_{i+1}<=1}. Expect fractional vertex (1/2)^5."""
from fractions import Fraction
import itertools, json
n = 5
cons = []
for i in range(5):
    a = [0]*5; a[i] = -1
    cons.append((a, 0))
for i in range(5):
    a = [0]*5; a[i] = 1; a[(i+1) % 5] = 1
    cons.append((a, 1))

def solve5(rows, rhs):
    M = [[Fraction(rows[i][j]) for j in range(5)] + [Fraction(rhs[i])] for i in range(5)]
    for col in range(5):
        piv = next((r for r in range(col, 5) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        for r in range(5):
            if r != col and M[r][col] != 0:
                f = M[r][col] / M[col][col]
                for k in range(col, 6):
                    M[r][k] -= f * M[col][k]
    return [M[i][5] / M[i][i] for i in range(5)]

def feas(x):
    return all(sum(Fraction(cons[k][0][j])*x[j] for j in range(5)) <= cons[k][1] for k in range(10))

pts = {}
for combo in itertools.combinations(range(10), 5):
    x = solve5([cons[k][0] for k in combo], [cons[k][1] for k in combo])
    if x is None or not feas(x):
        continue
    pts.setdefault(tuple(x), combo)
print("n_vertices_Q0:", len(pts))
for p in sorted(pts):
    print([str(v) for v in p], "sum=", sum(p))
half = tuple([Fraction(1, 2)]*5)
print("half_in_Q0:", half in pts)
print("max_c1_sum_Q0:", max(sum(p) for p in pts), " integer_alpha: 2 gap: 1/2")
json.dump({"verts": [[str(v) for v in p] for p in sorted(pts)]}, open("Q0verts.json", "w"))
