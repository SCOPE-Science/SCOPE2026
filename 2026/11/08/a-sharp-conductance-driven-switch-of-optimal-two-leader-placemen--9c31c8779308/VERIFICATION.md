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

# Reproduction

With Python 3.9 or newer and no third-party dependencies, run `python verify.py` in this directory. The script compares exact \(\operatorname{tr}(L_{FF}^{-1})\) values obtained by rational Gauss--Jordan elimination to six independently written class formulas, exhaustively across all leader pairs for a finite family of network sizes and chord weights. It separately verifies the exact rational difference identity, minimizer type and the presence or absence of conductance thresholds in a much larger finite grid.

Recorded successful replay: `PASS: 2696 exact full grounded-inverse pair comparisons; 2610 exact symbolic-formula/optimizer grid checks; all boundary checks`.

The infinite statements are proved in RESULT.md by block inversion, a rank-one update and exact polynomial sign analysis. The enumerations are safeguards against algebraic mistakes and do **not** prove infinitely many values or certify source novelty. This research package has not undergone independent external validation.
