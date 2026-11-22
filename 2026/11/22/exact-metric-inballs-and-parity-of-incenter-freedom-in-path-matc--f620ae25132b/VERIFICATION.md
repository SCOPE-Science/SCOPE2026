---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Mathematical verification and limits

The symbolic proof checks the exact path matching–stable-set correspondence, the complete irredundant facet description, the unsigned-incidence Gram form, and its all-order inverse. The facet-normal squared lengths are \(i(n-i)/n\) and \((n-1)/n\), with no omitted facets. The global inradius follows from tight adjacent facet inequalities, and its equality cases prove the entire optimal-center affine dimension. These are analytic arguments for every integer \(n\ge3\).

Run `python verify.py` from the directory containing that standalone file. The checker uses rational matrices to verify the inverse identities and upper facet lengths for \(3\le n\le30\), independently enumerates perfectly matchable vertex subsets for \(3\le n\le14\), tests the predicted parity-dependent central equality set and a strictly feasible relative-interior witness, and, with optional SciPy, independently optimizes the complete facet-clearance linear program for \(3\le n\le50\). All checks passed when run in the reviewed environment. Exact successful completion strings were `PATH_MATCHABLE_INBALL_PASS n=3..30; enumerations n=3..14` and `Independent LP verified n=3..50`. A finite replay is corroboration, not proof of the universal assertions.

The computation is confined to graph paths, uses the unscaled Euclidean metric of the vertex-subset embedding, and does not compute John ellipsoids, arbitrary-tree inradii, or the face lattice of the incenter locus. No independent external review or certification is asserted.
