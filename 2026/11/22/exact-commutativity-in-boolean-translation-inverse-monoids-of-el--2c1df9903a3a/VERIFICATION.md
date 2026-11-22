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

Run `python checker.py` with Python 3.8 or newer and no third-party dependencies. The bundled `checker_output.txt` records the observed run. The checker reconstructs \(\mathbb F_2\) linear systems for fixed translation labels, verifies the sixteen-support rank table, confirms the closed commuting-pair formulas at group orders \(2,4,8\), and directly multiplies all pairs in both the full and zero-collapsed monoids at group orders \(2,4\).

The software checks finite instances only. The unlimited family follows from the proof's disjoint-orbit product, elementary two-group classification of label pairs, and exact empty-subset quotient correction. No computational verification of arbitrary \(k\) or external independent validation is claimed.
