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

The seven-bit neighborhood graph and the independent three-row spacetime graph each have 64 vertices, and their exact breadth-first-search minima agree for all 256 rules. Reproduce with `python3 verify_windows.py` and `python3 verify_spacetime.py`; compare the `minimum_ring_length` fields in their JSON output. The polynomial gcd program `python3 verify_rule105.py` separately checks the sharp-rule orbit formula through ring length 240. The result is finite exhaustive proof of a uniform property, not a claim that finite simulation proves arbitrary dynamics without the graph reduction.

Captured verification records: `windows_output.json`, `spacetime_output.json`, `rule105_output.json`. Numerical witnesses are rechecked directly by the first program. The Rule 105 infinite-length statement follows from the explicit polynomial gcd proof in `RESULT.md`. No independent audit has been performed.
