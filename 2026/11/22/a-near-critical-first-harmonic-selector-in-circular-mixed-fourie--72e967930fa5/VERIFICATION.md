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

The adjacent recurrences cancel their mixed derivative terms; differentiating the proposed quartic primitive directly gives r(J_n^4-J_{n+1}^4). Its boundary values are zero and 2/[pi^2(2n+1)]. Hankel errors are integrable uniformly for 4<=p<=5 at each fixed order, and the difference of equal-mean periodic profiles is controlled by one bounded primitive, which justifies p down to 4 at fixed orders. The decisive uniform tail input was checked in Xu's original layout: (3.70), its transition estimate and Proposition 3.15's large-r estimate (3.75) give the mean tail A(4+t)v_k^(-t/2)/t; the p. 31 bounds for E1,E2,E3 are respectively 3/125, 13/55, 4/25 times (8/15)^t. Their sum is 578/1375 times that factor, so the frozen weaker bound is valid for k>=4, 0<t<=1. By contrast the fixed m lower tail from any large fixed R is A(4+t)R^(-t/2)/t-O_m(1), uniformly for that range. For k>=K use v_k>=v_K before sending t to zero: the difference of the two tails tends to (A(4)/2)log(v_K/R), which can dominate both errors; only finitely many k remain. This handles the quantifier issue. For arc length as stated, Parseval and Minkowski in L^(p/2)(r dr) give the coefficient (2pi)^2 times the squared modal gap and a pure mode 1 attains it. The common residue 3/pi^2, gap 2/pi^2 and (p-4)log(p-4)->0 give 4pi/sqrt(3) via the mean-value theorem. The frozen symbolic check was inspected, not executed; it would not establish the uniform Bessel bound.

## originality

PASS

The fixed-order endpoint gap and its normalized coefficient, the leading pole, and the general spectral stability reduction are prior work. The novel step supported here is a uniform near-critical open interval against every higher degree for each fixed lower index, in particular selection of the sharp first nonconstant degree. The prior fixed-index law cannot justify this quantifier, and Xu's uniform upper bound must be used with its v_k-dependent singular factor and a separate lower fixed-mode estimate to close the gap. The other first-mode determinations inspected are not near the endpoint.

## value

PASS

This identifies the actual worst nonconstant degree in a sharp inequality at its critical boundary, in a regime not addressed by the known even/high exponents. Preventing mode escape makes the known fixed-mode endpoint coefficient into an exact global coefficient. The interval need not be optimal or explicitly numerical for this infinite-order conclusion to be useful; it does not settle the intermediate exponent regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
