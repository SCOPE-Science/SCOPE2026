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

# Reproduction and mathematical limits

Run `python3 checker.py` from this package. The program has no third-party dependencies and reports `PASS: 532 independently indexed covariance/mean and spectral checks.` It enumerates every length-\(n\) word for \((q,n)=(3,5),(3,6),(3,7),(4,5),(4,6)\), computes each mean and mixed second moment with exact rational arithmetic, and verifies all entries of the proposed covariance. It also checks the constant, circulation and standard-contrast actions plus spectral trace and squared-trace identities for six alphabet sizes.

The rigorous all-size assertions follow from the explicit five-shift overlap proof, invariant subspace decomposition, squared radical inequalities and the bounded-dependent multivariate central limit theorem in `RESULT.md`. Finite enumeration alone does not establish generality. Independent mathematical validation was not performed.
