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

Reproduce from the directory containing this file with `python3 verification/replay.py`, using Python 3 and a C++17 compiler (`g++`). The replay reruns the graph isomorphism census, rebuilds two separate exact classifiers, compares full text outputs with the included certificates, checks uniqueness of the two-channel witness, and recomputes individual witness trajectories.

The graph enumeration covers every three-regular biadjacency matrix with three ones in each row and column for shore sizes three through six, modulo exact row/column permutations and shore interchange. The two classifiers each cover all \(3^n\) states on all nine canonical graph types. This is an exhaustive finite proof for those graph orders, not a sampling test or an assertion about larger graphs. Independent external mathematical audit has not been performed; historical-priority uncertainty remains.
