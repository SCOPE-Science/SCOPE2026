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
# Verification and reproducibility

The proof in `RESULT.md` is the all-dimensional justification. Two standalone checks are included as supplementary reproducibility artifacts; neither is presented as an independent audit or infinite-dimensional certificate.

`python verify.py` requires only Python's standard library and uses exact rational arithmetic. It checks the rank of finite simplex-skeleton boundary maps over \(\mathbb F_2\), the Gram determinant of the braid-chamber generators, every formula for the chamber rays and coefficient product in dimensions \(2\) through \(9\), support-membership equivalence and constructive decomposition, and affine interpolation on sampled barycentric-simplicial chains. The packaged run reports `PASS: 12615 exact assertions; n=3..10, all skeleton ranks and barycentric tests`.

`python verify_volume_hulls.py` optionally requires NumPy and SciPy; it constructs the full set of coordinate permutations of the exact chamber-ray expressions, projects to an affine chart, and recomputes convex-hull volumes. For \(3\le n\le5\) and all \(1\le s<n\), it reports `PASS: independent convex-hull volume ratios for 9 (n,s) pairs`.

All verification is finite. The general proof independently establishes the piecewise-linear deformation retraction and verifies all boundary parameter values. It computes the coefficient through exact determinant/product identities and separately proves the unclipped terminal-phase range. No unproved numerical extrapolation, formal proof assistant, or independent expert check is asserted.
