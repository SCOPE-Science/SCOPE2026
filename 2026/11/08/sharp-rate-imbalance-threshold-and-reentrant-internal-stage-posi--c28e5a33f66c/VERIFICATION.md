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

# Verification of the two-state Gauss internal-stage classification

Run `python verify_gauss_stages.py` with SymPy installed. The program independently solves the full coupled four-scalar stage equations for fifty pseudorandom rational positive rate/step triples, comparing the resulting exact stage matrices to the projector formulas. It additionally proves the relevant symbolic identities, evaluates the quadratic discriminant and double-root tangency, verifies both the negative-stage witness and the positive endpoint, and tests the sign classification on each sampled triple. The accompanying `verification_output.txt` is the recorded output of that same packaged program.

Finite tests supplement, and do not replace, the explicit universal proof in `RESULT.md`. There is no formal-machine or independently audited certificate for all real parameter values. The scope is the linear two-state problem with exact arithmetic formulas, not floating point guarantees of a particular implementation.
