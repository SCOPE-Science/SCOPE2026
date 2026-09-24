# Complete graded Betti census of edge ideals over the 112 connected 6-vertex graphs, with matching-bounds verification and an extremal witness

## Context

Betti numbers and Castelnuovo–Mumford regularity of squarefree edge ideals are a recognized
program since Hochster's formula, Fröberg's linear-resolution theorem, Kalai–Meshulam bounds,
and Ha–Van Tuyl-type matching bounds (induced-matching number ≤ reg ≤ minimum-maximal-matching
number). General bounds are known, but exact uniform Betti tables for a complete small-graph
slice with replayable logs were missing. This record covers the natural complete slice of all
112 isomorphism types of connected graphs on 6 vertices (OEIS A001349), plus a frozen 8-graph
connected 7-vertex sample.

## Definitions

- Let `G` be a simple graph on vertex set `[n] = {0,…,n−1}`, `S = k[x_0,…,x_{n−1}]` with
  `k = QQ` (characteristic 0 for the tables), and `I(G) = (x_i x_j : {i,j} ∈ E(G))`.
- Graded Betti numbers: `β_{i,j}(S/I(G)) = dim_k Tor^S_i(S/I(G),k)_j`.
- Projective dimension: `pd = max{i : β_{i,j} ≠ 0}`.
- Regularity (quotient convention): `reg = max{j−i : β_{i,j} ≠ 0}` (so `reg(I(G)) = reg(S/I(G))+1`).
- `im(G)` = induced-matching number; `mmm(G)` = minimum size of a maximal matching;
  `maxmatch(G)` = ordinary matching number.
- Scope: representatives of all 112 connected 6-vertex isomorphism types (canonical
  permutation-min masks sorted into ids 0,…,111), plus a frozen 8-graph connected 7-vertex
  sample (seed `sha256("lane-191-n7-sample-v1")`, masks
  900557, 946941, 741615, 1620724, 1830682, 580322, 1160695, 1103821 in 21-bit edge order).

## Result

1. **Enumeration.** All `2^15 = 32768` edge masks on 6 vertices contain 26704 connected labeled
   graphs, falling into exactly 112 permutation-min canonical types, matching the published
   count 112.
2. **Census (n = 6, over QQ).** For each of the 112 graphs the full minimal graded Betti table
   `{(i,j,β_{i,j})}`, `pd`, `reg`, `im`, `maxmatch`, `mmm` were computed exactly over QQ by two
   independent code paths (Hochster induced-subcomplex homology and Koszul–Tor strand homology);
   all 112/112 tables agree across the two routes:
   - Regularity: 67 graphs reg 1; 45 graphs reg 2.
   - Projective dimension: pd 5: 44 graphs; pd 4: 64 graphs; pd 3: 4 graphs.
   - Distinct full graded tables: 55. Most frequent: `(1; 8 at (1,2); 14 at (2,3); 9 at (3,4);`
     `2 at (4,5))`, occurring 8×.
   - Matching sandwich `im ≤ reg ≤ mmm` holds on all 112 graphs (0 violations, brute-force
     `2^m` matching enumeration). `reg = im` on 107/112; `reg = mmm` on 54/112.
3. **Extremal witness (proved lemma, field-independent).** Let `G*` be census id 4 with edges
   `{02, 04, 05, 12, 13}`. Then over any field,
   `reg(S/I(G*)) = im(G*) = mmm(G*) = 2`.
   `G*` has table `β = (1; 5 at (1,2); 5 at (2,3), 2 at (2,4); 1 at (3,4), 3 at (3,5);`
   `1 at (4,6))`, `pd = 4`, `reg = 2`. 40 of the 112 graphs satisfy `reg = im = mmm = 2`;
   `G*` is the canonically first such (lowest canonical mask).
4. **7-vertex sample.** `(reg, pd)` = `(1,6),(2,5),(2,5),(2,5),(1,5),(2,5),(1,5),(2,6)`
   (Hochster route only); full tables in the artifact JSON.

