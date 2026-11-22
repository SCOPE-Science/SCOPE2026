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

Run `python verify.py` with Python 3.9+, NumPy and SymPy. The verifier works directly with the stated matrix, checks three exact symbolic identities, then performs 7,272 formula-versus-direct-SVD comparisons over 9 horizon values, 8 shear values and 101 allocation values. It checks the lower-bound inequality in these comparisons, eight threshold tie examples, strict endpoint ordering on both sides, and the equal-step regime beyond the horizon boundary. The expected terminal message is `PASS`.

The main theorem is justified analytically in `RESULT.md`, specifically by an exact resolvent reduction, the sign variation of a derivative, strict monotonicity of the endpoint ratio, and algebraic crossing extraction. The finite checks are not a proof for arbitrary parameters. No independent audit has been performed. The result does not claim trajectory-error improvement, multistage generality or a solver-speed advantage.
