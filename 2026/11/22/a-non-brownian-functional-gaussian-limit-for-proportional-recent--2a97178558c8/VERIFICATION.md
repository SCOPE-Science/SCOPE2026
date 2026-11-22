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
# Verification scope

Run `python3 check.py` with Python 3 standard library. The checker exhaustively enumerates walks of lengths two through eight with three rational pairs of memory and reinforcement parameters. It verifies all conditional transition probabilities, exact path probability normalization, finite-horizon innovation covariance decompositions, positivity bounds on the deterministic coefficients, and neutral-memory Brownian covariances. Recorded outcome: **PASS, 4,196 exact-rational assertions**.

The functional limit is an infinite-dimensional mathematical theorem established by the analytical steps in `RESULT.md`, not by the finite checks. The critical new tightness input is a \(\sum_k(q_{j,k}-q_{i,k})^2\le C(j-i)\) deterministic coefficient estimate, followed by a fourth-moment Burkholder bound. Full verification of the compact-log-time fundamental-solution lemma requires the cited primary derivation. No independent audit, formal-proof certification or external empirical validation is claimed.
