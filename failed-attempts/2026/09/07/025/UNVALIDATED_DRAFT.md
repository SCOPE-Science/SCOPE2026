# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified genus-26, multiplicity 6–9 census of numerical semigroups: exact counts, Frobenius distributions with gaps, and Wilf-ratio minima

*Self-contained draft — all claims replayable in seconds with stdlib Python (see §5).*

## 1. Objects and verification machinery

A **numerical semigroup** is a cofinite submonoid S ⊆ N (0 ∈ S, closed under +, N∖S finite).
- **Genus** g(S) = |N∖S| (number of gaps).
- **Multiplicity** m(S) = min(S∖{0}).
- **Frobenius number** F(S) = max(N∖S); **conductor** c = F+1 (so [c,∞) ⊆ S).
- **Embedding dimension** e(S) = number of minimal (indecomposable) generators.
- **Wilf ratio** W(S) = e·n/c where n = |S∩[0,F]| = c−g. The Wilf conjecture asserts W ≥ 1.

Fix m. The **Apéry set** Ap(S,m) = {w_0=0, w_1,…,w_{m−1}}, w_r = min{s∈S : s≡r mod m}.
Write w_i = m·k_i + i (1 ≤ i ≤ m−1). The **Kunz vector** k=(k_1,…,k_{m−1}) satisfies
(Rosales–García-Sánchez, *Numerical Semigroups*, Springer 2009; Kunz):
- (K1) k_i ≥ 1 for all i (since 1,…,m−1 ∉ S when m is the multiplicity);
- (K2) Σ k_i = g;
- (K3) k_i+k_j ≥ k_{i+j} if i+j < m; k_i+k_j+1 ≥ k_{i+j−m} if i+j > m (from w_i+w_j ∈ S lying above w_{(i+j) mod m}; i+j=m gives no constraint).
Conversely every k ∈ N^{m−1} satisfying (K1)–(K3) arises from a unique S with those invariants.
We take this textbook bijection as given (not re-proved here).

Consequences used as checks:
- Membership test: x ∈ S ⟺ x ≥ w_{x mod m} (write x = w_r + t·m, t ≥ 0).
- F = max w − m; genus rechecked by counting gaps {x ≤ F : x < w_{x mod m}}.
- Minimal generators ⊆ {m}∪{w_i}: any s = w_r+t·m with t > 0 splits off m's (r=0) or w_r (r≠0).
  Hence e = 1 + #{i : w_i indecomposable}, tested by trying all splits a+(w_i−a) with membership tests. In particular e ≤ m.
- If F ≡ 0 mod m then F ∈ mN ⊆ S (as m ∈ S), impossible. So **no semigroup of multiplicity m has F divisible by m** (gap theorem, §4).

## 2. Enumeration method (complete by construction)

Fix g=26, m ∈ {6,7,8,9}. Two deterministic programs (stdlib only, one core):

- **Method A (primary):** iterate over ALL positive compositions of 26 into m−1 parts —
  C(25,4)=12650 (m=6), C(25,5)=53130 (m=7), C(25,6)=177100 (m=8), C(25,7)=480700 (m=9) —
  and keep those satisfying (K3). No pruning, so completeness is by exhaustion.
- **Method B (cross-check):** ordered backtracking assigning k_1,…,k_{m−1} with sum and
  fully-assigned-triple pruning. Different code path, same output required.

Both ran in `replay_enumerate.py` in 1.93 s total. Results agree exactly (sorted-list equality).

**Theorem (computed census).** The exact counts of numerical semigroups of genus 26 by multiplicity are:

| m | N(26,m) | SHA-256 of sorted Kunz list* |
|---|---------|------------------------------|
| 6 | 793     | e060df15c3c8561e3a66a8ba88ac4aef887cba5e7c6fe22a33e65d6eb7d258c3 |
| 7 | 1528    | 4bb06b44845077a56ddf9686ebf2d6686ebc84d4271cc1cf3030a9fab0ba0bbe |
| 8 | 4035    | 203dd36fa6dadf1c862ea788041c2ac6f266dc0b31f23c2332009bc5aa3d2dd7 |
| 9 | 6783    | 9c1bd907b50d823ef93ab111b172f4f19bd8e031137c7d0a1ac0dddfbe7162d6 |
| total 6–9 | **13139** | — |

\*Hash over the concatenation of `k_1,…,k_{m−1};` in sorted order; recomputed by the cold verifier.

## 3. Frobenius distributions, proven gaps, extremal witnesses

For each S, F = max w − m. Full frequency tables (from the certified CSV):

- **m=6** (range [31,51]): 31:1, 32:4, 33:10, 34:19, 35:32, 37:46, 38:56, 39:65, 40:64, 41:91, 43:94, 44:48, 45:73, 46:33, 47:76, 49:53, 50:6, 51:22. Missing: **36, 42, 48**.
- **m=7** (range [30,51]): 30:1, 31:5, 32:15, 33:32, 34:55, 36:79, 37:116, 38:128, 39:163, 40:150, 41:180, 43:154, 44:110, 45:116, 46:76, 47:80, 48:37, 50:17, 51:14. Missing: **35, 42, 49**.
- **m=8** (range [29,51]): 29:1, 30:6, 31:21, 33:51, 34:97, 35:168, 36:202, 37:323, 38:313, 39:455, 41:478, 42:277, 43:465, 44:184, 45:375, 46:117, 47:277, 49:154, 50:14, 51:57. Missing: **32, 40, 48**.
- **m=9** (range [29,51]): 29:1, 30:7, 31:26, 32:66, 33:148, 34:233, 35:416, 37:541, 38:597, 39:686, 40:681, 41:809, 42:519, 43:698, 44:454, 46:279, 47:309, 48:94, 49:147, 50:44, 51:28. Missing: **36, 45**.

