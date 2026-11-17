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

From the actual RESULT.md, geometric S_n-fixed simplices are orbit-barycenter combinations of full Hamming-weight orbits, not fixed original vertices. Independent weight-distance calculations give diam(W_i)=2min(i,n-i), max cross-layer distance=min(i+j,2n-i-j); hence the fixed model is Ind of a bipartite band graph |i-j|<t=n-r. Inspecting the explicit fold proof and verify_fixed_rips.py, left/right neighbor containments successively reduce to s+1 disjoint edges where s=floor(floor(r/2)/(n-r)), making a cross-polytope boundary S^s for all 0<=r<n. The complement involution cannot fix a point and Lefschetz gives degree (-1)^(s+1). n=1,r=0 and r>=n agree with the exact models. The 55 direct orbit comparisons, 1,220 fold sequence checks and 28 explicit collapses in the saved verifier output corroborate, rather than replace, the unbounded argument.

## originality

PASS

Best-of-knowledge PASS for the full all-scale geometric S_n-fixed classification and complement character; ambient homology representations and Rips cohomological bounds do not determine geometric fixed points. An earlier single-radius n-2 assertion mentioned by the package is not treated as novelty; its unidentified primary source remains a search risk.

## value

PASS

Uniform geometric fixed-point homotopy at every Hamming radius for all cube dimensions is a natural equivariant invariant, especially when ambient Rips homotopy is complex. The variable-width band collapse gives a sharp sphere-dimension diagram, and complement character distinguishes symmetry not encoded by the nonequivariant sphere count; not a parameter renaming or tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
