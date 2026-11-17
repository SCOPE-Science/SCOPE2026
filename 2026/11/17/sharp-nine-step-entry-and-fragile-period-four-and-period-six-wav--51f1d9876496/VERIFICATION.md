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

Exact checks: `python3 verify_capped.py` exhaustively checks all 19,683 nine-trit states and all 826 realizable quotient cycles; `python3 verify_labeled.py` exhausts seven finite labelled graphs. The supplied `.out` files contain actual deterministic output. The finite quotient, not small graph samples, establishes the claim for arbitrary shore sizes. The 1995/1997 finite-graph papers were unavailable in full text; independent validation remains unperformed.
