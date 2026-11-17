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

# Reproducibility

The supplied `verify_horocycle.py` checks the exact area identity at five positive gap pairs using the hyperbolic cosine law rather than geodesic tangent angles. It then evaluates the expectation integral numerically for three large segment lengths and compares it to the two-term logarithmic asymptotic. Last, it evaluates the limiting cdf at six thresholds and checks the \(24/z\) tail numerically, then uses fixed-seed sampling to compare the event probability and the beta/uniform rare-event mark means at a finite threshold. Execute with `python verify_horocycle.py` in an environment with Python 3 and SciPy.

Recorded numerical outcome: `HOROCYCLE_TRIANGLE_AREA_LIMIT_CHECKS_OK`.

Analytic proofs of convergence in law, moment thresholds, the logarithmic constant term, and the marked total-variation limit appear in the RESULT.md proof. The numerical checks are finite consistency tests, not exhaustive verification over all real parameters. No external independent audit has been performed.
