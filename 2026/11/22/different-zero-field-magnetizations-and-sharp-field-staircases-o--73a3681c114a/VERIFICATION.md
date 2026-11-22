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

Run `python3 verify.py` using Python 3 standard library. Each implementation computes the minimum induced-edge count and number of extremal vertex subsets for every size 0 through 9, on each of the two explicit 27-edge cubic graphs. Each scans all 262144 vertex subsets, with no random samples. The two enumeration algorithms use direct edge summation and least-significant-bit recurrence, respectively, and assert all tabulated integers. A separate evaluation of linear energy branches produces all field plateaux and degeneracies. The reported output is `ALL_EXHAUSTIVE_CHECKS_PASSED`.

Limits: exact finite computation certifies only the specified 18-vertex graphs and the stated Hamiltonian. No independent audit or literature-priority certification has occurred.
