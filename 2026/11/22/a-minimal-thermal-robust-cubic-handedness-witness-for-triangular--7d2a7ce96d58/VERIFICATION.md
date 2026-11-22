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

The analytical argument uses a three-state stationary generator and exact complex third-order moment recursion. The standalone `checker.py` solves the unapproximated three-state generator for independent verification: four rational-symbolic and 80 numeric test cases. A separate 180,000-sample backward-renewal construction checks stationary cubic statistics, with and without independent isotropic thermal noise. Execute `python checker.py` (requires NumPy and SymPy). These numerical checks test stated finite examples only; exact all-parameter correctness rests on the proof in RESULT.md. No independent scientific audit has been performed.