## Proof / evidence

- **Enumeration:** canonical form = minimum permuted edge-mask over all 720 vertex permutations;
  `numpy.unique` of canonical forms yields 112 types. The auditor independently recomputed 26704
  connected labeled graphs and 112 canonical types; artifact masks match exactly.
- **Betti numbers:** Route A evaluates Hochster's formula
  `β_{i,j} = Σ_{|W|=j} dim H̃_{j−i−1}(Δ_W; k)` via exact fraction Gaussian elimination on every
  induced independence-complex boundary matrix. Route B computes `Tor_i` as homology of the
  degree-`j` strand of `K_• ⊗ S/I` (Koszul complex on the variables; basis `e_S ⊗ m` with `m`
  supported on an independent set), which equals minimal-resolution Betti numbers by construction.
  The artifact logs per-graph agreement flags plus one contributing `(W, r, dim)` Hochster witness
  per nonzero `β_{i,j}`. The auditor recomputed all 112 n=6 and all 8 n=7 tables from scratch
  with an independent exact-QQ Hochster implementation: 120/120 agree.
- **Matchings:** brute-force `2^m` subset enumeration per graph; auditor recomputation agrees on
  all 112 triples.
- **Witness lemma proof.** `M = {(0,4),(1,3)}` is a matching whose only cross pairs
  `01, 03, 41, 43` are all non-edges, hence induced: `im ≥ 2`. Every edge meets `{0,1,3,4}`, so
  `M` is maximal; no single edge is maximal (02 misses 13; 04 misses 13; 05 misses 13; 12 misses
  04; 13 misses 04), so `mmm = 2`. On `W = {0,1,3,4}` the independent sets are exactly
  `∅`, singletons, and `{01,03,14,34}`: `Δ_W` is the 4-cycle `0−1−4−3−0` with `H̃_1 ≅ k`
  (cycle `01−14+34−03`; rank 3 vs 3 computation; logged `(W,r) = (0134,1)` contributor to
  `β_{2,4}`). Hochster gives `β_{2,4} ≥ 1` over any field (C4 boundary signs totally unimodular,
  so characteristic-independent), hence `reg ≥ 2`. The general Ha–Van Tuyl bound `reg ≤ mmm`
  gives `reg ≤ 2`. Equality throughout.

## Limitations

- Full Betti tables are certified over QQ (characteristic 0) only; the witness lemma is stated
  and proved field-independently.
- The "resolution" side is Koszul–Tor minimal-resolution homology rather than logged
  Gröbner/Schreyer–Buchberger differentials (no Macaulay2 run was available); honestly disclosed.
- The 7-vertex component is an 8-graph frozen sample (Hochster route only), not a complete census,
  and must not be cited as complete.

## Reproducibility

- `output/artifacts/census_n6.json`: all 112 tables with `(pd, reg, im, maxmatch, mmm)`,
  per-graph dual-agreement flags, and Hochster witnesses.
- `output/artifacts/census_n7_sample.json`: the 8-graph sample tables.
- Re-derivation: exact-QQ Hochster recomputation over all `2^6 = 64` subsets per 6-vertex graph
  (seconds-scale with stdlib + fractions/numpy); brute-force matching enumeration over `2^m`
  edge subsets; canonical enumeration over `2^15` masks with 720-permutation minimization.
  The auditor replayed all of the above with independent code.

## References

- Hibi, Higashitani, Kimura, Tsuchiya, Dominating induced matchings of finite graphs and
  regularity of edge ideals. https://arxiv.org/abs/1412.3881
- Jacques, Betti Numbers of Graph Ideals (PhD thesis). https://arxiv.org/abs/math/0410107
- Banerjee, Yogeshwaran, Edge ideals of Erdős–Rényi random graphs.
  https://arxiv.org/abs/2007.08869
- OEIS A001349 — number of connected graphs with n nodes. https://oeis.org/A001349
- Macaulay2 EdgeIdeals package documentation.
  https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/EdgeIdeals/html/
