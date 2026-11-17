---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: G_n is the additive space of alternating n-by-n matrices even in characteristic two. For coordinate additive character gamma_B, the step E(u,v)=uv^T-vu^T pairs exactly as u^TBv, and averaging over uniform v leaves probability u in ker B=q^{-rank B}. Alternating rank=2r, with multiplicity [n choose 2r]_q |GL_{2r}|/|Sp_{2r}|; Parseval yields the chi-square formula for all t>=0. Factoring the multiplicity and using a uniform q^{-quadratic in r} bound gives both even and odd s-offset limiting chi-square series. For t=floor(n/2)+a_n the sum goes to zero, while for t=floor(n/2)-a_n rank at most 2t forces nullity>=2a_n and the uniform-random nullity union bound tends to zero. Independent GF(2) enumeration found n=3 rank counts {0:1,2:7} and n=4 counts {0:1,2:35,4:28}, and directly verified Fourier expectation 2^{-rank B} for every character through n=4. Tests do not establish asymptotic TV cutoff alone.

## originality

PASS

PASS best-of-knowledge: previous alternating-bilinear-form association schemes and uniform matrix rank distributions supply background multiplicities, but the additive walk with independent uv^T-vu^T increments, exact all-time chi-square, even/odd dimension-dependent fixed-offset profiles and TV cutoff at n/2 were not shown in the inspected original transvection-walk and rank-distribution sources. Historical scheme priority qualified because Delsarte–Goethals full text was inaccessible.

## value

PASS

PASS: The complete additive alternating-form walk has a natural finite-field stochastic mixing problem, and an explicit exact rank-Fourier spectrum with a sharp dimension-half cutoff and a parity-dependent critical χ² profile is an informative reusable invariant rather than routine tabulation. The paper does not claim the classical form-rank multiplicities as independently new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
