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
Run `python3 verify_crown_scale3.py` with Python 3 (standard library only). It constructs graph distances and Čech facet generators independently from the closed-form formulas, checks exact equality of face sets at scales three, four, and five for all tested sizes, computes reduced simplicial boundary ranks over \(\mathbb F_2\), and checks the predicted integral symmetry traces by independent simplicial Lefschetz calculations. The executable was run for \(n=3,4,5,6\) and returned `ALL_FINITE_CHECKS_PASS`. The respective nonzero reduced mod-two Betti numbers are \(2,3,4,5\), in dimensions \(2,4,6,8\).

The general all-order integral homotopy proof is mathematical: identify the scale-three complex as a join sphere with the interiors of \(n\) disjoint top simplices removed; then use its cellular long exact sequence, connectivity, Hurewicz and homological Whitehead. The group action follows by naturality of the same exact sequence and the degree of swapping join factors. Mod-two calculations alone cannot detect odd torsion or certify a general integral theorem. There has been no independent audit.
