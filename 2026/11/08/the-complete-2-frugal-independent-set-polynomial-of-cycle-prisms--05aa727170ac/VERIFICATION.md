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
# Exact independent-set checks

Run `python3 verify.py`; only the standard library is required. The verifier constructs every vertex and all three neighbours in the actual labelled prism, considers all three choices per column (vacant, row zero, row one), and independently checks every candidate for independence and at-most-two occupied neighbours. Its coefficient arrays agree exactly with the cyclic-run formula for each \(3\le n\le10\).

For all \(3\le n\le80\), it additionally verifies integrality of every counted run summand and the proposed maximum size and extremal count by direct formula evaluation. These finite checks corroborate, but do not replace, the all-length structural bijection and counting proof. External independent review has not been performed. No assertion beyond the labelled cycle-prism family is implied.
