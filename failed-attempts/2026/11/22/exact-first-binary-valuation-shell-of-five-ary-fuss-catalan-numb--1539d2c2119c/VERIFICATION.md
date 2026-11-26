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

The odd denominator leaves the Kummer count of carries in n+4n unchanged. Independently eliminate the four no-incoming-carry states. With suffix GF A_uv for zero carries, their equations are A00=1+t(A00+A01), A01=1+t(A10+A11), A10=1+t A00, A11=1+t A10. They give 1+t A10=1/D for D=1-t-t^3-t^4. For one carry the only productive carry-generating transition is from 10 with input 1: the next column must have both operand bits zero (or be part of zero flushing), giving a source term t(1+t A10) at state 10. Eliminating the same zero-carry transitions with this source yields t^3(1+t)/D^2. This treats L=0 and end padding without extrapolation. Independent replay: python /workspace/review-work/check-shell.py, which also computed the digit-sum counts through L=15 and checked literal quotients modulo four for n<256. The first nonempty block contains n=5, verified by the integer quotient test. The unique dominant root r=1/phi is a double pole with normalized coefficient r(1+r)/((1+r^2)^2(1+2r)^2)=(3+sqrt(5))/50. The parity product has leading coefficient phi^4/5, giving the stated ratio. No claim about other arities or valuation levels is needed.

## originality

FAIL

A distinct indexed same-day record gives a complete rational bivariate distribution for exactly the same sequence and dyadic blocks. Its first coefficient in the valuation variable exactly recovers the shell, from which the other asserted counts and asymptotics follow. This establishes subsumption, not who obtained the theorem first or any direction of dependence.

## value

FAIL

Valuation one is a natural and useful refinement of parity. However, the frozen exact invariant and its consequences are mechanical extractions from the separate complete GF for precisely the same dyadic blocks. The frozen record supplies no distinct nonmechanical result beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
