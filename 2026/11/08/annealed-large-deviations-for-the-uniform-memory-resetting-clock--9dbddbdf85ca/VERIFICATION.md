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

# Verification and reproducibility

The proof in RESULT.md is analytical. The essential steps are the scalar memory-generator equation, its unique regular Kummer solution, a uniform negative-real-argument asymptotic, and the essentially smooth cumulant-function large-deviation theorem. The domain boundary at \(s=1\) is treated separately through positivity and the no-reset event.

Run `python3 CHECK.py` using only the Python standard library. The script compares rational series coefficients, an independent integral representation for the mean, the Legendre transform and seeded simulation of the defining recursion. The test run completed with **561** assertions. No finite numerical test is claimed as an infinite proof or an independent audit.

Limits of verification: the quoted Kummer asymptotic and Gärtner–Ellis theorem are standard analytical inputs; their hypotheses are explicitly matched in the proof. The source literature was inspected for novelty claims, but a global publication-priority guarantee is not possible. The independent-audit channel has not been performed.
