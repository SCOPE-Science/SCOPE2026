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

Pass applies to the replacement RESULT.md, not an unqualified translation invariance of extremizing directions in the frozen Finding. In the stated ordinary norm, for an extremizing sign vector ε with both signs, J(ε+c1)=Jε but ||ε+c1||∞=1+|c|, so c≠0 strictly lowers the ratio. The repair specifies actual centered direction vectors and separately explains the quotient interpretation and the translation invariance of the base scores. For a maximizing interior Jacobian, cube duality and PSD Cauchy–Schwarz force any normalized maximizing direction to maximize its quadratic form on the cube; J_ii>0 makes every nonvertex direction strictly improvable in some coordinate. The repaired proof derives the threshold derivative at α<2 even across support boundaries, since the positive-part power is C¹ and the derivative of total mass in the threshold is negative. At α=2 the piecewise-affine restriction to an arbitrary segment handles boundaries without passing to a discontinuous full-support Jacobian. The exact sign-cut norm is 4AB/(A+B). Jensen is strict within each nonconstant positive-mass block for α<2, and the unique optimal mass ratio is (h/k)^γ. The positive derivative of log F on 0<k/h<1 gives unique balanced sizes (up to complement), the strict odd deficit and the asserted pattern. Sharpness comes from differentiating at an interior witness; the constant map for n=1, full-support sparsemax and the limiting softmax statement also check. No uploaded code was executed.

## originality

PASS

The repaired distinct result is the exact global optimization over simplex outputs for the normalized Tsallis power, with its strict odd-dimensional deficit and rigid interior patterns. The entmax construction and separable-entropy Jacobian, generic fixed-weight matrix step, and earlier endpoints are not credited as new. Correctly centering directions does not expand the originality claim. The judgment rests on the specific available comparisons, not on a claim of exhaustive priority.

## value

PASS

The exact mixed-norm constant measures the full probability-mass change under bounded score perturbations for a widely used sparse map. The strict odd deficit and the sharp two-block shape identify the precise obstruction to attaining the usual dimension bound, rather than just recovering a generic smoothness estimate. The revised differential direction statement identifies which score perturbations approach the bound without implying unquotiented translation invariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
