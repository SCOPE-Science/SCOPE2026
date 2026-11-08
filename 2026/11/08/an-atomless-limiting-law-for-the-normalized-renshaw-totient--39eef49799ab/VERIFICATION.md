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

# Reproducible checks and proof boundaries

Running `python3 verify.py` from the directory containing the supplied files reproduces `verification_output.txt` using only the Python 3 standard library. It checks direct \(T(n)\) enumeration and its CRT approximation for \(1\le n\le1200\); exact formulas for inputs divisible by four; the distinctness of all \(1024\) finite-prime products formed from the first ten odd primes; and the first normalized mean through \(X=100000\) against a finite Euler product.

The first-moment numerical comparison uses truncation, and the finite-prefix injectivity test is only a finite illustration. The mathematical proof in `RESULT.md` separately establishes the universal CRT estimates, probabilistic weak limit, Euler product convergence, injectivity for arbitrary finite prime prefixes, absence of atoms, and full support. These infinite statements have not been independently audited. A numerical match alone cannot establish them, and no convergence rate is inferred.
