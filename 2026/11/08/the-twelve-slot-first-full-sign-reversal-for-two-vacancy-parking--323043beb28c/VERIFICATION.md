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

Pinned RESULT.md blob db1579cf99557325b48f25a1df6e10c28bf0aa82 uses the classical blockwise parking-function count, reflection for left parking, and sub-Markov kernel convexity to prove the occupied-set subprobability is bias-independent for prespecified car-index p_k. With m=n-2, W_ab=(n-2)!∏f(occupied block lengths) are exact positive integers, and Cov(X_i,X_j)=(ZW_ij-H_iH_j)/Z². Inspected source CHECKER.py blob e9b06ead7fad7ee9cff71deb676f2520cfee6936; independent separate rational recomputation for every 4≤n≤12 confirmed Z=3(n+1)^(n-3), all adjacent sign strings, and every n=12 pair. Min adjacent Q=581409157300000000, max nonadjacent Q=-3692131919133336000. The claim asserts no extrapolation past 12; exact finite calculation is exhaustive on the stated domain.

## originality

PASS

Best-of-knowledge: the strong prior bilateral procedure paper supplies all block weights, but not the exact joint two-vacancy covariance sign matrix and first complete adjacent positivity at n=12. The contribution is the motivated finite boundary, not old parking-count identities.

## value

PASS

A natural two-vacancy occupancy covariance matrix changes from edge anticorrelation to every nearest-neighbor covariance positive at an exact first street length, while all nonneighbor pairs are negative. The 12-site sharp cutoff with complete 66-pair classification is a meaningful finite transition of a classical random combinatorial model, not an arbitrary row of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
