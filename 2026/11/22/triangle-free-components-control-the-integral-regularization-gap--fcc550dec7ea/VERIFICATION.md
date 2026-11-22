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

Run `python3 check.py` using Python 3 with only the standard library. The script independently constructs the two directed allowed-two-path boundary maps over the two-element field, computes rank of the full map and its forbidden-output projection, and compares the resulting dimension gap with the triangle-free nontrivial connected-component count. The supplied `check-output.txt` records a successful execution on all 1099 simple graphs with at most five vertices and four additional structured graphs (1103 graphs total). Its exact bitwise rank method is deterministic. It does not verify arbitrary graph sizes, integral Smith invariants, general persistent maps, or independent mathematical review; those rely on the written chain-level argument.
