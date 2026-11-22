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

# Reproducibility

Run `python verify_min_total_cycles.py` with standard Python 3. The program enumerates total dominating sets directly from the original cyclic neighbor condition for orders 3 through 20, retains only minimizers, checks all query supports through size five, compares exact polynomial coefficients and structural predictions, tests size-six obstructions for orders up to fifteen, and verifies alternating reduced Euler characteristics on eleven representative orders.

Expected terminal line: `MINIMUM_TOTAL_DOMINATION_CYCLE_PASS 93592 60 11`. The three integers are the direct support comparisons, polynomial coefficient comparisons, and reduced Euler checks, respectively.

The unrestricted reduction and the parity-dependent odd-cycle trace lemma are written out in `RESULT.md`. Neither the finite computation nor the Euler-characteristic checks establish the claimed unrestricted homotopy type on their own. That type follows from the graph models, the spanning-tree collapse and the simplicial-join identity. No external mathematical validation has been performed.
