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

# Verification of the stated mathematical result

The proof's essential nonstandard calculation is the strict-cell Jacobian for all clipped outputs, including its signs and complete absolute row sum. Independent exact rational face enumeration in `checker.py` compares this formula with the sorted-prefix closed form for 340 small group-size tuples. The test also confirms 120 finite perturbation pairs constructed to realize the extremizing cell and 120 independent random Lipschitz inequalities using a separate bisection projector. Execute `python checker.py` from the extracted package directory with Python 3 and NumPy available.

Mathematical completeness derives from the proof of all active clipping configurations, the piecewise-affine global bound and the strictly feasible extremizing configuration, not from the finite test count. The proof does not establish earlier-publication priority or independent verification.
