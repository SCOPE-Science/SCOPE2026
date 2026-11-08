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
# Reproducibility and scope

The proof is self-contained in `RESULT.md`. Execute `python CHECK.py` under Python 3 with NumPy installed. The checker explicitly constructs all 12 cosine-orbit levels, 18 candidate resonances, and character-to-sensor restriction matrices, and tests the 35-dimensional observability matrices at all resonances and one ordinary coupling. It checks the predicted 6/9/3 resonance multiplicities and the independence of each eigenspace restriction. These finite numerical tests do not establish exact equality or inequivalence of algebraic ratios: that is proved in the cyclotomic/Galois argument in the result.

The number of time steps is sufficient, not optimal; no uniform stability constant at or near collisions is claimed. No independent audit or external certification has been performed.
