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

Run `python3 CHECK.py` from the directory containing this file. `CHECK.py` constructs the original thin-spider edges, identifies all independent sets by directly testing those edges, computes base-graph and reconfiguration distances using independent breadth-first searches, and compares against the theorem's closed formulas. All 35 choices of \(2\le r\le8\), \(1\le k\le r\) pass, including every ordered pair of states. It also checks degree/edge/state enumerations and connectivity for each choice. A separate integer check compares the two expressions for the diameter maximum for all \(2\le r\le200\), \(1\le k\le r\).

The checks do not exhaust an unbounded parameter family and do not certify bibliographic originality. The proof, not the finite computation, establishes the all-length claim. Independent audit: not performed.
