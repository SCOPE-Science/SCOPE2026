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

# Reproducibility

Run `python3 verify.py` in this directory using the Python standard library. The source independently constructs the undirected multigraph of binary necklaces with weight at most the chosen bound, uses a labeled-edge bridge algorithm to test the claimed two-or-four forbidden transitions, and constructs the full directed binary overlap graph to check the existence of an Eulerian circuit through each candidate consecutive edge pair after contracting the pair into a shortcut.

The undirected check covers 63 parameter cases for \(1\le n\le13\), \(1\le k\le\min(n,6)\). The independent directed contraction check covers 45 parameter cases for \(1\le n\le9\), \(1\le k\le n\), and verifies the locally admissible candidate count. Actual output from the program:

```
BRIDGE_CHECKS_OK 63
EULER_CONTRACTION_CHECKS_OK 45
VERIFY_OK
```

These are finite reproducibility checks, not an assertion that an infinite theorem was exhaustively tested. The all-length proof is in RESULT.md. All computational evidence is reproducible from the included standalone file; no network, external scripts or unavailable library dependencies are required.
