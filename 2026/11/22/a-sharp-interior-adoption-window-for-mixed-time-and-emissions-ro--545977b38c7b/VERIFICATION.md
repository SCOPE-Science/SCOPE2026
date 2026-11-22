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

# Reproducibility and limits

Run `python check_mixed_routing.py` using a standard Python 3 installation. The checker uses exact `fractions.Fraction` arithmetic and a fixed pseudorandom seed. It verifies 3,000 rational two-road parameter sets at six adoption levels, checking each user's exact Wardrop complementarity constraints, class conservation and the exact quadratic emission identity, together with the rational counterexample to pure-endpoint optimality. These tests cannot establish the theorem outside those samples; the universal correctness evidence is the analytic proof in `RESULT.md`.

For the displayed instance, the exact emission values are \(21/5\), \(15/4\), and \(21/5\), and the improvement from either pure endpoint is \(9/20\). Model assumptions include continuous nonatomic traffic, same congestion contribution from both classes, two parallel roads, and affine emissions. No independent third-party audit or field verification is claimed.
