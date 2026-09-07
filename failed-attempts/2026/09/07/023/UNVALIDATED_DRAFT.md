# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified interval for the maximum cap in PG(4,5): 51 ≤ m₂(4,5) ≤ 126, with an explicit complete 51-cap

## Abstract

**Status of claim.** We do *not* determine the exact value m₂(4,5). The exact census by symmetry-broken integer programming described in the assignment is infeasible in this environment (no ILP solver, stdlib-only Python, no network) and is not claimed.

**What is proved.** Let m₂(4,5) denote the maximum cardinality of a cap (no three collinear) in PG(4,5). We prove by a combination of machine-checked enumeration and self-contained counting:

> **Theorem.** 51 ≤ m₂(4,5) ≤ 126.

The lower bound is an explicit complete 51-cap in normalized GF(5)⁵ coordinates, machine-verified to contain no three collinear points among all 20 306 lines and to be maximal (every outside point lies on a secant). The upper bound is an elementary hyperplane-counting chain m₂(2,5)=6 ⇒ m₂(3,5)≤26 ⇒ m₂(4,5)≤126, where the base m₂(2,5)=6 is proved by an exhibited oval plus a 53 130-case exhaustive check (58 ms), and all incidence numbers used are both proved theoretically and independently re-verified computationally.

All scripts use only the Python standard library, rerun in seconds, and cross-check each other (independent re-enumeration, SHA-256 line-table checksum `b5cd6693…bec70`).

## 1. Setting

Let V = GF(5)⁵. Points of PG(4,5) are 1-dimensional subspaces ⟨v⟩, v≠0. We represent each point by the unique *normalized* vector whose first nonzero coordinate equals 1. Lines are 2-dimensional subspaces; each has q+1 = 6 normalized points. Hyperplanes are 4-dimensional subspaces, written a·x = 0 for a≠0 (dual point).

A *cap* is a set K of points with no three collinear, i.e. no line contains ≥3 points of K. A cap is *complete* (maximal by inclusion) if every point outside K lies on a line joining two points of K (a *secant*). m₂(4,5) is the largest |K| over all caps. Analogously m₂(2,5), m₂(3,5) for plane and solid sections.

**Coding-theory reading (motivation only, not needed for proofs).** A k-cap in PG(4,5) with 5×k matrix H whose columns are representatives gives a 5-ary linear code of length k, redundancy 5 (dimension k−5 if H has full rank), and distance ≥4 (no 1, 2, or 3 dependent columns correspond exactly to: nonzero points, distinct projective points, no three collinear). Completeness is equivalent to covering radius 2 (every syndrome is a combination of ≤2 columns). Hence our 51-cap is a [51,46,≥4]₅ code with covering radius 2 if H has rank 5 (it does — the points span V; e.g. standard basis multiples occur up to scale among the list). We do not claim weight-distribution or quantum-code consequences beyond this elementary translation.

## 2. Geometry enumeration: 781 points, 20 306 lines

**Lemma 2.1 (counts).** PG(4,5) has (5⁵−1)/(5−1) = 781 points. It has 20 306 lines, each with 6 points; each point lies on 156 lines.

*Proof.* Points: nonzero vectors 5⁵−1 = 3 124 fall into groups of 4 nonzero scalars, giving 3 124/4 = 781. Lines: 2-dimensional subspaces. Count ordered pairs or Gaussian binomial: (3 124·3 120)/(24·20) = 20 306. Each line has (5²−1)/(5−1) = 6 points. Lines through a point: quotient V/⟨p⟩ ≅ GF(5)⁴, whose 1-spaces (points of PG(3,5)) number (5⁴−1)/4 = 156. ∎

*Machine check.* `artifacts/gen_pg45.py` enumerates normalized points (781), spans every pair to build lines (sorted 6-tuples), and asserts 20 306 lines and 156 lines/point. Runtime ~2.2 s. SHA-256 over lines as u16le stream: `b5cd6693a7cfca1fad62e89d432c48cf7afeaf41fbf0240922b0bcd9083bec70`. The independent verifier `artifacts/verify_cap.py` re-enumerates both tables from scratch (different code path) and reproduces the same counts and checksum in ~2.0 s.

