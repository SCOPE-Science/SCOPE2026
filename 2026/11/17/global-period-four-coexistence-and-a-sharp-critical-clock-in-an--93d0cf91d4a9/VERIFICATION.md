---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For mu>-1, nu>-2 the odd cubic T(z)=z+z³ and the second odd implicit relation are strictly invertible. The two-step return is odd strictly decreasing, and its modulus f is continuous strictly increasing and sublinear at infinity; every amplitude orbit is eventually monotone and bounded. Substitution a=b+b³, t=b² gives exact residual -b H(t), H=t^4+3t³+3t²-nu*t-mu, with H strictly convex. Root counts and the unique fold tc follow from H′=0, muc=-3tc²(1+tc)². At positive roots 1-f′=2tH′/[(1+3t)(1+3a²)], determining stability and basins. Independent symbolic expansion verifies f(a)=a-3a^5+O(a^7) at mu=nu=0, yielding n a_n^4→1/12 by reciprocal difference; for mu=0,nu<0 the cubic term yields n a_n²→-1/(2nu). Endpoint mu=muc within mu>-1 is correctly conditioned.

## originality

PASS

Oliveira first defined the same alternating cubic implicit system and its local degenerate flip; the exact globally monotone return map, quartic all-real root census, bistable four-cycle basin separation and sharp critical clocks extend those local conclusions. Existing general nonautonomous GAS exclusion does not imply model-specific fold/basins.

## value

PASS

An exact global period-four coexistence/bistability partition for a published local degenerate-flip example, with a precise algebraic fold, repelling separator and two critical power-law clocks, is a natural and useful strengthening. It supplies global information not present in local normal-form coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
