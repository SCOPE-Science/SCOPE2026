---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the sharp natural cubic variation theorem

Run `python3 check_natural4.py`. The program needs only Python 3's standard library and reports exact rational confirmations of the spline middle-piece identity, an outward-rounded rational enclosure for the unique balancing mesh ratio, and independent critical-point integration of the three cubic pieces on a finite set of test data. The final stress test is finite and is not an exhaustive proof for all data or all positive spacings.

The infinite-data and infinite-mesh claims rely on the analytical argument in `RESULT.md`: exact decomposition into single jumps, curvature equations, characterization of all cubic extrema, and the positive-coefficient derivative inequality proving the two branches move in opposite directions. In particular, the rational bracket supports the printed numerical mesh ratio, whereas global uniqueness follows from the two monotonicity proofs rather than numerical optimization.

The published-source comparison distinguishes derivative-supremum norms, squared-curvature criteria, and three-knot range defects from the four-knot variation minimax. Historical unindexed equivalences have not been excluded, and no external mathematical validation is asserted.
