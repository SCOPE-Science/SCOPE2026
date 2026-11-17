---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For every odd s>=3, the identity F_s=s integral_0^1 (tx+(1-t)y)^{s-1}dt proves convexity and compactness. Symmetry forces the nearest B_s point to (1,1) to lie on the diagonal at a=s^{-1/(s-1)}, giving the inward square-corner excess sqrt(2)(1-a). Convexity of distance-to-B_s bounds the square-to-body directed excess at that value. For xy<0, F_s=(u^s+v^s)/(u+v) bounds the sole coordinate exceeding the square by 2^{1/(s-1)}-1; a strictly concave scalar comparison on [0,1/2] shows this is smaller than the diagonal excess. Homogeneous Phi_p=F_p, Phi_2p=F_p(x,-y) and Phi_{2^k}=x^{2^{k-1}}+y^{2^{k-1}} then yield precisely the three claimed convex families, including p=3,k=2 boundaries; expansion 1-e^{-u} yields the asymptotic constants. The analytic inequality, not the script grid, supports all odd s.

## originality

PASS

Best of knowledge: Fouvry–Waldschmidt classify exactly which domains are convex and Lemma 3.1 proves convexity, but their full relevant published mathematical text does not give the exact fixed-square Euclidean Hausdorff metric or constants. Their older large-degree inner/outer square estimate is nonsharp and cannot imply exact constants. No matching complete formula emerged from current Resultary or literature queries. Existence of a differently phrased sharp formula remains a residual priority risk.

## value

PASS

The natural complete convex binary-cyclotomic family previously had qualitative convexity and coarse square approximation; the exact two-sided Hausdorff invariant, all odd divided-power extension, and contrasting prime/dyadic rates provide usable sharp quantitative geometry. This is a motivated structural metric result rather than a renamed convexity claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
