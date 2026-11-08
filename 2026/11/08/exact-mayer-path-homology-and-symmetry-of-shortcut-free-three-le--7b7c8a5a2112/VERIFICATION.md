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

The standalone `verify.py` is executable with Python 3 and the standard library alone. Run from this directory with `python3 verify.py` and compare the standard output with `verify_output.txt`.

The code independently enumerates allowed elementary paths, computes the full forbidden-face matrix, constructs a basis of its kernel, and checks every exact boundary rank over the prime field of order 2521 at primitive roots of orders 2 through 10. It evaluates every permitted Mayer index for eight parameter triples and compares them with the closed dimension formulas. It also performs chain-level permutation-matrix checks of the full representation character for three parameter triples and all eight simultaneous transposition patterns in the three levels at five root orders.

The proof is algebraic over the complex numbers. Modular ranks and characters are finite tests only. The input model has no source-to-sink shortcut, no augmented degree-minus-one chains, and no higher directed paths. The tested dimensions are not an exhaustive search of the unbounded parameter domain. No independent mathematical audit has been performed.
