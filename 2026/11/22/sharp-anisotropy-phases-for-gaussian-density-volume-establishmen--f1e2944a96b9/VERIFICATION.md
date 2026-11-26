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

The positive-volume superlevel condition is equivalent to the single threshold F(D) in RESULT.md, since a centered Gaussian changes to a ball under x=Sigma^(1/2)y with Jacobian D. Below the peak-density threshold the set is empty, and at the threshold it is a singleton, so neither can meet V>0. For the spectrum, min(lambda)>=tau/(dK) from the trace and ratio bound. Consequently the pairwise-linear ratio constraints and trace define a compact positive polytope. Strict concavity of sum log(lambda_i) excludes every nonvertex as a minimizer. If the ratio constraint is unsaturated, a nonzero small trace-preserving change is possible; if it is saturated and there is an intermediate eigenvalue, rescale all endpoint entries by the same small factor and compensate in one intermediate entry, preserving all tight constraints in both directions. If only the two endpoints occur, all the high/low equalities fix their ratios and the trace fixes the scale, proving that these spectra are the vertices. AM–GM gives the upper endpoint uniquely, and the segment from a minimizing spectrum to the isotropic one is feasible (the ratio constraints are linear on that eigenvalue segment) and covers the complete intermediate determinant interval by continuity. The sign of d(log F)/dD is negative below D_0, zero at D_0 and positive above it; clamping proves all three regimes and both boundary cases. In particular K=1 forces isotropy. The real k-objective is strictly convex with the stated stationary point, so floor/ceiling with clipping and ties suffices. The continuous optimizer set is exactly the admissible determinant fiber, including arbitrary orientations in the low-volume regime; rounding the optimum is valid for the integer count but need not preserve uniqueness of the optimizing covariance. The frozen checker was inspected, not executed; numerical sampling and scalar optimization are not the all-dimensional proof. Replay: RESULT.md, Proof §§1–4, with the explicit trace-preserving perturbation above.

## originality

PASS

Best-of-knowledge pass for the exact fixed-dimension, condition-capped Gaussian level-volume phase diagram and full optimizer set, including the finite multiplicity rather than a dimension-free determinant bound. The closest indexed two-endpoint spectral results optimize a different KL expression even after trace normalization. The inspected reverse Young/Specht result optimizes over a continuous mixture and does not give the fixed-cardinality sharp determinant interval. No priority claim is made for Gaussian ellipsoid volume, the scalar derivative or reverse-AM–GM ingredients; the classical original Specht article remained inaccessible and is a specific priority risk.

## value

PASS

For a centered Gaussian with a fixed second moment and bounded condition number, the precise mass-versus-volume tradeoff and covariance equality set are meaningful static benchmarks. The exact finite-dimensional endpoint matters: a looser dimension-free bound shifts the first transition and can misidentify its optimal spectrum. The classification tells when the determinant constraint is binding and when isotropy is uniquely optimal; its scientific value is that benchmark, not a prediction of persistence or a recommendation about biological releases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
