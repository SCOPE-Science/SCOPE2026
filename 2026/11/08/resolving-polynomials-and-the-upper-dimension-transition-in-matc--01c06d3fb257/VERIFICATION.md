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

The standalone `verify.py` uses breadth-first search for the shortest-path metric of every graph in the stated finite test range. For each subset it independently checks the definition of resolving and determines inclusion-minimality by deleting each selected vertex. It compares the resulting coefficient counts with independent algebraic coefficient formulas and with the stated structural characterization.

Executed command: `python3 verify.py`.

Observed result:

`VERIFY_OK instances=41 vertex_subsets=15872 resolving_sets=4473 minimal_resolving_sets=979 distance_BFS=PASS iff_characterization=PASS all_set_polynomial=PASS minimal_polynomial=PASS`

Test range: every triple of integers with \(3\le a,b\le5\), \(a+b\le10\), and \(0\le t\le\min\{a,b\}\). This exhausts \(15{,}872\) vertex subsets across \(41\) graphs. The unrestricted theorem is justified by its proof, not by finite verification; the stochastic limit is proved by a binomial-to-Poisson argument. No independent mathematical audit has been performed.
