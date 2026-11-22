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

The standalone `CHECK.py` was run with Python and mpmath and passed 84 finite diagnostics. It checks spherical harmonic multiplicities for dimensions 2, 3, 4, 5, 7; the Tricomi-to-saddle ratio at several weighted exponents and dimensions; and finite radial-cutoff endpoint estimates in three regimes. The checks are not substituted for the analytic proof.

Critical proof dependencies are the beta-moment diagonal formula, convergence of the ordinary oscillatory endpoint for \(\lambda-\gamma>-2\), a rotated-saddle asymptotic with the \(e^{i/2}\) correction, a uniform integration-by-parts tail bound for \(\gamma\le1\), and the matching high-degree endpoint construction. Independent audit has not been performed.
