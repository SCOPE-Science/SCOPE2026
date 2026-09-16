"""Script S: correct induction — the partition must be CHOSEN well (a ~ 0.63n forced by
cover lemma), not adversarial. Quantify: D(a,b)/n^2 near optimal split vs degenerate a=n.
Also: what does cover lemma give? It returns a with BOTH: nonB<=Kn^2 AND a bounded away
from 0,n (else B-part C(a,2)b tiny but then... ). Actually if cover lemma returns a=n
(X=all, B empty since Y empty, nonB = all edges = Theta(n^3)) — violates nonB<=Kn^2 unless
e(H) itself O(n^2). So usable partitions have b=|Y| linear. Check D(a,b) for a/n in [.5,.75]."""
from math import comb
N = 600
b = [0]*(N+1); ch = [0]*(N+1)
for n in range(3, N+1):
    best = -1; ba = 0
    for a in range(n+1):
        v = comb(a, 2)*(n-a) + b[n-a]
        if v > best: best = v; ba = a
    b[n] = best; ch[n] = ba

print("D(a,b)/n^2 restricted to splits near optimum:")
for n in [100, 200, 400, 600]:
    row = []
    for frac in [0.5, 0.55, 0.6, 0.634, 0.7, 0.75, 0.8]:
        a = round(frac*n); bb = n - a
        D = b[n] - (comb(a, 2)*bb + b[bb])
        row.append(f"a/n={frac}:D/n2={D/n**2:.4f}")
    print(f"n={n} " + " ".join(row))
    print(f"   optimal a*={ch[n]} a*/n={ch[n]/n:.4f}")

print("envelope closure on GOOD splits (a/n in [0.5,0.75]) with C,K:")
for C, K in [(0.5, 0.1), (1.0, 0.2), (2.0, 0.2)]:
    worst = 1e18
    for n in range(3, N+1):
        for a in range(int(0.5*n), int(0.75*n)+1):
            bb = n - a
            D = b[n] - (comb(a, 2)*bb + b[bb])
            slack = C*(n*n - bb*bb) - D - K*n*n
            worst = min(worst, slack)
    print(f"  C={C} K={K}: min slack={worst:.1f} closes={worst>=0}")

print("density-stability: e(H)/C(n,3) for near-extremal? brec ratio path (already have).")
print("Also D(a,b) for a/n in [0.5,0.75], n<=600: max D/n^2:")
mx = max((b[n]-(comb(a,2)*(n-a)+b[n-a]))/n**2 for n in range(3,N+1) for a in range(int(.5*n),int(.75*n)+1))
print("  max =", mx)
