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

# Reproduction

Run `python verify.py` in this directory with Python 3 and an available C++17 compiler. No network access or third-party packages are needed. The script compiles the two included implementations into a temporary directory, runs each executable, and checks their full outputs against the \(28\)-sector exact table. It also checks the graph's strongly regular parameters and its explicit nine-coclique partition, and verifies the spectral formula for every cardinality.

The completed run printed `VERIFIED: 134217728 spin states; both exhaustive methods agree; all analytical profile/degeneracies verified.`. The Gray-code program uses exact incremental cut updates; the subset-DP program uses exact induced-edge recurrences. Each visits all \(2^{27}\) binary spin assignments, so the finite counts are exhaustive, not statistical estimates. The algebraic upper-bound proof and explicit construction establish the maximum-cut profile independently of enumeration.

No finite-temperature, infinite-volume or quantum-model conclusions are certified. Independent scientific audit has not been performed.
