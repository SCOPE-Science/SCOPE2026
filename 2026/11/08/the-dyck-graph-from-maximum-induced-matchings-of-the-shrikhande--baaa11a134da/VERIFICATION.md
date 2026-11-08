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

# Reproducible finite checks

Run `python3 verify_cayley.py`, `python3 verify_latin.py`, and `python3 verify_equivariant.py` from the directory containing all embedded files, retaining `isomorphism.txt` beside `verify_cayley.py`. All programs use only the Python standard library and fail with an assertion if a required claim is false. The first counts every three- and four-edge candidate and checks a complete 32-vertex/48-edge isomorphism certificate; the second independently constructs the complementary cyclic Latin-square graph and computes all 32 exchange eccentricities; the third independently verifies the explicit Z4^2 translation-orbit map and adjacency-voltage correspondence.

Recorded outputs: `CAYLEY_OUTPUT.txt`, `LATIN_OUTPUT.txt`, `EQUIVARIANT_OUTPUT.txt`. These were captured after successful execution. The cardinality proof is an exhaustive finite certificate, not a non-enumerative general theorem. No separate independent audit is claimed.
