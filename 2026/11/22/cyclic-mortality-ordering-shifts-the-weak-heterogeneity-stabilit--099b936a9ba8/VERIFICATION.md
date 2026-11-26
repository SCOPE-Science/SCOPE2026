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

Independent analytic replay: on the simplex write 2Hx=1+qKx, where K has first row (0,1,-1), is cyclic skew and satisfies K²=-3I on the tangent plane. For alpha=0, x=u-epsilon Ka/(3q) then has a·x=0, D=1 and 2Hx=d. The tangent derivative is the restriction of diag(x)(d epsilon a^T+qK); its image is tangent since qKx=epsilon a and x·d=1. Its ambient trace is therefore the intrinsic trace, epsilon² sum_i x_i a_i², giving S₂ epsilon²/3+V epsilon³/(3q) with the stated sign. To verify the homogeneous term directly, for h=Hx the three-way weight is 2(h⊙h)+2H(x⊙h); normalization follows from x^T H=1-h^T. At u its tangent derivative is 3H+2H²/3. Thus J_base=qK/3, J(0,alpha)=(1+alpha/2)J_base+(alpha/2)J_base², det J_base=q²/3, and the homogeneous trace is -alpha q²/3. The first implicit-function theorem applies to the restricted polynomial field. The linear-in-mortality trace coefficient is a rotation-invariant linear form at each fixed alpha, hence vanishes on the zero-sum plane. The trace can thus be written as its exact pairwise cubic minus alpha q²/3 plus alpha epsilon² times an analytic function. The second implicit-function theorem gives the unique positive trace crossing for small nonzero epsilon of either sign, with the stated coefficients, and determinant continuity and negative trace slope give both stability sides. At p=3/4 the two directions have V=+2 and -2, and the difference is 32 epsilon³+O(epsilon⁴). This checks linear behavior at the crossing, not a nonlinear Hopf bifurcation. CHECK.py was inspected, not executed; its finite numerical runs are not proof. Its mixed-derivative tests should be read with the analytic branch and cyclic-symmetry argument, not as a general symbolic continuation of that branch.

## originality

PASS

Credit the initiating paper with the tournament model, variance scaling, exact pairwise trace and homogeneous-rate Jacobian. The supported distinction is the evaluated oriented cubic coefficient and the strict threshold difference with an identical unordered multiset of mortality rates. No inspected stronger result covers that comparison; the initiating paper's small-difference supplement remains a specific priority risk.

## value

PASS

It supplies a concrete limitation of variance or any unordered rate summary in a model where variance is already the natural leading descriptor. It identifies the first order at which cyclic assignment matters, predicts the sign, and provides an explicit same-multiset witness. That local invariant is meaningful without a claim of global persistence, empirical calibration, or Hopf-cycle classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
