# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact toroidal queen domination for the 11×11 wrap-around board: γ_T(11) = 5

## Abstract

On the toroidal board `T_11 = Z_11 × Z_11` with queen moves along rows,
columns and both diagonals modulo 11, we prove the domination number is
exactly **5**. We exhibit an explicit 5-queen dominating set and prove by
translation-reduced exhaustive enumeration that no 3-queen and no 4-queen
set dominates (2 queens are already excluded by counting). The complete
check replays deterministically in under one second with only the Python
standard library. This closes the `T_11` stratum; notably the value equals
the classical planar `γ(11) = 5`, contrary to the counting-bound intuition
that suggested a `{3,4}` frontier.

## 1. Definitions

Cells are `(r,c) ∈ Z_11 × Z_11`. A queen at `q = (r0,c0)` attacks `x=(r,c)`
iff

- `r = r0` (row), or
- `c = c0` (column), or
- `r − c ≡ r0 − c0 (mod 11)` (main diagonal), or
- `r + c ≡ r0 + c0 (mod 11)` (anti-diagonal),

including `q` itself. `N(q)` is this 4-line union. `D ⊆ T_11` dominates iff
`⋃_{q∈D} N(q) = T_11` (all 121 cells). `γ_T(11)` is the minimum `|D|`.

## 2. Neighbourhood size and translation symmetry

**Lemma 1 (|N| = 41).** For every `q`, `|N(q)| = 41 = 4·11 − 3`.

*Proof.* Each of the four lines has 11 cells. Pairwise intersections are
exactly `{q}`: row∩col/diag/antidiag share only `q` by definition; for odd
`n = 11`, diag∩antidiag is `{q}` since `(x+t,y+t) = (x+s,y−s)` forces
`2t ≡ 0`, hence `t ≡ 0`. So inclusion–exclusion gives `44 − 3 = 41`
(the queen counted 4 times). Verified computationally for all 121 cells
in `verifier.py` step [1]. ∎

**Lemma 2 (translation reduction).** For `t ∈ T_11`, `D` dominates iff
`D + t` dominates. Hence every domination orbit contains a representative
with `(0,0) ∈ D`.

*Proof.* Attack conditions depend only on differences `r − r0`, `c − c0`,
`(r−c) − (r0−c0)`, `(r+c) − (r0+c0)` mod 11, all preserved by joint
translation. Given `D ≠ ∅` pick `q ∈ D` and translate by `−q`. ∎

Consequence: to decide existence of a `k`-dominating set it suffices to
check sets containing `(0,0)`:

- `k = 3`: `C(120,2) = 7140` canonical triples;
- `k = 4`: `C(120,3) = 280840` canonical quadruples.

Both are exhaustively checkable in milliseconds. No SAT solver and no
`D4` reduction is needed (translations already make the search trivial).

**Lemma 3 (k = 2 impossible).** `γ_T(11) ≥ 3`.

*Proof.* `|N(q1) ∪ N(q2)| ≤ 82 < 121`. ∎

## 3. Lower bound: no 3-set and no 4-set dominates

**Theorem (exhaustive UNSAT).** No 3 queens and no 4 queens dominate `T_11`.

*Proof by deterministic enumeration.* Using bitmask coverage built from
explicit line lists (stdlib only):

- all 7140 canonical triples containing `(0,0)`: 0 dominate; maximum
  coverage is **92/121**, e.g. `{(0,0),(1,2),(2,10)}` leaving 29 cells bare;
- all 280840 canonical quadruples containing `(0,0)`: 0 dominate; maximum
  coverage is **108/121**, e.g. `{(0,0),(1,2),(2,4),(3,1)}` leaving 13 cells
  bare (`(4,3),(4,8),(4,9),(5,8),(6,3),(6,10),(7,3),(7,6),(8,5),(9,3),
  (10,3),(10,6),(10,9)`).

By Lemma 2, any hypothetical 3- or 4-dominator would translate to a
canonical one, contradiction. Hence `γ_T(11) ≥ 5`. Replay:
`python3 artifacts/verifier.py` steps [3]–[4] (~0.2 s). ∎

*Cross-check.* A second, independently written implementation using the
attack predicate `(r==r0 or c==c0 or r−c≡… or r+c≡…)` rather than line-list
unions reproduces the same maxima (92 and 108, same extremal examples) and
the same UNSAT verdicts. Random sampling of 200 000 unrestricted 4-sets
also peaks at 108, consistent with exhaustiveness.

*Remark on counting.* `3·41 = 123 ≥ 121` suggested 3 queens might suffice
with overlap ≤ 2. In reality generic queen pairs already overlap in ~12
cells (4 slopes: same-slope parallels are disjoint, the 12 cross-slope
pairs each meet once), so triples peak at 92, not 123. The counting bound
is extremely slack on the torus.

## 4. Upper bound: explicit 5-dominator

