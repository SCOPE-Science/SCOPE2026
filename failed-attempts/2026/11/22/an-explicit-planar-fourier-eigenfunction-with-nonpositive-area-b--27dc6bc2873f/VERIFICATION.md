---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two-dimensional Gaussian transform sends the parameter t of the ordinary Laguerre generating function to -t; even indices and L_j(0)=1 give a real nonzero self-Fourier Schwartz function vanishing at 0. The finite binomial expansion gives zQ(z)/8!. An independent integer sign check uses D_[a,b](t)=(1+t)^7 Q((a+bt)/(1+t)); on [0,4] its coefficients in increasing order have signs -------+, so Descartes' rule and the endpoint signs give one zero in (0,4). The minimum coefficients in the same test for [4,7], [7,10], [10,16], [16,24], [24,26], [26,28], [28,32] are respectively 83223, 83223, 3469440, 19229184, 1105024, 1105024, 42986496. All coefficients of Q(32+t) are positive. Integer Horner evaluation gives Q(73/20)=-4366428590023/1280000000 and Q(183/50)=85807489517127/781250000000. Thus the sign change is unique, the origin is a zero, and the nonpositive set is the full closed disk with area rho/2 in the stated interval. This proves the inequality, not historical improvement.

## originality

FAIL

Cohn–Gonçalves, arXiv:1712.04438v3, Problem 1.1 and §4, give a rigorously certified planar +1 eigenfunction sign-radius bound 0.756207 in Table 4.1, using Gaussian–Laguerre polynomials with g(0)=0. In their class the zero set has area zero. Their admissible witness therefore gives nonpositive area at most pi times its squared radius, in particular less than pi(0.757)^2 < 73/40 < 183/100. This proves the headline unrestricted bound with a stronger value. The exact tuple (22,20,-4,1) was not found in the inspected text; the prior implication is numerical and structural, not a claim of identical coefficients.

## value

FAIL

A small rational example is pedagogically usable, and unrestricted definite-set minimization is well motivated, but the frozen contribution is presented as a strict improvement for that problem. An older exact construction gives a better area bound, and the package has no sharp degree cutoff, constrained new optimum, or other independently justified need for this particular larger-area tuple.

The dated certificate retains the supplied scientific assessment, sources and limitations.
