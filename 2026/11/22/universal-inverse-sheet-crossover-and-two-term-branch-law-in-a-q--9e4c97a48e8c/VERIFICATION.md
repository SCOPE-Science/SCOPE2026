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
# Reproducibility

Run `python verify.py` with Python 3 and SymPy. It checks exact symbolic polynomial/determinant identities, phase-level counting against total variation, fixed-coupling asymptotics after the two finite stationary points are included, and 18 finite small-coupling crossover diagnostics. The local run completed with PASS. No finite test certifies the asymptotic assertions; those follow from the phase-counting proof in `RESULT.md`. Unrestricted one-step inverse fibers are not equivalent to fully backward-reachable orbits.
