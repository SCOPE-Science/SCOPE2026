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

The full result is analytic. The key exact identities are the branch monomial matrices, the occupation-to-eigenvalue correspondence when the final cyclic residue is zero, and the Fourier identity \(\operatorname{Re}[(1+\omega)/(1-\omega)]=0\) for \(\omega^3=1\), \(\omega\ne1\). These imply the Green–Kubo covariance \(\Sigma=I/3-\mathbf1\mathbf1^\top/9\). The standard finite-state spectral argument establishes the endpoint-conditioned central limit theorem; bounded second moments supply the uniform integrability used for the mean.

Run `python check_occupations.py` with Python 3.9 or later. The checker performs exhaustive exact-integer checks over every binary word of length 3 through 11 (except the all-left word), with direct matrix products and residue counts. The computation is finite and does not certify the infinite central limit theorem or independent mathematical validation.
