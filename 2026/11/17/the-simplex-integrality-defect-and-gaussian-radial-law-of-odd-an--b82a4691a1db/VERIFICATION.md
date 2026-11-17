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

Run `python3 antihole_verify.py` from the same directory as these files; no external Python packages are required. The verifier computes exact integers and rational fractions and prints an explicit `PASS 122 exact checks` line. It checks the independent maximum-clique matrix for \(n=5,7,9,11,13\), the cyclic-edge determinant, the cap determinant, the exact volume and exact squared-radius mean, together with the analytic covariance and delta-method variance.

A separate finite check used halfspace intersection on the full maximal-clique system of \(\overline{C_n}\), for \(n=5,7,9\). It found respectively 12, 16 and 20 vertices, matching precisely the predicted integer stable-set vertices plus the single fractional apex. This independently corroborates the polyhedral premise in these dimensions only.

The infinite-dimensional-in-parameter conclusion (every odd finite dimension) is established by the explicit determinant proof and the cited Koster–Wagler/Padberg theorem. The central limit theorem follows by one-dependent sums and the delta method. Finite checks or numerical simulations are not treated as proofs of those unrestricted statements. No external mathematical audit has been performed.
