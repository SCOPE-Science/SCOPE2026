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
The standalone `verify.py` enumerates every label tuple in 33 parameter pairs \((k,n)\) with \(2\le k,n\le8\) and \(k^n\le15000\) (36,490 tuples altogether). It calculates actual orbit-length histograms, compares exact Möbius formulas, checks the weight probabilities sum to one, and checks the documented \((4,3)\) and \((10,6)\) examples. Command: `python3 verify.py`. Expected output: `PASS: 33 exhaustive (k,n) pairs, 36490 labeled points; formulas, normalization, and examples verified`.

The checker does not claim exhaustive verification across all dimensions and does not numerically validate invariant densities, ergodicity, metric entropy, or Lyapunov spectra. Those assertions rely on the analytical conjugacy, the product-measure argument, Birkhoff's theorem, entropy additivity and the classical entropy formula for piecewise-expanding invariant densities. It does not address the perturbed family or Lebesgue-basin sizes. No independent mathematical audit has been performed.
