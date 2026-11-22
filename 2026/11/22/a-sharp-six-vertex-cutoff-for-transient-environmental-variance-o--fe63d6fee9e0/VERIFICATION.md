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

# Reproduction

Run `python3 checks/edge_environment_checker.py` with Python 3.10 or newer. The checker constructs the joint edge-state transition distribution by explicitly selecting environmental-update vertices and independently branching the incident-edge transition coins. It compares computed exact-rational means and variances to the closed expressions, for 4–6 vertex stars and paths, both homogeneous environmental starting states, and a nonextremal five-vertex tree, a four-cycle, and additional path tests from three through six vertices with alternative rational probabilities. All assertions passed during preparation.

The universal proof is given in `RESULT.md`. The finite-state checker has a bounded test domain, cannot certify arbitrary time or arbitrary graph order, and makes no claim to independent scientific validation. The rational five-vertex witness is verified by a closed algebraic substitution and by full-state enumeration. The stationary Bernoulli assertion follows from a finite irreducible chain with product invariant law under conditional independent edge updates.

Historical priority was checked against primary source full text, earlier independent-edge evolving-network models, general random-scan context and available records. These checks do not exhaust unpublished or unindexed mathematical literature. No external audit has been performed.
