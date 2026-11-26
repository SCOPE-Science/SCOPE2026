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

Poisson thinning and independent false positives give y_j=a+j theta q^j. Eliminating the geometric sequence (y_j-z)/j yields z^2-Bz+C=0. Independently checked its factorization: the larger root exceeds a by 4 theta q (3q^2-3q+1)>0, and y_1 minus that root equals -3 theta q (2q-1)^2, so even at equality q=1/2 it cannot have positive target signal. The smaller root reconstructs the input triple and gives the stated inverse. The Jacobian in (a,theta,q) is 2 theta q^2(3q^2-3q+1)>0; the coordinate changes are nonsingular, including the smooth one-sided restriction at f=0. With only levels 1,2, increasing a by any sufficiently small positive amount and solving for q and theta preserves both exact responses and the parameter restrictions, even when a starts at zero. The signs of the consecutive differences of y are those of 2q-1 and 3q-2; monotone transformation to p preserves the ties and all three regimes.

## originality

PASS

Poisson-based eDNA detection, inhibiting effects, and exponential parameter recovery are prior ingredients. The inspected sources do not give the exact three-population-probability global inverse on the constrained domain or the inadmissibility of its second algebraic root. The claim is credited only for this model-specific identifiability threshold and its algebraic consequences, not priority for the ingredients.

## value

PASS

The result resolves a concrete design ambiguity: when target load, dose-dependent inhibition and background are all unknown, exact data at the first two calibrated levels leave a continuum of solutions, whereas the third level separates the effects even without monotonicity. The positive-signal exclusion of the extra algebraic solution is needed to turn a quadratic elimination into a globally usable structural-identification benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