## 3. Lower bound: explicit complete 51-cap

**Theorem 3.1 (certified lower bound).** There exists a complete 51-cap in PG(4,5). Hence m₂(4,5) ≥ 51.

*Witness.* The 51 normalized vectors below (`best_cap.json` is authoritative; indices refer to the enumeration in `points.json`):

| # | idx | coords | # | idx | coords | # | idx | coords |
|---|-----|--------|---|-----|--------|---|-----|--------|
| 1 | 20 | (1,3,4,0,0) | 18 | 246 | (0,1,1,0,2) | 35 | 518 | (1,1,2,1,3) |
| 2 | 22 | (1,3,1,0,0) | 19 | 266 | (0,1,2,0,3) | 36 | 520 | (1,3,1,3,4) |
| 3 | 39 | (1,2,0,2,0) | 20 | 294 | (1,4,0,2,2) | 37 | 521 | (0,1,3,4,2) |
| 4 | 69 | (1,4,2,2,0) | 21 | 299 | (1,1,0,2,2) | 38 | 539 | (1,2,0,1,2) |
| 5 | 76 | (0,1,4,4,0) | 22 | 311 | (0,1,1,1,1) | 39 | 550 | (1,2,0,2,4) |
| 6 | 78 | (1,2,3,3,0) | 23 | 322 | (1,3,1,1,1) | 40 | 579 | (1,3,2,1,2) |
| 7 | 86 | (0,1,2,1,0) | 24 | 326 | (0,1,4,4,4) | 41 | 605 | (1,1,3,2,4) |
| 8 | 109 | (1,0,1,2,0) | 25 | 339 | (1,2,4,2,2) | 42 | 613 | (1,3,4,4,3) |
| 9 | 114 | (1,2,1,2,0) | 26 | 364 | (1,2,1,2,2) | 43 | 619 | (1,4,1,1,2) |
| 10 | 120 | (1,3,2,4,0) | 27 | 369 | (1,4,1,2,2) | 44 | 621 | (0,1,1,1,2) |
| 11 | 122 | (1,3,3,1,0) | 28 | 378 | (1,2,4,3,3) | 45 | 638 | (1,3,2,4,3) |
| 12 | 130 | (1,1,2,4,0) | 29 | 400 | (1,2,1,4,4) | 46 | 651 | (0,1,1,2,4) |
| 13 | 140 | (1,4,1,4,0) | 30 | 401 | (0,1,1,4,4) | 47 | 694 | (1,4,2,3,2) |
| 14 | 145 | (1,3,1,4,0) | 31 | 413 | (1,3,0,1,3) | 48 | 714 | (1,2,4,3,2) |
| 15 | 199 | (1,1,2,0,2) | 32 | 445 | (1,3,4,3,4) | 49 | 765 | (1,4,1,1,4) |
| 16 | 241 | (0,1,4,0,3) | 33 | 449 | (1,1,2,4,2) | 50 | 774 | (1,1,3,3,2) |
| 17 | 245 | (1,3,2,0,4) | 34 | 500 | (1,2,2,3,4) | 51 | 775 | (1,2,1,1,4) |

*Machine-readable authoritative copy: `artifacts/best_cap.json` (`size:51`, `indices` and `coords` arrays). Coordinate–index consistency is itself checked by the verifier.*

*Proof of cap property (computed).* `artifacts/verify_cap.py` re-enumerates points and all 20 306 lines from scratch, checks coordinate–index agreement, then counts cap points per line. Result: maximum occupancy 2, zero lines with ≥3 cap points. Secant lines (exactly 2 cap points): 1 275 = C(51,2), as expected when no line is overfull. Replay time ~2 s. ∎

