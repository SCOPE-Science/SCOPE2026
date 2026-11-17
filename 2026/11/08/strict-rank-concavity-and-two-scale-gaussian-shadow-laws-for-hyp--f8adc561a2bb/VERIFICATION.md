---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

A Haar projection onto an intrinsic two-plane is equivalent up to nonsingular planar linear transformation and translation to independent Gaussian planar point coordinates. The maximizing k-subset changes only at ties of a pair of projected Gaussian coordinates; each unordered pair has exactly two tie directions. The tied score is N(0,1/2), independent of the others, and the chance of exactly k-1 larger scores gives n(n-1) binom(n-2,k-1) times the integrated Gaussian tie density. Quantile substitution yields F_n(k)=n E[f(Beta(k,n-k))] with f(q)=sqrt2 exp(-Phi^{-1}(q)^2/2). Differentiation gives f'=-2sqrt(pi)Phi^{-1}, f''<0, and F(k+1)-F(k)=E[f'(Beta(k+1,n-k))]. Strict order-statistic stochastic increase proves every internal second difference negative; complement symmetry fixes the central maximizer and f<sqrt2 almost surely gives the strict bound. Beta concentration yields dense rank limit; fixed-k nBeta(k,n-k) -> Gamma(k,1) and Mills asymptotics with uniform integrability prove 2sqrt(pi)k sqrt(2log n). Independent normal-tie numerical integration gave strict concavity sequences at n=6,10, not used as infinite proof.

## originality

PASS

Older Gaussian k-facet and k-set papers, especially Leroux–Rademacher 2023, furnish a general expected crossing/facet integral and therefore cover the unadorned integral count as a special case. Black–Criado 2024 studies random shadows of fixed polytopes including hypersimplices and general bounds. The surviving mathematical contribution in the assigned theorem is the explicit concave beta-quantile kernel, rigorous all-finite-rank strict maximization, and dense versus fixed-rank two-scale sharp asymptotic. The cited accessible primary full texts were inspected for these consequences, with residual concern about older k-set theory.

## value

PASS

Expected number of vertices in a random planar shadow is central in random polytope geometry and pivot complexity. The exact rank-optimized, strictly concave hypersimplex profile is a natural complete classification, and the contrast between O(n) central ranks and O(sqrt(log n)) fixed ranks provides nontrivial sharp geometry not inherent in generic upper bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
