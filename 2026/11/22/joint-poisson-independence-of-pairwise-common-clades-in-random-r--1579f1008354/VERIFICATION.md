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

Run `python3 verify_phylo33.py` with standard Python 3. The exact enumerator constructs all rooted leaf-labelled unordered binary trees for \(3\le n\le6\), compares exact clade/cherry presence frequencies with the combinatorial contraction formulas, checks the cherry-count variance and the shared-tree overlap covariance reduction. Its completed run reports 231 rational assertions and 945 trees at \(n=6\). The analytic proof, rather than these finite tests, establishes joint convergence for every fixed number of trees. No independent mathematical audit has been performed.
