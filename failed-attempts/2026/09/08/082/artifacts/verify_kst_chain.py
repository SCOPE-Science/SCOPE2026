"""Replay recorded induction chain + KST ceilings + min-pair feasibility.

All arithmetic is exact integers except explicitly-marked float displays.
Read-only: prints a verification log.
"""
from math import floor, sqrt, comb

print("=== 1. Recorded induction chain a(n)<=floor(a(n-1)*n/(n-2)), base a(40)=127 ===")
a = {40: 127}
for n, prev in [(41, 40), (42, 41), (43, 42)]:
    a[n] = (a[prev] * n) // (n - 2)  # exact floor of positive rationals
    print(f"a({n}) <= floor({a[prev]}*{n}/{n-2}) = floor({a[prev]*n}/{n-2}) = {a[n]}")
assert (a[41], a[42], a[43]) == (133, 139, 145), "chain must replay recorded maxima"
print("CHAIN REPLAYS RECORDED MAXIMA (133,139,145): OK")

print()
print("=== 2. What the chain needs for a strict improvement ===")
for a41 in (133, 132, 131):
    x42 = (a41 * 42) // 40
    print(f"if a(41)<={a41}: a(42)<=floor({a41*42}/40)={x42}")
print("=> chain yields ex(42)<=138 iff ex(41)<=132 (the exact width-one decision).")

print()
print("=== 3. Classical KST real bound m <= n/4*(1+sqrt(4n-3)) ===")
for n in (41, 42, 43):
    real = n / 4 * (1 + sqrt(4 * n - 3))
    print(f"n={n}: KST real ceiling {real:.4f} -> integer <= {floor(real)}")
print("(KST alone is far weaker than recorded 133/139/145: no improvement possible.)")

print()
print("=== 4. Min-pair-sum feasibility (convexity floor) ===")
print("minpair(n,m) = min over degree seqs of sum C(d,2); necessary: minpair <= C(n,2).")

def minpair_and_seq(n, m):
    s = 2 * m
    q, r = divmod(s, n)
    mp = (n - r) * comb(q, 2) + r * comb(q + 1, 2)
    seq = [q + 1] * r + [q] * (n - r)
    return q, r, mp, seq

def pair_sum(seq):
    return sum(comb(d, 2) for d in seq)

def erdos_gallai(seq):
    d = sorted(seq, reverse=True)
    if sum(d) % 2:
        return False
    n = len(d)
    S = [0] * (n + 1)
    for i, x in enumerate(d, 1):
        S[i] = S[i - 1] + x
    for k in range(1, n + 1):
        right = k * (k - 1) + sum(min(x, k) for x in d[k:])
        if S[k] > right:
            return False
    return True

for n, m in [(41, 133), (42, 139), (43, 145), (42, 138), (43, 144), (40, 127)]:
    q, r, mp, seq = minpair_and_seq(n, m)
    cap = comb(n, 2)
    assert sum(seq) == 2 * m and pair_sum(seq) == mp
    assert erdos_gallai(seq), f"balanced seq must be graphic {(n, m)}"
    print(f"n={n} m={m}: balanced {r}x{q+1}+{n-r}x{q}, "
          f"minpair={mp} cap={cap} slack={cap-mp} graphic=True => NOT EXCLUDED")

print()
print("=== 5. Variance-cap values V(n,m) = (n-1) + 2m/n - 4m^2/n^2 ===")
print("V is an UPPER bound on degree variance implied by KST; near-regular seqs have var<1.")
for n, m in [(41, 133), (42, 139), (43, 145)]:
    # exact rational via integers: V = ((n-1)*n*n + 2*m*n - 4*m*m) / n^2
    num = (n - 1) * n * n + 2 * m * n - 4 * m * m
    den = n * n
    q, r, mp, seq = minpair_and_seq(n, m)
    mu_num = 2 * m  # mean = mu_num/n
    # exact variance numerator: sum (n*d - 2m)^2 / n^3 ... var = (1/n)sum d^2 - (2m/n)^2
    s2 = sum(d * d for d in seq)
    # var = (s2*n - 4m^2)/n^2 /... var = s2/n - 4m^2/n^2 = (s2*n - 4m^2)/n^2
    vnum = s2 * n - 4 * m * m
    print(f"n={n} m={m}: V = {num}/{den} = {num/den:.4f}, "
          f"balanced-seq var = {vnum}/{den} = {vnum/den:.4f} << V => no exclusion")
print()
print("CONCLUSION: {sum-to-2m, KST pair-count, variance cap} are jointly satisfiable")
print("with large slack at (41,133),(42,139),(43,145). No argument from these caps alone")
print("can prove ex(42)<=138 or ex(43)<=144.")
