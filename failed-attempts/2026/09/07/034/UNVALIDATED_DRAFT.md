# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Isotopy-stratified transversal-number census for group-based Latin squares of orders 7 and 8 with exact-cover witnesses

Lane 57 — 2026-09-07. Self-contained computational census report.

## Abstract

Let G7 = {Z7} and G8 = {Z8, C4×C2, C2³, D8, Q8} with normalized Cayley tables on
symbols 0..n−1. For each base we generate 30 seeded isotopes by independent uniform
row/column/symbol permutations (Python `random.Random(5757+k)`, k=0..29) plus the base
itself: 186 squares total. We deduplicate to isotopy-class representatives by exhaustive
row/column/symbol backtracking, compute for each representative the transversal number
τ (maximum partial-transversal size) and the full-transversal count N by exact-cover
branch-and-bound with node logs, and exhibit explicit cell-by-cell witnesses replayed by
an independent stdlib-only verifier that reads only the CSVs.

**Certified result.** The 186 squares collapse to exactly 6 isotopy classes, represented
by the 6 group tables themselves. Certified τ/N table:

| rep (stratum) | n | τ | N | DFS nodes (N) | partial-search nodes (τ) |
|---|---|---|---|---|---|
| Z7_base (cyclic 7) | 7 | 7 | 133 | 988 | 28 |
| Z8_base (cyclic 8) | 8 | 7 | 0 | 3705 | 3378 |
| C4xC2_base | 8 | 8 | 384 | 3977 | 33 |
| C2³_base | 8 | 8 | 384 | 3945 | 33 |
| D8_base (dihedral 8) | 8 | 8 | 384 | 4105 | 33 |
| Q8_base (quaternion) | 8 | 8 | 384 | 4169 | 38 |

Every seeded isotope shares its stratum's (τ,N) (verified for all 186 by independent
permutation enumeration, 0 mismatches). Cyclic Z8 is certified transversal-free with a
maximal partial transversal of size 7; the other four order-8 group tables each attain
τ=8 with explicit transversals; Z7 attains τ=7 with N=133. All witnesses replay from
CSVs alone; N values are double-counted by two independent algorithms.

This is a **micro-census of seeded isotopy neighbourhoods of group tables**, not a
classification of all Latin squares of orders 7–8 (whose numbers are astronomically
larger). No new infinite family is claimed. The value is a machine-checkable,
isotopy-stratified τ/N table with witnesses in a range where transversal-free
(e.g. cyclic order 8) and transversal-rich squares coexist.

## 1. Definitions (proof vs computation separated)

A Latin square of order n on symbols 0..n−1 is an n×n array with each row and column a
permutation of 0..n−1. A **transversal** is a set of n cells, one in each row, each
column, and each symbol. A **k-partial transversal** is k cells with distinct rows,
columns, symbols. **τ(S)** = maximum k; **N(S)** = number of full transversals
(rows ordered, so each transversal counted once). Both are **isotopy invariants**: if
T[i][j] = σ(S[ρ(i)][κ(j)]) for bijections ρ,κ,σ, transversals map bijectively, so
τ,N are constant on isotopy classes. (Proof: apply ρ,κ,σ to cells; distinctness is
preserved. This is elementary and used below.)

**Isotopy** here means row/column/symbol permutations only (not transposes/paratopy).

## 2. Constructions — reproducible, no hidden choices

### 2.1 Normalized Cayley tables (proven Latin, proven groups)

Identity is index 0; row 0 and column 0 are 0..n−1 by construction. Latin property is
machine-checked for all tables; group axioms (associativity over all triples) are
machine-checked in `selfcheck.log`.

- **Z7, Z8:** L[i][j] = (i+j) mod n.
- **C4×C2:** elements (a,b), a∈Z4,b∈Z2, listed [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1)];
  (a1,b1)+(a2,b2) = ((a1+a2)%4,(b1+b2)%2).
- **C2³:** elements [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)] with
  componentwise mod-2 addition.
