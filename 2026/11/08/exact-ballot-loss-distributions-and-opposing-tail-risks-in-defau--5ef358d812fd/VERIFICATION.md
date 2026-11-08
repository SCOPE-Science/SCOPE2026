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

# Reproducibility

Run the included `verify_cycle_loss.py` with Python 3 (standard library only). The verifier does not depend on remote services, datasets, or unpublished files.

The script independently constructs the complete lost-ballot distribution by iterating over casting configurations and following each voter to the first casting delegate or a noncasting cycle; it compares this against the polynomial recursion with exact rational coefficients. All 16,739 loopless functional graphs with two through six labelled voters are included in the structural bound tests at two rational probability choices; 2,534 graph cases have direct full-distribution comparisons. It also verifies the closed-form six-voter tail-risk inequality at one rational test point. Observed: all tests passed.

Proof for general \(n\) is analytic, and finite enumeration does not establish the unbounded theorem by itself. The code is a transparent regression check of critical calculations. Independent audit has not been performed.
