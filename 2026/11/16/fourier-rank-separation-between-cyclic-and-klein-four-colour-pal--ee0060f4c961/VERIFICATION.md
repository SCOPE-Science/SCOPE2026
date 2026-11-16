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
The supplied scripts reproduce the full Fourier multiplier spectrum over the two abelian groups of order four, with independent enumeration methods. `checks/verify_book_direct.py` uses a direct sum over every proper colouring and every frequency through \(n=4\), and `checks/verify_book_formula.py` uses character orthogonality and a direct three-term sum for every balanced frequency through \(n=8\). They ran successfully prior to this package. Both require only Python 3. Finite tests are corroborative; the all-order proof is given in RESULT.md.

Exact normalizations: unnormalized Fourier transform, counting convolution, and counting-measure \(\ell^2\). Multipliers at unbalanced frequencies vanish because the proper-colouring family is invariant under simultaneous colour translation. The minimum positive modulus excludes zero modes, so inverse norms refer to the Moore--Penrose pseudoinverse and the quotient by the convolution kernel. No independent mathematical audit has been performed.
