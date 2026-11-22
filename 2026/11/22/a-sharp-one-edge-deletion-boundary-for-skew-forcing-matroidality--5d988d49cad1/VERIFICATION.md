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

# Verification

Run `python3 verify.py` using Python 3 without third-party dependencies. The program independently implements the exact skew color rule, exhaustively checks the closure-exchange axiom over all vertex subsets for every `K_{a,b}` minus one edge with `a+b<=10`, checks the explicit size-parametric exchange witness for `3<=a<=40, 2<=b<=40`, and checks the exceptional star/isolated direct-sum closure through 13 leaves. Successful run ends in `VERIFY_OK`. These computations corroborate rather than prove the unrestricted cases.
