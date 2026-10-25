---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Let N_lambda(K) be the minimum number of translated lambda K covering K, 0<lambda<1. Both inequalities in coin_w(K)=inf_lambda N_lambda(K)/(1-lambda) follow from gamma_m(K)<=lambda when N_lambda=m and approximating gamma_m from above for the converse. For q=ceil(1/lambda), a line segment has exactly q-covering number: q translated lambda-intervals cover it, while q equally spaced witnesses j/(q-1) have mutual spacing >lambda, giving a q-point lower bound. An r-dimensional product witness grid has q^r fibers, each requiring N_lambda(K) translates of lambda K, and a product cover attains the bound. Thus N_lambda(K direct_sum C^r)=N_lambda(K)q^r, including any convex K. Since q>=2, the infimum implies coin_w(K direct_sum C^r)>=2^r coin_w(K). If the base infimum is attained at gamma_m(K)=lambda_* in [1/2,1), then choose lambda>lambda_* arbitrarily close; N_lambda(K)<=m and q=2, giving the opposite inequality by taking the limit. This avoids relying on finite-cover attainment exactly at gamma_m. For triangle and affine-regular hexagon, the published exact base coin_w=9, gamma_3=2/3 imply both the lower and upper bounds 9*2^r for every integer r>=1, in particular 18 at r=1. Cases lambda=1/2 (q=2), lambda approaching 1 or 0, and non-attained gamma_m are accounted for; equality for arbitrary K without the attainment hypothesis is not proved.

## originality

FAIL

Originality FAIL by direct prior mathematical implication, not search failure. Bezdek--Khan Proposition 4.2 already gives the exact scale-by-scale theorem N_lambda(K direct_sum C^r)=N_lambda(K)ceil(1/lambda)^r; their own weak index definition coin_w(K)=inf_m m/(1-gamma_m(K)) is definitionally equal to inf_lambda N_lambda(K)/(1-lambda). Since ceil(1/lambda)>=2, the advertised universal lower bound follows by immediate monotonicity of the infimum; when a minimizing ratio >=1/2 exists, evaluating at that ratio gives the upper equality. Their same paper supplies base coin_w=9 at gamma_3=2/3 for the triangle and affine-regular hexagon. Thus the claimed exact prism numbers 18 and all 9*2^r cube extensions are elementary specializations of the existing source theorem and source table, although not printed explicitly and despite the authors noting the absence of a more general weak cylinder corollary. The mathematical coverage is decisive because it uses no additional nonstandard lemma beyond previously published Proposition 4.2 and the published definition/base values. The later survey and Wu--Fan--He are not needed to reach that implication; an inaccessible plausible paper is merely an additional residual risk, not the failure reason. Resultary returned the same target, not independent earlier evidence.

## value

PASS

The weak covering index is an intrinsically motivated convex-geometric optimization invariant, and the authors introducing it explicitly left the weak cylinder calculation only as upper estimates. The universal lower law and a sharp attained-ratio condition give structural product behavior for any base convex body and exact higher-dimensional values for two nontrivial planar bases. The exact value 18 of two concrete one-codimensional prism families, and 9*2^r for all r, is information a covering-geometry researcher could use without a paper-sized downstream theorem. Value is modest, because the proof is short and depends critically on established product-covering machinery; the result does not claim a universal weak cylinder equality or solve broad dimension-wise extrema.

The dated certificate retains the supplied scientific assessment, sources and limitations.
