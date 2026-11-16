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

# Mathematical verification

The exact symbolic reproducer `verify_tree_quadratic.py` computes the parameter derivatives of \((1-r^2)/(1+qr^2-r\lambda)\), simplifies their cubic-denominator numerator to the theorem's explicit polynomial, and confirms its degree is at most two for formal parameters. It substitutes both exact rational extreme examples at \(q=4\), \(r=1/4\) and verifies their exact squares / endpoint factorization. It also tests finite-site Gram positivity on a radius-two piece of the five-regular tree at the origin and both boundary examples. It was executed successfully with SymPy and NumPy.

The proof of global positivity, completeness of the extreme-point list, and finite-site strictness does not rely on the finite-site tests. Its noncomputational inputs are the classical spectral interval and absolutely continuous Kesten measure, together with elementary positive polynomial geometry. No independent mathematical audit or external certification has been carried out.
