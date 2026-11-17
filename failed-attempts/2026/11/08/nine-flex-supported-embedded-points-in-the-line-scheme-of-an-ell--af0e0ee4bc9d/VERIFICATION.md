---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The Grassmannian binary-cubic restriction gives four coefficients. After linear tangent elimination, the quadratic coefficient is kappa(t)e^2 and cubic is tau(t)e^3. At ordinary points kappa is a unit, giving e^2=0; at nine simple flexes kappa has simple zero and tau is unit, giving (t e^2,e^3). The conormal first layer is O_E(1), the second is nine length-one skyscrapers; Riemann-Roch yields 3n+3(n+1)+9=6n+12. Independent local Groebner and Hilbert identities checked.

## originality

FAIL

FAIL: published general plane-curve cone theorem on the same date covers every smooth complex plane curve of degree d>=3 with local ideal (t^(r-2)u^2,...,u^r), conormal O_C(d-2), and full Plucker Hilbert polynomial. Setting d=3 (nine simple flexes, r=3) gives exactly both local rings, nine embedded residues and P=6n+12.

## value

FAIL

FAIL as a distinct contribution beyond the published general contact-filtration theorem; the cubic is its straightforward natural specialization. The underlying scheme is a meaningful object but no independent theorem or new mechanism remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
