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

The displayed homotopy type follows from the field-module fixed-subspace classification, Armstrong's orbit fundamental-group theorem, the Möbius-function Euler formula and two-dimensional Hurewicz–Whitehead theory. These are independent of finite computational checks.

Reproduce the binary quotient with `python verify.py` using Python 3 and SymPy. The script enumerates 65 vertices of the proper-subspace building, 315 strict two-vertex flags and 315 three-vertex flags; the sevenfold action gives (11,45,45) cell orbits. All signed cellular boundary compositions vanish. Integral spanning-tree elimination and Smith normal form give 35 unit invariant factors, zero first homology and rank-ten second homology. For other listed field orders, the script tests only the displayed Burnside polynomial identity, not the actual finite-field action.

No independent mathematical validation or external certificate is claimed. Nontrivial field orders beyond two rely on the proved general formulas, not exhaustive enumeration. Homotopy equivalence is not homeomorphism.
