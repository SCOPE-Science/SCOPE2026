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

The analytic proof in RESULT.md is the controlling evidence. The standalone `check_fifth.py` is ordinary verification code and requires only Python 3 for the exact Fourier-word checks; NumPy additionally enables independent torus-grid integration.

Run `python3 check_fifth.py`. Observed output:

```text
Exact signed Fourier-word checks: 40 (n=1..8, k=1..5)
Independent Haar quadrature checks: 75 (exact bandlimited 401x401 torus grid)
Total checked identities: 115
```

The exact stage counts integral signed Fourier coefficients (not floating-point coincidences). The grid stage evaluates separate oscillatory integrals at phases 0, pi/6 and pi/2; the finite trigonometric bandwidth is below the grid modulus. Computations cover finite indices only; the low-length resonance classification proves all indices.

The published map is analyzed on its zero-restoring-force parameter slice, so the result must not be extrapolated to nonzero restoring force, arbitrary initial measures or the wrapped phase. No independent mathematical audit has been performed.
