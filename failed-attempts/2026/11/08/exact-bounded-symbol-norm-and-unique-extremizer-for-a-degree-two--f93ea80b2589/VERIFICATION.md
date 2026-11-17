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

PASS: In the orthonormal basis e0=sqrt(1-r^2)/(1-rz^2), e1=ze0, the compression imposes m0=m1=0 and m-1=-1. The even boundary weight pushes under z->z^2 to Poisson P_r. The half-angle transformation of the derivative at v=2r/(1+r^2) is odd under t->((1-r)/(1+r))^2/t; strict convexity and coercivity select the unique median. L-infinity/L-one duality against g=z-v z^-1 gives norm >=1/F; the phase-aligned symbol meets all moments, and equality forces uniqueness. Boundary 0<r<1 ensures g has no zero. Independently checked stationarity and strict competitors for five parameters (25 numerical assertions); this supports, but does not replace, the exact argument.

## originality

FAIL

FAIL: an earlier dated and fully read 2 Nov 2026 result gives the same Blaschke family, identical rank-one operator and normalization, coefficient c=2r/(1+r^2), same reciprocal integral and unique bounded symbol; it additionally evaluates the integral with complete elliptic integrals. This is decisive statement-level prior coverage, not merely thematic overlap.

## value

FAIL

FAIL: the entire final exact norm, unique minimizer and symbol formula are supplied by the earlier result, with a stronger special-function evaluation. The submitted proof is correct but provides no independently motivated new mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
