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

The center is the unique vertex of degree greater than two, so automorphisms permute equal-length arms. The matching complex is the independence complex of the line graph. Delete all central edges to get the join X of A_i=Ind(P_(ell_i−1)); the link of central edge i replaces its factor by B_i=Ind(P_(ell_i−2)), with the empty-face join unit for ell_i=1. Cone interiors are disjoint. In a path, deletion of the penultimate vertex leaves a cone and its link is shorter by three. In residue one, the inclusion B_i→A_i has cofiber the suspension of the contractible path complex Ind(P_(3k−2)) for k≥1, and is the identity for k=0. Hence it is a homotopy equivalence: use the homology isomorphism on equal sphere types, including component bijection for S^0. Residue zero has contractible B_i; residue two has contractible A_i. Thus two residue-two factors make all links and X contractible, exactly one yields one suspended exceptional link, and with none the r equivalent link maps cone off X zero, one, or r times. After the first such cone the remaining r−1 attach by null maps. When s=0 the all-unit case is a set of r isolated vertices; the single residue-two case adds a separate cone vertex to a contractible component. For the integral action, a generator of each relevant factor lies in degree k−1, so the augmented join orientation contributes (−1)^k to an equal-arm transposition. Orient link classes using their isomorphisms to the base and orient cones by the apex first. The relative boundary is then the ordinary augmentation on R tensored with the join orientation lattice, so its integral kernel is exactly the claimed signed lattice. The exceptional link index is fixed in the one-residue-two case, and its cone has the same sign character. The frozen Python and recorded 765 rank/146 trace checks were read as bounded corroboration, not rerun or used to infer the integral lattice.

## originality

PASS

The full mixed-arm phase/count formula together with the actual integral equal-arm action is distinct on inspected evidence. Earlier broad wedge and suspension reductions, the matching classification for arms of lengths four and six via subdivision, and the uniform four-edge integral sign-twisted augmentation case are credited as covered; no priority is inferred from the absence of other matches.

## value

PASS

The all-size classification determines precisely when a natural one-branch tree matching complex is contractible, how many spheres survive, and which orientation signs and integral lattices occur under full arm symmetry. Mixing lengths gives distinct phenomena, notably cancellation after adding a second residue-two arm and a single coherent augmentation lattice across different residue-one lengths. These facts supply data not obtained just by knowing a forest matching complex is a wedge or the equal-arm four-edge specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
