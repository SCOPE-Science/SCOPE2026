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

# Reproducible checks
Run `python3 verify_mixed_hamming.py` with standard Python 3 (no third-party modules). For thirteen complete graphs, the program independently lists center neighborhoods, enumerates all Boolean traces of supports up to size four, and evaluates adaptive rank through a finite minimax recurrence. It tests the asserted piecewise table for both open and closed conventions, yielding 26 exact finite comparisons. It constructs and rechecks two depth-three decision trees on the ternary rook graph; the eight leaf centers in each tree reproduce all prescribed answers. `checks.txt` is the captured successful output. This verification does not replace the symbolic proof for unbounded alphabet sizes or dimensions; no independent scientific audit was conducted.
