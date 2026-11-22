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

# Mathematical verification

The symbolic part is proved in `RESULT.md`. The provided `checker.py` uses only the Python standard library (`fractions.Fraction`) and reproduces 160 exact-rational cases across varying couplings, proximal thresholds, and supercritical margins. The code verifies the antipodal identities, Schur inequalities, invariant-cone transition identities, diagonal-start entry inequalities, and eight initial steps of the escaping cone for each rational test case. To execute from these extracted files: `python checker.py`. Expected final message reports `PASS: 160 exact rational cases`.

Finite checks are not substituted for the general proof. In particular the certificate does not classify the critical curvature ratio, establish global convergence of every subcritical trajectory, classify non-antipodal cycles, or extend the model to correlated dimensions or stochastic gradients. No independent review has been performed.
