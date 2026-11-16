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

The proof is analytic and uses no computer-assisted infinite inference. Its critical steps are the exact Fourier factorization, the \(R^{-1/2}\) endpoint rescaling, a nonstationary-phase averaging argument, Fresnel integrals with fixed normalizations, and continued-fraction approximations valid for every irrational aspect ratio.

Run `python3 CHECK.py` from an extracted package to perform a small collection of direct numerical quadrature sanity tests using only Python's standard library. The checks sample six exactly resonant radii across three rectangular aspect ratios, and two generic radii for the two-term profile. Finite quadrature does not verify the asymptotic limit, the all-real-radius little-o term, or historical originality. No external audit or independent validation has been performed.
