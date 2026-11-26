---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In a 231/312-avoider the inversion graph is a union of cliques: any induced two-edge path on three positions would be 231 or 312. A clique containing positions i<j contains every intervening position, since an inversion from i to j forces at least one inversion with any intermediate position. These consecutive cliques are the decreasing layers, and the absence of cross-layer inversions determines the value order. Thus the n−1 bits are fair and independent. The terminal zero is correctly handled by the extra T0 in the matrix formula; the cut interpretation preserves first-order definability. Aperiodicity makes iteration of T0 stabilize at a fixed state within each closed class, so the finite chain converges and its stationary and absorption systems have rational solutions. In the pattern family, an overlap of length at most L is impossible by the final 1; for longer overlaps the shift is at most t+1 and the suffix includes the delimiter 1 among the first L characters, unlike the prefix. For a fixed start, conditioning on a designated marker there rules out all earlier overlapping hits; earlier disjoint hits depend solely on the prefix before it. This independently yields equal first-hit probabilities and justifies the replacement symmetry. Each marker ends in 1, so the terminal zero creates no extra hit. The k=floor((n−1)/N) independent blocks each hit one chosen marker with probability 2^−N; the case n−1<N is correctly covered. A pattern-at-x formula has N−1 nested existential position quantifiers and cut tests of rank two; least-start selection adds at most two, giving N+3. Disjunctions of O(b) patterns use polynomial written length, and endpoints a=0,b are valid. Bounded replay independently checked exact first-hit counts using the avoidance recurrence A_L=2A_(L−1)−b A_(L−N).

## originality

FAIL

The October 26 indexed finding proves the same full rational spectrum for the same uniform layered class and logic, with the same exact finite-size first-marker identity and an exponential bound. Not only is its different marker family nonoverlapping, it mechanically gives at least as good size, convergence and rank bounds: with t=max(1,ceil(log2 b)), encode each t-bit label bit x as 1x. The length-2t payload then has no 00, so its 001-payload-1 marker has length 2t+4, one less than the frozen N. Its occurrence and least-start formulas give rank at most 2t+7 by the same direct quantifier count, and polynomial size. The alternative proof of rationality does not change the conclusion; the older entry even supplies effective evaluation from the sentence.

## value

FAIL

Exact attainment instead of density and quantitative FO witnesses are worthwhile objectives. In this frozen claim the exact result and mechanism are covered, and the advertised length, rank and convergence bounds are already attained or improved by choosing a simple payload family in the existing construction. The differences are presentational rather than a motivated improvement or a new exact invariant. There is no distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
