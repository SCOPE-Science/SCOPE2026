---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For normalized cube Laplacian L=I-A/d, normalized Walsh characters of weight j have heat eigenvalue exp(-2tj/d). Restriction to a fixed codimension-c face aggregates 2^c inner Walsh indices by their Hamming weight r, leaving for each free index S a row-scaled m-by-(1+min(c,K-|S|)) Vandermonde matrix at distinct z_j. Thus every block has stated min rank; summing gives exact formula for all d>=1,c,K,m in stated ranges. For c>=2 two restricted degree-one eigencharacters cancel for all time. For c=1 and K=d, the precisely normalized 1/sqrt2 blocks [[1,1],[r^k,r^{k+1}]] give all squared singular values, determinant and unique D-optimal tau; derivative of log determinant changes sign only at r=(d-1)/(d+1). Independent fresh NumPy rank checks for d=2..5, all c,K and m=1,2,3, and block determinant computations at d=2..5 exactly matched predicted rank and determinant up to numeric tolerance; infinite proof is Walsh/Vandermonde.

## originality

PASS

Best-of-knowledge: earlier dynamical-sampling general finite-frame criteria apply to graph eigenspace sensor restrictions, but available sources did not establish the complete Boolean-coordinate-face rank profile, exact full-band singular spectrum or unique D-optimal second time. The closest 2026 Bulai et al. primary paper has only accessible abstract and inaccessible full text (Oxford VPN disconnected), so overlap remains a concrete priority risk; not treated as automatic failure.

## value

PASS

A fully explicit observability and conditioning classification for the most symmetric finite graph resolves a natural dimension-vs-time sensing question. The codimension-two impossibility and codimension-one two-snapshot exact recovery sharpen generic dynamical-frame criteria; the optimal second-time formula is an exact usable experimental-design invariant, rather than a mere substitution into a textbook formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
