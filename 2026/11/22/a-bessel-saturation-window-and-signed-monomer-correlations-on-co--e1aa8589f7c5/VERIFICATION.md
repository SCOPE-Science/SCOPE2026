---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---

# Reproduction and verification

The supplied `CHECK.py` is standalone Python 3 source and requires no external packages. Invoke `python3 CHECK.py` after extracting the files. Its expected completion line is `MONOMER_DIMER_EXACT_CHECKS_PASSED 728`.

The checker validates exact rational matching-count probabilities on numerous small graphs, constructs all labeled matchings by recursion through four smaller-shore vertices, checks finite pairwise covariance signs and the cross-shore variance identity, and checks the explicit total-variation bound numerically across several sizes and imbalances. It does not check or certify the infinite theorem or the first-order error formula. The latter follows from the exact normalized tilt identity and integrable domination by \(\binom J2\) in Step 2 of `RESULT.md`. The covariance limits are obtained by dominated moment convergence, and the finite signs are verified by both path parity and Laguerre orthogonality.

Scientific limitations: fixed integer imbalance, positive uniform activity, equilibrium measure. No formal proof certificate or comprehensive historical-priority determination is supplied.
