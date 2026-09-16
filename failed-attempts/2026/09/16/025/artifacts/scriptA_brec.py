"""Script A: brec DP, density limit, window lemma, B_rec builder + C7 detector."""
import itertools, math, json, sys
from math import comb

def brec_dp(N):
    b = [0]*(N+1); ch = [0]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a,2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch

N = 2000
b, ch = brec_dp(N)
gamma = 2*math.sqrt(3)-3
print("gamma=2sqrt3-3 =", gamma)
for n in [10, 50, 100, 500, 1000, 2000]:
    print(f"n={n} brec={b[n]} C(n,3)={comb(n,3)} ratio={b[n]/comb(n,3):.6f}")
print("optimal splits a(n) for n=3..30:", [ch[n] for n in range(3,31)])
print("ratio a(n)/n for large n:", [(n, round(ch[n]/n,4)) for n in [100,500,1000,2000]])
x_star = (math.sqrt(3)-1)/2
print("theoretical x*=|V2|/n =", x_star, " a*/n =", 1-x_star)

# Window lemma: binary cyclic strings length 7, every length-3 window sums to 0 or 2
good = []
for bits in itertools.product([0,1], repeat=7):
    ok = True
    for i in range(7):
        s = bits[i]+bits[(i+1)%7]+bits[(i+2)%7]
        if s not in (0,2):
            ok = False; break
    if ok: good.append(bits)
print("num binary necklaces (labelled) with all window sums in {0,2}:", len(good))
for g_ in good[:20]: print(g_)
