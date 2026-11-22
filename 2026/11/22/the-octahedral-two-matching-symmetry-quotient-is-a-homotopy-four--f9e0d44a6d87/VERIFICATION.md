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

# Reproducible verification

Run `python3 verify_octahedral_orbit.py` from a directory containing the provided script. It needs the standard library only; no external data, previously generated state, or downloaded computation files.

The checker verifies all 4,096 edge subsets; exactly 771 nonempty two-matching faces; all 48 octahedral graph automorphisms; the acyclicity of the 377-pair covering-space discrete-Morse matching; generation of the group by three elements with fixed points; construction of 4,670 quotient flag-orbit cells; the integer boundary-squared identities; 1,021 isolated unit cancellations followed by 1,313 exact unit Schur-complement cancellations; and an independent direct rank computation from the original boundaries over characteristic two, three, and five. It ends with `OCTAHEDRAL_TWO_MATCHING_FULL_SYMMETRY_S4_VERIFIED`.

The resulting cellular chain complex has one copy of \(\mathbb Z\) in degree zero and one in degree four, and no other cells after reductions. The program proves the stated finite algebraic identities and group facts, not the general Armstrong, Hurewicz, or Whitehead theorems used in the proof. There has been no independent external mathematical audit.