- **D8** (dihedral, order 8): same element list as C4×C2; (a1,b1)·(a2,b2) =
  (a1+(−1)^b1·a2 mod 4, b1+b2 mod 2). So rotation-reflection rule.
- **Q8** (quaternion): order [1,−1,i,−i,j,−j,k,−k]; encode (sign,basis), basis 0=1,1=i,2=j,3=k.
  1·x=x·1=x; equal non-identity basis squares to −1; distinct non-identity bases multiply
  cyclically i·j=k, j·k=i, k·i=j with sign +1, reverse products −1. Explicit code in
  `work/census.py`. Validated: associative, non-abelian, center size 2, element orders
  [1,2,4,4,4,4,4,4] (vs D8 [1,2,2,2,2,2,4,4]), confirming Q8 vs D8.

Group validation output (orders/center) matches textbook invariants, confirming the five
order-8 bases are pairwise non-isomorphic as groups.

### 2.2 Seeded isotopes (186 squares)

For each stratum with base B (n×n) and each k=0..29: `rng=random.Random(5757+k)`;
`rp=rng.sample(range(n),n)`, `cp=...`, `sp=...` drawn in that order; then
`S[i][j]=sp[B[rp[i]][cp[j]]]`. Plus B itself (`rp=cp=sp=identity`). Total 6×31=186.
Seeds, permutations, and matrices are all stored in `squares.csv` (columns
sq_id,stratum,kind,n,seed,rep_id,matrix with rows `|`-separated). By construction every
seeded isotope is isotopic to its base; τ/N constancy per stratum is therefore a theorem,
and is additionally verified computationally for all 186 squares (see §4).

Seed reuse across strata (same 5757+k in each stratum) is intentional per spec and
harmless: bases differ, so isotopes differ; assignment to representatives is computed,
not assumed.

## 3. Isotopy reduction: 186 → 6 (computed evidence, exhaustively logged)

**Method (exact, logged).** Test S∼T: search bijections ρ (rows), κ (cols), σ (symbols)
with T[i][j]=σ(S[ρ(i)][κ(j)]). Backtracking order ρ0,κ0,ρ1,κ1,…; maintain partial σ and
σ⁻¹; on each new ρ(i) or κ(j), check all newly completed cells (i,j) for σ-consistency
(conflict = same S-symbol mapped to different T-symbols or injectivity violation).
Count every recursive call as a node. On success verify witness by direct replay; on
failure the full tree was exhausted (proof of non-isotopy for n≤8).

**Procedure.** Process squares in stratum order. Maintain rep list; for each square test
against existing reps in order until isotopic (log each test with nodes/ms). n-mismatch
(7 vs 8) is trivially non-isotopic, logged without search. After greedy assignment,
run all 15 pairs among final reps exhaustively to certify pairwise distinctness.

**Result.** Reps = the six bases in stratum order. Every isotope matched its own base on
first same-n test (witness found in 17–20 nodes). Cross-group tests proved
non-isotopy with 521–3785 nodes each (ms-scale). Rep-pair table (`rep_pairs.csv`):

- Z7 vs any order-8: n-mismatch (trivially distinct).
- Z8–C4xC2: 2185 nodes; Z8–C2³: 969; Z8–D8: 2185; Z8–Q8: 1865;
  C4xC2–C2³: 3785; C4xC2–D8: 2825; C4xC2–Q8: 3657; C2³–D8: 521; C2³–Q8: 3657; D8–Q8: 3657 —
  all exhaustive, all non-isotopic.

Full per-test log: `isotopy_log.csv` (645 tests + header). This is consistent with
Albert's theorem (isotopic groups are isomorphic): distinct groups cannot have isotopic
Cayley tables; our search certifies it directly for these tables without invoking the
theorem.

**Uncertainty.** None on this step: search is exhaustive for n≤8; witnesses replay.

## 4. Transversal census τ/N (computed evidence, doubly counted)

### 4.1 Algorithms

