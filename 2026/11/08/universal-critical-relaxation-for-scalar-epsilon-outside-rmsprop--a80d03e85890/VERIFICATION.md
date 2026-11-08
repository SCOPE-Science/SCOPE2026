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

# Verification notes

Run `python checks/verify.py` using a Python 3 interpreter. It requires only the standard library. The checker verifies exact rational identities, a finite-hit initialization, amplitude inequalities in finite trajectories, eventual alternation in sampled non-finite-hit trajectories, and scaled convergence for five distinct choices of \(a\), \(\varepsilon\), and \(\beta\).

Observed result: `EXACT_IDENTITIES 36`, `NUMERICAL_SCENARIOS 5`, and `VERIFY_OK finite_checks_only_analytic_proof_required`.

The theorem is not inferred from numerical sampling. Its infinite-time proof uses the exact critical multiplier, a stable linear memory recurrence, a dominated-convergence argument for weighted histories, and Cesàro averaging of reciprocal increments. The numerical sample sizes do not impose finite-time bounds and some initializations can exhibit exceptionally long transients near finite-hit resonance. Independent verification has not been performed.
