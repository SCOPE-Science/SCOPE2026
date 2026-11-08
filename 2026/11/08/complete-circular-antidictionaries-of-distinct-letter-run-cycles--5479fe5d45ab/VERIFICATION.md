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

# Computational verification and proof boundary
Run `python3 verify_distinct_run_antidictionary.py` in the directory containing the script. It independently constructs the factor set from cyclic shifts, obtains each minimally absent candidate by a prefix extension with an occurring proper suffix, and compares entire sets (not just cardinalities) with the theorem's expression. It also compares the closed cardinality formula with the constructed list. A verified execution returned `PASS: 485 independent full finite antidictionary comparisons`.

The brute-force profiles cover \(2\le q\le5\), individual lengths in \(\{1,2,3\}\), total period length at most nine, and seeded additional profiles (bounded by period ten). The two-letter case is a computational boundary check. Finiteness is not an exhaustive proof for arbitrary parameters: the universal result follows from the run-decomposition argument in `RESULT.md`.
