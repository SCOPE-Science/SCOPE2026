---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently generated GP(8,3) with 16 vertices/24 edges and tested all 65,536 induced vertex subsets with union-find: 50,996 nonempty forest faces; face vector (16,120,560,1820,4368,7984,11200,11792,8672,3792,672). Deterministic vertex-order matching gives 25,475 pairs and critical dimensions 0:1,8:8,9:33,10:4. Independently checked all 375,040 Hasse covers acyclic, formed exact integer Morse matrices d9 (8 by 33, rank 8) and d10 (33 by 4, zero). Columns (21,3,2,1,5,10,12,18) of d9 have determinant -1, proving primitiveness. After degree-unit cancellations, 25 nine-spheres remain and every ten-cell has zero degree attaching map into their 9-skeleton, yielding precisely wedge^25 S9 plus wedge^4 S10.

## originality

FAIL

FAIL decisively: Oct 25 publication proves the exact same Möbius–Kantor GP(8,3) induced-forest homotopy type with the exact same Betti multiplicities and integer wedge decomposition; changed matching/verification files do not create a new mathematical theorem.

## value

FAIL

FAIL as submitted: the full Möbius–Kantor induced-forest homotopy class was already determined on the very same graph and complex in an earlier original result. Its different acyclic matching gives reproduction, not a new exact invariant or new structural consequence. The graph is natural but pre-existing identical classification does not meet unknown/non-implied criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
