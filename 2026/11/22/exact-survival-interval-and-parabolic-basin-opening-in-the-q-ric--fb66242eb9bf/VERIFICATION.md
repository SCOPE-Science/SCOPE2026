---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The stated scaling gives the normalized map and is realizable by positive physical parameters. Its denominator is ≥1−k/e>0 (the first > in proof line 51 should be ≥ at t=1). The maximum image α/(e−k) lies below 1, and the map is increasing on the image. The factor G(t)/t=α/(e^t−kt) has its unique peak at c, where the denominator equals α_c; its endpoint values at 0 and 1 are below one. This yields the three regimes, both Lambert-W roots and increasing-branch stability. In the two nonextinction regimes, the right-hand preimage of the basin endpoint is uniquely forced by equality of t exp(−t) on the two branches, with the larger root >1. Monotone iteration after the first step gives exactly the stated endpoint and exterior behavior; below the fold each step contracts t by at most α/α_c. Expanding e^t−kt around c gives G(c+u)−c=u−cu²/[2(1−c)]+O(u³); telescoping reciprocal increments yields the asserted 1/n law away from both fold endpoints. The square-root fixed-point displacement is −sqrt(2δ/k)+O_k(δ) for the lower root; the implicit upper-end derivative b'(c)=−b_c(1−c)/[c(b_c−1)] then gives exactly the length coefficient. Monotone convergence precludes nonconstant cycles; invariance and bounded continuous test functions reduce invariant probabilities to mixtures of the finite set of fixed points.

## originality

PASS

This is a bounded pass for the model-specific global classification and quantified fold opening, not for the known map, its Lambert-W equilibria, the saddle-node mechanism, or parabolic convergence in general. The strongest readable precise analogues concern different Allee recurrences and do not give the normalized q-Ricker cutoff or its length coefficient. The publisher's accessible record establishes overlap on local bifurcations and equilibria but cannot resolve whether additional global results appear in the inaccessible article or thesis; that risk remains material and explicit.

## value

PASS

For a previously studied model, the result supplies a concrete global answer not obtainable just from its local equilibria: initial density can be too high as well as too low, with an explicit upper cutoff and an interval of nonextinction already at the fold. Critical relaxation and the exact one-sided change of that interval quantify time to recovery and basin size. Classifying the full half-line in a sector where all states land on the increasing branch also gives a clean exclusion of cycles and a tractable invariant-measure benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
