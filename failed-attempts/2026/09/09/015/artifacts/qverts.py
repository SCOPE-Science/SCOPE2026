"""Exact vertex enumeration of Q(C5) = {x>=0, x_i+x_{i+1}<=1, sum<=2}.
Enumerate all basic points: choose 5 tight constraints from 11, solve exactly."""
from fractions import Fraction
import itertools, json

n = 5
# constraints as (a, b) meaning a.x <= b
cons = []
for i in range(5):
    a = [0]*5; a[i] = -1  # -x_i <= 0
    cons.append((a, 0, f"x{i}>=0"))
for i in range(5):
    a = [0]*5; a[i] = 1; a[(i+1) % 5] = 1
    cons.append((a, 1, f"edge{i}-{((i+1)%5)}"))
cons.append(([1]*5, 2, "odd-hole sum<=2"))

def solve5(rows, rhs):
    # Gaussian elimination exact
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

def feasible(x):
    return all(sum(Fraction(cons[k][0][j])*x[j] for j in range(5)) <= cons[k][1] for k in range(11))

pts = {}
for combo in itertools.combinations(range(11), 5):
    rows = [cons[k][0] for k in combo]; rhs = [cons[k][1] for k in combo]
    x = solve5(rows, rhs)
    if x is None or not feasible(x):
        continue
    key = tuple(x)
    pts.setdefault(key, combo)

print("n_vertices_Q:", len(pts))
for p in sorted(pts):
    print([float(v) for v in p], [str(v) for v in p])
frac = [p for p in pts if any(v.denominator != 1 for v in p)]
print("fractional_count:", len(frac))
json.dump({"verts": [[str(v) for v in p] for p in sorted(pts)]}, open("Qverts.json", "w"))
