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

# Reproducibility

Run `python check.py` with Python, SymPy and NumPy. The checker verifies the symbolic derivative identity, exact quartic Fourier resonance enumeration, positivity/negativity signs behind the one-root proof, a root bracket, the sharp equality example, numerical random tests, and the range of the five-point cyclic centered derivative. A successful output reports the algebraic root, the sharp real fourth-power norm and the two-norm spectral benchmark.

The infinite collection of possible real inputs is handled by the analytical phase reduction and Descartes sign proof in RESULT.md, not by finitely many test cases. No independently validated proof certificate is asserted.
