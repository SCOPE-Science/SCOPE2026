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

# Reproducibility and limits

The proof uses only exact radial Hermite overlap formulas, elementary incomplete-gamma integrals and a polynomial factorization valid for every integer index. The standalone `CHECK.py` uses symbolic polynomial integration for the first fifteen levels, verifies 39 adjacent-gap identities and independently integrates ten disk radii numerically. It prints `HERMITE_DISK_TRIPLE_CROSSING_PASS algebraic_differences=39 integrated_profiles=15 numeric_radii=10` on success. This check supports but does not replace the infinite-dimensional analytical proof.

The normalization is \(r=\pi(x^2+\xi^2)\), so disk area equals \(A\) exactly, and \(h_1(t)=2\sqrt\pi\,t h_0(t)\). The theorem concerns spectral *adjacency* and the global maximizer; it does not assert that no separate, nonadjacent lower levels happen to coincide.

No independent mathematical audit has been performed.