*Proof of completeness (computed).* The same run collects, for each outside point (730 of them), whether it lies on a secant line. Covered: 730/730; uncovered: 0. Hence the cap is maximal by inclusion — a complete cap. ∎

*Canonical invariants (computed, not a full PGL-class certificate).* Hyperplane-section spectrum (781 hyperplanes a·x=0, counts of cap points per hyperplane):

```
{1:2, 2:7, 3:14, 4:10, 5:20, 6:36, 7:37, 8:58, 9:73, 10:111,
 11:141, 12:116, 13:93, 14:47, 15:14, 16:2}
```

i.e. 2 hyperplanes meet the cap once, …, 2 meet it in 16 points; maximum section 16, no hyperplane contains more. This spectrum is PGL(5,5)-invariant and is reproduced by the verifier on every run. We did **not** compute the stabilizer order or a canonical form (would require nauty/Sage); PGL-equivalence class is therefore not certified — stated as a limitation.

*Provenance (not part of proof).* The witness was found by randomized greedy maximal-cap construction plus drop-and-refill perturbation (~300k iterations over several seeds; best 51 from seed 2, 3 000 greedy trials; 300k-iteration intensive run with no improvement, suggesting local optimality but proving nothing). Search scripts `cap_search.py` / `intensive_search.py` are included for provenance only; correctness of the theorem depends solely on the verifier, not on how the witness was found.

## 4. Upper bound: m₂(4,5) ≤ 126

We chain three lemmas. All incidence numbers are proved by quotient-space counting and were additionally verified by exhaustive enumeration (`hyperplane_check.py`, ~7 s).

**Lemma 4.1 (base: plane).** m₂(2,5) = 6.

*Proof.* The conic X₀X₂ − X₁² = 0 gives 6 points: (1,t,t²), t∈GF(5), plus (0,0,1); a direct check over the 31 lines shows no three collinear (verified in 3 ms by `pg2_proof.py`). So m₂(2,5) ≥ 6.

For ≤6, PGL(3,5) acts transitively on ordered pairs of distinct points (given ⟨a⟩≠⟨b⟩ and ⟨c⟩≠⟨d⟩, extend {a,b} and {c,d} to bases of GF(5)³; the linear map sending one basis to the other induces the required collineation). Hence any 7-cap can be moved to contain the fixed pair P₀=(1,0,0), P₁=(0,1,0). Their line has 4 further points; deleting that line leaves 25 candidates. A 7-cap containing the pair would be the pair plus a 5-subset of the 25 with no three collinear overall. There are C(25,5) = 53 130 such subsets; `pg2_proof.py` checks all of them against all line triples and finds none extends. Total 54 ms. Hence no 7-cap exists. ∎

**Lemma 4.2 (solid).** m₂(3,5) ≤ 26.

*Proof.* Let K ⊂ PG(3,5) be a cap, k = |K| (k≤1 trivial). Fix P∈K. By §2-style counting (verified: each point of PG(3,5) lies on 31 planes, each line on 6 planes; plane ≅ PG(2,5)): each plane Π through P meets K in a plane cap, so |K∩Π| ≤ 6 by Lemma 4.1, i.e. |K∩Π|−1 ≤ 5. Summing over the 31 planes through P, each other point Q∈K lies on exactly the 6 planes through line PQ, so Σ_{Π∋P}(|K∩Π|−1) = (k−1)·6 ≤ 31·5 = 155. Thus k−1 ≤ 155/6 < 25.84, so k ≤ 26. ∎

*Computational cross-check.* `hyperplane_check.py` enumerates PG(3,5) (156 points, 806 lines, 156 planes of 31 points each; 31 planes/point, 6 planes/line) — all sets match the theoretical numbers.

**Lemma 4.3 (4-fold).** m₂(4,5) ≤ 126.

