---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The logit equilibrium equations, trace crossing, canonical linear normalization, Taylor derivatives and first Lyapunov coefficient in RESULT.md reconstruct consistently. The formula ell=-beta_H[p(2+za/q)+epsilon(1+theta)N(1-N)(-2q+za)]/16 follows using the sigmoid identity H3p^2-H2^2p/H1=-2 beta_H h, and yields the stated theta=1/3 condition. Explicit rational/logarithmic witness has 0<N<1 and opposite signs for eps=100 and 400. This is a correct local Hopf classification; the cubic-zero case does not prove a Bautin point.

## originality

FAIL

FAIL. Already published on 2026-10-26 and independently on 2026-11-02: identical two-strategy logit-resource ODE, identical beta-Hopf crossing, first Lyapunov sign threshold and impossibility for theta>=1/3. Under s_prior=-s_submitted, the November 2 variables a=P-R-s_prior-T, b=R+s_prior, c=s_prior-P, constant -s_prior agree exactly with the submitted a,b,c,s. Its M=(1-3theta)(P-s_prior)-(3-theta)(R+T) is - (1+theta) times submitted C2. Numerical examples differ but not the theorem.

## value

FAIL

FAIL. A new witness and a reparameterized analytic Hopf coefficient are useful consistency checks but cannot constitute an original, motivated mathematical advance after two earlier complete exact sign classifications of this model. No distinct final mathematical theorem survives unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
