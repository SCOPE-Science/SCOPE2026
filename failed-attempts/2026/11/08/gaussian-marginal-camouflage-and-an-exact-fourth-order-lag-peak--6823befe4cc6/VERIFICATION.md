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

PASS

Equilibrium redraws produce the exact bivariate mixture w times the stationary OU Gaussian pair plus (1-w) independent equilibrium endpoints, w=e^{-rt}. Wick's rule gives K(t)=2v² e^{-(r+2lambda)t}(1-e^{-rt})>0. Its derivative has one positive root t*=r^(-1)log[2(r+lambda)/(r+2lambda)], and reparameterizing s=rt establishes the monotone peak and two endpoint limits. The same-covariance Gaussian has smaller mutual information by the strict Gaussian maximum-entropy/KL identity. Independent symbolic calculation checked K against the earlier *general four-time cumulant* with coincident endpoints and verified the maximum derivative. The finite numerical checks are not necessary to establish the identities.

## originality

FAIL

The earlier November 2 published theorem on Poisson-rethermalized OU motion gives precisely the same process as its stationary velocity, matching covariance, and the full connected four-time cumulant 2sigma^4 exp[-(gamma+r)(a+2b+c)](exp(rb)-1), including repeated time limits. Set a=c=0, b=t, gamma=lambda, sigma²=v to obtain the submitted K(t) IDENTICALLY; the time maximizing this difference of two exponentials follows by a one-line derivative. The bivariate mixture is immediate from the same renewal process, and the strict mutual-information excess is the standard Gaussian entropy extremality for that positive cumulant. Thus the main quantitative claim and natural consequences are subsumed; a fresh proof cannot restore originality.

## value

FAIL

The proposed novel fourth-order lag peak is a routine extremization of an exact fourth-order correlation function already available for this identical model from a stronger prior theorem. The bivariate mixture and strict mutual-information inequality are immediate conditioning and Gaussian extremality, not independent motivated gaps after that coverage; correctness and a physical interpretation alone do not create distinct mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
