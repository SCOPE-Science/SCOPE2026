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

With the stated same-sign gate and v_0=0 the first update is pure gradient descent, so v_1=s theta_0 and theta_1=(1-s)theta_0. If theta_t v_t<0, then v_(t+1)=s theta_t and theta_(t+1)=(1-s)theta_t, whose product is strictly negative for s>1 and theta_t nonzero. The asserted formulas follow; the inherited contribution is permanently zero, not the stored v_t. The multiplier has modulus s-1, giving the exact convergence factor, neutral two-cycle, and divergence in their stated regimes. The ordinary-momentum characteristic polynomial is z^2-(1+alpha-s)z+alpha; the two endpoint Jury inequalities are s>0 and 2(1+alpha)-s>0, with alpha<1 supplying the remaining condition. This gives the strict comparison window for alpha>0. The printed source indicator is imprecise, but the recurrence being proved agrees with the source prose and the frozen gate assumption. This verifies deterministic exact scalar arithmetic, not finite precision, noisy gradients, or rotated modes of a nondiagonal multivariate problem. Inspected VERIFICATION.md and the NumPy-based verify.py as finite diagnostics and did not run the uploaded script.

## originality

PASS

The narrow explicit all-iterate absorbing-branch and stability-comparison statement was not identified in the inspected prior sources. Credit the original sign gate, its gradient-descent step after a crossing, and the classical separate GD and heavy-ball thresholds; the calculation is an immediate consequence of those inputs, not a new optimizer or stability criterion in general. Its routine character is decisive on value.

## value

FAIL

The motivating stability comparison is sensible, but this exact slice does not add a nonroutine mathematical boundary. Zero initialization forces a gradient-descent step, and for s>1 textbook scalar gradient descent reverses sign on every step. The optimizer's already-intended response to that reversal forces the very same update again, independently of alpha. After this immediate observation, the entire phase diagram and comparison are exactly the two textbook GD/heavy-ball intervals, with no further branch, competition, or sharp estimate to resolve. The correct explanation may be useful pedagogically, but this frozen result does not analyze the regimes where retention versus suppression is genuinely in question. No surviving distinct claim justifies a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
