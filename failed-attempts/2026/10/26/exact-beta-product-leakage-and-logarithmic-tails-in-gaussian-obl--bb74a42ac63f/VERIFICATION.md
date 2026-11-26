---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the orthonormal pairs, L u_perp=a u and R v_perp=b v, where a,b are the two projected scalar slopes. Accordingly the only nonzero block is [[-ab,a],[b,0]], so the squared norm is a^2+b^2+a^2b^2 and the orthogonal projector gives zero. The normal component of a Gaussian sketch column along the independently sketched state direction is standard normal conditional on that direction and length. Thus each slope is G/sqrt(Q) with G standard normal and Q independent chi-square with s degrees of freedom; the two slopes are independent. Ratios Q/(Q+G^2) give the two independent beta variables. Conditioning on the first beta factor gives the tail integral including t=0; beta integration gives the stated Mellin transform for real p<alpha and the positive-moment cutoff for W. At p=1 the reciprocal first moment is (s-1)/(s-2) for s>2, giving (2s-3)/(s-2)^2; it diverges for s=2. For the logarithmic tail, negative log of a beta factor has density B_*^-1 exp(-alpha z)(1+r(z)), where r=(1-exp(-z))^-1/2-1 is decreasing and integrable. Splitting the convolution at z/2 bounds (r*r)(z) by 2 r(z/2)||r||_1 for z large, so the integrated density has leading term z exp(-alpha z)/(alpha B_*^2). Substitute log(1+t), then t=x^2 for the norm. With either one-sided sketch, the symmetry of the scalar laws lets one set the other slope to zero; the beta endpoint gives x^(-s)/(alpha B_*) asymptotically. The archival verifier was inspected but not run; simulations and finite quadrature do not prove these claims.

## originality

FAIL

Two verified sources together cover the core as a direct corollary. Resultary 359d8df14ce8 studies a symmetrized statistic, but its Proof §§1–2 explicitly gives the entire pre-symmetrization block Pi_rho(Z) and the Gaussian-ratio marginal laws under its specified coupling. Setting rho=0 gives two independent G/chi_s slopes. This is exactly the audited stochastic block in canonical coordinates; Gaussian rotation invariance and padding unused columns give arbitrary orthonormal pairs and the rectangular ambient dimensions. Taking its unsymmetrized norm gives the elementary identity 1+W=(1+a^2)(1+b^2). Each reciprocal is Beta(s/2,1/2), so the exact law, Mellin transform, and leading logarithmic coefficient are specializations of known beta-product laws, including Dunkl §5.1 with coincident first shapes. Setting one slope to zero yields the single-beta comparison. The catalogue comparison is about demonstrable mathematical coverage, not a claim of historical priority: the related catalogue record carries a later displayed date and has a different stated target, but the intermediate matrix law overlapping this claim is explicit.

## value

FAIL

The discrepancy between orthogonal and oblique handling of a normal forcing is a natural diagnostic, and the one-sided/two-sided contrast is useful. In the submitted narrowly specified test, however, the model's full random block is already given by an indexed result, and the exact invariant is a direct algebraic specialization of a known product law. The moment and one-sided consequences require no additional invariant or new geometric distinction beyond that block. This is insightful exposition of a known implication, but does not establish a surviving independently valuable new exact claim under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
