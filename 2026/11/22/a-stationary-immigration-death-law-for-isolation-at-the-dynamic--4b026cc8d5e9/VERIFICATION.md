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

# Reproducibility and verification

Run `python3 check_isolation.py` with Python 3 and no third-party dependencies. The program verifies the tagged-vertex factorization against exhaustive, exact-rational two-snapshot edge histories for several small complete graphs, checks convergence of exact temporal-support means for several fixed observation arrays, checks marginal mass balance, and checks the time-lag covariance.

The included program passed **347 deterministic assertions**. Finite checks independently stress the exact identities but do not establish the infinite theorem. The proof in `RESULT.md` relies on exact edge transitions, tagged-edge independence, inclusion–exclusion, mixed factorial-moment convergence, and the standard connectivity threshold theorem. There is no claim of independent mathematical audit or of functional sample-path convergence.
