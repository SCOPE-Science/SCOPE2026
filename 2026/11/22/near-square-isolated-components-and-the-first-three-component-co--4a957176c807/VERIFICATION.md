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

Transfer adjacency is exactly sharing an immediate predecessor in Young's lattice, equivalently symmetric difference of two Ferrers cells. This is invariant under conjugation. Fixed barycentric coordinates are constant on each conjugation orbit and have clique support; rescaling each coordinate by the orbit size yields the stated orbit triangulation. Because the original is flag, one-skeleton compatibility is completeness of cross edges. For the near-square shape, using the two donor row lengths and a recipient among the remaining rows or a new row gives exactly the four displayed distinct neighbors. Comparing columns interchanges A with D and B with C; in each pair the Ferrers symmetric difference is four, including m=3. Thus there is neither a nearby fixed singleton nor an admissible pair orbit incident to the near-square singleton. Independently growing the Young lattice from rank zero, building edges by common-predecessor buckets, and joining admissible orbit representatives only when their cross-edge multiplicity is the product of their sizes reproduced all 24 component counts. At n=24 there are 1575 partitions, 32 orbit vertices and components of size 1, 2 and 29; the isolated vertex is (5,5,5,5,4).

## originality

PASS

The October 18 fixed-locus record already states the admissible-orbit model and classifies orders through 22. Those parts are covered and are not credited here. The supported distinctions are the isolated near-square family at every m≥3 and the sharp enlargement to the n=24 triple-disconnection boundary, with the new n=23 check and the 1,2,29 split of orbit vertices. Neither follows from the earlier small-order table or the ambient and vertex-level classifications.

## value

PASS

The near-square calculation identifies a structural isolation mechanism for the actual geometric fixed locus, even after exchanged-edge midpoints are admitted. The first triple-disconnection rank is a natural boundary in the existing equivariant topology problem, not an arbitrarily chosen new table endpoint. The exact orbit split at that first rank provides a reproducible benchmark without claiming higher homotopy information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
