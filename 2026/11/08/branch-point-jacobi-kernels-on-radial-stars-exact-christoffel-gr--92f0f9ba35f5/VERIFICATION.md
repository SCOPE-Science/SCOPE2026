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

# Verification of the Jacobi-star kernel finding

The analytical derivation in `RESULT.md` checks the cyclic projection, Beta normalization, endpoint Jacobi norms, Gamma telescoping, and locally uniform hard-edge Riemann sums. No external mathematical review or independent validation has been performed.

`check_star.py` requires Python 3 and `mpmath`. Run `python check_star.py` in a directory containing that file. Its observed output is:

```
JACOBI_STAR_KERNEL_CHECK_PASS moment_and_center=8 hard_edge=6 normalized_universality=3 total=17
```

Eight finite checks compare independent Gram-matrix evaluation with the Jacobi kernel and the closed center value. Six further finite checks compare the scaled kernel at fixed complex arguments with the integral-defined limiting kernel at two increasing degrees for each of three ray counts. Three additional checks compare the centered limits at two distinct outer Jacobi exponents and compare the corresponding finite-degree centered kernels at two shell degrees. The finite convergence tests are not an infinite proof; the locally uniform estimates are proved in the mathematical argument.

The proof does not depend on downloaded datasets, random seeds, or another finding's code. The general theorem is restricted to \(q\ge2\), \(\alpha,\beta>-1\), and identical equally spaced rays. The checker depends on `mpmath` for special functions and numerical integration.
