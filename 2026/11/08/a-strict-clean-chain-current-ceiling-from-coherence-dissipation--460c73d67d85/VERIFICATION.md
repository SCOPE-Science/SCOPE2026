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

The standalone `checks/coherence_current.py` uses Python, NumPy and SymPy and solves the full Hermitian stationary response system from its coefficients, not an assumed tridiagonal solution. It verifies nine independent exact-rational configurations (including rational tilt and untilted fields), where the dissipation sum-rule equality is checked with exact symbolic zero residual. It also verifies 120 randomized real-potential configurations, with \(N=2,3,4,5,6,7\), against matrix current continuity, the derived current ceiling and the coherence identity.

Expected command: `python checks/coherence_current.py`.

Expected result: `PASS 9 exact rational identities and 120 randomized matrix diagnostics; total 129`.

No random finite sampling proves the universally quantified result; the exact proof is contained in `RESULT.md`. The nonstandard critical checks are source-response normalization, the all-size positive Hilbert–Schmidt decomposition, strict positivity, and the equality classification. These are established symbolically in the proof. Publication priority and independent experimental validation are not certified.
