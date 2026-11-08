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

# Verification

Run `python verify.py` using ordinary Python 3 and no third-party packages. The program constructs \(\mathbb F_4\) and \(\mathbb F_9\) as explicit quadratic quotient fields, computes the Frobenius involution by exponentiation, enumerates each self-adjoint upper triangular candidate with an idempotent-compatible diagonal, multiplies its matrices in the quadratic extension field, and compares all rank coefficients to the proposed formulas. The cases are \((q,n)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4)\). A passing execution ends with `VERIFY_OK`.

Observed distributions included \((n,q)=(5,2)\): \((1,16,128,128,16,1)\) for ranks zero through five, and \((n,q)=(4,3)\): \((1,0,162,0,1)\). The checker implements multiplication and the idempotency tests directly, not the unitary conjugacy proof.

The mathematical proof of the all-dimension theorem relies on the Hermitian unitriangular factorization lemma and the stabilizer count, both written explicitly in `RESULT.md`. The asymptotic proof uses an elementary comparison of central binomial ratios and discrete-Gaussian tails. Finite enumeration cannot establish either infinite claim. The full texts of two related journal papers could not be accessed, so exhaustive publication-priority verification remains outstanding. Independent audit has not been performed.
