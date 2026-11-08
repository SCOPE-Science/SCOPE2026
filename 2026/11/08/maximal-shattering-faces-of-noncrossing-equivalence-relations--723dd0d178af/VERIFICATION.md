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

# Reproducibility and limits

Run `python3 verify_noncrossing.py` using the standard Python 3 library. The script independently generates unrestricted set partitions with restricted-growth strings, filters noncrossing partitions from quadruple violations, computes every pair-equality concept, and compares direct trace shattering with the theoretical one-edge-deletion criterion.

For orders \(n=2,3,4,5,6\), it exhausts all \(2^{\binom{n}{2}}\) query supports; for \(n=7\), it exhausts every support of size six. Both checks compare the top stratum against an independently implemented tree plus geometric-crossing predicate. It also checks the diametral crossing matching's graph structure for even orders four through fourteen. Exact stdout is in `verification_output.txt` and ends with `NONCROSSING_PARTITION_SHATTERING_PASS`.

The unrestricted proof is in `RESULT.md`. The exact top-stratum count uses the published noncrossing-tree formula; its identification with the shattered supports is proved in the result. Neither finite enumeration nor successful exit alone establishes the universal statements, and no independent mathematical auditing is claimed.
