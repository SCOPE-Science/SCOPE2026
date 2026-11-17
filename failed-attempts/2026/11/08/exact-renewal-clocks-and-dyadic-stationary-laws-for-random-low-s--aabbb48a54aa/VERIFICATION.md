---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

FAIL

The renewal-time formula tau=B+G+1, pgf zP(z)/(2-z), shell masses Pr(B+G>=j), invariant mass E[B]+2 and renewal covariance identity follow correctly by conditioning on binary digits and the transfer equation. However, RESULT.md additionally describes the successive returned positions as "independently uniform" and says "independently uniform returned positions" without restricting independence to excursion labels. Read literally as independence between return coordinates, that assertion is false: take deterministic B=1, independent stationary first-return X0 and X1. Both have uniform marginals on (1/2,1], so Pr(X0>7/8)=Pr(X1>7/8)=1/4. Yet X0>7/8 forces the first geometric digit G=0 and X1=2X0-1, giving Pr(X0>7/8, X1>7/8)=Pr(X0>15/16)=1/8, not 1/16. Thus a stated independence quantifier fails; conditional uniformity given current excursion length remains valid. 57 independent exact-rational shell-density equivalences and this analytic counterexample were checked; a finite test is not a replacement for the analytic counterexample.

## originality

FAIL

The mathematically sound main package, including exact invariant shell densities, finite/infinite mean criterion, iid return times B+1+G and return pgf, was already explicitly proved in the published Nov 1 Resultary theorem for precisely this same family and all countable reset distributions. The later U(z)=1/(1-F(z)) and section-indicator covariance are standard renewal consequences of that prior exact iid clock and stationary section mass; they do not establish an independently original scientific claim. Further the returned-position iid implication is false.

## value

FAIL

Correct original elements would merely evaluate routine renewal generating functions and stationary indicator covariance from the earlier full distribution, without a separately motivated new hard invariant. The extra claimed independence of consecutive return coordinates is incorrect. No distinct worthwhile original claim survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
