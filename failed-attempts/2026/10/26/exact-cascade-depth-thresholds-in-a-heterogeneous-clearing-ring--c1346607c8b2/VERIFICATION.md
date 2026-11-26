---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Admissibility keeps operating resources nonnegative, so the proportional clearing update maps [0,1]^n into itself. The row-wise Lipschitz constants are lambda_i<1; hence the fixed point exists uniquely. In deficits put Lambda_i=product_{j=0}^{i-1} lambda_j and T_i=sum_{j=1}^i s_j/Lambda_j. Induction along the unshocked banks gives d_i=Lambda_i(d_0-T_i)_+; the induction uses s_i>0 to absorb the outer positive part. If sigma<=s_0+T_{n-1}, the candidate d_0=(sigma-s_0)_+ has d_{n-1}=0 and satisfies the fixed-point equations. Since the T_i strictly increase, exactly the stated prefix defaults, with equality at tau_i leaving bank i solvent. If sigma>s_0+T_{n-1}, the actual fixed point has d_0>=sigma-s_0>T_{n-1}, which forces every downstream deficit positive. In this branch closing the ring gives the stated derivative 1/(1-product_i lambda_i) at bank 0 and its downstream attenuations. The full-cascade interval can be empty, and even at its boundary the last bank still pays in full. This proof does not assume a feasible shock reaches a formal threshold.

## originality

FAIL

The heterogeneous all-depth formula is more explicit than the related homogeneous-cycle and ring endpoint statements inspected. It is nevertheless a mechanical specialization of proportional clearing: each unshocked node has a single incoming payment, and each scalar positive-part affine deficit map has positive slope and negative intercept. Composing them gives a single hinge with a back-discounted sum for its break point; applying the closing equation below and above the final hinge gives the whole claimed classification. This is direct implication, not a claim that the exact heterogeneous list was found in prior literature. A missing lawful full-text copy of Eisenberg–Noe is not the grounds for failure.

## value

FAIL

Thresholds for contagion depth are a natural quantity, and the expression is a convenient benchmark for a toy topology. In this model the sole-predecessor and single-shock restrictions reduce the entire question to serial evaluation of one scalar hinge and a one-equation closure once every bank defaults. The exact thresholds are mechanically implied, and the finding adds no nonroutine multi-path effect, previously unresolved comparable-model threshold mechanism, or distinct structural result beyond this calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
