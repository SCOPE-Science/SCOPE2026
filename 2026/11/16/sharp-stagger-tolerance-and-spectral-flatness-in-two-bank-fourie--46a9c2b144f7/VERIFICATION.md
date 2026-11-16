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

The analytical proof derives the complete \(2\times2\) fiber Gram trace and determinant from a unitary Fourier decomposition. The global upper bound is fixed by the zero-residue block. Testing the quadratic at its lower squared singular value gives the exact phase interval, with a common lower squared singular value at the boundary. A root monotonicity computation and the parity arithmetic finish the claim.

The included standalone `hermite_shift_check.py` requires NumPy and is run with `python hermite_shift_check.py`; it reports `HERMITE_SHIFT_CHECKS_PASS 1791`. It constructs full complex matrices for \(1\le m\le32\), several shifts and four derivative weights, then independently checks their singular values against the fiber formulas. It checks the optimal phase plateau, the sharp boundary and the one-dimensional even-grid half-shift singularity. Numerical tests are not proofs for unbounded grid sizes; the symbolic argument supplies the universal assertions.

The exact spectral conventions and the physical-noise normalization limitations appear in `RESULT.md`. Historical priority beyond inspected sources remains unverified. Independent mathematical audit: not performed.
