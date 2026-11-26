---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Every simple cycle uses both hub edges at two different leaves, so the forest complex is the union of p balls formed by allowing a double edge at one index, with the same entire cross-polytope sphere as boundary. The action permutes the interiors freely and transitively. The pushout of one ball by the boundary orbit map maps continuously and bijectively to the orbit space and is homeomorphic to it by compactness and Hausdorffness. The radial sphere model splits as the fixed line plus the reduced permutation representation: all nonidentity elements act without fixed vectors in the latter for prime p. Thus the boundary orbit map is the unreduced suspension of the weighted free lens covering, not just a map with the same degree. The cone homology sequence carries the lower suspended lens torsion across unchanged and takes the cokernel of multiplication by p on top suspended homology, with zero kernel; this gives exactly the even degrees 2 through p−1 and no other reduced groups. At p=3 the cover is the degree-three circle cover and only the top cokernel occurs. The connected lens space suspends to a simply connected space and the attached cell has dimension at least three. Collapsing one contractible ball in the original CW complex gives p−1 spheres of dimension p. The supplied flag-orbit checks and saved p=3,5 output test the boundary quotient over fields, not the attaching degree or general integral conclusion; no execution of uploaded code was needed.

## originality

PASS

Best of available evidence supports the ordinary leaf-rotation attaching-map and integral-torsion result as distinct, not the unquotiented wedge, the shared ball decomposition or lens-space homology itself. The known equivariant decomposition is substantial overlap, but the evidence inspected establishes neither this specific boundary orbit map nor these integral cyclic orbit groups. Rational acyclicity for a different group and an integral representation on the unquotiented homology do not imply them.

## value

PASS

For a common graphic-matroid complex with torsion-free homology, the natural prime rotation produces unboundedly many distinct degrees of integral torsion. The explicit suspended covering determines the actual attaching map of the ordinary orbit space, a strictly more informative fact than the homology list or the known unquotiented module. This is a uniform structural result, not a small-prime table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
