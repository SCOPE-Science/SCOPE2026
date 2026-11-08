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

# Verification of exact observable correlations

Run `python3 check.py` using Python 3's standard library. The checker compares forward iteration with the explicit rotation conjugacy for six parameter pairs, including both signs of the common-center parameter and the equal-slope boundary. For stationary coordinate and threshold-bit sequences, it evaluates midpoint quadrature of the direct covariance definition at lags 0, 1, 2, 3, and 11 and compares against the closed formulas. The accepted numerical tolerance reflects finite mesh quadrature near circle wrap points, not a bound for arbitrary lags or parameters. The success marker is `CIRCLE_COVARIANCE_AND_STURMIAN_CHECK_OK`.

The infinite mathematical claims are not certified by those samples. Their proof in `RESULT.md` explicitly derives: (a) both affine branches' shared fixed center; (b) the monotone logarithmic rotation conjugacy; (c) the invariant probability density and Fourier coefficients of the coordinate; (d) the periodic Green kernel and its zero-modulus limit; and (e) the threshold rotation interval, Fréchet lower joint-probability bound, discrepancy telescope and minimal Sturmian factor complexity.

Scope: \(0<s,b<1\), exponent \(d=1\), equal endpoint parameter \(a=c=s\), with all stationary correlations taken under the specified pullback of circle Haar measure. For rational rotation this is one invariant probability among many. Endpoint visits are treated modulo the circle identification, and noncanonical real representatives can have one exceptional bit value; the exceptional set has invariant probability zero. No independent audit has been performed.
