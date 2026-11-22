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

# Verification notes

The exact algebraic certificate is the identity
\[
AB+BA+C^2+\frac{I}{24}=
\frac12\bigl(A+B-(A-B)^2\bigr)+\frac32\left(C-\frac I6\right)^2.
\]
The first bracket is positive semidefinite because \(A+B\preceq I\) and \(-(A+B)\preceq A-B\preceq A+B\). The proof gives a self-contained positive-contraction factorization justifying the noncommutative matrix inequality. The witness uses exactly rational diagonal entries and \(\sqrt{30}/12\) off-diagonal entries; its coefficient has exact eigenvalues \(1/12,-1/24\). The equality proof uses annihilation by both positive summands and reconstructs the common reducing two-dimensional block.

Reproducibility: run `python verify_z3_effects.py` with `numpy` and `sympy`. Its exact symbolic tests confirm the witness and contact polynomial. Its seeded randomized tests include 9,000 convolution coefficients for dimensions \(1,2,3,4,6,9\), plus 999 rank-one family points; those calculations cannot establish an all-dimensional theorem, and this proof does not depend on them. The checker is embedded in full.

Only an internal self-review has been performed. The cited 2024 work on POVM Jordan negativity could not be inspected in full; no bibliographic uniqueness or independent validation is asserted.
