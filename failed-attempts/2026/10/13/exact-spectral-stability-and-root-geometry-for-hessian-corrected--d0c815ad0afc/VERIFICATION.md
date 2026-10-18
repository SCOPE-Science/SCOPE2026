---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

On an SPD quadratic each eigendirection satisfies z_{k+1}=(1-beta*lambda+alpha-theta*lambda)z_k-(alpha-theta*lambda)z_{k-1}. Degree-two Jury inequalities give modal |m|<1 and 0<beta*lambda<2(1+m), m=alpha-theta*lambda. With 0<=alpha<=1 and theta>=0, monotonicity reduces interval stability to alpha-theta*mu<1 and L(beta+2theta)<2(1+alpha); latter also ensures m_L>-1. Quadratic discriminant and product/sum signs give the claimed complex/positive-real/negative-real/opposite-sign root regimes. Independently cross-checked 30000 endpoint and modal cases; unrestricted algebra is exact.

## originality

FAIL

A public October 4, 2026 primary mathematical record on the SAME constant-parameter Hessian-corrected heavy-ball recurrence already gives the exact same modal polynomial, Jury inequalities, uniform stability budget L(beta+2theta)<2(1+alpha) (for 0<=alpha<1), discriminant bands (1+-sqrt(m))^2, opposite-sign roots for m<0, and a strictly stronger modewise optimal rate analysis. Present extra alpha=1 boundary and real-root sign naming are immediate textbook extensions, not an independently original mathematical advance. Full prior RESULT.md was inspected, not inferred from a search snippet.

## value

FAIL

The submitted principal invariant and geometric phase boundaries are already contained in, or immediate elementary consequences of, the earlier stronger analysis of exactly the same method. The only extensions (alpha=1 conditional endpoint, labels for signs of real roots) are straightforward Jury/discriminant substitutions with no independently motivated new boundary or classification beyond the prior stronger result. Correctness alone is not an adequate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