- **N (exact-cover DFS):** fix row order 0..n−1; depth-first over rows, trying each unused
  column whose symbol is unused; bitmask used-cols/syms; increment count at depth n;
  record first witness; count nodes. For Z8 with N=0, the 3705-node tree is the
  exhaustive unsatisfiability certificate.
- **Independent N recount:** iterate all n! column permutations (`itertools.permutations`),
  count those with all-distinct symbols. Algorithmically independent of the DFS
  (no shared code path beyond the matrix). Census asserts equality; verifier repeats it
  from CSVs alone.
- **τ (maximal partial, MRV branch-and-bound):** recurse over subsets of rows; at each
  node pick the unassigned row with fewest available (col,sym) options; branch take-each
  then skip; prune when |cur|+remaining ≤ best. Count nodes. For reps with N>0, τ=n
  follows from the transversal witness alone; the search confirms it in ~33 nodes. For
  Z8 (N=0), the size-7 witness plus the N=0 unsatisfiability proof certifies τ=7=n−1 as
  maximal (no size-8 exists, size-7 exhibited).

All searches are exhaustive for n≤8; 40320 column perms max, trivial.

### 4.2 Certified table and witnesses

N/τ values in Abstract are the census output (`census_log.csv`), double-counted
(DFS == perm enumeration for all 6 reps) and triple-counted by the independent verifier.

**Transversal witnesses** (`transversals.csv`, cells `r,c,s` sorted by row):

- Z7_base (N=133, τ=7): `0,0,0; 1,1,2; 2,2,4; 3,3,6; 4,4,1; 5,5,3; 6,6,5`
- C4xC2_base (N=384, τ=8): `0,0,0; 1,1,2; 2,4,6; 3,5,4; 4,3,7; 5,6,3; 6,7,1; 7,2,5`
- C2³_base (N=384, τ=8): `0,0,0; 1,2,4; 2,3,6; 3,4,7; 4,6,5; 5,1,3; 6,7,1; 7,5,2`
- D8_base (N=384, τ=8): `0,0,0; 1,1,2; 2,4,6; 3,5,4; 4,3,5; 5,2,7; 6,7,3; 7,6,1`
- Q8_base (N=384, τ=8): `0,0,0; 1,2,3; 2,4,6; 3,6,4; 4,1,5; 5,3,7; 6,5,2; 7,7,1`

Each has distinct rows/cols/symbols covering 0..n−1 and symbols matching the base matrix
(verifier checks). Stratum maxima: since each stratum is one isotopy class, these are
simultaneously base values and stratum maxima; no seeded isotope beats its baseline
(theoretically impossible by isotopy invariance of τ/N).

**Maximal partial witness** (`partial.csv`): the unique transversal-free rep:

- Z8_base (N=0, τ=7): `0,0,0; 1,1,2; 2,4,6; 3,2,5; 4,3,7; 5,6,3; 7,5,4`
  (rows {0,1,2,3,4,5,7}, cols {0,1,4,2,3,6,5}, syms {0,2,6,5,7,3,4} — 7 distinct each,
  matching the cyclic table; row 6 / col 7 / sym 1 omitted). Maximal because N=0 rules
  out size 8.

**Full-stratum invariance.** Independent perm recount of N for all 186 matrices in
`squares.csv` matches the rep's N in all 186 cases (`selfcheck.log`, 2.2 s). So the
table covers the entire seeded set, not just reps.

### 4.3 Consistency check (not part of proof): Hall–Paige

The Hall–Paige theorem (complete mappings) predicts a finite group has a transversal in
its Cayley table iff Sylow 2-subgroups are trivial or non-cyclic. Of our bases: Z7
(odd) yes; Z8 (cyclic Sylow) no; C4×C2, C2³, D8, Q8 (non-cyclic 2-groups) yes. Observed
N>0 exactly in those cases. This agreement is a sanity check, not a substitute for the
exhaustive counts.

## 5. Replay verification (independent, stdlib-only)

