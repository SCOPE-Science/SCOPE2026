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

# Computational checks and limits

The `VERIFY.py` script uses Python and SymPy to build monic integer polynomials by iterated polynomial resultants, independently factor their reductions over finite prime fields, and compare all squarefree factor degrees with the stated residuosity and Frobenius-order cases. It also checks that all factors at repeated-root primes have degree at most the exponent prime and checks the characteristic-exponent specialization.

Actual execution: `python VERIFY.py` printed `status: PASS`, with **243 squarefree reductions**, **22 repeated-root reductions**, **265 prime/case tests**, and five parameter cases, for all rational primes below 251. Tested cases include \(p=3\) with radicands \((2)\), \((2,5)\), \((2,5,7)\); \(p=5\) with \((2,3)\); and \(p=7\) with \((2,3)\).

The finite calculations are not an exhaustive check of the infinite theorem. The argument for arbitrary parameters and all primes uses explicit Kummer independence, the affine Galois action, Frobenius cycle types, Chebotarev, and elementary finite-field extension containment. No independent mathematical audit has been performed.
