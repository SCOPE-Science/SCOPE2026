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

The finite certificate is `verify.py` together with `ORBIT_CLASSES.json`. Running `python3 verify.py` enumerates all maximal antichains of Boolean lattices through five atoms using a standalone maximal-clique algorithm, checks their maximality, computes every shattered support with trace-class splitting, and determines all six-support symmetry orbits by applying all permutations of five atoms.

The expected antichain counts are 2, 3, 7, 29, 376; the five-atom shattered support count vector is 1, 32, 285, 1090, 1780, 1224, 310, followed by zero at size seven. The exact six-support orbit sizes are 5, 5, 10, 15, 15, 20, 30, 30, 60, 60, 60. These are exhaustive finite tests. The unrestricted exponential lower bound and Sperner upper bound follow by the explicit mathematical arguments in `RESULT.md`; the script is not used to infer them.

A completed local run terminated with `BOOLEAN_MAXIMAL_ANTICHAIN_SHATTERING_PASS`. Historical novelty beyond the inspected publications is not independently certified, and the exact dimension for six or more atoms is not determined.
