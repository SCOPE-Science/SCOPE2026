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

# Reproduction and scientific limits

Run `python3 verify.py` from the directory containing this file with NumPy and SciPy installed. Observed output:

```
CHECKS_PASSED 153
PHYSICAL_CHECKS_PASSED 161
```

The checker compares 130 finite Gauss–Seidel sweeps against independently evaluated triangular systems, 20 step-kernel approximations and convergence diagnostics, three near-leading eigenvalues with the nonprincipal Lambert expression, and eight Gram-square-root physical-similarity conditions. The evidence concerns finite cases and software calculations only. The mathematical proof of \(\mathcal S_2\) convergence, complete nonzero spectral description, and exact asymptotic spectral radius is supplied in `RESULT.md`; finite tests cannot certify these global claims or establish literature priority. The statements involve a canonical coefficient embedding and a distinct physical Hilbert norm, which are not interchangeable for singular values.
