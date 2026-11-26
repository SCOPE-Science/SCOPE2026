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

The finite triangle-free diagram over the named biclique determines and realizes a complete injective type. For a fixed shore assignment the count is [I(F[X])I(F[Y])]^n; only coordinates with an empty neighbourhood cause duplicate decorations, contributing O_r(2^((r-1)n)). Proper colourings have full weight 2^r, one monochromatic edge gives (3/4)2^r, and two forbidden pairs retain at most 5/8 (overlapping) or 9/16 (disjoint) of the subsets. This proves the leading counts and the sharp rarity after normalization; the denominator correction contributes a smaller (9/16)^n term. Arity one has count 2^(n+1)-1, and at arities at most four the non-bipartite event is impossible. A pentagon with isolated labels proves positivity at every r>=5. For the conditional law on a fixed labelled pentagon, the ten maximal decorations have equal weights 24^n, and conditioning on nonempty neighbourhoods changes each product distribution by o(1); its Bernoulli marginals are 1/3 at the two defect endpoints and 1/2 elsewhere. An independent bounded calculation uses signed active-shore assignments with net factor 1-1-1=-1 per inactive label to recover all thirteen exact pentagon coefficients, and counts defects colour-first via connectivity of the cross-edge graph. It reproduced 1,81,3561,113541 at n=0,1,2,3 for a fixed pentagon, A_5=120 and A_6=6120, and the normalized coefficients 60/721 and 340/1017. Replay: python3 /workspace/review_evidence/check_1_2_4.py. The finite reproduction is not the proof of the asymptotic theorem.

## originality

PASS

Credit the exact per-pattern enumeration and its pentagon specialization to the earlier Cartesian-product identity. The distinct finding is the fixed-arity chromatic limiting measure on balanced growing bicliques, the sharp non-bipartite probability at all fixed arities, and the conditional neighbourhood mixture. These are not stated by the closest exact enumeration, which treats independent parameter graphs in its asymptotic analysis, nor by the inspected biclique-recovery or odd-cycle colouring works.

## value

PASS

An increasingly large named biclique forces bipartite internal diagrams in the uniform complete-type limit although the ambient graph permits induced odd cycles. The full chromatic limiting law describes arbitrary fixed finite tuple patterns, and the optimal exponential defect rate and conditional densities explain how the exceptional cycles occur. This is a structural asymptotic phenomenon, not just a table of pentagon counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
