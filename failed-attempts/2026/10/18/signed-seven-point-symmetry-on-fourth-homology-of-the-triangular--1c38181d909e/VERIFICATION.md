---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The graph uses unordered pairs as vertices, adjacency by intersection of distinct pairs, and open neighborhoods of size ten. The source collapse map on a free pair t<s substitutes t-[t:s]^{-1}∂s for t and kills s, so inclusion, permutation with orientation sign, and projection compute the original graph action even though the collapses are not equivariant. In an independent exact reconstruction with tuple faces and a different free-face ordering, there were 18,495 augmented faces and 8,025 elementary collapse pairs, leaving (1,21,210,860,1131,222) faces in degrees -1 through 4 and none higher. Exact rational row elimination gave rank 215 for ∂4. Without 5-cells, integral H4 is a subgroup of a free abelian group with rank 222-215=7, so there is no torsion. Backward substitution of the collapse maps and signed permutations of rational cycles reproduced all 15 traces, including -5 for a transposition. The character determines the rational module; an integral representation identification is not inferred.

## originality

FAIL

Two distinct indexed 2026-10-18 records together cover the entire finding: 67fee7b5bd24 proves the exact rational representation by canonical star cycles, and 1f5fdf985e86 gives the integral sphere wedge, hence the asserted integral fourth homology. This is demonstrable overlap, not evidence that either record preceded the frozen one within that day. No distinct theorem remains in the frozen Finding.

## value

FAIL

The distinction between the signed and unsigned actions on this natural example is inherently useful. But the submitted finding is the already covered group and rational representation, not a new structural result or invariant: the group is an immediate consequence of the wedge and the character is identical to the signed-star calculation. Independent recomputation corroborates the covered facts but supplies no separate scientific contribution as frozen.

The dated certificate retains the supplied scientific assessment, sources and limitations.
