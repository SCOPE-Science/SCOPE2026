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

Decomposition at every simultaneous zero gives the unique gap-product law, with positive first-block coefficients b_m of 1−1/A(z), A(z)=sum C_m²z^m. In the frozen Schur-complement proof, the compression of multiplication by the product of two Catalan moment variables is a bounded positive operator; its v-spectral moments are b_2,b_3,… and hence log-convex. The first missing determinant is b_1 b_3−b_2²=9. The local lattice ratio cancels when the two sites are in different gaps and is b_(y−x)b_L/(b_(L−x)b_y) when in the same gap. Log-convexity gives this inequality by consecutive ratios; local squares imply full log-supermodularity, then finite FKG implies positive association. Arbitrary positive site fields cancel from the squares. The untilted strict pair covariance follows from the explicit Catalan joint/marginal ratio and the strictly increasing Catalan ratios. Semilength 2 has only one possible site, so the pair clause is vacuous. Independent Boolean inclusion-count inversion through n=8 recovers b_1,…,b_8=(1,3,18,141,1280,12778,136374,1529713) and checks all 1023 lattice squares at those orders; the all-n argument is analytic.

## originality

FAIL

The two pivotal items claimed as new, the first-common-return renewal decomposition and the all-order log-convexity certificate for its block weights, follow from established results. In fact Liu–Pego's Hausdorff/Pick equivalence gives the stronger assertion that the entire shifted block sequence b_(m+1)/16^(m+1) is a Hausdorff moment sequence, with no exceptional first-index argument. For the classical product-renewal law this supplies exactly the hypothesis of the elementary two-cut FKG criterion. Thus the complete claimed specialization follows by direct standard implications even without an earlier paper using its exact Dyck wording.

## value

FAIL

The distinction between association and the full, tilt-stable FKG lattice property is scientifically meaningful. In this frozen example, however, the hard-looking first-common-return weight property is already a direct stronger moment consequence, the lattice test is an elementary gap-factor comparison, and the strict unweighted two-point calculation is a direct Catalan ratio. No additional nonmechanical invariant or structural conclusion is established beyond those deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
