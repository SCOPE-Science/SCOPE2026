---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For α=1−δ, β=1+δ, 0<δ<1, direct algebra gives s˙=s(1−s) and d/dt log(xyz/s³)=0. Every positive nonconstant periodic orbit therefore lies on s=1 and on one 0<p=xyz<1/27 smooth connected circle, with no stationary points. On s=1, x˙=δx(y−z) and x˙²=δ²[x²(1−x)²−4px]; the exact 2/δ real-cycle quadrature is correctly normalized. Independent symbolic calculation verifies the nonstandard Picard–Fuchs polynomial identity with B=6x^5−15x^4+11x³−(6p+2)x², yielding p(1−27p)T″+(1−54p)T′−6T=0. The nonsingular coalescing-root substitution gives T→2π√3/δ near p=1/27. The unique analytic Gauss solution then supplies the full exact formula. Positive hypergeometric coefficients prove strict dT/dp<0, and DLMF zero-balance terms produce 3/δ[log(1/p)+6p(log(1/p)−5/2)+O(p²|log p|)]. Independent symbolic checks and six high-precision real quadratures agree, but do not substitute for the all-p proof.

## originality

FAIL

A decisive reduction to already-published Hesse-pencil period theory covers the full statement. The exact critical May–Leonard invariant cubic is projectively equivalent to the Hesse family with ψ^-3=1-27p; its original-time one-form is a p-independent scalar multiple of the Hesse holomorphic residue. Zhou (2017) equation (2.12) gives precisely the normalized 2F1(1/3,2/3;1;ψ^-3) period. The physical prefactor is determined by the central linearized frequency, while strict decrease and both logarithmic coefficients are direct Gauss-series and DLMF consequences. This is mathematical implication/coverage, not merely a similar title or heuristic analogy.

## value

PASS

The original-time period of the classical critical three-species neutral cycle family is a motivated natural invariant, with p=xyz as its complete cycle coordinate. Exact strict nonisochrony, the positive small-amplitude period floor, unbounded heteroclinic slowdown, and the first log-correction give quantitative dynamics useful for comparison of ecological cycle scales. This is mathematically meaningful even though the exact law is implied by earlier Hesse period theory and hence not original. It is not an arbitrary finite computation, but a complete parameter interval classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
