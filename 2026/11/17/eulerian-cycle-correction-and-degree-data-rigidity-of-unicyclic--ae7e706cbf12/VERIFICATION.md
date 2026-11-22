---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. Graphical-zonotope vertices correspond bijectively to acyclic edge orientations. Each orientation yields exponent Σ_v signed_degree(v)^2. Fourier-Walsh expansion of even local vertex factors survives only even-degree edge subsets; for a connected unicyclic graph these are empty and the unique cycle, giving 2^n prod F_d plus (-1)^c 2^n prod_{cycle} B_d prod_{off} F_d. Exactly 2^(n−c+1) cyclically directed edge assignments are not vertices; along those cycles signs cancel at both incident edges, leaving independent forest F_{d−2} factors to subtract. Formula depends only on length c and on/off-cycle degree multisets. Independently enumerated every acyclic signing for two nonisomorphic six-vertex C4+two-leaf graphs, obtaining identical shells {4:2,8:16,12:14,16:16,20:6,28:2}. Not a weighted/multicyclic or interior radius claim.

## originality

PASS

PASS qualified: the strongest equivalent radial theorem found is tree-only; a unique cycle contributes a nonempty even subgraph and two forbidden directed orientations, requiring new correction terms. A directly read open-access graphical-zonotope paper concerns fan/deformation geometry, while a full face-count source concerns f-polynomials, not Euclidean vertex shells.

## value

PASS

PASS. The entire radial shell distribution of a natural unicyclic family is invariant under reattachment/reordering of trees with the same separate degree data, exhibiting nonisomorphic equispectral realizations. The unique-cycle Fourier correction is a motivated structural extension of tree radial laws, not a face-vector recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
