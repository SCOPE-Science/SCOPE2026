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

The dual has full 2-skeleton and tetrahedra exactly the connected four-sets. For odd n the torus need not be bipartite, but the needed assertion is local: any closed walk of length <=5 has zero column winding for n>=6, and even row-step parity; thus any induced five-vertex graph here is bipartite. If all its four-vertex deletions are connected its minimum degree is two or more, forcing K_{2,3}, which the product excludes since no distinct pair has three common neighbors. The triangle-free four-set count is 16n stars, 52n induced paths and 5n squares. Independently using the 35 cycle coordinates complementary to a cube vertex, the 35x38 cube boundary has 35 unit Smith factors. I also independently checked the 36 supplied templates as data, enumerating connected tetrahedron translation types and retaining actual coface offsets on the infinite strip; there are 73 types, of which 37 survive in the consecutive-column cubes, and each chosen triangle is free at its removal and outside those cubes. The cyclic cases 6–13 reproduced. For a uniform check, lift each connected tetrahedron to a strip window of span <=3. For n>=7, two such lifts meeting in a projected triangle, aligned at one common vertex, agree on its other vertices: each difference from the aligned vertex is in [-3,3], whose residues are distinct. No wrap-around changes incidences or the template orbits, with n=6 checked directly. The cube union glued along full single-column simplices has H_3=Z^{3n}, H_2=0. Adding only relative cells of dimension <=2 after collapse preserves H_3 and embeds H_2 into free relative H_2. Simple connectivity and Euler characteristic then give the wedge; alternatively use the saturated integral attaching matrix of the 3-cells over the full 2-skeleton, a wedge of two-spheres. Duality gives degrees 4n-6 and 4n-5, and the lower of those groups excludes pure shellability of the original.

## originality

PASS

The closest comparison gives only the higher dual degree for the open cylinder. The exact same host appears at threshold three, and a high-girth ordinary four-cut theorem excludes the host. No inspected source establishes the periodic four-cut topology or mechanically implies the integral wedge result.

## value

PASS

The integral topology of a full periodic family is determined beyond the known open-cylinder rank: the collapse gives a uniform reduction to local cubes, isolates the surviving 3n independent classes, and proves saturation and the exact second homology. The mixed degrees give an immediate non-shellability obstruction for a natural regular grid family, contrasting with top-only results for path grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
