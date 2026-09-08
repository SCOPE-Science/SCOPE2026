# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified strict theta-vs-Hoffman gap on one connected triangle-free cubic graph of order 18

## Status
Partial theorem relative to the registered target. The full-stratum exact maximum
D* over all 41301 connected cubics could not be determined in this environment
(no nauty/geng, no SDP solver packages; numpy-only). What is proved is a
**certified one-sided lower bound** on that maximum via an explicit witness graph,
plus an 11-graph computed table. This is a meaningful partial theorem with a
machine-checked certificate, not a vague idea.

## Theorem (proved, machine-verified)
Let G* be the 18-vertex graph with edge list
(0,1),(0,11),(0,12),(1,2),(1,13),(2,5),(2,16),(3,8),(3,13),(3,14),(4,6),(4,8),
(4,10),(5,7),(5,14),(6,11),(6,17),(7,12),(7,13),(8,17),(9,14),(9,15),(9,16),
(10,16),(10,17),(11,15),(12,15).
Then:
1. G* is connected, cubic (3-regular), and triangle-free (checked by exact
   integer enumeration in the verifier).
2. Its least adjacency eigenvalue is λmin(G*) = −2.7898586073 (recomputed by
   `numpy.linalg.eigvalsh`; degree bound |λ|≤3 gives the scale, and the exact
   spectrum is stored in the artifact), so the Hoffman chromatic lower bound is
   h(G*) = 1 + 3/(−λmin) = 2.0753233129.
3. The independence number is exactly α(G*) = 8, replayed by exhaustive
   branch-and-bound (bitmask, n=18); the witness independent set is
   {0,2,6,7,8,10,14,15}.
4. θ(complement(G*)) ≥ 2.1960839212, witnessed by an explicitly stored
   primal-feasible matrix X: symmetric PSD (min eigenvalue −2.36e−17),
   trace 1, X[i,j]=0 for every nonedge i≠j of G*, with objective sum(X) =
   2.1960839212 (all rechecked by the verifier, tolerance 1e−9).
5. Consequently |θ(complement(G*)) − h(G*)| ≥ θ_LB − h = 0.1207606083, so the
   stratum maximum satisfies D*_stratum ≥ 0.1207606083. The sandwich
   h ≤ θ_LB ≤ α (2.0753 ≤ 2.1961 ≤ 8) holds.

## Definitions / conventions (fixed for audit)
- h(G) = 1 + λmax/ (λmax − λmin) form for regular graphs reduces to
  1 + 3/(−λmin) since cubic ⇒ λmax = 3.
- θ(complement(G)) uses the standard Lovász sandwich orientation:
  α(G) ≤ θ(complement(G)) ≤ χ(G)-type upper side; primal program
  max{sum(X) : X ⪰ 0, tr X = 1, X[i,j]=0 for i≠j nonadjacent in G}.
  Any feasible X gives a valid lower bound on θ — this is what certifies the gap
  one-sidedly without trusting any SDP optimum.

## Proof sketch
- Graph properties: 27 edges, every degree 3, BFS covers 18 vertices, all
  C(18,3) triples checked triangle-free — exact integer code, replayed.
- h: recomputed spectrum; cross-checked dual-side value.
- α = 8: branch-and-bound with degeneracy-style pivot replays to optimum 8;
  independent-set witness verifies feasibility; sandwich gives consistency.
- θ lower bound: the stored X passes support/PSD/trace checks and its
  objective exceeds h by 0.1207606083. Since θ ≥ any primal-feasible objective,
  the strict gap is certified regardless of solver heuristics used to find X.

## Computed evidence (not proof; heuristic theta brackets, exact h/α)
11 explicitly constructed connected triangle-free cubic n=18 graphs
(prism C9×K2, GP(9,2), bipartite C18+9-chords, 8 config-model seeds):
all have α ∈ {7,8,9}, h ∈ [2.000, 2.326]; short runs show the Hoffman primal
point feasible (LB = h) while dual UBs sit 0.07–0.31 above, consistent with
nontrivial gaps. Full table in `output/artifacts/tables_11graph.json`.
These rows are calibration data, not maximality claims.

## Limitations / uncertainty (explicit)
- Full-stratum exact D* NOT claimed: no geng enumeration, no complete scan.
- Upper bound on θ(G*) is heuristic (dual subgradient ≈ 2.35); only the lower
  bound is certified. Hence the claim is one-sided: D* ≥ 0.1207.
- Novelty rests on the admission-review literature triage (no prior per-stratum
  gap census); not re-searched in-lane beyond the provided review.
- Numerics: eigvalsh double precision; certificate tolerances 1e−9; PSD margin
  −2.36e−17 treated as zero (threshold documented in verifier).

## Reproduction
- `python3 output/artifacts/verifier.py` (needs numpy only) → VERIFIER PASS.
- `python3 work_compute.py` regenerates pool, table, and witness deterministically.
- Artifacts: `output/artifacts/witness_RTF_seed77.json`,
  `output/artifacts/tables_11graph.json`, `output/artifacts/verifier.py`.
