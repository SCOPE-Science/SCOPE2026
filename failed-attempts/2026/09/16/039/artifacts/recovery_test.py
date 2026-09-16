"""Bounded recovery test: natural candidate separating families admit O(n^d)
vertical cells, so type-counting / arrangement viewpoints cannot force 2d-2.
We count cells of the standard cylindrical/vertical decomposition and
S_phi(B) types for two concrete semialgebraic families over R:
 (1) d=3 halfspaces  a1 x1 + a2 x2 + x3 >= 0  on a generic grid of parameters;
 (2) point-hyperplane style arrangement cells vs n=|B|.
Prints fitted growth exponents (log-log slope) over available n range.
"""
import itertools, math
import numpy as np

def fit_slope(ns, vals):
    x = np.log(np.array(ns, float)); y = np.log(np.array(vals, float))
    A = np.vstack([x, np.ones_like(x)]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m

# (1) d=3: B = parameters a=(a1,a2) on kxk grid (x3 coeff fixed 1);
# sample points x on grid; count realized sign patterns of a.x'-x3... use
# phi(x;a) := [a1*x1+a2*x2+x3>=0]; types over B = distinct sign vectors
# realized as x varies over a dense sample (proxy: fine grid).
gx = np.linspace(-2, 2, 25)
pts = np.array(list(itertools.product(gx, gx, gx)))
out1 = []
for k in [2, 3, 4, 5, 6, 7, 8]:
    ga = np.linspace(-2, 2, k)
    A = np.array(list(itertools.product(ga, ga)))
    n = len(A)
    # sign matrix: rows pts, cols params
    S = (pts[:, 0][:, None]*A[:, 0][None, :] + pts[:, 1][:, None]*A[:, 1][None, :]
         + pts[:, 2][:, None] >= 0)
    pats = set(map(tuple, S.tolist()))
    out1.append((n, len(pats)))
print("halfspace types (n=|B|, #types):", out1)
print("fitted type exponent:", round(fit_slope([n for n, _ in out1],
      [v for _, v in out1]), 3), "(expect <= d = 3)")

# (2) arrangement cells of n planes in R^3 (generic position): exact formula
# (n^3+5n+6)/6 cells; vertical decomposition size is Theta of that = O(n^3).
def arr3(n): return (n**3 + 5*n + 6)//6
ns = [4, 8, 12, 16, 24, 32]
print("arrangement cells:", [(n, arr3(n)) for n in ns])
print("fitted arrangement exponent:", round(fit_slope(ns, [arr3(n) for n in ns]), 3),
      "(expect -> 3)")

# (3) generic 2d-2 comparison: n^(2d-2) vs n^d at d=3
n = 32
print(f"at d=3,n={n}: n^d={n**3}, n^(2d-2)={n**4}, arrangement={arr3(n)}")
print("CONCLUSION: hyperplane arrangements realize only Theta(n^d) cells,")
print("a full polynomial degree below n^(2d-2); they cannot witness tightness.")
