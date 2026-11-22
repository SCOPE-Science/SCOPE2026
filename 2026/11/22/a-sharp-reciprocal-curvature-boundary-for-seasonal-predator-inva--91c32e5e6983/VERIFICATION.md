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

A standalone `verify.py` contains exact rational checks of the curvature polynomial, interval bounds and two neutral baselines. Running `python verify.py` passed. Additional midpoint quadrature of two explicit periodic intakes checks the expected strict signs but is **not** the proof of the universal or existential statements. The full proof in `RESULT.md` uses a unique periodic scalar linear response, integration over a period, strict Jensen convexity/concavity and an explicit construction of an everywhere-positive seasonal carrying capacity. No external formal certification or independent validation is claimed.
