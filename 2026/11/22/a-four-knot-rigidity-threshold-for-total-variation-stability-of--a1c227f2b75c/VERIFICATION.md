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

With the weighted quadratic loss written with a factor 1/2, b=-M^{-1}C^T 1 gives strict positive KKT multipliers at the zero affine fit. Since C has kernel span(1,x) and full row rank, small perturbations leave the fit in this affine subspace with a linear formula and positive multipliers. The weighted normal equations express its slope as a positive linear combination of the nodal increments with coefficients c_j. A unit step maximizes the resulting l1 gain L max c_j, and is realizable near b. The gap-weighted average of L c_j equals one by testing v=x. All c_j agree precisely if each interior knot equals the centroid, impossible with at least two distinct interior knots, and at three knots equivalent to m_1 h_1=m_3 h_2. The three-site projector has only the identity and affine pieces; four uniform sites have exactly four candidate piece operators. Integrating along a finite partition of an input segment yields the upper bound (boundaries use continuity). Independent exact arithmetic recovered the face norms (1,7/6,7/6,6/5), both positive multiplier vectors and input/output variations 1 and 6/5 for the explicit witness. Also checked 1,600 rational three-site cases, an irregular-grid gain of 902/769, and the uniform-grid formula through n=39; the affine slope summation proves the general lower bound, not the finite checks. Frozen verifier inspected, not executed. Independent replay: python3 /workspace/evidence/convex_bv_exact.py.

## originality

PASS

Best of available evidence: the result concerns the deterministic two-input Lipschitz norm on the quotient by constants, using unweighted adjacent variations of nodal values. Neither the documented affine-fit ingredient, standard convex projection machinery, isotonic contractivity, nor nearby coordinate-norm constants supplies the strict all-mesh obstruction together with the sharp initial coefficient. No equivalent or dominating theorem was identified in inspected sources.

## value

PASS

The deterministically relevant quantity is variation of a change in the estimate, not mean-square error or variation of a single fit. A sharp mass-balance exception at three sites, universal failure for every positive mass profile and mesh from four sites on, and an attained first failure of 6/5 give a usable shape-constrained stability boundary. The limit 3/2 applies to the constructive lower bound only; no exact longer-grid or arbitrary four-site norm is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
