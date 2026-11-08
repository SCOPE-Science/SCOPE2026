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
# Verification details

The proof uses conditional uniform-spherical coordinates to derive the exact \(3\times3\) Gram density, a gamma-ratio expansion, a local cubic logarithmic expansion, and Gaussian/marginal concentration to make the error \(O(d^{-1})\) in integrated absolute value. Both extreme cdfs are then orthant integrals with explicit signs. This is a mathematical argument for fixed three points and compact normalized thresholds, not an inference from simulation. The source comparison excludes the previously published positive-order triangle effect and the exact special right-angle integral.

The standalone checker samples normalized Gaussian directions on actual spheres, compares the maximum and minimum geodesic-angle cdfs against the claimed expansion, and integrates the exact special-case right-angle formula. Run `python check_extreme_spherical_sides.py` with `numpy` and `scipy` available. Its success is a numerical cross-check only; it does not establish the uniform \(O(d^{-1})\) limit or certify historical priority. No independent mathematical audit has been conducted.
