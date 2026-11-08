---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproduction

Run `python verify_star.py` with the Python 3 standard library. The script independently enumerates all injective labelled states for \(3\le n\le7\) and \(2\le k<n\), rebuilds allowed and colliding jump rates, verifies the positive killed-generator eigenfunction at every state, and checks the two-state matrix exponential against analytic formulas. It printed `PASS: 50965 finite-state and numerical identities; n=3,...,7; 2<=k<n`.

## Analytic evidence

The infinite-parameter result follows from an exact two-class lumping, an explicit \(2\times2\) matrix exponential, and a positive eigenfunction of the full killed generator. The Doob transform equalizes the two class-switch rates to \(\sqrt{k(n-k)/(n-1)}\); this yields independent equal-rate exponential holds and therefore a Poisson switch count. Terminal-time survival and suppressed-jump stationary distributions follow from the same two-class generator but use different normalizations.

## Limits

Finite checks are diagnostic only; they do not establish all integer sizes or all continuous times. No independent review or certification has been carried out. The claimed novelty concerns exact hub laws for the star, not the general Doob-transform method.
