# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Digit-restricted order-2 bases for Z_p inside decimal digits {0–4}: impossibility and certified threshold table

## 1. Problem and result

Let p be prime and U(p,10,D)={x∈[0,p−1]: every decimal digit of x lies in D}.
For D₄={0,1,2,3,4} and p=197,
U={0,1,2,3,4,10,11,12,13,14,20,21,22,23,24,30,31,32,33,34,40,41,42,43,44,
100,101,102,103,104,110,111,112,113,114,120,121,122,123,124,130,131,132,133,134,140,141,142,143,144},
|U|=50 (25 below 100, 25 in [100,144]). For A⊆U put S(A)={(a+b) mod p:a,b∈A}.
A is an order-2 digit-restricted basis if S(A)=Z_p. Unordered-pair counting gives
|A|(|A|+1)/2≥p, so for p=197, |A|≥20 since 19·20/2=190<197≤210=20·21/2.

**Assigned target.** Find A⊆U(197,D₄) with |A|≤22 (stretch 21) and S(A)=Z_197.

**Outcome (refutation + replacement).** No such A exists — indeed no A of *any* size exists —
for any of p∈{173,179,181,191,193,197} with D∈{{0,1,2},{0,1,2,3},{0,1,2,3,4}}.
We prove this in two tiers and publish the certified threshold/maximal-coverage table
with best heuristic sets. What was meant as an upper-bound construction becomes a
non-existence theorem with explicit maximal-coverage records.

- **Theorem A (interval-gap; pure proof).** For p∈{191,193,197}, no A⊆U(p,10,D₄) satisfies S(A)=Z_p.
- **Theorem B (exact full-universe certificate).** For p∈{173,179,181} (D₂,D₃,D₄) and for all six p with D₂/D₃,
  the full universe itself fails: |S(U)|<p (table below), hence no subset covers. For D₂ this already
  follows from counting 18·19/2=171<p.
- **Computed records (existence, verified; optimality not claimed).** Best annealed k-sets and greedy
  baselines with explicit sets and coverage fractions (e.g. best 22-set for p=197 covers 163/197;
  full-U maximum is 173/197).

## 2. Proof of Theorem A

U(D₄)⊆[0,44]∪[100,144] regardless of p (all elements ≤144). Hence for any A⊆U, integer
(pre-mod) sums lie in I₁∪I₂∪I₃ with I₁=[0,88], I₂=[100,188], I₃=[200,288].
Fix residue r∈[0,p−1]. Its integer representatives are r+kp. Since p≥173, r+2p≥346>288,
only r (k=0) and r+p (k=1) can lie in the feasible union. Moreover r≤196<200 so r∉I₃.
Thus a necessary condition for coverage is r∈I₁∪I₂ or r+p∈I₂∪I₃.

- p=197: r∈I₁∪I₂ gives [0,88]∪[100,188]; r+197∈I₂ impossible (≥197>188);
  r+197∈I₃ ⇔ r∈[3,91]. Union: [0,91]∪[100,188]. Missing: **92–99, 189–196 (16 residues)**.
- p=193: union [0,95]∪[100,188]. Missing: 96–99, 189–192 (8 residues).
- p=191: union [0,97]∪[100,188]. Missing: 98,99,189,190 (4 residues).
Each missing residue is uncovered by every A. Since at least one residue is missing,
S(A)≠Z_p. ∎

Consequence: for p=197 any A misses ≥16 residues, so |S(A)|≤181; the true ceiling is
tighter (173, see §3) because U is not interval-contiguous.

## 3. Proof of Theorem B (machine-checked exact enumeration)

For the remaining cases the interval condition permits coverage, so we enumerate S(U)
in exact integer arithmetic: all |U|² modular sums. If |S(U)|<p, no A⊆U can cover since
S(A)⊆S(U). Results (|S(U)|/p):

| p | D₂ (|U|=18) | D₃ (\|U\|=32) | D₄ (\|U\|=50) | tri lb |
|---|---|---|---|---|
| 173 | 71 (0.410) | 131 (0.757) | 165 (0.954) | 19 |
| 179 | 63 (0.352) | 117 (0.654) | 171 (0.955) | 19 |
| 181 | 63 (0.348) | 117 (0.646) | 171 (0.945) | 19 |
| 191 | 59 (0.309) | 111 (0.581) | 179 (0.937) | 20 |
| 193 | 67 (0.347) | 123 (0.637) | 177 (0.917) | 20 |
| 197 | 65 (0.330) | 119 (0.604) | 173 (0.878) | 20 |

