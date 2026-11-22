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

# Computational reproducibility

Run `python CHECK.py` under Python 3 with NumPy and SciPy installed. The checker evaluates the decay poles, compares the closed Laplace transforms against independently numerically inverted Fourier resolvents, tests the exact characteristic-polynomial identity at rational parameter values, and verifies crossing counts and signs across 240 independently seeded positive parameter combinations. The expected output starts with `PASS 845`.

The numerical checks cover finite examples and do not establish the universal theorem. Universal pole ordering, uniqueness of the distance crossing, the velocity threshold, and mean-time ordering follow instead from the analytic identities in RESULT.md. The exact reference source and all required model assumptions are specified there. An independent audit has not been performed.
