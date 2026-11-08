---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone verifier executes with Python 3 and the standard library. It independently enumerates all binary subsets of cyclic groups of orders one through thirteen and checks the subgroup-coset classification and divisor-sum formula. For orders up to ten, it explicitly constructs every translate and tests each possible two-point trace against the autocorrelation count. It independently tests the elementary abelian groups of ranks two and three using bitwise group addition. The expected terminal line is `ALL_LOW_VC_TRANSLATION_CHECKS_PASS masks=16382 n=1..13 direct_n=1..10`. These checks are finite; the algebraic proof establishes the unrestricted result.
