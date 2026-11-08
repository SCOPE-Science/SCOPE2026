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
# Verification of the classification

`verify.py` is a stand-alone Python 3.10+ standard-library program. It builds every nonempty face in two independent ways, checks equality, enumerates the full signed simplicial boundary, verifies every matched incidence and acyclicity of the fully oriented Hasse graph, computes independent mod-two homology, and evaluates exact integer algebraic Morse boundaries.

For six columns, the 53-by-1 integral Morse boundary is identically zero. For seven columns, the 23-by-92 integral Morse boundary has exact rank two: columns indexed 11 and 33 span every other column integrally and their two entries at rows indexed 1 and 3 have determinant -1. These checks prove the only two nontrivial Smith factors are units. The resulting 2-connected CW complex has no attaching obstructions beyond these dimension-three degree vectors.

The output of a completed replay appears in `verify_output.txt`, ending `ALL_VERIFY_OK`. This finite replay directly proves the three new cases m4,m5,m6 and also independently checks the literature-implied m7 classification. The shellability theorem for eight or more columns is sourced from the cited literature, and the displayed polynomial is independently checked at five column counts; those sampled values are not substituted for the symbolic Euler proof. No independent external audit was carried out.
