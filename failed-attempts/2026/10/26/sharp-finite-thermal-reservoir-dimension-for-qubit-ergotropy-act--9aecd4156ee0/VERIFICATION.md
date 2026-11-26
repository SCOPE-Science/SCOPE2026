---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With the stated finite resonant nondegenerate ladder, each interior total-energy block contains just |g,k> and |e,k-1>; the final excited population from the block is a convex combination of its two initial diagonal probabilities, maximized at the larger via an independent swap or identity. The upper isolated level contributes (1-p)w_(d-1). Because w_k=q w_(k-1), the maximizing choice is the same in each block. The reduced qubit stays diagonal by total time-translation invariance and covariance of partial trace, yielding ergotropy Delta*[2E_d-1]_+. E_d is the maximum of two affine functions of p, hence maximized at an endpoint of [1/2,1]; p=1/2 gives 1/2 for q<=1, while p=1 gives 1-w_0. Activation is strict and equivalent to Z_d>2; d=2 is impossible, q=1 first works at d=3, and for 0<q<1 the condition becomes q^d<2q-1, which forces q>1/2 and the stated strict integer rounding. The swap branch has positive slope for d>=3 and intersects the identity branch at p=1/(1+q), where E_d<=1/2. Its 1/2 crossing therefore gives the stated strict p threshold when activation is possible. The defining sum is strictly increasing in q and brackets 1 between q=1/2 and 1 when d>=3. The root near 1/2 obeys 2 delta=2^(-d)(1+2 delta)^d; bracketing by delta=0 and C*2^(-d) for a fixed C>1/2 first bounds delta=O(2^(-d)), and expansion then gives both remainder estimates. Direct subtraction from the infinite endpoint pq yields the stated positive penalty in the swap branch. Independent bounded replay (python3 /workspace/branches/d5a2cf82-2e5f-4e1c-b8a9-02e04ae63138/replay_ladder.py) returned REPLAY_OK 1042 checks; these are not the proof.

## originality

FAIL

Actual prior coverage, not just a possible overlap: Scharlau and Müller (2018), Section IV.1, solve the fixed finite resonant ladder qubit reachability problem and give the same maximal transition parameter 1-w_0. The frozen all-d optimum is their result in the excited-population variable; the other claimed contributions are routine consequences of that same endpoint. The paper is not identified in the frozen prior-work discussion.

## value

FAIL

The physical question of minimum bath dimension is motivated, but this finding does not supply a distinct scientific increment over the existing complete finite-ladder solution. The switch to ergotropy, the threshold rounding and finite-cutoff subtraction are routine inactive/active-branch and geometric-series consequences. The asymptotic expansion of the same scalar root does not establish another motivated gap or boundary beyond the already exactly characterized parameter. A useful exposition or separately checked derivation is not a surviving distinct research finding under this review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
