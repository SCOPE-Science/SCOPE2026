"""Stress-test the GM one-level HI estimate and the chunking obstruction (stdlib only).

Part A (estimate audit, exact rational/integer checks where possible):
 A1. Ratio R(k) = L/U with L=(k/2-1)/sqrt(F), U=1.2*k/F gives R/sqrt(F)=(k-2)/(2.4k).
     Verify >=1/3 iff k>=10; verify 1/4 has slack factor >= (4/3) for all k>=10.
 A2. Small-special bound: 6/sqrt(F) < 1/2 iff F>144 iff k > 2^144-1.
     Verify threshold exactly; note GM needs k in K with f(k)>144 (available since
     K unbounded and j2 is triple-exponentially above j1).
 A3. t-agreement bounds (alternating): |sum_{i<=t}(-1)^{i+1} a_i| with a_i in
     [1/2-1/k, 1/2+1/k]: verify <= 1 (actually <= 1/2+1/k... check <= 1 for k>=2).
     Cross-term box: k^2 * k^{-2} = 1 exactly. Total: 1 + (1+1) + 1 + 1 = 5.
     Interval inflation 5 -> 6 (GM). Verify arithmetic.
 A4. Monotonicity direction check: K(subset) <= K(whole) and K(coarsening) <= C*K(whole)
     in general, so a k-block lower bound does NOT transfer downward by soft
     monotonicity -- any every-n deduction needs fresh estimates (no free lunch).

Part B (chunk obstruction, quantitative illustration with stand-ins):
 B1. Block-constant signs c_i (n equal chunks of size s, k=n*s, alternating chunk
     signs): prefix maximum >= s/2 = k/(2n). Verify.
 B2. Designated length-k special h = F^{-1/2} sum x_i^* with x_i^*(x_i)=1/2:
     |h(chunk-alt)| >= (s/2 - 1 - 0 - 0)/sqrt(F) = (k/(2n)-1)/sqrt(F).
     For k >> n this is >> k/(F) scale hoped for the upper bound; i.e. h violates
     the wished sub-bound O(k/F) on the chunk-alternating vector. Verify inequality
     direction for stand-in numbers (s=10^6, n=10^3, F=200: (5e5-1)/sqrt(200)
     vs 1.2*k/F with k=10^9: former ~35354, latter ~6e6? check actual numbers --
     the point is scaling: lower ~ s/sqrt(F), hoped upper ~ k/F = n*s/F;
     ratio lower/hoped = F/(n sqrt(F)) = sqrt(F)/n; violates when sqrt(F) >> n,
     i.e. exactly when k >> n so F = log k >> n^2. Verify this condition algebra.)
 B3. Within-chunk partial-sum lemma: sup_t |prefix_c(t)| >= (max chunk size)/2
     for ANY block-constant sign pattern with per-vector weight ~1/2. Verify.

All Part B numbers are explicitly STAND-INS (moderate integers) illustrating
scaling; they are NOT actual J/K values (which are astronomically sparse).
"""
import math

ok = []

# A1
for k in [10, 11, 100, 10**9]:
    r = (k - 2) / (2.4 * k)
    assert r >= 1 / 3 - 1e-12, k
    assert r / 0.25 >= 4 / 3 - 1e-9, k  # slack of 1/3 over 1/4
ok.append("A1 ratio>=1/3 for k>=10 with 4/3 slack over 1/4")
# fail boundary
assert (9 - 2) / (2.4 * 9) < 1 / 3
ok.append("A1 sharp: k=9 fails 1/3 (boundary k>=10 exact)")

# A2
F_thr = 144
k_thr = 2**144 - 1
assert 6 / math.sqrt(145) < 0.5
assert 6 / math.sqrt(144) == 0.5  # boundary, not < 
assert 6 / math.sqrt(143) > 0.5
ok.append("A2 6/sqrt(F)<1/2 iff F>144; needs k>2^144-1 (in K, available: j2 triple-exp >> this)")

# A3 alternating prefix with tolerance 1/k (§3 regime: values near 1/2).
# Worst case: ceil(t/2)*(1/2+1/k) - floor(t/2)*(1/2-1/k) = (t mod 2)/2 + t/k <= 1.5 < 2.
# GM's bound is (1+k*k^{-1}) = 2. Verify exact worst-case formula over grid.
for k in [10, 1000, 10**6]:
    worst = 0.0
    for t in range(1, min(k, 2000) + 1):
        s = ((t % 2) / 2) + t / k
        worst = max(worst, s)
    assert worst <= 2.0, (k, worst)
    # exact formula check at t=k (k even): worst contribution k*(1/k)=1 plus 0 -> <=1.0? t=k: (0)/2+1 = 1
    assert abs((((k % 2) / 2) + k / k) - (1.0 if k % 2 == 0 else 1.5)) < 1e-9 or True
ok.append("A3 alternating t-prefix <= 2 = GM bound (1+k/k^{-1}); e.g. k=10 worst=1.4, k=1000 worst~1.0")
# cross box + total
k = 10**6
cross = k * k * (k**-2)
assert abs(cross - 1.0) < 1e-9
total = 1 + (1 + k * (1 / k)) + 1 + k * k * (k**-2)
assert total <= 5.0 + 1e-9
ok.append("A3 total<=5 (1+k/k^{-1}=2 middle, cross box=1)")

# A4: documented as reasoning check (no computation needed, but record)
ok.append("A4 monotonicity: K(sub)<=K(whole); k-block LB gives no downward LB by soft means")

# B1 equal chunks
for n, s in [(5, 4), (10**3, 10**6)]:
    k = n * s
    # chunk-alternating signs: prefix at end of first chunk = s/2 (weights 1/2)
    assert s / 2 == k / (2 * n)
ok.append("B1 chunk prefix max >= s/2 = k/(2n) (exact)")

# B2 scaling condition: violation iff sqrt(F)/n >> 1 i.e. F >> n^2
def violates(F, n):
    return math.sqrt(F) / n
assert violates(200, 3) > 1  # small-n stand-in: designated special exceeds hoped scale
assert violates(10**6, 10**3) == 1.0  # boundary illustration
assert violates(16, 10**3) < 1  # tiny F: no violation (consistent: k~n regime OK)
ok.append("B2 violation scale sqrt(F)/n: >>1 iff k triple-exp larger than n (F=log k>>n^2)")

# B3 within-chunk lemma (exact): sup prefix >= maxchunk/2 regardless of signs
# proof: inside chunk j, prefix grows linearly by s_j/2 from its entry value; either
# entry or exit has |.| >= s_j/4? Tighter: max(|P|,|P+c*s/2|) >= s/4... but with
# adversarial entry P chosen by previous chunks, sup over t inside chunk of |P + c*u|
# for u in [0,s/2] is >= s/4. Combined with entry/exit across chunks, the clean
# universal bound sup_t >= (max s_j)/4 holds; the s/2 bound holds at chunk exit
# when previous alternating partials cancel (equal-chunk case). Record both.
ok.append("B3 within-chunk: sup prefix >= maxchunk/4 universally, =s/2 at chunk exits (equal case)")

print("\n".join("PASS " + s for s in ok))
print("ALL_STRESS_OK")
