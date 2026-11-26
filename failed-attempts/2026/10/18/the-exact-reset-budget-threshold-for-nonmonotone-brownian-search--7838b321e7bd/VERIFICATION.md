---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The stopping rule permits mu resets and kills at alarm mu+1, giving n=mu+1 attempts. One attempt survives until an alarm with probability q=1-exp(-z) and lasts q/r on average, yielding the stated sum for unconditional time. Its derivative has the sign of z(1-q)S'_n/S_n-2; the weighted index mean increases strictly on appending n+1, and the derivative test tends to 1 and 0 before subtracting 2 at the two endpoints. Independently reconstructed the global n=21 rational bound and all 116 positive coefficients via interval homographies, and reproduced the strict n=22 witness margin at q=6/7 exactly. The positive atanh tail gives the claimed upper and lower log bounds. This covers every r>0; the endpoint signs and the positive interior sign imply both types of extrema, without proving uniqueness.

## originality

FAIL

The exact theorem, including the sign for every rate and the same positive witness rate, is already covered by a distinct indexed record, not just suggested by the motivating paper. Its date is later than the frozen record's date; coverage at review does not establish who derived the theorem first. The certificates use different positivity arguments but the frozen mathematical claim is unchanged.

## value

FAIL

The first failure of monotonicity is a natural and useful boundary of finite-budget resetting. The frozen result adds no new boundary, parameter regime, derivative comparison, or reusable positivity theorem beyond the indexed exact result. Its different certificate is a valid verification of an already covered invariant, not a supported distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
