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

The supplied standalone `verify.py` uses only the standard library, exhaustively regenerates the 201 nontrivial set partitions and 9011 strict chains, forms all 3009 orbit cells of the order-three subgroup, checks every integral boundary composition, performs 1482 exact unit chain cancellations, and verifies gcd-of-minors 3, 9 and 27 for the remaining 3-by-41 boundary. This establishes the claimed integral homology and agrees with Euler characteristic -37. It does not programmatically certify Armstrong's theorem, geometric-lattice shellability, or Whitehead's theorem; their applications are proved mathematically in RESULT.md. The splitting is noncanonical and no independently performed review is represented.
