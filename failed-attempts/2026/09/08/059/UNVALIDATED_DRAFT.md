# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-170: stability-constrained degree-sequence elimination for ex(n,C₄), n = 44..48

## 1. Problem and baselines

Let ex(n,C₄) be the maximum number of edges in an n-vertex simple C₄-free graph.
OEIS A006855 is exact through a(40) = 127 (b-file to n = 40). Above that, the
recorded bounds (McKay lower bounds, Mar 2022; Alekseyev upper bounds, Jan 2023,
live-fetched 2026-09-08) are:

| n  | recorded lower | recorded upper | KST floor | vertex-deletion chain from a(40) |
|----|----------------|----------------|-----------|----------------------------------|
| 41 | 132 | 133 | 140 | 133 |
| 42 | 137 | 139 | 145 | 139 |
| 43 | 142 | 145 | 150 | 145 |
| 44 | 148 | 151 | 155 | 151 |
| 45 | 154 | 158 | 160 | 158 |
| 46 | 157 | 165 | 166 | 165 |
| 47 | 163 | 171 | 171 | 172 |
| 48 | 168 | 176 | 176 | 178 (via 172) |

Observations proved in the accompanying scripts (stdlib only):
- The classical KST bound m ≤ n(1+√(4n−3))/4 is strictly weaker than every
  recorded upper bound (its floors are 140,145,150,155,160,166,171,176).
- The vertex-deletion recurrence m ≤ ⌊n·a(n−1)/(n−2)⌋ chained from the exact
  a(40) = 127 reproduces the recorded upper bounds at n = 41..46 exactly and
  gives 172/178 at n = 47/48 — so the recorded 171/176 there already embed a
  further argument, identified here as pair counting (which independently
  forces a(47) ≤ 171 and a(48) ≤ 176 since no degree sequence realizes
  m = 172 at n = 47 or m = 177 at n = 48).
- The recorded upper bounds therefore equal min(deletion chain, pair counting)
  everywhere in 41..48; any strict improvement needs a genuinely new constraint.

## 2. Results

### Theorem A (proved; verification-critical files committed).
For each (n, m) in {(44,151),(45,158),(46,165),(47,171),(48,176)} — i.e. the
recorded upper-bound value — let S(n,m) be the set of nondecreasing degree
sequences d₁ ≤ … ≤ dₙ with Σdᵢ = 2m and ΣC(dᵢ,2) ≤ C(n,2) (pair-counting
feasibility). Then |S(n,m)| and the number surviving the sound
neighborhood-stability filter of Lemma N below are:

| n | m (recorded top) | \|S(n,m)\| (pair counting) | survivors of Lemma N | eliminated |
|---|------------------|---------------------------|----------------------|------------|
| 44 | 151 | 573209 | 434 | 572775 (99.92%) |
| 45 | 158 | 35745 | 66 | 35679 (99.82%) |
| 46 | 165 | 465 | 62 | 403 (86.7%) |
| 47 | 171 | 12 | 5 | 7 (58%) |
| 48 | 176 | 117 | 21 | 96 (82%) |

Every eliminated sequence is rigorously impossible as the degree sequence of a
C₄-free graph with m edges (Lemma N is a proved necessary condition); the
survivor lists are committed explicitly in `artifacts/elimination.json`.
This does NOT close any interval (survivors remain), so it is a partial
theorem: it reduces the stability/flag-algebra search space for the top count
to the listed survivors (e.g. just 5 explicit sequences at (47,171) and 21 at
(48,176)).

### Lemma N (neighborhood-stability; proved).
Let G be C₄-free, v a vertex of degree D, N(v) its neighborhood. Then
  Σ_{x ∈ N(v)} d(x) ≤ (n−1) + D + ex(D,C₄).
*Proof.* Put U = ∪_{x∈N(v)}(N(x)∖{v}) ⊆ V∖{v}, so |U| ≤ n−1, and
Σ_{x∈N(v)}(d(x)−1) = |U| + overlap, where overlap = Σ_{w∈N(v)}C(cnt(w),2) with
cnt(w) = |N(w) ∩ N(v)|: indeed a vertex z ∉ N(v)∪{v} adjacent to two distinct
x,y ∈ N(v) would close the 4-cycle v–x–z–y–v, so only w ∈ N(v) contribute;
and w ∈ N(v) adjacent to three distinct x,y,z ∈ N(v) would close a 4-cycle
with v, so cnt(w) ≤ 2, and each such w contributes exactly C(2,2) = 1, which is
half its contribution to e(N(v)). Hence overlap = e(N(v)), and e(N(v)) ≤
ex(D,C₄) since N(v) induces a C₄-free graph. ∎
The applied filter checks, for every position i (adversarially covering every
vertex), with degrees sorted descending d*₁ ≥ … ≥ d*ₙ:
  Σ_{j≤D, j≠i…} (top-D degrees among the other n−1) ≤ (n−1) + D + ex(D,C₄),
using the exact values ex(D,C₄) = a(D) for D ≤ 20 (OEIS exact rows
0,1,3,4,6,7,9,11,13,16,18,21,24,27,30,33,36,39,42,46,50); all enumerated
sequences have max degree ≤ 10, verified in-log, hence strictly inside the
exact range. The check `EX.get(dv, 999)` fails safe (fails open) outside the
table; the verifier asserts max degree ≤ 20.

### Computed evidence (not claimed as theorems).
- Reproducible ER₇-polarity witnesses (min-degree deletion + greedy fill,
  deterministic seeds): C₄-free graphs with 130,135,140,146,151,156,162,167
  edges at n = 41..48 (`artifacts/witnesses.json`, independently re-verified by
  pair-common-neighbourhood check). These sit 1–3 edges below the recorded
  McKay lower bounds (deltas −2,−2,−2,−2,−3,−1,−1,−1): they do NOT improve the
  database and are supplied as calibrated starting points, not as claimed
  improvements.
- Negative computational findings: (i) ER₇ induced-subgraph optima found are
  130/135/…/167 with greedy fill adding 0 further edges (saturated); subset
  simulated annealing repeatedly converges to the same values, indicating the
  ER₇ route is exhausted; (ii) generic GRASP/annealing from random starts
  stalls at ~118–119 at n = 41; (iii) the AG(2,7)-incidence route yields only
  ~90–114 induced edges — worse; (iv) a two-level (G−v pair-counting) filter
  was tested and eliminates nothing beyond Lemma N (an earlier run wrongly
  reporting full elimination contained a chaining bug, caught by re-verification
  against known realizable cases ER₅/ER₇ — details in WORKLOG).

## 3. How to reproduce (seconds to minutes, stdlib only)

  python3 output/artifacts/verify.py
re-checks every witness edge list (counts + C₄-freeness) and every survivor
list (sums, pair-counting inequality, Lemma-N satisfaction, ex-range guard).
Regeneration:
  python3 make_witnesses.py    # deterministic ER7 deletion witnesses
  python3 make_elimination.py  # full enumeration + Lemma-N filter + log

## 4. Limitations (explicit)

1. No recorded bound is beaten: no width-one closure, no strict upper- or
   lower-bound improvement. The fallback claim was NOT met.
2. Lemma N leaves survivors (434/66/62/5/21); the top counts are not ruled out.
3. Enumeration covers only the single top count per n (not full intervals).
4. The ex(D,C₄) table is used only inside the exact range (max degree ≤ 10
   observed, guard ≤ 20); the method would need certified ex values for larger
   D to extend to bigger n.
5. Lower-bound search was bounded compute (~30 min across engines); stronger
   engines (ILP/SAT, McKay's own unpublished witnesses) were out of scope.
