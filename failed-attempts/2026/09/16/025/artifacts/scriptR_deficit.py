"""Script R: upper-bound induction closure — exact deficit + cover-lemma formulation.
R1: exact D(a,b) = brec(a+b) - C(a,2)b - brec(b) over grid; D/n^2 bounded? (need C-term absorbable)
R2: verify envelope F(n)=brec(n)+C n^2 closes: need C(a+b)^2 >= D(a,b) + C b^2 + K(a+b)^2
     i.e. C(2ab+a^2) >= D(a,b) + K n^2. Since D>=0 (brec optimal), find constants.
R3: check ratio a/n range usable (a can be 0..n; D(a,b) worst case?)."""
from math import comb

N = 400
b = [0]*(N+1); ch = [0]*(N+1)
for n in range(3, N+1):
    best = -1; ba = 0
    for a in range(n+1):
        v = comb(a, 2)*(n-a) + b[n-a]
        if v > best: best = v; ba = a
    b[n] = best; ch[n] = ba

print("R1: D(a,b)/n^2 over grid (n=a+b<=400): worst 10")
recs = []
for n in range(3, N+1):
    for a in range(n+1):
        bb = n - a
        D = b[n] - (comb(a, 2)*bb + b[bb])
        recs.append((D/n**2, n, a, D))
recs.sort(reverse=True)
for r, n, a, D in recs[:10]:
    print(f"  D/n^2={r:.5f} n={n} a={a} D={D}")
print("min D/n^2:", min(r[0] for r in recs))

print("R2: envelope check C=1,K=0.1: C(2ab+a^2)-D-Kn^2 >= 0?")
for C, K in [(1.0, 0.1), (0.5, 0.1), (0.3, 0.05)]:
    worst = min(C*(2*a*(n-a)+a*a) - (b[n]-(comb(a,2)*(n-a)+b[n-a])) - K*n*n
                for n in range(3, N+1) for a in range(n+1))
    print(f"  C={C} K={K}: min slack={worst:.1f} closes={worst>=0}")
