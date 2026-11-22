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

The Dulac factor B=1/(xy) differentiates to −r/(ky)+a/(x+b)²−σ/x, strictly negative for σ≥a/(4b), including equality by (x+b)²≥4bx. Conversely for any σ below cutoff choose k>3b and sufficiently small r with e∈(0,1), then y*=2rb(k−b)/(ak), d=ea/2−σy*>0. The predator nullcline slope strictly exceeds the prey nullcline slope across the rising range, so their only positive intersection is x=b; the Jacobian trace and determinant are positive by the strict k,r choices. Boundedness, positive invasion at (k,0), invariant boundary axes and unstable unique interior equilibrium allow Poincaré–Bendixson to produce a positive periodic orbit. Independently checked the exact rational example: x*=1, y*=29/1500, trace 19/30000, determinant 2233/1875000, and verified the Dulac identity algebraically. No uniqueness or stability of cycles is claimed.

## originality

PASS

Best-of-knowledge originality relative to compared statements and actual independent material, not a proof of absolute priority. Sharp quantifiers are σ fixed with all other positive parameters arbitrary for exclusion AND existence of some parameter choice for every σ smaller. Local Hopf conditions and mortality thresholds are not equivalent; Lu–Huang remains substantive historical-priority risk.

## value

PASS

An exact global no-periodic-orbit versus cycle-realizability threshold for a biologically standard saturating predator-prey system provides a clear structural boundary, including equality and a constructive converse. A sharp parameter-uniform criterion is more useful than a generic Dulac sufficient condition or one numerical Hopf example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
