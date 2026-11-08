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

Run `python verify.py` using Python 3.10 or later (standard library only). The script generates cyclic clique graphs, computes exact random-greedy expected independent-set sizes by the first-selected-vertex recurrence over residual vertex masks, and compares them to the analytic formula evaluated via a convergent exponential series using decimal arithmetic. Exact arithmetic is used for the graph expectations; a high-precision numerical comparison tests the formula but is not an infinite proof. The analytic proof in `RESULT.md` supplies the all-parameter identity and the strict sign.

The finite checks cover clique orders three through five, ring sizes three through six subject to a 24-vertex cap, plus additional sign tests. The source and scripts do not assert externally certified correctness or historical priority.
