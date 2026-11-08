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

## Exact arithmetic checks

Run `python3 check_core.py` from the directory containing that file. The script uses standard-library `fractions.Fraction` and verifies the full selected-branch core graph and invariant weight equation for every integer \(2\le k\le150\). During review it reported 22,648 exact rational core-state checks and 705 physical-lattice point checks, all passing.

## Analytical check and boundary conditions

The exhaustive finite-state transition formula for all integers \(k\ge2\) is proved by five cases: left endpoint, left interior, central node, right interior, right endpoint. Half-open core boundaries \(c/2\), \(c\), \(1-c\) are included in the intended branches. Normalization of the invariant weights, detailed balance and annealed metric transitivity use exact finite graph algebra. Separately, the physical maps act as left/right nearest-neighbor translations of every two-sided dyadic lattice point for all positive admissible perturbations, giving the classical random-walk arcsine law without an extra core-theorem hypothesis; the strict inequality at the central point requires a positive perturbation. The cosine basis proves the spectrum for all integers \(k\ge2\). No independent audit was carried out.

## What has not been checked or claimed

Finite tests do not establish the general theorem. No full-parameter resolution of the source problem, uniqueness on the entire core, almost-everywhere initial-state law, or strong mixing of this periodic finite chain is asserted. The priority comparison remains conditional on the inspected sources and available indexes.
