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

# Reproducibility and limits

The source `artifacts/verify_gold_gabor.py` requires Python 3. Optional NumPy is used only for a direct projector-Gram spectrum cross-check in the smallest instance. Run from the result directory with:

`python3 artifacts/verify_gold_gabor.py`

It constructs \(\mathbb F_{2^m}\) for \(m\in\{2,3,4,5\}\) using irreducible binary polynomials, computes graph indicators and every overlap, applies exact integer Walsh--Hadamard transforms, and independently verifies the complete predicted nonzero ambiguity magnitude counts for the tested \(r\)'s. At \(q=4\), optional NumPy constructs all 256 time-frequency projector vectors and checks the complete Gram spectrum against \(N|A_g|^2\). The actual execution printed `GOLD_GABOR_ALL_EXACT_TESTS_PASS` and `direct_projector_Gram_eigenvalues_q4=PASS`.

A separate exact finite-field check of the polar radical and derivative-fiber formulas for degree six verified both parity branches and multiple exponents. Neither finite test proves the infinite family. The mathematical proof rests on finite-field subfield kernels, multiplicative cyclic groups, exact character orthogonality, and the full Weyl-basis identity in RESULT.md.

Independent audit and validation have not been performed. No claim about nonlinear phase retrieval follows from the measured complex-linear rank.