*Proof.* Let K ⊂ PG(4,5), k = |K|. Fix P∈K. Hyperplanes through P: 156 (quotient GF(5)⁴ gives (5⁴−1)/4); hyperplanes through a line: 31 (quotient GF(5)³ gives (5³−1)/4); hyperplane section ≅ PG(3,5). Each hyperplane H∋P meets K in a solid cap, so |K∩H| ≤ 26 by Lemma 4.2, i.e. minus P ≤ 25. Summing: Σ_{H∋P}(|K∩H|−1) = (k−1)·31 ≤ 156·25 = 3 900. Hence k−1 ≤ 3 900/31 ≈ 125.81, so k ≤ 126. ∎

*Computational cross-check.* `hyperplane_check.py` verifies on the enumerated PG(4,5): every hyperplane has 156 points, every point lies on 156 hyperplanes, every line lies on 31 hyperplanes.

**Corollary 4.4 (interval).** 51 ≤ m₂(4,5) ≤ 126.

## 5. What is NOT claimed

- **No exact census.** K* = m₂(4,5) is not determined; no (K+1)-unsatisfiability certificate and no branch-and-bound optimality log are provided (they would require an ILP/SAT solver unavailable here).
- **No record claim.** Offline (no network) we could not consult current Hirschfeld–Thas–Davydov m₂ tables or quantum-cap databases. The upper bound 126 is elementary and almost certainly weaker than published specialized bounds (Hill/Pellegrino/Thas-type); the 51-cap is certified but we make no claim that it beats the literature — it is a replayable benchmark witness, well above the trivial ovoid 26.
- **No PGL classification.** Stabilizer order, weight distribution of the full [51,46] code, and canonical-form equivalence are not computed.
- **Heuristic optimality evidence is nil.** The failure of 300k perturbation trials to exceed 51 and the 49–51 spread across seeds suggest 51 is a strong local optimum, but this is anecdotal, not a bound. It is reported only as search context.

## 6. Reproducibility

Files under `output/artifacts/` (verification-critical: `gen_pg45.py`, `points.json`, `lines.json`, `best_cap.json`, `verify_cap.py`, `pg2_proof.py`, `hyperplane_check.py`; provenance-only: `cap_search.py`, `intensive_search.py`, `cap51.json` copy):

| command | result | time |
|---|---|---|
| `python3 output/artifacts/gen_pg45.py` | 781 pts, 20 306 lines, 156/point, sha256 `b5cd6693…bec70` | ~2.2 s |
| `python3 output/artifacts/verify_cap.py output/artifacts/best_cap.json` | max occupancy 2, 0 bad lines, 1 275 secants, completeness 730/730, spectrum as above | ~2.0 s |
| `python3 output/artifacts/pg2_proof.py` | oval verified, 53 130 subsets checked, m₂(2,5)=6 | ~0.06 s |
| `python3 output/artifacts/hyperplane_check.py` | PG(4,5): 156/156/31; PG(3,5): 31/31/806/6 | ~7.3 s |

All scripts require only the Python standard library. Total replay < 15 s. The verifier re-enumerates geometry independently, so a bug in the generator cannot mask a non-cap (counts and checksum would diverge).

## 7. Limitations and next steps

1. Gap is wide (51 vs 126); closing it needs symmetry-broken ILP/SAT with a real solver (CBC/SCIP/Kissat) plus PGL-canonical filtering, outside this environment.
2. Stabilizer/canonical-form computation (nauty/Sage) would make the 51-cap citable up to equivalence and is the natural next step.
3. Stronger analytic bounds (Hill, Thas, Pellegrino, linear-programming/Delsarte) were not attempted; incorporating them with careful citations is future work once network access allows a literature check.
4. The heuristic found 49–51 across seeds within seconds and 51 survived 300k perturbations; a principled study (multiple isomorphism types, second-moment analysis of hyperplane spectrum) could clarify whether 51 is near-optimal or an artifact of greedy bias.

---
*Environment: Python 3.12.3 stdlib-only (+numpy/sympy present but unused), no pip/solvers, no network. All timings on the lane-30 workspace machine.*
