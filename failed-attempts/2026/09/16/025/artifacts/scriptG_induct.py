"""Script G: compare with complete bipartite-plus B(a,n-a) (one level) sizes;
test whether B_rec is exactly optimal one-level B at small n, and check the
induction-deficit numbers that the upper bound proof must absorb."""
from math import comb
import itertools

def brec_list(N):
    b = [0]*(N+1); ch = [0]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a, 2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch

b, ch = brec_list(40)
print("n: brec, onelevel-max, gap-to-complete")
for n in range(3, 21):
    one = max(comb(a, 2)*(n-a) + comb(n-a, 3) for a in range(n+1))
    print(f"n={n} brec={b[n]} onelevel+complete={one} C3={comb(n,3)}")

# Induction deficit: for upper-bound proof we need, for every partition (X,Y),
# e(H) <= C(|X|,2)|Y| + ex(|Y|) + [non-B triples bounded by O(n^2)].
# Key numeric question: is brec superadditive-deficient, i.e. how big is
# D(n) = max over a of [C(a,2)(n-a) + brec(n-a)] - brec(n)? (=0 by def)
# and how big is the one-step error of gamma*C(n,3) supersolution? (script A showed ~Theta(n^2)?)
# Recompute exactly: deficit of gamma*C(n,3) as supersolution, fit constant.
import math
gamma = 2*math.sqrt(3)-3
print("\nsupersolution slack S(n)=gamma*C(n,3)-max_a[C(a,2)(n-a)+gamma*C(n-a,3)]; S(n)/n^2:")
for n in [10, 20, 50, 100, 200, 500, 1000]:
    m = max(comb(a, 2)*(n-a)+gamma*comb(n-a, 3) for a in range(n+1))
    S = gamma*comb(n, 3)-m
    print(f"n={n} S={S:.2f} S/n^2={S/n**2:.5f}")
