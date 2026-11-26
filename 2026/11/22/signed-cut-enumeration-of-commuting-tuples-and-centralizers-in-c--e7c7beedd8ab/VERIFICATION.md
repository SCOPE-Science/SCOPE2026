---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical and computational checks

The result derives the sign-compatibility criterion from the Tits product in every arrangement hyperplane coordinate. It proves a bijection between commuting tuples with prescribed product and independently marked signed-magnitude cuts. For the centralizer, it counts refinements by local partitions of the original blocks, and then counts the optional cuts in each common-product fiber. All ranks and tuple lengths are covered mathematically.

Execute `python verify_type_b_faces.py` with Python 3 and no third-party modules. It builds real-coordinate sign vectors for every type-B face through rank four and computes actual compatibility, rather than importing the formula under test. Expected output includes face counts `1, 3, 17, 147, 1697`; commuting-pair counts `1, 7, 97, 2023, 56257`; ordered triples `15, 449, 20175` through rank three; and quadruples `31, 1921` through rank two. It verifies all element centralizers, chamber intervals, and signed-suffix overlap identities in the indicated ranks. Success ends in `VERIFY_OK`.

These finitely many computations do not prove the formulas at higher rank. The asymptotic comes from the proved generating function and the location and residue of its unique dominant pole.
