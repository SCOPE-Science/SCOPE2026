---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Disjoint column supports make the modulus diagonal, with the v-entry r_v=||Te_v||. For r_v>0 the polar update gives edge weight lambda_vu(r_u/r_v)^t, and gives a zero outgoing column if r_v=0. The resulting p-mass at v is at most b_v^(1-t)(sum_children b_u)^t, by bounding each r_u in the weighted quadratic mean by (sum_children b_u)^(1/p). This remains valid for countably many children, vanishing weights, and p<1. Scalar weighted AM–GM then bounds it by ((1-t)I+tQ)b, where Q adds child masses. Unique parents make Q positive and contractive on l1; Q^k counts each vertex once exactly when it has depth at least k. Iteration and the binomial expansion thus give the precise depth-weighted sum over the original masses, including n=0, and justify that every iterate is in the same Schatten class. Since each vertex has finite depth, dominated convergence gives the endpoint result. Splitting at K, and setting K=floor(nt/2)+1 for the Chernoff estimate, gives precisely the claimed strict depth tail and e^(-nt/8). On L equally weighted positive path edges of normalized weight L^(-1/p), exactly one more terminal edge vanishes in each iteration up to L, so the p-energy is (L-n)/L for n<L and gives the stated supremum by sending L to infinity.

## originality

PASS

The supported distinction is the explicit binomial-depth estimate and its same-ideal decay consequence on general rooted branching trees. The one-step edge formula and same-Schatten unilateral result are already known, as is the scalar path iteration on which the sharp nonuniformity witness rests. Neither is being credited for originality in isolation.

## value

PASS

Equal-ideal convergence at every p>0 is a meaningful endpoint question, including the quasi-Banach regime. This solves it for a natural nontrivial branching class with operators outside the previous smaller-ideal and direct-sum hypotheses, and provides usable quantitative decay governed by initial depth tails. The simple path witness clarifies why a unit-normalized, depth-free uniform rate is not an acceptable replacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
