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

The scalar Ricker upper comparison x_n<=U_n, U_n→r=1-a exponentially for r∈(0,1), yields summable positive predator log-increments at Delta=0 and strict exponential decline at Delta<0. At neutrality, a putative positive predator limit forces prey eventually below r and contradicts predator stationarity; two scalar Ricker comparisons then give x_n→r. The stable prey multiplier 1-r<1 and slowly varying predator imply (x_n-r)/y_n→-1/(b+r); a reciprocal increment tends db/(b+r)^3, giving n y_n→(b+r)^3/(db) and n(r-x_n)→(b+r)^2/(db). Independently verified the linearization and coefficient symbolically. Strict-invasion rate follows by Cesaro and positive fixed point demonstrates sharpness. The numerical checker tests cases, not the infinity proof.

## originality

PASS

The paired all-positive initial-data neutral amplitudes are not contained in the source model’s local transcritical analysis; broader qualitative convergence is plausibly known but does not imply both coefficients without added asymptotic analysis. The inaccessible Wang–Niu full text remains explicit.

## value

PASS

The exact paired universal inverse-time amplitudes at a sharp biological invasion threshold are nontrivial global quantitative limits for the specific harvested Holling-II Ricker map, meaningful beyond local bifurcation coefficients. The proof combines global comparison and singular neutral relaxation; an arbitrarily chosen initial population does not affect the leading constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
