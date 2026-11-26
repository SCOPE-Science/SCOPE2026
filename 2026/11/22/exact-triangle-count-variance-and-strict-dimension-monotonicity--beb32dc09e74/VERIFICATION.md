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

Write S_ij=sign⟨X_i,X_j⟩; ties have probability zero even at d=1. Independent flips of individual X_i show that only even-degree edge subsets survive when expanding products of edge indicators (1+S_ij)/2. Given X_1,X_2 with inner product C, the angular disagreement probability for the signs of a third point is arccos(C)/π, so their product has conditional mean b(C)=2 arcsin(C)/π. At C=±1 and d=1 this holds directly. The triangle sign product thus averages to E[sign(C)b(C)]=8u_d. The four-cycle 1–3–2–4–1 averages to E[b(C)²]=32h_d by independence of the two fresh points. The five-edge diamond has exactly the empty even subset, its two triangles, and this four-cycle. Hence p_d=(1+8u_d)/8 and the joint positive-diamond probability is (1+16u_d+32h_d)/32; subtracting p_d² gives c_d. The absent sixth edge is not constrained. Disjoint triples are independent, and one common vertex also gives independence by conditioning and rotational invariance. Exactly C(n,2)C(n−2,2) unordered pairs share an edge; for n=3 this term is zero. Coupling R_d by normalized Gaussian coordinates gives an almost surely strict drop including d=1→2. Both arcsine moments drop, u/4−u² is nondecreasing on [0,1/8], and p(1−p) is strictly increasing in the relevant p-range. There are always diagonal terms, so the variance is strictly decreasing regardless of whether edge-overlap pairs exist. Low-dimensional arcsine inputs are constant π/2 at d=1, uniform on [0,π/2] after arcsine at d=2, and arcsine of a uniform [0,1] variable at d=3; the last two moments there are π/2−1 and π²/4−2 by integration. Substitution yields the quoted constants. For fixed n, E[R_d]=√(2/(πd))+O(d^(−3/2)) from the gamma ratio, E[R_d²]=1/d and E[R_d³]=O(d^(−3/2)) by beta moments. Uniform bounds arcsin(r)=r+O(r³) and arcsin²(r)=O(r²) give u_d=1/(2π√(2πd))+O(d^(−3/2)) and h_d=O(1/d). The variance excess linear in u has multiplier (3/4)C(n,3)+(1/2)C(n,2)C(n−2,2); all other terms are O_n(1/d). This yields the positive coefficient and independent-edge limit. No finite check or assumption about uniformly growing n is needed.

## originality

PASS

The supported distinct claim is the all-dimension exact ordinary triangle variance, exact shared-edge covariance, strict variance ordering, and sharp fixed-n variance excess. The single-triangle mean formula and strict dimension decrease are already covered for the continuous spherical model in Bubeck–Ding–Eldan–Rácz §6; the frozen discussion of earlier mean bounds alone undercredits that source. The elementary d=1 extension does not warrant independent novelty credit.

## value

PASS

Ordinary triangle counts measure latent dependence even though the edge density equals that of independent fair edges. An exact variance, its strict order in dimension for every fixed node count, and the sharp excess coefficient quantify that statistic's noise; the shared-edge term can grow as n⁴ and cannot be read off the prior mean. This is a natural exact invariant, not a claim about optimal testing or any joint n,d regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