`verifier.py` reads **only** `squares.csv`, `transversals.csv`, `partial.csv` in its own
directory. It: (1) parses each matrix, checks Latin (rows/cols are 0..n−1 perms);
(2) checks each transversal witness (n cells, distinct rows/cols/syms, M[r][c]==s);
(3) checks each partial witness (τ cells, distinct, matching); (4) **recounts N from
scratch** via column permutations and asserts claimed N, τ==n iff N>0, and τ==n−1 for
transversal-free rows. Fresh-process run:

```
squares.csv: 186 Latin squares verified.
transversal Z7_base: n=7 N=133 recount=133 witness OK.
transversal C4xC2_base: n=8 N=384 recount=384 witness OK.
transversal C2^3_base: n=8 N=384 recount=384 witness OK.
transversal D8_base: n=8 N=384 recount=384 witness OK.
transversal Q8_base: n=8 N=384 recount=384 witness OK.
partial Z8_base: n=8 tau=7 N=0 recount=0 witness OK (maximal: n-1 with no full transversal).
ALL CHECKS PASSED ...
```

Log archived as `verifier_run.log`. Runtime seconds, no dependencies.

## 6. Limitations and what is NOT claimed — read before citing

1. **Seeded strata only.** We census isotopy neighbourhoods of six group tables (186
   squares → 6 classes), not all Latin squares of orders 7–8 (which number in the
   millions/billions per main class). The stratification is deliberately narrow and
   computationally closable; do not cite as a full order-7/8 transversal survey.
2. **No beating isotope.** Because isotopy preserves τ/N (elementary proof above), no
   seeded isotope can beat its group-table baseline. The "stratum maximum" is the base
   value. This empties one reading of the target hypothesis; the certified table itself
   (fallback claim) is the contribution.
3. **Computation, not theory.** N=384 coinciding across all four non-cyclic order-8
   groups is a verified computation (two algorithms + verifier), not a theorem with a
   structural explanation here. Conjectured relation to group structure is left open.
4. **Scope of maximality proof.** τ-maximality for transversal-free Z8 rests on
   exhaustive n≤8 search (3705+3378 nodes), not a general argument. No claim for n>8.
5. **Prior art.** Existence/asymptotics of transversals, Hall–Paige, and survey results
   (Montgomery 2024; Cavenagh–Wanless; Wanless 2009) are acknowledged background; this
   work adds only the concrete isotopy-stratified witness package for these six strata,
   absent from those surveys to our knowledge (live checks 2026-09-07 in topic brief).
   Closeness to order-10 DCLS transversal work (SCOPE-FAIL-20260907-009) is by design
   reduced in scope to n≤8 group-based τ/N only.

## 7. Files and reproduction

All paths under `output/artifacts/` (verification-critical only):

- `squares.csv` (186 rows: sq_id,stratum,kind,n,seed,rep_id,matrix)
- `transversals.csv` (5 rows: rep_id,stratum,n,N,tau,witness)
- `partial.csv` (1 row: Z8 maximal partial)
- `verifier.py` — `python3 verifier.py --dir output/artifacts`
- `verifier_run.log` — archived fresh run
- `isotopy_log.csv` — 645 backtracking tests with nodes/ms
- `rep_pairs.csv` — 15 rep-pair exhaustive non-isotopy certificates
- `census_log.csv` — per-rep N/dfs-nodes/ms, τ/partial-nodes/ms
- `run_meta.json` — seeds, rep list, assignment, τ/N map
- `census_stdout.log`, `selfcheck.log` — group-axiom checks + 186-square invariance

Generation: `python3 work/census.py` (deterministic; timings vary, node counts stable).
Verification: `python3 output/artifacts/verifier.py --dir output/artifacts` (seconds).

Base matrices: Z7/Z8 by addition mod n; others defined in §2.1 and stored verbatim in
`squares.csv` base rows, e.g. Z7_base `0 1 2 3 4 5 6|1 2 3 4 5 6 0|…`; Z8_base analogous
8×8 cyclic; non-cyclic 8×8 rows in CSV. Any discrepancy between this text and the CSVs
is resolved in favour of the CSVs as verified by `verifier.py`.
