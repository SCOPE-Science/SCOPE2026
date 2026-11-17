---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For identical unit chores, ex-ante weighted envy-free is exactly E[X_i]=m w_i and deterministic WEF1 is (x_i-1)/w_i <= x_j/w_j for nonempty recipients. For m<n a missing recipient forces all counts <=1, yielding hypersimplex membership; m=n forces counts one. At m=n+1 only an extra chore can be assigned to a maximal-weight recipient; mixing over S produces (t+1)/(t(n+1)) vs 1/(n+1). Exchange-chain inequalities between supported vectors give rational ratios along edges and component total weights N_C/m, hence each support set determines at most one rational weight. n=2 the interval (m-1)p <= x <= (m-1)p+1 yields mp integer or (m-1)p integer. These proof implications are sound. A separately written Fraction enumeration checked 440 two-agent configurations; bounded tests do not prove general claims. Source RESULT.md blob dc7758b9b530a91c40fbc3e328c190294dcba2d2 and verifier blob d5f0c70c220ce6911220cd24ca2413a5a332655c inspected.

## originality

FAIL

A 2026-11-02 full primary Resultary theorem already characterizes the same probability/entitlement feasibility problem for all m,n by a tied-Adams-priority hypersimplex, proving precisely the same m<n and m=n boundaries, rationality for m>=n, and the 2-agent modular criterion. Its stronger all-m condition implies the submitted n+1 subset formula and fixed-(n,m) finiteness. Difference in proof method/numbered corollary is not original.

## value

FAIL

The general arithmetic structure and n+1 census are meaningful in themselves, but the *submitted* results add no previously unknown independent mathematical fact over the November 2 exact all-m priority-score theorem. Finite subset enumeration and an alternative proof of the prior theorem do not constitute a new valuable result. The whole claim is rejected rather than cosmetic repairs to a known theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
