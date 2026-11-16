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

Exact verification is supplied in the same directory as `verify_recursion.py`, `verify_bruteforce.py`, and `kernel6.json`. Run both Python programs without external dependencies.

The first checker generates all \(231\)-avoiders of sizes one to six recursively, computes exact binary-field ranks, verifies twenty independent integer left-kernel vectors against every degree-at-most-two incidence column, and exhaustively enumerates the twelve admissible three-swap cubes. The second independently generates the relevant sets by checking forbidden triples, computes ranks over the field with three elements, rechecks the signed kernel vectors directly, and checks the explicit parity-cube construction. Both replayed successfully.

A modular rank bound alone would not establish a real upper bound. Here twenty independent *integer* null vectors provide the missing upper bound, while rank \(112\) over \(\mathbb F_2\) gives the lower bound. The statement for all larger orders follows from an explicit symbolic embedding; no finite check is extrapolated to infinity.

The computations do not establish full higher-degree ranks or unindexed-literature priority. Independent mathematical audit has not been performed.
