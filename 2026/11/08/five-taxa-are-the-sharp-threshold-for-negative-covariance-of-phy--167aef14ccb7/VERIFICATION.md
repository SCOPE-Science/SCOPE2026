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

# Reproducibility

Execute `python check.py` in an environment with Python 3 and no third-party dependencies. The program uses exact rational values throughout, enumerates fixed-size leaf subsets directly from rooted edge-descendant sets, checks the witness outcomes and exact covariance and correlation, compares the analytic five-taxon covariance polynomial to 120 independent rational trees, and checks 720 four-leaf sampling distributions over balanced and caterpillar topologies. The actual embedded code was replayed and returned `PASS`.

The minimality proof is analytic: an affine relation handles size-two samples, all-taxa samples are deterministic, and the remaining four-taxon case is exhausted by the two rooted binary shapes and continuity. The exact five-taxon sign region is obtained from the near-complete-sampling covariance formula. Finite checker tests neither prove novel publication priority nor certify the infinite theorem independently of its written reasoning. No independent scientific audit has been performed.
