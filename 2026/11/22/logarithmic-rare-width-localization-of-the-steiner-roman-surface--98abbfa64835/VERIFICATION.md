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

# Verification and reproducibility

Run `python verify.py` from the directory containing the embedded source. Requires Python 3, NumPy and SciPy. The diagnostic compares 2,500 exact spectral-width evaluations with direct symmetric-matrix eigenspectra, checks all eight minimum directions and three coordinate-axis maximum directions, verifies 51 monotone exact CDF quadratures, compares five thresholds against 524,288 independently sampled unit directions, and tests four lower- and four upper-endpoint asymptotic ratios. All 2,577 deterministic assertions passed on the packaged source.

At width tolerance \(\varepsilon=0.001\), the exact/narrow-tail leading-term ratio was approximately \(1.003481527857\). At tolerance \(\varepsilon=0.0001\), the exact/two-term wide-tail ratio was approximately \(0.999847871102\). These numerical observations do not prove the infinite limits; the analytic Rayleigh, local-tangent and matched-integral arguments appear in `RESULT.md`.

The proof is for the complete quadratic image of the unit sphere, its convex hull, and Haar-uniform viewing directions; it does not establish stability for deformed surfaces, a two-dimensional shadow area distribution, or a quantitative remainder bound beyond the stated little-o terms. Independent audit has not been performed.
