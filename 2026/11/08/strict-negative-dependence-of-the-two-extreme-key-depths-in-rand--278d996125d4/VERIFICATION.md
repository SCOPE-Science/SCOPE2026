---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The root rank L is uniform 0..n-1. Conditioned on L the two extreme depths are independent, distributed as A_L and A_{n-1-L}, with A_0=0, A_k=1+sum_{j=2}^k Bernoulli(1/j). The record-indicator law and coupling imply expectation of any nonconstant increasing depth function is monotone, nonconstant in subtree size. Reverse Chebyshev covariance with the opposite-sized subtrees is strictly negative; indicators of thresholds a,b<=n-2 give strict quadrant inequality. The conditional mixed moment is n^-1 sum_{l=0}^{n-1} H_l H_{n-1-l}, giving Cov=1-H_n^(2) via harmonic generating functions; finite exact permutation enumeration for n=2..6 independently reconfirmed every quadrant and moment. Central root ranges epsilon n..(1-epsilon)n yield independent Bernoulli sums with means log n+O_epsilon(1) and variances log n+O_epsilon(1); triangular-array CLT plus endpoint probability <=2epsilon proves joint independent normals. The boundary n=2 covariance -1/4 is included.

## originality

PASS

Published random-BST results give marginal depth/ancestor laws and distances between rank-selected keys, but do not appear to give the joint strict negative-quadrant theorem and exact mixed covariance for the deterministic two extreme ranks in inspected theorems. Both root decomposition and record variables are classical inputs; claim of novelty is only their exact two-extreme dependence synthesis.

## value

PASS

Joint negative dependence is a mathematically meaningful contrast to asymptotic independence of the two most extreme searches in the foundational random BST model. Exact finite-size covariance and strict all-threshold inequalities are natural reusable invariants, not mere relabeling of a single-depth expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
