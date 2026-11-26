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

Let H(X)=ΛX+XΛ, M=t uu^T+s vv^T and P0=(2Λ)^(-1). The Riccati equation becomes P=P0-H^(-1)(PMP), with invertible differential at zero; the real analytic branch is positive definite and stabilizing by continuity. For the full nonnegative quadrant strict stability of the open loop gives stabilizability, and Q=I gives detectability. With Z=H^(-1)(P0MP0), expansion gives P=P0-Z+H^(-1)(ZMP0+P0MZ)+O((|t|+|s|)^3). Taking the mixed trace gives sum_{ij} (u_i v_i)(u_j v_j)/(4 λ_i^3 λ_j(λ_i+λ_j)); symmetrizing gives K. Analyticity and axis cancellation supply the sharper O(ts(t+s)) remainder with positive mixed-trace sign in Δ. All w are products u_i v_i. Equal rates give rank-one PSD K; for unequal a,b the principal determinant numerator on denominator 64a^6 b^6(a+b)^2 is ab(a+b)^2-(a²+b²)^2=-(a-b)^2(a²+ab+b²). The 1,2 example has K11=1/8, K12=5/192, K22=1/256; w=(1,-4) gives -1/48. Strict complementarity follows for small t=s>0; n=1 and zero directions are included. Inspected checker.py and its recorded 2,043 exact assertions, not executed; the all-parameter conclusion follows from the expansion and determinant, not the rational grid. This is a zero-strength result, not global submodularity.

## originality

PASS

Known first-order Riccati support sensitivity and Gramian set-function results do not supply the sharp mixed-sign classification in the sources inspected. Novelty is the all-direction iff and strict two-mode obstruction, not existence of Riccati derivatives.

## value

PASS

The result identifies exactly when every pair of weak channels has nonnegative leading defect and supplies an exact, minimal two-state complementarity witness despite open-loop stability. This distinguishes a genuine design boundary from a single counterexample, without implying a guarantee for finite-strength greedy selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
