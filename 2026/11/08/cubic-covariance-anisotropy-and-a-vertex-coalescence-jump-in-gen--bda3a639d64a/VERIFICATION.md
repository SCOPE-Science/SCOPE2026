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

# Reproducibility and scope of verification

Run `python3 check_parking_covariance.py` beside the extracted document files. The script requires the Python 3 standard library only. It reconstructs every distinct vertex in dimensions 2 through 6 for three exact rational parameter pairs. It computes full covariance matrices exactly, verifies the action on the all-ones vector and a transverse contrast, and checks the independently derived two formulas against the exact matrix eigenvalues. The script also checks limiting constants at dimensions 100, 500 and 2000.

Analytically verified ingredients are (1) exposed orbit decomposition with correct handling of coalescence at \(a=1\); (2) coordinate-sum and squared-norm identities; (3) permutation-equivariant spectral decomposition; (4) convergence of all factorial-tail moments; (5) Poisson and positive-Poisson variance identities; and (6) the leading cubic-degree asymptotics. The finite script is not an all-dimensional formal proof. Historical priority remains provisional. No independent mathematical audit has been performed.
