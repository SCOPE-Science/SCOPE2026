"""Corroborate the emergent witness-family theorem (elementary Liouville version):
  g=(sqrt5-1)/2 satisfies |k g - l| >= g/2 * 1/k  (i.e. |g-p/k| >= 1/(2 phi k^2)),
  and g/M lies in D_rel(c,1) for c<=1/2, i.e. |k w-l|>=c*w/k.
"""
import math

g = (math.sqrt(5) - 1) / 2
phi = (1 + math.sqrt(5)) / 2

# 1. elementary Liouville bound: min k*|kg-l| should be >= g/2
N = 20000
worst = 1e9
for k in range(1, N + 1):
    lc = int(round(k * g))
    for l in [lc - 2, lc - 1, lc, lc + 1, lc + 2]:
        d = abs(k * g - l)
        if d > 1e-12:
            worst = min(worst, d * k)
print("min k*|kg-l| over k<=%d: %.12f  (elementary theory >= %.12f = g/2)" % (N, worst, g / 2))

# 2. membership g/M in D_rel(c,1) with c=0.5: brute force k<=K, M<=Mmax
c = 0.5
K = 3000
Mmax = 200
viol = 0
for M in range(1, Mmax + 1):
    w = g / M
    for k in range(1, K + 1):
        lstar = int(round(k * w))
        for l in [lstar - 1, lstar, lstar + 1]:
            d = abs(k * w - l)
            if d + 1e-12 < c * w / k:
                viol += 1
print("membership violations (c=0.5, M<=%d, k<=%d): %d" % (Mmax, K, viol))

# 3. vacuity lemma sanity: absolute class needs omega>=c (k=1,l=0)
c0, Qs = 0.01, 5.77e48
print("absolute class: omega>=c=%.3f required; 1/Q*=%.3e -> interval empty: %s" % (c0, 1 / Qs, (1 / Qs) < c0))
