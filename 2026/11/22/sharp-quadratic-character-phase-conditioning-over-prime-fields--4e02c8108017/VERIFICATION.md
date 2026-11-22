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

# Reproduction and verification

The theorem is proved symbolically in `RESULT.md`, including the exact multiplicative-character block decomposition, character-sum bounds, explicit determinant and trace inequalities for the constant block, the exceptional \(p=5\) upper-edge comparison, and the asymptotic computation. The only non-elementary imported ingredient is the standard Gauss/Jacobi relation \(|J(\chi,\psi)|=\sqrt p\) when all three characters \(\chi\), \(\psi\), and \(\chi\psi\) are nontrivial.

Run `python CHECK.py` using Python 3 and NumPy. The program uses primes \(5,7,11,13,17,19,23,29,31,37\), each with three nonzero shifts. It directly constructs each phase matrix, computes its singular values, tests the claimed endpoints, tests the proposed quadratic-character weak vector, checks strict separation from the next singular value, and compares the constant-block endpoint formula. The observed result is `PASS 140 singular-value, unique-minimal-mode and block checks`. Finite double-precision experiments are not proofs of the universal or strict statements.

The phase normalization is \(\omega=\exp(2\pi i/p)\), with complex (unnormalized) singular values. The code does not claim independent validation, an exact finite certificate for all primes, or historical novelty certification.
