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
The antiunitary theorem is proved by the symmetric quadratic part \(T=(A+A^{-1})/2\), the identity \(T^2=(I+A^2)^*(I+A^2)/4\), an exact constrained-pair scalar maximization, connectedness and circular symmetry, and the equivalence of quadratic-norm attainment with the peripheral spectral projection being nonzero. The infinite direct-sum example has a missing norm-attaining eigenvector and a nonzero spectral-edge limit.

The self-contained finite diagnostic script `verification_example.py` was executed with Python 3 and NumPy and returned `PASS: 603 deterministic algebraic and finite-block assertions`. It covers planar rotation blocks and finite truncations only, and is not used to certify the infinite-dimensional spectral criterion. The same analytic proof covers degenerate cases \(\rho=0\), \(\rho=1\) and \(|q|=1\). No independent mathematical review or external certification has been performed.
