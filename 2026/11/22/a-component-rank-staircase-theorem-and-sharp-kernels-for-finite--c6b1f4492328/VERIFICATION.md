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

The general proof inducts on a finite rank threshold and exhausts local extensions into an occupied equivalence component and fresh singleton-component extensions. Its necessity and sufficiency arguments transfer arbitrary local ranks to a sorted staircase of unused-component ranks. The ordered-chain specialization then inducts on the two concrete extension types: insert into a marked chain gap, or create a new chain. Necessity and sufficiency are both established, and the boundary cases of the empty host, no unused chains, and zero-length gaps are stated.

Run `python check_chainrank.py` from the extracted package directory to compare a direct one-point-game recursion with the closed formula on all disjoint-chain hosts of up to ten vertices, over every marked subset and thresholds zero through four. The construction of both computations is visible in the source. Its observed result was `ALL_CHECKS_OK 66963 marked host configurations (each through 4 thresholds)`.

Run `python check_component_rank.py` from the same extracted directory for a separate graph-component test. It recursively tests the actual game for every graph on each component in ten small size profiles and every marked position, versus the general staircase. The observed output was `GENERAL_COMPONENT_CHECK_OK 838 marked graph-component positions`. Both checkers are finite regression tests, not substitutes for the all-size proof. The literature overlap check reviewed the 2026 definition and pure-order theorem, identified distinct first-order invariants in two indexed disjoint-chain results, and retains priority uncertainty from the inaccessible indexed full texts. No independent review is represented.
