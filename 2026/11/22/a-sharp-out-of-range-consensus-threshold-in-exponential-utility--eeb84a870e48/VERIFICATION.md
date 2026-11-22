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

The analytic proof separately verifies exact gap contraction, convergence, monotonicity and uniqueness of the crossing, and both extreme-utility asymptotics; the divergence follows from a monotone Riemann-sum estimate. The standalone `check.py` tests direct updates versus the exact series for 50 parameter combinations, numerically isolates the threshold for six positive biases, and displays high-learning scaled convergence. It uses Python's standard `math` module only.

Run `python check.py` next to the extracted file. Finite numerical tests are diagnostics; no exhaustive computational proof or external independent validation is claimed. The source's utility bias has been specialized to the positive exponential family. This record has not received an independent scientific audit.
