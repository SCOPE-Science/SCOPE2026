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

# Reproducibility and proof limits

The original numerator is evaluated by three independent integer algorithms in `CHECK.py`: the two-index Bergman polynomial, the centered triangular sum and an independently reindexed residue formula. The script checks their agreement for coprime pairs with \(1\le k\le9\), \(1\le n\le22\), checks reciprocal structure, compares the universal coefficient polynomial for \(1\le k\le10\) at large \(n\), and uses `numpy` to check representative polynomial root clusters.

Run `python3 CHECK.py` after installing the single package named in `requirements.txt`. During preparation the script passed **108530 assertions**. The numerical root computations are finite and floating-point; they are not an exhaustive proof of the theorem, the absence of unit-circle roots, or novel publication priority.

The infinite result instead depends on an exact finite coefficient identity, quantitative composite-trapezoid estimates for piecewise-quadratic tent products, a finite Fejér Fourier identity, and complex-polynomial root perturbation via Rouché's theorem, all specified in `RESULT.md`. The proof assumes the standard previously published Bergman numerator formula and only treats fixed \(k\), not uniform \(k\to\infty\). Independent audit has not been performed.
