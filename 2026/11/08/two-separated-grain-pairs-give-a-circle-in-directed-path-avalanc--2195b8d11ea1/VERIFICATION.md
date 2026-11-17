---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Binary threshold-one parallel firing shifts the four support positions right by one per round until sink absorption, so all generating simplices are precisely clipped translates. Set L=g+2. At each of t trailing-zero removal stages, the terminal vertex link is a triangle joined to an edge along a cone apex, giving exactly five legal free-face pairs and deletion K_m -> K_(m-1). At base m=L+2 one tetrahedron, one triangle and consecutive edges admit four elementary pairs deleting vertex 0, then three free-face pairs eliminating the two triangles/pendant leaf, leaving C_L. Total 5t+7. Independently reconstructed all simplices and checked exact freeness at each pair for 72 L,t instances; proof itself is uniform and covers arbitrarily large g,t.

## originality

PASS

The 2026-11-01 published one-bar filtration theorem uses identical four-grain initial support and proves the terminal complex is S1, hence the S1/homology/one-grain corollaries are ALREADY COVERED, not novel. Its complete published proof is by successive homotopy pushouts along contractible attaching subcomplexes and does not provide an elementary simplicial collapse onto a specific canonical L-cycle, or an all-parameter 7+5t free-face certificate. The audited final claim is the latter stronger simple-homotopy/collapse statement; it is not a logical corollary of homotopy equivalence alone. Do not claim novelty for the terminal S1 or persistence.

## value

PASS

An explicit uniform simplicial collapse with exact linear cost and an identified canonical polygon is a motivated combinatorial-topology strengthening of an existing family homotopy calculation. It provides a concrete simple-homotopy witness, not merely another homology rank; this extra assertion has independent structural content despite known terminal S1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
