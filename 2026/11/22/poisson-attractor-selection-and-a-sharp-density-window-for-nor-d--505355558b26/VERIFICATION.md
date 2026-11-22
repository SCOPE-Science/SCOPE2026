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

The reproducible checker is the included standard-library Python file `verify_nor_cube.py`. Invoke `python3 verify_nor_cube.py` and verify the final `PASS` line. Its finite test covers all \(65{,}812\) states for dimensions one through four, compares direct trajectories with an independent neighborhood-union polynomial, checks \(F^3=F\), and confirms the exact first-image moments and universal-orbit identification. The analytic Poisson bound uses the published local-dependence theorem with \(b_1=N(1+D)r^{2d}\), \(b_2=NDr^{2d-2}\), \(b_3=0\); the critical window follows since \(N=2^d\) and \(D=\binom d2\). The finite checker is not an infinite proof or an independent audit. No external certification has been performed.
