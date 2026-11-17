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

The proof is analytical and applies to every pair of integers \(a,b\ge2\). The standalone Python 3 checker, `artifacts/verify.py`, uses no third-party packages. It integrates moments of complete-clique anchored Lipschitz polytopes chamber by chamber using exact rational Dirichlet expectations, assembles and orthogonally centers independent clique blocks, and checks the claimed contrast eigenvectors and remaining spectral trace and determinant. It independently verifies the monotonic balance parameter over a finite integer grid.

Run `python3 artifacts/verify.py` in the directory containing this file. Expected completion message: `TWO_CLIQUE_POLAR_COVARIANCE_CHECKS_PASSED clique_sizes=5 ordered_pairs=25 exact_matrix_entries=1325 balance_profiles=1936`.

The exact calculations cover clique sizes \(2\) through \(6\) and balance-profile dimensions \(3\le N<90\); the theorem in `RESULT.md` proves all parameters beyond these ranges. Numeric approximations, sampling, and external theorem-certification systems were not used. A separate independent mathematical audit has not been performed.
