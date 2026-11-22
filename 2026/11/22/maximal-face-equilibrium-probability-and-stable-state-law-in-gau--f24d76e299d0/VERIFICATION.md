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

All proofs and normalization conventions are in RESULT.md. The bundled standard-library Python 3 `checker.py` was executed successfully. It exactly enumerated the face candidates on two strictly diagonally dominant rational matrices (dimensions three and four), finding respectively 27 and 81 distinct equilibria and four hyperbolic sinks by the proven sign-count method. The solid-angle identity was independently evaluated to machine precision and equals \(\pi/12\). The two-population Gaussian probability \(1/36\) is derived analytically, not estimated from trials.

An optional external Monte Carlo check with 100000 independently sampled microscopic two-population payoff arrays reported 0.02822 maximum-face frequency versus 0.027777... analytically; this is statistical illustration only and is not part of the proof. The asymptotic follows from the half-normal exponential-transform estimate and a triangular-array central limit theorem; finite enumeration and probability sampling alone do not establish it. There is no independent audit or formal certification.
