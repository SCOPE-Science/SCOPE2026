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

## Reproducibility

Run `python verify.py` with an ordinary Python 3 interpreter. The checker constructs every relevant token edge from the base adjacency rule, independently reconstructs the proposed paths, validates simple cycles and complete disjoint edge coverage for every integer from 3 through 150, and computes the cut of the explicit parity lift. It additionally exhausts cuts through order 7 up to complement symmetry using Gray-code incremental updates.

The all-parameter theorem is established by the written coordinate classification and a parity-cut argument. Enumeration through finite order is not an infinite proof; no computational infeasibility or failure is used as a mathematical impossibility claim. The script uses no third-party packages and no external files.
