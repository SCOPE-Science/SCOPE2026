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

# Reproduction and limits

Run `python verify_tilting.py` with Python 3, NumPy, and SciPy. The checker constructs explicit positive two-by-two matrices, computes the logarithm Fréchet derivative with eigenvalue divided differences, and compares the resulting trace ratio with the independently derived one-dimensional resolvent integral; it also tests several near-alignment coefficients. The finite checks are supplementary and cannot prove strictness, attainment, uniformity, or the logarithmic limit. These facts are established analytically in RESULT.md. No independent mathematical audit or external certification has been carried out.