**Gap theorem (proved + computationally complete).** *A priori*, F ≢ 0 mod m (§1). *A posteriori*,
exhaustion shows these are the ONLY absences in each interval: every non-multiple of m in the
range occurs. Formally the cold verifier asserts `missing == [F in [lo,hi] : F % m == 0]` for each m.

**Maximal-Frobenius witnesses (F=51=2g−1, hence symmetric).** Present in every m (22 / 14 / 57 / 28 witnesses).
Canonical representatives (Kunz, Apéry, generators all re-verified by membership):
- m=6: k=(3,6,9,3,5), Ap={0,19,38,57,22,35}, gens **⟨6,19,22,35⟩**, e=4, W=2.
- m=7: k=(4,8,3,2,5,4), Ap={0,29,58,24,18,40,34}, gens **⟨7,18,24,29,34,40⟩**, e=6, W=3.
- m=8: k=(3,4,7,1,2,4,5), Ap={0,25,34,59,12,21,38,47}, gens **⟨8,12,21,25,34,38,47⟩**, e=7, W=7/2.
- m=9: k=(1,2,3,4,5,6,2,3), Ap={0,10,20,30,40,50,60,25,35}, gens **⟨9,10,25⟩**, e=3, W=3/2.
  (Check e.g.: 10,20,30,40,50,60 ≡ 1,…,6 mod 9 are ≥ w_r hence in S; 25,35 similarly; F=60−9=51; gaps count 26 verified.)

**Minimal-Frobenius witnesses** (unique per m): m6 F=31 k=(6,5,5,5,5); m7 F=30 k=(5,5,4,4,4,4);
m8 F=29 k=(4,4,4,4,4,3,3); m9 F=29 k=(4,4,3,3,3,3,3,3), e=9 (ordinary-like fan).

## 4. Wilf verification and minima

**Computed result.** All 13139 semigroups satisfy W = e·(c−g)/c ≥ 1 (exact `Fraction` arithmetic; no floating point).
Per-m minima are unique (one witness each):

| m | min W | Kunz | F/c/e/n | generators |
|---|-------|------|---------|------------|
| 6 | **9/8 = 1.125** | (6,5,5,5,5) | F=31,c=32,e=6,n=6 | ⟨6,32,33,34,35,37⟩ |
| 7 | **35/31 ≈ 1.12903** | (5,5,4,4,4,4) | F=30,c=31,e=7,n=5 | ⟨7,31,32,33,34,36,37⟩ |
| 8 | **16/15 ≈ 1.06667** (slice-closest) | (4,4,4,4,4,3,3) | F=29,c=30,e=8,n=4 | ⟨8,30,31,33,34,35,36,37⟩ |
| 9 | **10/9 ≈ 1.11111** | (2,4,2,2,4,4,4,4) | F=35,c=36,e=4,n=10 | ⟨9,19,21,22⟩ |

Remarks: for m=6,7,8 the Wilf-minimal witness coincides with the Frobenius-minimal witness;
for m=9 they differ (F-min has W=6/5=1.2, e=9; W-min has F=35, e=4). The slice-closest-to-violation
semigroup is the m=8 ordinary-adjacent fan (4,4,4,4,4,3,3), W=16/15. Generator minimality of each
witness was rechecked by the split test (e.g. m9 min: 19,21,22 indecomposable; Apéry non-generators
41=19+22, 42=21+21, 43=21+22, 44=22+22 decompose).

## 5. Replay instructions (auditor path, minutes on one core)

```
python3 output/artifacts/replay_enumerate.py   # ~2 s: two-method enumeration, CSV + log + summary
python3 output/artifacts/cold_verifier.py      # ~5 s: independent recheck of every CSV row + SHAs + OEIS g≤9 sanity
```

Inputs: none (genus/multiplicities hard-coded, deterministic lex order, no randomness, no seed needed).
Environment: CPython 3.12 stdlib only (`hashlib, json, csv, fractions, itertools`); no GAP/Sage/numpy.
Outputs: `census_26_m6-9.csv` (13139 rows), `enumeration.log` (counts/SHAs/timings),
`summary.json` (F-dists, witnesses). Expected SHAs and counts are in §2; any deviation fails the scripts'
internal assertions.

Validation already performed: (i) Method A vs B sorted-list equality per m; (ii) cold-verifier full
recheck (Kunz, Apéry, F, genus=26, conductor, e ≤ m, Wilf ≥ 1, generator lists); (iii) totals for g ≤ 9
reproduce OEIS A007323 (1,2,4,7,12,23,39,67,118), confirming the enumerator against published totals;
(iv) SHA recomputation. GAP `numericalsgps` cross-check was unavailable in this environment (no binary).

## 6. What is new vs. known; uncertainties

- Known: total n_26 = 770832 (OEIS A007323, Bras-Amorós/Fromentin); Kunz theory (textbook); GAP `numericalsgps`
  can enumerate on demand. None publishes the (26,6–9) multiplicity-stratified closed certificate with joint
  Kunz vectors + F-distributions + proven gaps + Wilf minima + witnesses + replay logs offered here.
- This draft proves no infinite-family theorem; the gap characterization "missing ⟺ F≡0 (mod m)" within the
  observed ranges is a finite computed fact plus one elementary lemma, not a new structural conjecture.
- Uncertainty: correctness depends on the cited Kunz bijection and on the (auditable, <700-line) scripts;
  a transcription error in inequality signs would shift counts — guarded against by the OEIS g≤9 reproduction
  and the two-method agreement, but an independent GAP recount by a reader is welcomed.
