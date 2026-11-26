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

Reconstructed GP(10,2) and enumerated perfect matchings via inclusion/exclusion along its ordered edges: 36 intact, 12 through each edge, and 24 after deletion. Their subset closures give 30,503 intact and 20,977 nonempty faulted simplices. Cyclic rotation reduces all 30 edges to representatives (0,1), (0,10), (10,12), not depending on any stronger symmetry. A separate implementation checked the entire oriented Hasse diagrams, and by reverse topological incidence elimination reproduced the signed matrices and integral Smith factors 1^3,2; 1^4,2; 1^6,2; and 1^9,2 intact. All Morse CW models have one zero-cell, no one-cells, and only two- and three-cells after that. Hurewicz identifies the attaching maps of the three-cells with their degree columns. Unimodular changes in source and target are realized by homotopy equivalences of wedges of two-spheres, so the corresponding homotopy cofibers split into a degree-two Moore space and four (intact: twenty) three-spheres. Independently checked all three recorded eight-triangle chains against the original simplicial boundaries: each is an available faulted cycle, and none belongs to the intact mod-two three-boundary image (rank 1833). Therefore the inclusion is nonzero on mod-two H_2. H_1 vanishes on both sides; naturality of the coefficient exact sequence identifies the mod-two map with tensoring the integral H_2 map with F_2. Both integral groups are Z/2, so the integral map is an isomorphism.

## originality

PASS

The distinct supported contribution is the precise faulted homotopy type together with the inclusion-induced isomorphism. The intact type is previously established. A same-day distinct result has group-level overlap for one fault and refers to an unspecified separate classification, but its stated two-fault result and one-fault comparison do not supply the one-fault Moore-plus-four-spheres type or identify the map. No priority is inferred from the shared date.

## value

PASS

The intact dodecahedral Moore summand motivates asking whether its order-two class persists after removing an edge of the underlying graph. This computes the actual map for every fault, not merely two groups of the same size, and distinguishes persistence of the torsion class from the loss of sixteen free H_3 generators. The exact homotopy type and explicit cycles provide a comparison point for further fault calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
