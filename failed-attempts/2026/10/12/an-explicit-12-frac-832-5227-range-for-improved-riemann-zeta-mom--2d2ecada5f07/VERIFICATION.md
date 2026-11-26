---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The formal bound and strict comparison in the Finding follow from the published level-set bounds. On [T,2T], a maximal one-spaced subset covers the associated level set by intervals of bounded length. Dyadic summation bounds its contribution by V^k N(T,V) up to T^ε, with the region |ζ|<1 costing O(T). The Bourgain cutoff can be raised by an arbitrarily small ε-loss: above T^(13/84) use monotonicity of N and the bound at that endpoint. Direct rational checks put the maximum at σ₂=58907/445121: the two active affine branches agree there and both give 2−520/445121+σ₂(k−12); the classical endpoint at σ₁ and the first high-value term at σ₃ are strictly lower on the claimed interval. Subtraction from 2+(k−12)/8 gives δ(k), with zero exactly at k*=12+832/5227. Dyadic summation in T then gives M_k(T) as stated. The comparison beyond k=12 is against the affine continuation of the classical interpolation line; the primary paper does not establish that line as a classical bound for k>12.

## originality

FAIL

The exact number 832/5227 is not stated in the strongest identified source, but the result is a direct corollary of its stronger, published level-set theorem and the very same three-regime moment argument. De Faveri–Pandey already explicitly identify the extension beyond 12. All four affine functions for fixed k are obtained from their exact displayed exponents by replacing the weight V^12 with V^k; the same two bounds are still active at their already identified crossover, and a single affine equality gives the stated ν. No new large-value bound, different regime, or additional mathematical ingredient supplies the extension. The negative originality decision rests on that verified implication, not on an exact-phrase match or an unsuccessful search.

## value

FAIL

The endpoint arithmetic is useful exposition of the published proof, but the finding adds only the routine crossing against the affine continuation of a comparison line. That line is not itself a classical bound established by interpolation for k>12, and the crossing is neither a limit of the method nor a barrier for moment bounds. The stated range does not capture a new analytic constraint or a separately useful exact invariant beyond the existing envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
