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

# Verification

The analytic theorem covers every deterministic initial pair and every i.i.d. real random oracle slope with positive first moment and finite second moment. Its critical transfer matrix follows from conditioning and its exact determinant from polynomial expansion. The cone-preserving Perron argument proves the full continuous parameter-domain result. For the binary special case, the exact three-symbol reset block proves almost-sure finite hitting and a geometric tail; an independent second-moment recurrence proves exponential divergence. These infinite claims are proofs, not empirical extrapolations.

The standalone `verify.py` uses Python 3 standard-library rational arithmetic and returns `VERIFY_OK exact_rational_checks= 578`, as recorded verbatim in `verification_output.txt`. Its checks include exact symbolic determinant, exhaustive binary paths through nine draws, exact moment iterations and reset matrices on 225 rational input pairs. Numerical growth-rate approximations are explanatory only. The verifier has no network dependencies or nonstandard Python imports. `python3 verify.py` reproduces the checks.

The result does not claim an independent audit, higher-dimensional validity or precedence beyond inspected literature. All additional scientific validation remains unperformed.
