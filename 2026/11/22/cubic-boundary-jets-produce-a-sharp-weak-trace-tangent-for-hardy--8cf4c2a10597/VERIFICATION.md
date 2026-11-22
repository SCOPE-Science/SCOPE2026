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

# Reproducibility and verification

The exact Hilbert–Schmidt identity is \(\sum_{n\ge1} n^2\|h\varphi^{n-1}\|_{H^2}^2=96\). After the Cayley, Laplace, and dilation unitaries, the integral kernel is \(32\sqrt2 e^{-2x}(x-2u)e^u\mathbf1_{u<x}\), whose squared double integral is also \(96\). The trace-class comparison remainder is the product of Hilbert–Schmidt operators with squared norms \(1/4\) and \(1/3\), and the inverse Liouville variable covers exactly \((0,1)\). The potential is positive and explicitly printed in RESULT.md.

Run `python3 verify.py` with the Python standard library to check the monomial coefficient sums (exact rational arithmetic), transformed kernel norm (exact rational moments), and reported leading constant. These checks do not replace the proof of the Weyl limit: that limit is proved by compact-support form density and two-sided min–max inequalities in RESULT.md. No independent audit has yet been performed.
