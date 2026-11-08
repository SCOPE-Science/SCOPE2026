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

The unrestricted integral homotopy theorem is proved in `RESULT.md`, using the published connectivity and homology theorems and the independently established primitive spherical top classes. The finite checks are corroboration only.

Reproduce with `python3 verify_bidirected_wedge.py` from the directory containing the supplied files; no nonstandard Python modules are needed. The program checks the directed-path face predicate and face counts, exact maximal-facet orientation patterns, and complete mod-two boundary ranks for bidirected cycle sizes from four to nine. It also constructs a greedy acyclic matching for the pentagonal case, checks all 190 nonempty Hasse covers for acyclicity, and confirms the resulting critical-cell distribution. The full program output in `verification_output.txt` ends with `ALL_BIDIRECTED_CYCLE_CHECKS_OK`.

Finite mod-two Betti numbers do not certify integral wedge decompositions. The required integrality instead follows from the top-chain argument, Hurewicz, and Whitehead; no computational claim extends beyond the stated tested sizes. Independent review has not been performed.
