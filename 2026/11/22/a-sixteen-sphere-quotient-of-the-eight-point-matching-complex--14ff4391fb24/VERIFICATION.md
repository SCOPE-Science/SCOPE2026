---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Barycentric flags have one vertex per matching size, so rotations preserve their orientations and cannot identify two distinct points of one closed simplex. The signed flag-orbit boundary is thus the cellular boundary of the actual quotient. The connectivity bound floor((n+1)/3)-2 gives simple connectivity upstairs. Any based edge loop in the quotient lifts edge by edge after translating representatives to meet the previous endpoint; at the globally fixed barycenter of the antipodal perfect matching it ends where it starts. It contracts upstairs and hence downstairs. Independently of the submitted pivot calculation, each top flag has sizes (1,2,3,4), and deleting size 4 yields a unique free three-member flag in the sense of incidence: the three-edge matching has exactly two unused labels and thus exactly one completion. This bijection is equivariant. The corresponding rows form a signed identity submatrix of the integral degree-three boundary, so it is a split injection, H3 vanishes, and H2, a subgroup of its free cokernel, is free. Independently enumerating compatible edge-orbit packs, then counting fixed flags ending in a pack of r orbits by the number of surjections from r orbits to the ordered steps, gives fixed-cell vectors (763,4410,6300,2520) for the identity; (1,0,0,0) for each odd shift; (7,2,0,0) for shifts 2 and 6; and (75,194,132,24) for shift 4. Burnside gives (107,576,804,318) and Euler characteristic 17. Thus H2 has rank 16; a wedge of Hurewicz representatives is an integral homology equivalence of simply connected CW complexes and hence a homotopy equivalence. This establishes the conclusion without relying on finite-field checks for torsion or on reading Armstrong's original. The frozen verification script was inspected, not executed. The orbit-pack recipe and split-injection argument above reproduce the decisive integral calculation.

## originality

PASS

The exact catalogue match is the record under review. The strongest distinct same-size result has a different group action, and the inspected primary results treat the original complex or its characteristic-zero homology representations. No inspected statement covers the integral ordinary C8 orbit-space homotopy type. The assessment is best of current evidence, not a priority certificate.

## value

PASS

At eight labels the matching complex is simply connected by the standard connectivity bound, but the full rotation has a fixed matching and the quotient is not a covering-space calculation. The integral wedge type is a complete and useful datum for small nonfree quotients: it determines that there is no torsion or residual fundamental group, unlike what Euler characteristic or rational character information alone could establish. The different C7 outcome at precisely the same size further motivates distinguishing the action. No all-sizes or equivariant classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
