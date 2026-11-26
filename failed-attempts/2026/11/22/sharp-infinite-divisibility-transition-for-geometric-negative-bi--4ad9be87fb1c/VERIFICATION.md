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

The pgf has quartic numerator (1-qz)^4+delta^4 and a pole of order five at 1/q. Its log coefficients are q^n/n times five minus the reciprocal power sum of the four rescaled numerator roots. For delta >= sqrt(2) all rescaled moduli are at least one, giving coefficients between q^n/n and 9q^n/n, hence summability and compound Poisson including equality. Below the threshold the nearer conjugate pair dominates along infinitely many n with cosine > 1/2 (periodicity or irrational rotation); the farther pair decays. Each pure endpoint is negative binomial, with positive summable log coefficients. The density as displayed splits into normalized exponential and shape-five gamma components, giving q=1/(1+lambda), delta^4=576/[lambda(1+lambda)^4(lambda^5+48)], and the stated unique cutoff by strict monotonicity; positive intensity variance verifies overdispersion.

## originality

FAIL

The earlier integer-shape zero-inflated NB result materially covers the phase transition and its purported strengthening. Its full proof treats the identical quartic numerator at shape four. The extra geometric factor changes the pole order but cannot change the smaller logarithmic convergence radius on the subcritical side, or produce a singularity at the positive real point at that radius. The same prior Pringsheim argument implies infinitely many negative coefficients by subtracting a polynomial if there were only finitely many. The XRani boundary then follows by substituting the explicit mixture weights. Different pgfs do not give distinct threshold mathematics here.

## value

FAIL

The infinite-divisibility question for the named law is natural, but the asserted mathematical advance is the same root obstruction already proved for the identical quartic. Adding the known geometric log series, removing a possible finite negative polynomial, and substituting the elementary XRani weights do not supply a substantively distinct result under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
