"""S1: exact brec DP, density limit gamma=2sqrt3-3, supersolution check, error growth."""
import math
from math import comb
N = 3000
b = [0]*(N+1); ch = [0]*(N+1)
for n in range(3, N+1):
    best = -1; ba = 0
    for a in range(n+1):
        v = comb(a, 2)*(n-a) + b[n-a]
        if v > best: best = v; ba = a
    b[n] = best; ch[n] = ba
gamma = 2*math.sqrt(3)-3
print("gamma =", gamma)
for n in [7, 8, 10, 20, 50, 100, 500, 1000, 2000, 3000]:
    print(f"n={n} brec={b[n]} C(n,3)={comb(n,3)} ratio={b[n]/comb(n,3):.6f} a*={ch[n]}")
# error e(n) = brec(n) - gamma*C(n,3): check O(n^2) with constant
print("\ne(n)=brec-gamma*C(n,3), e(n)/n^2:")
for n in [50, 100, 500, 1000, 2000, 3000]:
    e = b[n]-gamma*comb(n, 3)
    print(f"n={n} e={e:.1f} e/n^2={e/n**2:.5f}")
# supersolution check: gamma*C(n,3) >= C(a,2)*(n-a)+gamma*C(n-a,3) for all a<n<=N?
import numpy as np
worst = -1e99; worstt = None
for n in range(3, 501):
    Gn = gamma*comb(n, 3)
    for a in range(0, n):
        lhs = comb(a, 2)*(n-a)+gamma*comb(n-a, 3)
        d = lhs-Gn
        if d > worst: worst = d; worstt = (n, a)
print("\nmax deficit C(a,2)(n-a)+gamma*C(n-a,3)-gamma*C(n,3) over n<=500:", worst, worstt)
