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
# Reproducibility checks
The mathematical proof relies on the published finite-graph cycle-mean theorem and on the explicitly displayed integer cycle-space and transfer-matrix arguments. The included Python programs provide separate finite cross-checks; they do not substitute for the infinite-family proof. They use Python 3 only, with no external packages.

- `code/check_spokeless.py` exhaustively computes eventual orbits for both three-state rules, for every colouring at rim lengths from 4 through 9. It checks all three activity populations, and records the observed periods as ancillary finite data. The observed-period pattern is **not** extrapolated as a theorem.
- `code/check_cycle_rates.py` independently lists all simple undirected cycles in each missing-spoke wheel for rim lengths 4 through 8, computes maximum positive directed colour-increment means, and checks the analytic classification for every colouring.
- `code/verify_spoke_formula.py` multiplies the explicit transfer matrices over 27 consecutive rim lengths and checks the closed recurrence identities and counts.

The stdout outputs are embedded as `logs/*.log`; compare them by running the scripts. For the stated ranges the output includes explicit PASS messages. No independent reviewer has performed a separate audit.
