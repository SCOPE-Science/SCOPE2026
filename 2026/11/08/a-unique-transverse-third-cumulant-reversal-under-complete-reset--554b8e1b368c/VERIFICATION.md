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

# Reproducible verification

The self-contained `verify.py` uses the Python 3 standard library only. Run it from the extracted package with `python3 verify.py`. Its independent Cartesian real/imaginary Fourier–monomial generator implementation evaluates stationary moments exactly as rational numbers rather than using the factored formula to generate them. It then compares 100 combinations of strictly positive rotational diffusion and resetting, including zero or positive thermal diffusion, against the explicit stationary mean, transverse second moment, mixed raw third moment, and cumulant factorization.

The verification additionally checks all polynomial coefficients, sign restrictions, the exact boundary substitution identity, illustrative thermal threshold ordering, and limiting-scale probes. Replay produced: `PASS: 713 exact-rational assertions and independent limiting checks`; the dimensionless example \(d=1\) gave \(R(1,0)\approx2.011189483675225\), \(R(1,1)\approx0.6552389514134325\), with thermal floor \(\sqrt2-1\approx0.41421356237309515\).

The unique-root and monotonicity statements for every permitted parameter are established in `RESULT.md` by polynomial signs, Descartes' rule, the intermediate value theorem, and an exact boundary factorization. A finite verifier is not an independent proof of those quantified statements. The stochastic model assumes a constant-rate clock resetting both position and orientation; other reset protocols are not covered. No external independent audit has been performed.
