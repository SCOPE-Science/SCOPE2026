---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Finding's inequalities, equality classes and rigidity are mathematically correct. For f=h_K² the intersection norm squared is the frame sum. The columns are exchangeable and orthogonal, not independent (correct the word 'independent' in RESULT.md:32); the proof uses their correct conditional law. Projection removes degrees zero and two, since these are exactly the restricted quadratics. For each even surviving degree 2m the covariance identity and equatorial average give multiplier d[1+(d−1)p_{d,2m}(0)]. The product ratio (2m+1)/(d+2m−1) is strictly less than one for d≥3. The extreme positive and negative equatorial eigenvalues on the residual space are at degrees four and six respectively, giving the constants and the equality spaces. Separately generating the normalized zonal polynomials via their differential equation (python /workspace/independent_checks.py 3) recovers the critical multipliers in symbolic dimension; this is a check, not the proof for every degree. The perturbations sqrt(1+εY) are support functions by positive definiteness of the spherical curvature operator for sufficiently small ε, and K is an ellipsoid iff the defect vanishes. No uploaded verifier was executed. There is also a false ancillary limitation in RESULT.md:56 (not needed for the Finding): the least-squares Q is globally positive definite here. Indeed for F(x)=h_K(x)^2 extended homogeneously and standard Gaussian G, the projection formula gives 2Q=E[F(G)(GGᵀ−I)]=E[D²F(G)], in the distributional integration-by-parts sense. F is convex and F(x)≥r²||x||² for an inscribed origin-centered ball of radius r>0. On any line its second derivative measure is positive and nonzero (the quadratic lower growth precludes an affine function); integration against the strictly positive Gaussian density gives vᵀQv>0 for every v≠0. Thus the warning about a nonpositive nearest quadratic does not describe an actual obstruction under the stated assumptions.

## originality

FAIL

Direct prior implication, not an access-based rejection. Goldstein–Lebowitz–Tumulka–Zanghì, arXiv:1406.2576v2, analyze the same Haar frame sum for arbitrary real L² functions and give both its exact covariance reduction and the full real equatorial spectrum with harmonic degree labels. Removing constants and quadratics and taking the extreme remaining eigenvalues gives exactly the claimed numbers and equality spaces. Taking f=h_K² gives the geometric inequality immediately. The only further ingredients are the classical dimension-three form of the same spectrum and routine small-harmonic support-function realizability; no independent quantitative mechanism or separate novel result survives in the frozen Finding.

## value

FAIL

The supporting-hyperplane observable is well motivated and the two-sided estimate is useful as exposition. However, the asserted new content is a mechanical restriction of an exact published frame-variance spectrum and routine realization by smooth perturbations of a ball. No independent sharp geometric invariant beyond that corollary, nor new stability in a separate metric, is established in the frozen Finding. Narrowing to the realization or the classical d=3 numbers would not leave a genuine distinct valuable result. No repaired claim is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
