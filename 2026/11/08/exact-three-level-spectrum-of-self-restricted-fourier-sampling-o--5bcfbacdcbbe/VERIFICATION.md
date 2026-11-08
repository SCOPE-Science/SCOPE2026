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

The self-contained checker `check_spectrum.py` constructs finite fields of sizes \(2,3,4,5\), enumerates their invertible two-by-two matrices, independently calculates the ambient finite-field character sums \(K(A)\) for every ambient matrix, checks the full Gram matrix, and compares every singular value and multiplicity against the theorem. It uses Python 3 and NumPy and exits nonzero on a failed assertion.

Observed output (replayed from the packaged checker):

```
q=2, |GL_2|=6, Gram spectrum=[(4, 5), (8, 0), (16, 1)], condition=2, direct Fourier check PASS
q=3, |GL_2|=48, Gram spectrum=[(9, 10), (27, 16), (81, 22)], condition=3, direct Fourier check PASS
q=4, |GL_2|=180, Gram spectrum=[(16, 17), (64, 50), (256, 113)], condition=4, direct Fourier check PASS
q=5, |GL_2|=480, Gram spectrum=[(25, 26), (125, 108), (625, 346)], condition=5, direct Fourier check PASS
GL2_RESTRICTED_FOURIER_SPECTRUM_PASS
```

The universal result relies on the exact general Fourier coefficient identities, the full operator identity, the elementary irreducible decomposition and Schur orthogonality proved in `RESULT.md`. The four finite tests provide a reproducibility check, not proof for infinitely many fields. No independent mathematical audit, certification or verification channel has been completed.
