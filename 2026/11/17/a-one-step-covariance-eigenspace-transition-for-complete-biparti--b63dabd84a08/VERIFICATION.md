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

# Verification and limitations

The standalone file `check_covariance.py` uses Python 3 standard library `fractions.Fraction` to compute all seven moment classes independently from conditional beta integration and from averaged uniform order-statistic moments on a two-antichain ordinal-sum order polytope, which is Euclidean-isometric to the original stable-set polytope. It checks every ordered pair \(2\le a,b\le15\) (196 pairs) and separately tests the exact sign of the critical integer factor over 8,970 additional integer parameter configurations.

Reproduce: `python3 check_covariance.py`; recorded result: `BIPARTITE_STABLE_COVARIANCE_CHECKS_PASSED exact_rank_and_beta_profiles=196 threshold_sign_tests=8970`. The script compares exact fractions for the moments, block matrices, and determinant identities. The script's finite range does not prove the infinite theorem. The manuscript supplies the beta integral derivation, two-block eigenspace decomposition, strict determinant sign argument and limiting asymptotics for all integers in the claimed domain. External historical priority and independent mathematical validation remain unperformed.
