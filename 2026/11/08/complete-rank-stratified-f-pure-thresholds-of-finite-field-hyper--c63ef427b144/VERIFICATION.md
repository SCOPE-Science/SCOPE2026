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

# Verification evidence

`verify_moore.py` is a self-contained Python 3 program (no external packages). It constructs the signed-permutation polynomial for the Moore determinant, computes sparse modular polynomial powers after exact truncation by \((y_1^{p^s},\ldots,y_m^{p^s})\), and confirms that the first vanishing power is exactly the one predicted by the theorem. Tests include \(q=2,3,4\) and \(m=2,3,4\) where indicated. The independent rational-point-count census enumerates matrices over prime fields, computes exact ranks by row reduction, and divides the rank counts by the number of nonzero field scalars to compare with the Gaussian-binomial formula.

Execute `python verify_moore.py`; its output is reproduced in `verification_output.txt`. Both programs' concluding lines are `ALL_CHECKS_PASSED` and `ARITHMETIC_CHECKS_PASSED`.

The program does not prove the parameter-uniform theorem; the all-\(N,q\) arguments are the determinant factorization, linear-kernel reduction, Frobenius containment, and unique leading-monomial certificate in `RESULT.md`. The finite-field arithmetic census uses only prime-base cases; nonprime field-size Frobenius exponents are tested directly at \(q=4\). No independent review or validation is asserted.
