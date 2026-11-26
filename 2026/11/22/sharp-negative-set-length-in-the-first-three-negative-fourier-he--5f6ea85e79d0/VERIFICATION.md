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

Multiplying the Laguerre generating series by the Gaussian gives (1−s)^(-1/2) exp(−πx²(1+s)/(1−s)); Fourier transforming near s=0 replaces s by −s, verifying eigenvalue (−1)^j. Eliminating the constant at z=0 gives the two stated polynomials A and B; the negative-leading b>0 and b=0,a>0 cases have infinite negative length. The b=0,a<0 case gives exactly the claimed two symmetric intervals and length ≈1.134785527737, with isolated zeros immaterial. For b<0 the positive rescaling gives zQ_t/480. Exact division gives Q_t=D(4z²−60z+150−80t)−180 with D=(z−r_-)(z−r_+). When t≤−1 and z between the roots, the second factor is at least 4(z−15/2)²+5>0, so Q_t≤−180 there and continuity at both roots gives strict extra length. The displayed algebraic Bernstein coefficients also agree with exact expansion. Independent integer/rational replays verified all 140 strict central-strip signs and 10 strict signs at t=2 for the positive tail, and all printed rational length bounds; the bounds exceed 17/10 whereas the target square-root gap is below that. Affinity in t gives entire central strips; positivity of D on [0,1] and [7,12] gives the full t≥2 tail by monotonicity. Touching endpoints in the first strip do not double-count positive length. Thus no t is an additional minimizer and the degree-six positive ray is unique in the specified three-mode space. Uploaded verify.py was inspected but not executed. The finite exact check certifies the listed inequalities, with uniform parameter coverage following from the analytic argument, not sampling.

## originality

PASS

The supported distinction is the exact all-competitor minimum and unique lower-degree ray in the one-dimensional Fourier −1 span of orders 2,6,10. The closest indexed result addresses the +1 space of orders 0,4,8 and is a precedent for the question, not an equivalent theorem. Other nearby work has different dimensions, Fourier signs or an eventual sign-radius objective. The exact −1 catalogue hit was this frozen record itself, and some close full texts could not be freshly inspected; no universal priority claim is made.

## value

PASS

The first three negative Hermite modes and the origin condition are canonical restrictions for the definite-set question. It is not obvious that the additional admissible degree-ten component cannot improve the measure; the exact certificate over the full parameter line proves that it never does. The value is an exact benchmark and rigidity statement for that natural finite family, not an unrestricted bound or a handpicked numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
