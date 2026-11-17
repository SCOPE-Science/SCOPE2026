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

Run `python verify_tree_isotonic_bv.py` from this directory with Python 3.10 or later; no optional libraries or external data are required. The checker independently calculates exact rational values from connected-subtree enumeration, from active-edge partition averaging on every cut-indicator basis vector, and from the rooted-side knapsack recurrence. It also builds strict KKT input vectors for every considered active forest and verifies 1,504 perturbed local projections with exact rational multiplier solutions. The check covers 20 complete finite test trees, plus side-profile and strict-KKT comparisons on selected trees. These tests establish reproducibility and catch normalization/edge-counting mistakes but do not replace the general combinatorial proof for all finite trees. No claim of independent audit, formal verification, or exhaustive all-tree enumeration is made.
