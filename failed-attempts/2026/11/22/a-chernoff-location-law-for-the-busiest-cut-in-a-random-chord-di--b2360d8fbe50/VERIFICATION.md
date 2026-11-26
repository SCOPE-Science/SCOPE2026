---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Conditioning on the scan without exposing the identities of future partners makes the down-step probability exactly H_k/(2n−k). Summing single and ordered disjoint double crossing-edge indicators gives E(H_k)=k(2n−k)/(2n−1) and E[H_k(H_k−1)]=k(k−1)(2n−k)(2n−k−1)/((2n−1)(2n−3)); subtracting the squared mean gives the displayed variance. The centered recursion has bounded martingale innovations and conditional variance 4p(1−p). On compact n^(2/3) windows the product q_r is bounded away from zero, Doob plus reversal gives sup|Y|=O_P(sqrt(n)), and the accumulated centered regression is O_P(n^(1/6)). Thus the normalized innovation martingale has variance clock tending to elapsed time and negligible jumps; anchoring at the middle gives the two-sided limit with diffusion one. The exact mean drop supplies −t²/2. For localization, write Y_(n+r)−Y_n=q_r sum_{j=1}^r ξ_(n+j)/q_j+(q_r−1)Y_n. Doob bounds the first maximum's second moment by O(R) and 1−q_r=O(R/n) bounds the second by O(R²/n), giving the stated summable annular probabilities (including the terminal truncated annulus). Beyond n/2, the two-edge switch couples choices of the next partner, so bounded differences make the uniform centering error o_P(n), smaller than the order-n deterministic gap. The compact argmax/supremum mapping and this tail bound prove the joint theorem, also for leftmost ties. Brownian scaling gives 2^(2/3) times the conventional location; the Brownian local law of the iterated logarithm gives positivity despite the quadratic drift, and the unbounded positive tail of B(1)−1/2 with a.s. finiteness gives nondegeneracy. The frozen checker was inspected, not run; the review rests on analytic reconstruction and exact agreement with the earlier model under the coupling below, not on finite enumeration.

## originality

FAIL

The matching scan is exactly the previously studied uniform priority-queue history, also called the sock-sorting process. Janson §8 explicitly identifies the uniform pairing, already proves the identical midpoint-centered excess limit (Theorem 8.5, also giving its leading mean correction), and supplies the local process and localization estimates from which the location and joint limit follow by rank change and the usual argmax mapping. This is positive prior-coverage evidence, not a conclusion from unsuccessful searching.

## value

FAIL

The location and height are meaningful statistics, and the direct scan proof offers explanatory value. But the frozen contribution is presented as a new joint law, not as a demonstrated new methodological improvement, sharper rate, or result for a different model. The model is exactly the earlier priority-queue model; the height law is already explicit and the joint law follows from the earlier local weak limit and tail bounds by a rank change and standard joint mapping. No further scientific gain is established by recasting it as a chord cut.

The dated certificate retains the supplied scientific assessment, sources and limitations.
