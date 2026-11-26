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

Independently use the Schur residual identity: the residual on unselected vertices is the inverse of the corresponding principal precision submatrix. For r remaining A-vertices and s remaining B-vertices set a=t+q, b=t+p. The two within-part contrasts contribute (r−1)/a+(s−1)/b and the constant-on-parts block has trace of inverse (a+b)/(ab−rs). Substituting (r,s)=(p−2,q),(p−1,q−1),(p,q−2) reproduces both positive denominators and all quartic coefficients. Their leading signs in q give exactly one positive crossing each by Descartes and the endpoint signs. Normalization by q³ gives the two simple limiting roots; the coefficients are polynomial in 1/q near zero, giving the asserted O_p(1/q) rates. The signs force AA, AB, BB in order with only the adjacent ties. The stated midpoint lies strictly between the limiting roots and the two negative tests suffice at finite sizes. Independent calculation also reproduces the p=3,q=30 numerical example. The frozen self-review has an incidental 'two ... orbits' typo; there are three as in the actual Finding and proof.

## originality

PASS

The prior Nyström objective is identical; the supported distinct theorem is exact phase order, ties, and the two limiting thresholds for every fixed p≥3 and sufficiently large q. The same-objective p=2 boundary result and heat-trace analog do not cover it.

## value

PASS

The two-landmark posterior-variance problem has three canonical competing configurations. The exact optimizer changes twice, and the mixed phase persists over a nonzero interval even at extreme asymmetry, unlike a lower boundary tending to zero. This fixes both asymptotic scales and provides a finite certificate for checking phase order, rather than just numerical examples or use of a standard trace identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
