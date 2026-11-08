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

# Verification of the quantum-ring capture theorem

With Python, NumPy, and SciPy available, run the self-contained checkers:

```shell
python check_resonances.py
python check_decay.py
```

`check_resonances.py` constructs the physical cyclic matrix in position space and compares the resulting eigenspace projection to an independently generated Fourier energy-class partition for all even sizes from six through fifty, at first resonance and additional detunings. It passes 115 comparisons, including the analytic values \(p_6=4/9\), \(p_8=1/3\), and \(p_{12}=2/9\).

`check_decay.py` computes no-capture norms by matrix exponentiation of the full non-Hermitian generator, including different positive loss rates and detunings, and compares to the spectral formula. It passes 20 tests. The long but finite propagation times are chosen so that numerical convergence is observed within the test tolerance.

The all-size claim is not based on finite tests: exact Fourier eigenvalues, an energy-class bright/dark decomposition, a unique discrete cosine minimum, and an opposite-parity approximation supply the mathematical proof. Finite-time checks cannot establish infinite-time decay in general, and spectral comparisons do not certify research priority. No external independent scientific validation has been performed.
