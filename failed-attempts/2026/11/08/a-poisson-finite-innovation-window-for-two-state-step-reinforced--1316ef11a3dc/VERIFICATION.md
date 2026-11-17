---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Conditionally on the recursively reinforced forest, each component carries one independent fair bit; the parity character E(-1)^S is exactly the indicator all components have even cardinality. Odd N cannot satisfy it. With Nq_N -> lambda, edge deletions form a Poisson(lambda) family of uniformly chosen recursive-tree labels. Nested cut pairs occur with probability O(q_N^2 N log N)=o(1); a typical cut fringe has size k with probability 1/[k(k+1)], and Poisson marking gives independent mean lambda/[k(k+1)] size counts. The odd-size mass sum_{j>=1}1/((2j-1)(2j))=log 2 yields bias e^{-lambda log2}; TV is half the bias. The supercritical Nq_N->infinity conclusion uses the specified Peres–Qin upper bound b_N<=alpha_N^(N/2)<=e^{-Nq_N/2}. Independently reconstructed exact step-count recursion at alpha=3/4 gives even N=4,6,8 biases 33/64,45/128,27423/114688; these finite checks support normalization but do not prove the Poisson limit.

## originality

FAIL

The prior November 2 published full Resultary theorem establishes exactly the same fair Z_2 reinforced-walk terminal distribution and Poisson nonroot-component intensity lambda/[k(k+1)] in a stronger ell1 sense, including odd-time uniformity and even-time TV 2^(-lambda-1). It additionally proves root-cluster deficit PGF and tail, so the current core scientific claim is strictly covered. The extra Nq_N->infinity mixing statement follows directly from an already published Peres–Qin exponential bound.

## value

FAIL

The finite-reinforcement crossover is a natural motivated probability law, but its exact bias and Poisson-fringe mechanism were already proved together; the Nq_N->infinity extension is a straightforward substitution into a previously available inequality rather than an independent valuable theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
