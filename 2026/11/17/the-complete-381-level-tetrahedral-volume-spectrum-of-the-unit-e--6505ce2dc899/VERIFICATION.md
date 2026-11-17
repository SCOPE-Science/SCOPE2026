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

# Executable verification

Run `python3 check_spectrum.py spectrum.tsv` with the Python standard library. The program uses exact ring arithmetic in the golden ratio, rebuilds 60 vertices from 30 original edges, exhaustively enumerates all 487635 tetrahedra, and compares all 381 exact volume-frequency rows; a second enumeration checks the two largest congruence classes. It also verifies the independent Cauchy–Binet identity for squared determinants. Expected marker: `SOCCER_TETRAHEDRON_SPECTRUM_PASS levels=381 combinations=487635`. This does not independently certify historical novelty.
