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

# Reproducing the finite evidence

Run `python check_cycle.py` with Python 3 and no extra packages. Check that it prints `ALL_CYCLE_3_COLORING_SHATTERING_CHECKS_PASS`, as recorded in `checks_output.txt`.

The program enumerates proper three-colourings, calculates exact VC dimensions for orders three through eight and exact Littlestone dimensions through seven by a separate minimax recurrence, checks all cyclic-window witness traces, and verifies all branches of the constructive online tree through order ten. It also compares the number of proper colourings with the chromatic polynomial and the predicted vertex–colour balance.

The analytic proof is all-order. Finite checks are consistency tests, not an infinite certificate. The online dimension for orders eight through ten is verified using a depth witness and the analytic counting upper bound, not an exact minimax run in those orders. No independent mathematical review is claimed.
