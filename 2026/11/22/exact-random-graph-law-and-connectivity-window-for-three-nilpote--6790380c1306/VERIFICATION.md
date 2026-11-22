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

Run `python3 check_graph_law.py` alongside `CHECK_OUTPUT.txt` to reproduce the exact small-case enumeration. The computations enumerate product maps and construct the graph directly, without relying on the formula for the graph frequencies. They confirm seven parameter pairs, but finite enumeration does not prove the all-parameter graph law or asymptotic connectivity statement. The proof establishes those statements by canonical multiplication tables, inclusion–exclusion, conditioning bounds, factorial moments, and an explicit disconnected-component bound. The historical priority comparison is not independently audited.
