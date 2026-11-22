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

# Reproducibility checks

The proof in `RESULT.md` derives the finite-Blaschke boundary-speed identity, the full quadratic expansion and all strict positivity claims by elementary exact Fourier and hyperbolic identities. Critical calculations requiring verification are the residue-class geometric moment sum and the strict concavity of the parallel sum of two hyperbolic tangents. The conjugate-pair normalization produces half-Hessian coefficients \(\kappa_{n,k}\); the actual real Hessian has eigenvalues \(2\kappa_{n,k}\).

Run `python3 check_hessian.py` in the same directory. This standard-library checker passed 1,399 finite diagnostics: exact closed-form spectrum versus series, conjugate-symmetry and positivity, exact unperturbed variance versus pairwise Poisson kernel integration, independent finite-difference curvature, and end-regime least-curved Fourier modes across \(5\le n\le17\). The finite checks are supporting tests, not proofs for arbitrary \(n\) or radius.

The theorem is local for \(n\ge5\); it does not determine exact transition radii, their uniqueness, all global minimizers, or radial perturbations. Prior literature and its remaining priority risks are described in `REVIEW.md`. Independent audit: not yet performed.
