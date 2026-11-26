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

In H_n the only dependence of the oriented roots is their sum, so the polar is the zero-sum cube section. At a polar vertex at most one coordinate is unsaturated. The sign sum forces precisely one zero at odd n and balanced saturated signs at even n. The odd facets are simplices; at even n the sole dependence yields coincident barycenters of the two equal-size vertex blocks and complementary directions, giving the centered free sum. Independently, in the free-sum model let a=−p min x and b=−q min y; the gauge is a+b and slack is s=1−a−b. Shifting toward a block vertex gives exactly t≤x_k−min x+s/p (or the y version), since the other coordinate inequalities only become easier. The block ranges are at least a/(p−1), b/(q−1). At least one is ≥(1−s)/d where d=p+q−2. Since p,q≤d, adding the appropriate slack term gives coverage at t=1/d. The one-minimum/equal-other-coordinates witness has both ranges 1/d and s=0, excluding every greater t<1; t=1 excludes it because it is not a vertex. A supporting functional shows face inheritance for t in (0,1), and every covering translate at the proposed t≤1/2 contains the center of P_n, giving radial extension from the covered boundary. This also handles n=3,4. Scaling the equality by 1/t gives c=1/t−1. The u_i versus ν_i notation mismatch in the free-sum model is evident from context and has no mathematical effect.

## originality

FAIL

The result is correct but the threshold for the auxiliary free sum, and therefore the cycle law, follow directly from a stronger published covering criterion that the dossier overlooked: Artstein-Avidan–Falah–Slomka Remark 5.2, immediately after Lemma 5.1. For P=Q_(p,q) of dimension d=p+q−2, each negative simplex vertex belongs to (p−1) times its own centered simplex (respectively q−1), since its negative is the sum of the remaining vertices. Thus −P⊆(d−1)P, and the prior criterion yields λ(P)≥1/d. To get equality, expose all but one vertex from each simplex by a functional equal to 1 on those vertices and to −(p−1), respectively −(q−1), on the omitted ones. The d exposed vertices are linearly independent in the complementary blocks (each proper subset of centered simplex vertices is linearly independent), giving a simplex facet with λ=1/d. Prior Lemma 2.2 forces the reverse inequality. Substituting this into the known cycle facet structure and applying the same paper's Lemmas 2.2 and 5.1 gives the whole frozen result. An exact pointwise gauge proof is an alternative verification of this application, not evidence that the thresholds were outside the prior theorem's coverage.

## value

FAIL

The invariant is natural and the parity effect pedagogically useful, but all stated sharp thresholds are mechanically implied by the known facet and asymmetry criteria. The explicit centered-simplex gauge substitution is routine and is not developed into a separately useful new theorem beyond those thresholds. Thus the frozen package does not establish a new exact invariant or substantial surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
