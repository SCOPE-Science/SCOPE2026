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

# Verification and limits

The self-contained `verify.py` enumerates all graph edge deletions for cycle sizes \(3\) through \(10\), independently recomputes incidence Gram determinants in exact integer arithmetic, obtains component-size products from graph traversals, and checks the complete finite mean formula. It verifies the deletion maximizing indices, evaluates a strict Kullback–Leibler identity and positive Schur-complement variances, compares the exact Gamma moment with the Stirling prefactor, and evaluates exact conditional log-product moments for composition sizes \(30,60,120\). The recorded execution returned `PASS 2086 exact Gram, moment, conditional fluctuation, KL and Stirling checks`.

These are finite computations. The all-size equalities and asymptotic limit theorems rely on the symbolic determinant, generating-function, and conditional Fourier-inversion proofs in `RESULT.md`, not the numerical checks. No independent mathematical audit or external certification has occurred. Reproduction requires Python 3 and SymPy.
