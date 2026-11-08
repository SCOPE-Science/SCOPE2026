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

# Reproducibility and scope

The proof in RESULT.md is the certificate for the universal characteristic-\(p\) statement. The standalone `verify.py` uses only Python's standard library and direct modular Gaussian elimination. From a directory containing that file, execute `python3 verify.py`. The exact output generated for the listed tests is embedded as `verification_output.txt`.

The verifier constructs coefficients of \(f_\lambda^3\) by two independent degree-three binomial expansions, builds the central graded matrix explicitly, computes its rank at \(\lambda=0,-1,2,1/2,3\), and checks the nonzero Toeplitz minor and the triangular determinant at the degeneration \(\lambda=0\). It also checks every graded map of multiplication by \(f_0^3\) has maximal rank. The tested primes are \(7,11,13,17,19,23,29,31\). Finite tests corroborate but do not prove all prime characteristics or assert complete classification of exceptional cross-ratios.

No independent validation, independent audit, or externally certified proof is claimed.