**Theorem (witness).** The following 5 queens dominate `T_11`:

```
W = {(4,3), (10,1), (8,5), (7,2), (6,10)}
```

Canonical translate by `−(4,3)`:

```
Wc = {(0,0), (2,7), (3,10), (4,2), (6,9)}
```

*Proof by coverage table.* Direct check: every `(r,c)` shares a row,
column, diagonal or anti-diagonal mod 11 with some `q ∈ W`. The artefact
`artifacts/coverage_table.csv` lists for each of the 121 cells the
first covering queen index, queen coordinates and line type
(row/col/diag/antidiag). `verifier.py` step [5] asserts full coverage for
both `W` and `Wc`. First-hit board map (queen index covering each cell,
rows 0–10 top to bottom):

```
1 1 1 0 4 2 3 0 2 3 0
0 1 3 0 4 2 0 3 3 2 1
2 0 3 0 1 0 4 3 3 1 2
2 1 0 0 0 1 3 4 1 3 2
0 0 0 0 0 0 0 0 0 0 0
3 1 0 0 0 2 1 1 2 4 4
4 0 3 0 4 0 4 2 1 4 4
0 1 3 0 1 2 0 3 3 1 3
2 1 2 0 2 2 2 0 2 2 0
1 1 1 0 2 2 2 4 0 0 4
1 1 1 0 1 1 1 1 0 0 1
```

Row 4 is covered entirely by the row of queen `(4,3)`; other rows mix
column/diagonal/anti-diagonal hits. Any cell can be hand-checked, e.g.
`(0,0)` shares anti-diagonal (`0+0 ≡ 10+1 = 0 mod 11`) with `(10,1)`;
`(10,9)` shares row with `(10,1)`, etc. ∎

Heuristic note: `W` was found by hill-climbing from random 5-sets
(best random 5-cover was 117; hill-climbing reached 121). Random 6-sets
already dominate frequently, confirming 5 is the threshold.

## 5. Main result

**Corollary.** `γ_T(11) = 5`.

*Proof.* §4 gives `γ ≤ 5`; §3 gives `γ ≥ 5`. ∎

## 6. Replay instructions

All artefacts use only the Python standard library:

```
python3 artifacts/verifier.py
```

Expected output (times machine-dependent, < 1 s total):

```
[1] |N(q)|=41 for all 121 cells: OK
[2] k=2 impossible by union bound 2*41=82<121: OK
[3] k=3 UNSAT: checked 7140 canonical triples ..., max cover 92/121 ...
[4] k=4 UNSAT: checked 280840 canonical quadruples ..., max cover 108/121 ...
[5] 5-witness [(4, 3), (10, 1), (8, 5), (7, 2), (6, 10)] dominates all 121: OK
[6] wrote coverage_table.csv (121 rows)
ALL CHECKS PASSED ... => gamma_T(11)=5
```

Files:

- `artifacts/verifier.py` — complete proof replay (neighbourhood sizes,
  counting bound, both exhaustive UNSAT loops, witness check, table emission);
- `artifacts/witness.json` — `W` and canonical `Wc`;
- `artifacts/coverage_table.csv` — 121 rows `(r,c,queen_index,queen_r,
  queen_c,line_type)`.

## 7. Limitations and scope honesty

- Single stratum `n = 11` only; no general formula for `γ_T(n)` is claimed.
- Optimality certificate is translation-reduced brute force (280 840 cases),
  not a DRAT/SAT proof. It is fully deterministic and solver-independent,
  which we view as stronger for this `n`, but it does not yield a
  checkable DRAT log as originally sketched.
- Minimality of the witness layout is not claimed (many 5-dominators
  exist; no census or uniqueness is given). Only existence + optimality of
  size 5.
- Correctness rests on: (a) Lemma 2 translation invariance (hand proof
  above), (b) correct enumeration of combinations containing `(0,0)`
  (stdlib `itertools.combinations`), (c) correct line generation mod 11
  (two independent code paths agree). No floating point or solver trusted.
- Relation to literature: this equals the planar value `γ(11) = 5`, so the
  hoped-for planar/toroidal separation does not occur at `n = 11`. The
  contribution is the first exact toroidal census at `n = 11` with replayable
  witness + UNSAT certificate, not a separation theorem. General toroidal
  upper bounds (e.g. Mynhardt-type) are consistent but imply no exact value.

## References (nearest prior work, all non-overlapping)

- Upper bounds for the domination numbers of toroidal queens graphs
  (Discuss. Math. Graph Theory) — bounds only, no exact `n = 9–12` census.
- Queen Domination of Even Square Boards (Elec. J. Combin.) — planar only.
- Improved lower bounds for Queen's Domination via an exactly-solvable
  relaxation (arXiv:2304.06620) — planar relaxation, no toroidal SAT census.
- Constructions, bounds, and algorithms for peaceable queens
  (arXiv:2406.06974) — different objective (peaceable maxima).
