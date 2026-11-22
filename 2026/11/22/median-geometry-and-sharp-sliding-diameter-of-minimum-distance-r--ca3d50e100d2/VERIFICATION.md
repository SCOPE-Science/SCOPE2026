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

Run `python checker.py` using Python 3.9 or later. The checker enumerates all minimum radius-r dominating sets from their original vertex subsets, calculates legal original-path slides, and uses BFS from each state to compute true distances. The observed result was: `PASS 90 parameter cases, 183806 ordered-pair shortest-path checks` for radii 2–5 and respective lengths 1–21, 1–22, 1–23 and 1–24. It verifies the claimed exact number of states, connectivity, full all-pairs metric and diameter at every tested parameter choice.

The exhaustive run concerns only the explicitly stated finite range. The infinite theorem is established symbolically from the coverage-gap bijection, legal-move correspondence, order-ideal interval and stars-and-bars calculation in RESULT.md. The median and isometric-dimension conclusions use standard finite distributive-lattice facts; they are not independent external certification.
