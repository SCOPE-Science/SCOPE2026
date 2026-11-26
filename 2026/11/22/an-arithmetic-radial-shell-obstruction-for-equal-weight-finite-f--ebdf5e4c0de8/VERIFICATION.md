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

Testing the normalized monomials up to 2m-1 forces the radial rule sum alpha_j x_j^k=k!, with alpha_j=q_j exp(-x_j)/C and x_j the distinct squared radii. The square of the polynomial vanishing on all nodes excludes fewer than m radii by positivity of e^{-x}dx, also for adjustable weights. At exactly m nodes orthogonality of the monic node polynomial gives an invertible integer-moment Gram system, so the nodes are algebraic; the first m moments give invertible Vandermonde equations and algebraic masses. For each pair of distinct nodes, exp(x_i-x_j)=q_i alpha_j/(q_j alpha_i) would be algebraic, contradicting Hermite–Lindemann. A common external positive factor cancels and angles do not enter the necessity. The monic orthogonal polynomial has m simple positive roots by the sign-change argument. Interpolation modulo that polynomial gives Gaussian exactness, and integrating squared Lagrange polynomials proves positivity of the masses. Regular 2m-gons remove all off-diagonal terms; weights alpha_j exp(x_j)/(2m) give unit diagonals. Thus the positive-weight minimum is m, while m+1 is a lower bound, not an existence assertion, for equal external weights. The restriction m>=2 is essential: at n=1 a single radius with x=1 and two antipodal samples gives equality. Read CHECK.py and VERIFICATION.md; the reported 106 checks only corroborate finite Laguerre identities and the degree-three example, and the supplied script was not executed.

## originality

PASS

Pass for the equal-external-weight obstruction at the exact radial minimum with arbitrary angles and multiplicities. Classical Gauss–Laguerre quadrature, angular averaging and Hermite–Lindemann are credited ingredients, not separate novel results. None of the inspected comparisons settles the exponential/integer multiplicity constraint at the exact-radial Gaussian threshold; older equivalent cubature statements are not excluded.

## value

PASS

The m-shell baseline is not arbitrary: it is the optimal positive radial count forced by exact Gaussian moments at degree 2m-1. The arithmetic obstruction distinguishes identical physical weights from individually adjustable weights at this natural minimum, even if arbitrarily many angular samples are allowed. It is an all-order structural design obstruction, not a claim that the next equal-weight shell count is achievable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
