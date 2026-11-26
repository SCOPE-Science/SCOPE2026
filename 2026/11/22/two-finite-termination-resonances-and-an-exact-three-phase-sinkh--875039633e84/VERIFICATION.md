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

For the symmetric balanced scaling DAD with hub and leaf factors x,y, the row equations are x²=1−mc and y²=(1−c)/(m+1), c=txy. The equation for t² increases strictly from zero to infinity, supplying existence and uniqueness. On the nonconstant subspace the balanced eigenvalues are (1−c)/(m+1) with multiplicity m−1 and 1−(m+1)c with multiplicity one. The log-factor derivative is the product of the two negative balanced half-step matrices, so squaring these eigenvalues gives the full projective factor. The equations b=a and b=−a give c=1/(m+2) and c=(m+2)/(m²+2m+2); strict decrease followed by strict increase proves the optimum, with the claimed value. Independently, every half-step on this initialized orbit replaces the active hub/leaf ratio r by R(r)=(tr+m+1)/(r+mt), starting at r=1. Away from mt²=m+1, R is injective, so if an iterate attains the balanced ratio (a fixed point), then 1 was already that ratio. R(1)=1 gives t=m/(m−1), and the symmetric initial matrix then has common row sums. When mt²=m+1, R is the constant t>1 and fixes both factor ratios in exactly two half-steps, not one. Substituting c=1/(m+1) at this resonance gives the stated rate ratio. The ordering after squaring separates by (m−2)(m³+2m²+m−2), with equality only at m=2. Symbolic factoring independently matched the frozen two-step residual.

## originality

PASS

The general local-rate formula, at-most-two-steps theorem, and certain small-instance scaling limits are already covered. No distinct retrieved statement covers the full family-specific competition of the leaf and hub modes, its exact optimizer, and the classification and comparison of initialized resonances. Credit is limited to that classification, not to the general matrix-scaling methods.

## value

PASS

A symmetric but non-block-constant natural test family exposes two distinct nonconstant mechanisms; the complete tuning classification shows when a fully symmetric orbit hides the worst perturbation and why exact termination can be suboptimal in the projective criterion. This is a useful distinction beyond producing a single scaling limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
