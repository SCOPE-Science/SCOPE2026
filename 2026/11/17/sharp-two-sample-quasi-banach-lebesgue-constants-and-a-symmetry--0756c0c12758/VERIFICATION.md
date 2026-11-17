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

# Reproduction and verification

The mathematical result requires \(0<p<1\), positive separation, and exactly two real sample sites. All-parameter validity rests on the analytic proof in `RESULT.md`: Gram inversion, the strictly convex log-ratio stationary analysis, precise asymptotics and the algebraic half-power case.

Run `python3 check.py` using Python 3 and its standard library. The actual run emitted `LAPLACE_TWO_SAMPLE_OK 16165 finite assertions`. Diagnostics sample multiple exponents/separations, interior and exterior cardinal values, the phase transition, explicit half-power formulas and the local square-root onset. Finite enumeration does not certify the infinite continuum of parameters and cannot establish novelty.

The independent audit status is not performed; no independent mathematical certification is claimed.
