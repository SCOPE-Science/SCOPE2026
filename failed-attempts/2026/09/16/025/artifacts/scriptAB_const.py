"""Script AB: literature-reference values for brec — check: is brec here the same as the
'recursive blow-up of edge {12|3}'-type construction in recent tight-cycle papers?
No search: just record the exact recurrence solution in closed form for the DRAFT:
brec(n) = max over chains of sum C(ai,2)*bi with ni+1 = ni - ai.
Also compute explicit constants: c_star = liminf C(|W|,2)/n^2 along the construction
sequence (measured 0.0233..0.0270) — lower-bound it rigorously: |W|/n -> ?
W = V1^(1): |V2^(0)|/n -> x*=(sqrt3-1)/2≈0.366; |W|/|V2| -> 1-x*≈0.634; so |W|/n ->
0.366*0.634 ≈ 0.232. C(|W|,2)/n^2 -> 0.232^2/2 ≈ 0.0269. Confirm limit arithmetic."""
import math
x = (math.sqrt(3)-1)/2
a = 1 - x
w = x*a
print(f"x*={x:.6f} a*={a:.6f} w*=|W|/n={w:.6f} c*=w*^2/2={w**2/2:.6f}")
# rigorous sandwich: for large n DP splits stay in [0.63,0.64]? check n=100..3000
from math import comb
N = 3000
b = [0]*(N+1); ch = [0]*(N+1)
for n in range(3, N+1):
    best = -1; ba = 0
    for a_ in range(n+1):
        v = comb(a_, 2)*(n-a_) + b[n-a_]
        if v > best: best = v; ba = a_
    b[n] = best; ch[n] = ba
import collections
bad = [(n, ch[n]/n) for n in range(100, N+1) if not (0.62 <= ch[n]/n <= 0.65)]
print("splits outside [0.62,0.65] for n>=100:", bad[:10], "count:", len(bad))
# second-level splits
bad2 = []
for n in range(100, N+1):
    m = n - ch[n]
    if m >= 100 and not (0.62 <= ch[m]/m <= 0.65):
        bad2.append((n, m, ch[m]/m))
print("second-level outside:", bad2[:10], "count:", len(bad2))
# measured surplus constant along even n
for n in [100, 500, 1000, 2000, 3000]:
    m = n - ch[n]; W = ch[m]
    print(f"n={n} |W|={W} C(W,2)/n^2={comb(W,2)/n**2:.6f}")
