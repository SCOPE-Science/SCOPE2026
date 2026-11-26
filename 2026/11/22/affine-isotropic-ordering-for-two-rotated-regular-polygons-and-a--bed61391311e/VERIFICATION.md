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

Each gap between successive distinct tangent normals contributes two polar sectors with radius sec(t), 0 <= t <= g_i/2, giving A=n S_1 and J=n(S_1+S_3/3)/2. Repeated normals add zero to these sums. Since n>=3 the centroid is zero and the covariance is J/(2A) times the identity, giving the determinant divided by A^2 exactly as stated. For two gaps use ab=1-(a+b)/T, where T=tan(pi/n), to obtain the positive bracket in (2); the sum of tangents has negative derivative until the midpoint. Coincidence and half-step yield the specified regular n- and 2n-gon classes, respectively. For three gaps, varying q in (alpha-2epsilon,(1+q)epsilon,(1-q)epsilon) changes S_1 by q^2 epsilon^3/4+O(epsilon^4) and S_3 by 3q^2 epsilon^3/4+O(epsilon^4) relative to q=0. Differentiation of F=(3S_1+S_3)/(3S_1^2) at (T,T^3) gives delta F=-q^2 epsilon^3/6+O(epsilon^4), verifying the cancellation and, with q=1/2, the precise coefficient in (3). The largest coordinate agrees and the second partial sum increases by epsilon/2. For fixed k>3 append equal delta entries and subtract (k-3)delta from the common largest coordinate; for sufficiently small delta<epsilon/2 this preserves the partial-sum inequalities and the sign by continuity. No uniform smallness or global Schur-concavity is inferred. The analytical checks are replayable from RESULT.md Steps 1–4. VERIFICATION.md and check_geometry.py were inspected, not executed; the 1140 reported finite checks are secondary (the sampling loop repeats some inputs since its weights depend on the sample index modulo seven). Usual terminology would call the displayed normalization L_K^4; the formula defines the precise quantity unambiguously.

## originality

PASS

The known normal-gap moment geometry is not new. The distinct content supported here is the strict normalized covariance ordering on the entire two-copy phase interval and the explicit opposite-sign majorization witness for three copies at every n. The closest statements on rotational overlap, Mahler comparison and isotropic constants of other intersections do not cover those signs. This is a bounded priority comparison.

## value

PASS

A sharp ordering of a standard affine invariant for the basic two-copy rotation family supplies precise extremizers, and the positive three-gap construction establishes an actual limit to extrapolating that ordering by majorization. The sign cancellation and its persistence for every n are substantive, rather than a numerical example or a new name for a known moment formula. The classification is complete only for the two-copy case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
