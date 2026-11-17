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

Conditioned on the driving Brownian environment, the linear SDE integrates to N(M_t,V_t) with M_t=x0 exp[−at−λ∫_0^t|B_s|^p ds], V_t=2D∫_0^t exp[−2au−2λ∫_{t−u}^t|B_s|^p ds]du. Brownian scaling identifies t^{p/2}V_t with an endpoint Laplace integral T=t^{1+p/2}. For any continuous f≥0 with f(1)>0, endpoint DCT gives 2D∫ exp[−2λT∫_{1−y/T}^1 f]dy →D/(λ f(1)), and the tail outside the endpoint neighborhood is bounded by T e^{−cT}; B_1≠0 almost surely. M_t t^{p/4}→0, yielding the joint weak limit (G,√(D/λ)Z/|G|^{p/2}). From Pr(|G|<u)∼√(2/π)u, conditioning on |Z| and DCT yields tail constant 2^{1/2+1/p}Γ(1/2+1/p)(D/λ)^{1/p}/π and moment cutoff s<2/p. For p=2, Z/|G| is Cauchy. No assertion of prelimit moment convergence. Independently checked Cauchy p=2 tail coefficient and the limiting conditional variance scaling algebra; inspected original SciPy verifier.

## originality

PASS

Best-of-knowledge originality is located in the joint entire-law scaling for arbitrary Brownian stiffness powers p>0 and sharp tail/moment family. The p=2 Cauchy scaling was already acknowledged in a 2026-10-26 rare-excursion study and should not be presented as independently unprecedented. Gupta–Klapp analyze identical p=2 physical model and moments, not a published all-p joint weak-limit theorem in the accessible abstract. The full 2026 preprint was inaccessible; exact implicit coverage is a material residual risk, not automatic rejection.

## value

PASS

The full scaling family yields a distributional limit with strongly coupled environmental endpoint and a sharp continuum of nonintegrable-moment thresholds. The p=2 Cauchy identification resolves a physically motivated density limit, while p≠2 and the exact tail constants quantify how changing the power of Brownian stiffness changes transport fluctuations. Nonuniform integrability explains finite prelimit versus divergent limit moments. This is more than reporting routine Gaussian-ratio algebra: the endpoint singular Laplace localization in a nonstationary random trap is the substantive step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
