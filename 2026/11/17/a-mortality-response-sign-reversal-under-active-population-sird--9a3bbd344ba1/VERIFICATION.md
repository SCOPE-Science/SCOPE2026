---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For the homogeneous invariant two-group sector, d=t(1-x)/(1+t) and x=s exp(-u). Integration gives u=(r/t)log[(1+t)/(1+t x)] for active and u=r(1-x)/(1+t) for fixed incidence. Unique positive fixed points follow from strict concavity and boundedness. The analytic expansion in epsilon=1/t gives active coefficient sr log(1/s)-(1-s), fixed coefficient (1-s)(sr-1); on r=(1-s)/(s log(1/s)) the active second coefficient is -(1-s)^2/(2s). Since log(1/s)>1-s, the wedge is nonempty; analytic remainders give the eventual opposite derivative and sidedness. Endpoint d_active(t)->0 as t->0 plus continuity and finite excess gives an attained finite positive maximum, not uniqueness. Independently recomputed coefficients with SymPy and fixed points numerically at s=1/2,r=3/2,t=100,1000,10000.

## originality

PASS

The 2026 originating SIRD paper defines living-population normalization and studies mortality response, while the published unrestricted multigroup theorem establishes uniqueness and certified root bounds, but neither inspected theorem states or algebraically implies the matched active-versus-fixed high-mortality sign wedge and equality second-order coefficient. These emerge from two distinct model equations and their asymptotic comparison. No matching prior record located; historical search is not proof of priority.

## value

PASS

The two standard force-of-infection normalizations can predict opposite qualitative large-mortality response even with identical epidemic rates and initial fractions. The sharp nonempty parameter region isolates the mechanistic living-denominator feedback and is a directly motivated modeling invariant, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