In every cell |S(U)|<p (rerun `python3 artifacts/verify_cover.py`, <2s). For D₂ the weaker
counting bound already suffices: unordered pairs 18·19/2=171<173≤p. ∎

Density reading: D₂ impossible by counting; D₃ tight-in-counting (32·33/2=528≫p) but
loose-in-geometry (~60–76% max); D₄ loose in counting (1275) yet capped at ~88–95% by geometry.

## 4. Heuristic search actually performed (for the record, and upper bounds)

Cost c(A)=p−|S(A)|, exact integer arithmetic. Annealing over k-subsets with swap moves,
geometric schedule T₀=2.0→T_min=0.01, 20 restarts×200k steps for the main targets
(seeds 1000–1019 for k=22, 2000–2019 for k=21), 8×80k for companions; then greedy
completion (add max-gain element until stall) and pruning. Code: `artifacts/sa_search.py`.

Main outcomes for p=197, D₄:
- k=22: **all 20 restarts reached 163/197 (cost 34)**. Example best set
  A*=[0,1,4,14,20,21,32,34,40,41,44,100,103,104,110,112,123,124,130,140,143,144];
  missing 34 residues incl. all 16 forced ones. Greedy completion of A* reaches the
  full-U ceiling 173 with 26 elements (better than greedy-from-empty mean 29.6).
- k=21 (stretch): best 159/197, e.g. [0,1,4,22,24,30,32,40,41,44,100,103,104,110,112,114,131,133,140,143,144].
- k=20: best 153/197.

Triangular-size bests (verified by recomputation; full list in `threshold_table.json`):
p173: D₃k19→122, D₄k19→145; p179: 114, 145; p181: 114, 145; p191: D₃k20→111 (=ceiling),
D₄k20→155; p193: 121, 157; p197: D₃k20→119 (=ceiling with only 20!), D₄k20→153.

Greedy-from-empty baseline (50 seeds 10000–10049 per cell; `artifacts/greedy_baseline.py`);
greedy always saturates at the |S(U)| ceiling above. Mean lengths to ceiling:
p197 D₄ 29.6 (min 27, max 32); p197 D₃ 22.9 (21–26); p173 D₄ 28.2; p179 D₄ 29.3;
p181 D₄ 29.5; p191 D₄ 29.5; p193 D₄ 29.5. So even reaching the (incomplete) ceiling
needs ~27–32 elements — far above the triangular 20 — quantifying the digit penalty.

## 5. How to reproduce (runtime)

```
python3 artifacts/enumerate_U.py     # universe sizes, triangular bounds, full-U fractions
python3 artifacts/verify_cover.py    # all impossibility certificates (PASS, <60s)
python3 artifacts/greedy_baseline.py # 50-run greedy table
python3 artifacts/sa_search.py --p 197 --dmax 4 --k 22 --restarts 20 --steps 200000 --seed0 1000 --out artifacts/sa_p197_D4_k22.json
```
All sums use integer `(a+b)%p` only; no floats. Seeds, sets, and scripts are saved.

## 6. Status of each statement (proof vs evidence vs conjecture)

- **Proved:** Theorems A and B (deductive + exact-enumeration certificates). The positive
  target "∃A, |A|≤22, S(A)=Z_197" is **false**.
- **Computed evidence (verified existence, not optimality):** every listed best set genuinely
  attains its quoted coverage (recomputed). That 163 is the *global* k=22 optimum is **not**
  proved; the true k=22 maximum lies in [163,173]. Likewise companions are best-found at stated budgets.
- **Conjecture (not claimed):** the 20-fold replication at 163 suggests SA is near the k=22 ceiling,
  but exhaustive proof over C(50,22)≈10¹³ is infeasible here and is not attempted.
- **Originality:** no priority claim is made. Per the brief, nearest literature covers unrestricted
  bases, analytic restricted-digit primes, and distinct-modulus coverings — disjoint from this
  finite digit-alphabet covering record. Live-web checks were unavailable; treat as triage.

## 7. Limitations

- Negative result is specific to decimal D⊆{0..4} with the [0,44]∪[100,144] envelope and p∈{173,…,197};
  other alphabets, bases, or larger p are untouched.
- Exact certificates depend on code correctness (short, auditable scripts; boolean-coverage cross-check included).
- SA budgets (20×200k main; 8×80k companions) are substantial but heuristic; better k-sets may exist below the |S(U)| ceiling.
