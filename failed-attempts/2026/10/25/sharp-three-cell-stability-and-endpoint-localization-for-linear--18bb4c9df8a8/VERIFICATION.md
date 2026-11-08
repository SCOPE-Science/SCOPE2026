---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The RESULT fixes positive a,b,c and exact continuous linear spline L2 orthoprojection. Reconstructed the standard hat Gram matrix, alternating-sign inverse, kernel row integral formula and endpoint maximum by absolute-value convexity. Independently computed the rational row formulas and row-dominance identities with SymPy, checked positive-factor differences and both n=3 degenerating meshes, and checked 24 exact sample cellwise integrals. These exact algebraic identities, not finite sampling alone, validate all-positive-three-cell inequalities, strictness, endpoint location and fixed-mesh sign attainment. The values agree with Malyugin 1983 n=3 theorem. No statement for higher spline degree or degenerately zero actual cells is proved.

## originality

FAIL

Decisive direct prior coverage. S. A. Malyugin (1983) already proves the exact L-infinity norm of the orthogonal projector onto continuous linear splines for every knot partition (Theorem 1) and its sharp n-cell extrema (Theorem 2), with the precise 5/3 infimum and 8/3 supremum for n=3. Foucart (2008) explicitly identifies this k=2,m=1 finite-breakpoint case as settled by Malyugin. The submitted work omits that original and presents its n=3 special case as new. A shorter-end algebraic expression does not rescue the original covered final finding as a whole.

## value

FAIL

A sharp finite-mesh stability benchmark for continuous spline orthoprojections is intrinsically mathematically motivated, and the elementary exact algebra is useful expository verification. However the submitted final contribution is a rederivation of the complete n=3 instance of Malyugin 1983 Theorems 1–2, including its headline constants and normalization; known-table recomputation is not a new scientific contribution. The shorter-boundary endpoint comparison has not been shown to be a new structurally substantive and non-implied result independent of the complete published norm formula. Correctness and reproducibility alone cannot establish distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
