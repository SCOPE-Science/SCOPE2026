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

The test script `check_cone.py` uses Python 3 and NumPy. It reconstructs the polynomial and polar pairing for finite prime fields and for \(\mathbb F_9\), checks the cone size, checks the exact integer-valued signed polar-character matrix identity, checks the Fourier Gram identity, and compares the complete numerical singular spectrum against the claimed multiplicities. Runs cover \(q=3,5,7,9,11\) and \(m=1\), plus \(q=3,5\) and \(m=2\), with both quadratic-form types and several distinct nontrivial additive characters.

Observed result: `ODD_QUADRATIC_CONE_SELF_FOURIER_PASS`. The largest absolute singular-value error in the eleven tested cases was less than \(2\times10^{-13}\).

These computations are finite tests, not a complete enumeration of all finite fields or dimensions. The universal conclusion rests on the algebraic proof in `RESULT.md`. No independent mathematical audit has been performed.
