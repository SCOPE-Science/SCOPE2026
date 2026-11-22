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

# Verification

Run `python3 verify_puncture.py` with Python 3.10+ (the script uses `int.bit_count`). The implementation uses only the Python standard library and performs full simplex enumeration of the scale-two hypercube Rips complex and its zero-vertex puncture for dimensions three through six. It also checks the actual integral boundary of every sixteen-tetrahedron coordinate-cube sphere; the relative link is the eight-triangle octahedron, with a unit on a distinct triangle per coordinate triple. All adjacent coordinate transpositions are checked with simplicial orientation signs. Its exact output is saved in `EXPECTED.txt`.

The proof of the all-dimensional theorem is the vertex-link core decomposition and pair long-exact-sequence argument in `RESULT.md`. Checking Euler characteristics alone does not prove a homotopy type or exclude torsion. The script verifies selected critical integer chain identities and combinatorial data; the infinite-dimensional quantifiers are proved symbolically in the text.
