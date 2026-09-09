# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Negative / obstruction record: 4x4x4 no-three-way hole hunt (lane-439)

## What was tried (target: hole + triangulation explanation; fallback: hole alone)
- Loaded live MBDB `no3way-04-04-04.mat`: the matrix is **48x64**, rank **37**
  (exact), not "36x64" as written in the topic text; column lattice proved
  **saturated** (gcd of 37x37 minors = 1), so hole search = cone point + infeasible fiber.
- Exhaustive low-degree certificates: R2 (2080) and R3 (45760) fully collision-free;
  R3 **midpoint-convex** (all 129024 parity-compatible pairs checked); R4 766264/766480.
- Non-unimodularity witness: explicit 37-set with **det = -2**, certified **empty**
  (no other column in its convex hull). Its Pi hole candidate (degree 9) was proved
  **feasible** (explicit 9-cell table), so not a hole.
- Pi-point campaign over 39 det=+-2 simplices (19 distinct Pi points, degrees 8-12):
  **all fibers feasible**. ~150k randomized q=2/q=3 midpoint trials and ~340
  span-preserving perturbations: **no infeasible fiber**; high-degree solver hit
  timeouts (Gale-pruned backtracker insufficient at degree >~10), so the search was
  inconclusive there rather than negative.

## Strongest verified facts (replay: `python3 output/artifacts/verify.py` -> ALL VERIFY_OK)
1. 48x64 0/1 structure, col sums 3, row sums 4; exact rank 37; 11-dim left nullspace.
2. Saturated lattice (q=1) with seed-logged gcd replay.
3. det=-2 empty simplex.
4. R2/R3 injectivity census + R3 midpoint-convexity theorem (129024 pairs).

## Why NO_RESULT rather than a weaker claim
- The fallback success criterion needs a vector passing **all four** checks
  (i)-(iv) jointly; no candidate passed (iv). The verified lemmas above each fail
  the "independently valuable" bar on their own: saturation simplifies but does not
  decide the flagged normality question, and the det-2 simplex does not imply a hole.
- No emergent theorem/obstruction/counterexample of standalone value was found; the
  near-misses are recorded here and in WORKLOG.md, not claimed as findings.

## Reuse value for future attempts
- Artifacts give a head start: saturated-lattice proof, empty det-2 simplex seed,
  fast exact fiber solver (good to degree ~10), R2/R3 tables, row/col permutations.
- Recommended next step: a real ILP/SAT fiber oracle (unavailable here) + Normaliz
  saturation run, aimed at degrees 10-20 where this hour could not decide fibers.
