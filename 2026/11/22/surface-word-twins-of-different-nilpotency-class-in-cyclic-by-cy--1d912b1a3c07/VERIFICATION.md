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

# Verification of the surface-word fiber formula

The file `verify.py` enumerates group elements by exponent pairs and implements group multiplication and group inversion directly. It records each commutator as a derived-group coordinate, then compares all fiber cardinalities to the exact rational expression obtained from integer Ramanujan sums; it does not use floating-point comparisons. The same calculations check convolution at genera \(2\) and \(3\) and independently enumerate determinant values for four small Heisenberg instances. The output in `checks.txt` records the seven group cases, four determinant cases, and final `ALL_CHECKS_PASS`.

Reproduce with `python verify.py` in a directory containing that file; Python 3 and its standard library suffice. The full proof establishing arbitrary prime-power parameters and all genera is given in `RESULT.md`.

Verification limits: the finite checks do not establish the general theorem, independently certify historical novelty, or evaluate word maps outside the stated family.
