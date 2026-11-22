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

Run `python3 verify_anticanonical.py` under Python 3.10 or later; no nonstandard libraries are required. The verifier checks the exact rational vertices of the planar polar, the ten unimodular three-cones, low-degree generating points, residue-class Ehrhart formulas and anticanonical Hilbert series identities. The source vertex data are stated in the result file and are independently testable as finite integer inequalities.

## Mathematical limits of the checker

Testing the first forty-two Ehrhart values is a diagnostic. The rigorous proof for all degrees uses (i) the rational Ehrhart quasipolynomial theorem with period dividing six, together with three exact samples per residue class, and (ii) the explicit fan of unimodular cones, which handles all lattice heights. The checker does not certify bibliographic priority, the behavior of other Fano deformations, or a complete ideal-of-relations calculation.
