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

Run `python checks/checker.py` using standard Python 3. No third-party modules are required. The provided `checks/output.txt` is the resulting run output. Six rational parameter choices cover a singular-density region, the exact essential-boundedness boundary, a bounded-density region, unbiased branches, and near-critical expansion. The checker verifies stationary cylinder masses by independent exact expressions for geometric-mixture and one-step Markov transitions through eight-digit cylinders: 3,066 equalities, plus moment and boundary algebra checks. The proof of uniqueness of stationary measures and the sharp all-exponent integrability characterization are analytic and are not inferred from the finite checker.

The selected absolutely continuous law exists for strictly \(p>1/2\). At and below that threshold uniqueness holds instead, with a Bernoulli digit law that is singular for biased inverse branches. Only the exact binary map and strictly positive branch probabilities are covered. Independent validation has not been performed.
