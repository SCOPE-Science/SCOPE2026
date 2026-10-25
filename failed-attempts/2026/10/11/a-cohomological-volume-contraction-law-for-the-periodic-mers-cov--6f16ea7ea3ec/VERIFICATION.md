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

Direct reconstruction from the exact source equations confirms tr J=-(d+d1+c+γ+βDv+β1βvT). From dot T/T=λ/T-βDv-d and dot D/D=λ1/D-β1βvT-γ, the claimed pointwise cohomology follows identically; integrate and use Liouville to obtain the exact endpoint ratio and exponential. On an ω-periodic strictly positive solution the endpoint ratio equals one and λ/T, λ1/D>0, proving det Φ(ω)<exp[-∫(d1+c)]<1. det Φ is positive and equals the product of the complex multiplier moduli, so at least one modulus is strictly below the stated fourth-root baseline. All quantifiers (continuity of coefficients, positivity of T,D; periodicity only for the Floquet portion) and normalization Φ(0)=I were checked. Independent SymPy Jacobian/cohomology identities vanish algebraically; numerical integration of a nonperiodic one-period segment gives det 0.669254913853902 vs both Liouville and endpoint-corrected expression 0.669254913853891, confirming the endpoint factor is necessary off-cycle. The numerical check is not the infinite proof.

## originality

PASS

NARROW BEST-OF-KNOWLEDGE PASS for the explicit log(TD) finite-time determinant representation as a separately stated formula: inspected primary literature does not print that expression for the same four-state periodic model. However, it is an immediate re-expression of the published model equations and classical Liouville identity, not a new stability theorem. The stronger directly evident negative-divergence bound, and the absence of a new dynamical consequence, are decisive under V; do not mistake a distinctive formula presentation for a substantive mathematical advance.

## value

FAIL

The ONLY advertised dynamical consequence is a volume contraction and at least one contracting Floquet multiplier. Yet without any cohomological calculation, the published positive four-state model has tr J=-(d+d1+c+γ+βDv+β1βvT)<-(d+d1+c+γ) at every positive state. Liouville already gives the STRICTLY STRONGER periodic estimate det Φ(ω)<exp[-∫(d+d1+c+γ)]<exp[-∫(d1+c)], and the same fourth-root multiplier deduction. For the published forcing averages the elementary upper bound is 0.8874700356624355 versus the claimed 0.9043571086383213. The exact alternative representation in λ/T and λ1/D is merely the sum of two displayed logarithmic state balances and adds no sharper parameter threshold, sign change, stability classification, bifurcation diagnosis, or new computable invariant. No independently motivated use of the new coordinates is established. Therefore a cheap routine divergence normalization yielding a weaker previously implied conclusion fails the common mathematical-value bar, even though its equality is correct and its formatting may be absent from indexed sources. A repair would require a genuinely substantive surviving theorem, not disclaimers, extra verification or rephrasing; none is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
