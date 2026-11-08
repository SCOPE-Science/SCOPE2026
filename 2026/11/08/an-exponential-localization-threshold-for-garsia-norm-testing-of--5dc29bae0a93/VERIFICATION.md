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

Execute `python CHECK.py` using Python 3.9 or newer; only the standard library is needed. It evaluates the finite Hardy-Hankel action on normalized Szegő vectors, checks the exact scalar profile against the matrix formula, checks critical ties and sampled inequalities, and compares small-amplitude asymptotics with direct optimizers.

The mathematical proof is in `RESULT.md`. The computation does not exhaust real amplitudes, degrees, or disk points. In particular, positivity on sampled grids is not used as evidence for the global critical threshold; the quadratic discriminant and exact derivative establish that threshold. The independently audited status is not asserted.
