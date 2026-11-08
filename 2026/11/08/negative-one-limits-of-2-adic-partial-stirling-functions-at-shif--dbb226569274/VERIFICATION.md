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

Run `python3 verify.py` using the accompanying standalone standard-library checker. It verifies the binomial-harmonic identity as exact rationals for 30 indices, compares modular and rational partial Stirling values for 27 indices, checks stabilized factorial units for four scaling parameters, and compares 96 finite approximants with the stated limit expressions at 13-bit precision. The mathematical proof of convergence is given in RESULT.md and is independent of finite experiments. No external certificate or independent audit has been performed.
