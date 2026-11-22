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

# Reproducibility and logical scope

The asserted conclusions follow from the exactly stated construction of the measurable tile, the full \(2\times 2\) fiber Gram matrix, Fourier-series Parseval normalization, residue classes modulo \(2b\), and density of irrational rotations. The two-sided infinite range of translated heights is essential: replacing the tile by a finite truncation generally changes the exact lower bound and cannot prove the infinite classification.

Run `python CHECK.py` with Python 3. It requires only the standard library. The executed run printed `TWO_COSET_UNBOUNDED_TILE_CHECKS_PASSED 3049`. The code checks sample matrix singular values, positive tile lengths and residue enumeration, and finite illustrations of irrational near-resonance. It cannot certify the infinite supremum or the completeness and frame dichotomy by enumeration.

The key analytic and arithmetic steps are documented in `RESULT.md`. Historical priority is provisional, and the investigation does not prove universal novelty or independently validate published analogues.
