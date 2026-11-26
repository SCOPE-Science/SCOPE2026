---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The matrix is irreducible Metzler and its upper eigenvalue λ has a positive right eigenvector. The eigenvector's second row gives λ>t−ν. An independent global check is to set q=(t−λ)/(ν+λ−t)>−1, including when s≥t. Then t−s=μq+νq/(1+q), a strictly increasing function of q, and q′=(k/(1+c)²−mq)/(μ+ν/(1+q)²). Thus λ′ has the sign of q−k/(m(1+c)²). With y=1+c and δ=k+t−r, this is the sign of δ−G(y), where G(y)=2k/y+k(μ₀−m)/(my²)+νk/(my²+k). G′ is the sum of −2k(y−1+μ₀/m)/y³ and −2mνky/(my²+k)², hence negative on y≥1. Its values run from k+L at y=1 down to 0 at infinity. This establishes strict decrease for δ≤0, one unique interior minimizer if 0<δ<k+L, and strict increase for c>0 if δ≥k+L, including the zero initial derivative at equality. A finite cap truncates these monotone branches. Bounded t−s and growing μ imply q→0, so λ→t; when δ≤0, s>t at finite c and λ>t. At an interior minimum λ=t−νk/(my²+k). As δ→0+, y→∞ and inversion of G(y)=2k/y+k(μ₀−m+ν)/(my²)+O(y⁻⁴) gives the claimed reciprocal divergence and quadratic rate improvement. In the rational example δ=50/33=G(3), with λ(2)=−1/11. Independent expansion gives det M=(−33c²+404c−223)/(363(1+c)) and strictly negative trace. Consequently λ is negative precisely between the two positive roots (202±√33445)/33, zero at the roots, and positive at nonnegative concentrations strictly beyond that closed interval. The high-dose limit is positive.

## originality

PASS

The initiating work already contains the model including the constant-reversion specialization, the Perron growth objective, favorable intermediate constant dosing and the bounded-dose schedule result under its hypotheses. The narrower mathematical contribution is the parameter-complete constant-dose phase split, strict uniqueness and exact root, singular transition law, and a rational sign diagram. The indexed finite-period result changes the optimization question. The available evidence supports originality of the narrower claim, not of the drug-plasticity model, intermediate dosing idea, or prior control theorem.

## value

PASS

The classification fills a specific mathematical gap left after the motivating bounded-dose result reduces schedule optimization to choosing a constant. It tells when a cap binds, when zero dose minimizes the model rate, and when exactly one interior dose minimizes it. The coupled divergence and diminishing gain quantify how the finite optimum is lost, and the rational example shows why negative asymptotic growth at an intermediate concentration cannot be inferred from either endpoint regime. This is a useful fixed-model classification, not a clinical assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
