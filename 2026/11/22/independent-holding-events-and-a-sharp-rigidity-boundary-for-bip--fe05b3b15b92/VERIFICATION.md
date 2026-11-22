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

# Verification of the cut-first exchange classification

The only executable dependency is Python 3's standard library. From a directory containing this file and `verify.py`, run `python verify.py`. An actual run of the packaged checker returned: `PASS 2345 exact assertions; K(3,3) holding variance 2/10125`.

The checker constructs all labelled spanning trees of \(K_{2,b}\) through \(b=6\) and \(K_{3,3}\), computes cut sizes and crossing-host-edge counts with exact rational arithmetic, verifies the holding probability and the sharp increment identity, tests both shape witnesses for three bicliques of width at least three, and checks pairwise detailed balance of the finite transition kernels on \(K_{2,3}\) and \(K_{3,3}\). No simulation and no floating-point calculation enter the stated exact tests. They are finite cross-checks: the all-size and arbitrary-horizon assertions depend on the deterministic structural proof in RESULT.md.

The exact chain definition is crucial. The common alternative insert-first then cycle-delete procedure has a different transition kernel and should not be used in this verification.

No independent external mathematical audit has been carried out.
