---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a positive bipartition concurrence, the source identity (Delta A_i)^2=sum_{k<l} lambda_k lambda_l(lambda_k-lambda_l)^2 is strictly below sum lambda_k lambda_l=C_i^2/4 because every contributing pair has both eigenvalues positive and hence |lambda_k-lambda_l|<1. Thus every positive cut has strict speed below sqrt(F_Q) when F_Q>0. At C_N>0, differentiating C_N^2 avoids any issue from individual zero-cut cusps: zero cuts contribute zero first derivative of their nonnegative squared concurrence, while at least one positive cut contributes strictly, giving the global strict bound. At C_N=0, existence of the ordinary derivative of the nonnegative function C_N forces it to be zero. QFI zero implies no projective state speed, hence zero concurrence speed. The GHZ family C_N=|sin 2theta|, F_Q=4 has interior ratio |cos 2theta|<1 and one-sided slopes of magnitude two at its nondifferentiable product cusps. The verifier checks only this illustration; the proof is analytic.

## originality

FAIL

The defining primary paper already performs the decisive saturation analysis: it explicitly states that the spectral inequality is never exactly saturated at any point with positive bipartite concurrence, only approached as concurrence tends to zero; it then says exact saturation of the general multipartite bound is confined to the product-state boundary. In the very example described as 'touched exactly', the same figure caption explicitly marks the product points as points where the derivative does not exist and states that the derivative merely approaches the envelope. The submitted theorem adds only the elementary observation that a differentiable nonnegative function has derivative zero at a zero, so it is a direct clarification of an internal wording inconsistency, not an original scientific theorem under the required bar.

## value

FAIL

Correcting the source's phrase 'touched exactly' is useful editorially, but mathematically the source already proves strictness for positive concurrence and marks the boundary contact points as nondifferentiable. The remaining step is the textbook fact that a differentiable nonnegative function has derivative zero at a zero. Under the required bar against cheap type/differentiability checks and mechanically implied corollaries, this does not constitute an independently valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
