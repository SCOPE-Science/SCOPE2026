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
# Verification scope

Run `python3 VERIFY.py` next to the submitted result. The script independently enumerates every cyclic binary source of length \(5\le n\le17\) (testing all \(2^n\) targets as well), verifies exact inverse-list counts including unreachable outputs, uniquely largest all-zero fiber, exactly \(n\) single-marker runner-up targets, image sizes and singleton counts. It also verifies rational-series recurrences against explicit composition sums for all lengths \(5\le n\le122\).

The finite test covers \(262112\) candidate output vectors across these lengths, not infinitely many. The complete mathematical proof for all admissible lengths is in RESULT.md. The verifier makes no claim of independent audit.
