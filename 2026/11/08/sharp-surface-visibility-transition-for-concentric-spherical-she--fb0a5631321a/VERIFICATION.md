---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS. Verified the three actual boundary-pair cases: outer/outer sight requires Z>=2rho^2-1, mixed requires Z>=rho, and inner/inner has zero positive visibility. Surface weights produce the displayed Q_d mixture. Monotonicity follows by coupled component selection and increasing angular thresholds; d=3 formula independently reduced symbolically to (1-rho^3)/(1+rho^2)^2. The Gaussian normal representation of Z gives the d^-1/2 window; integration by parts with gamma-ratio asymptotics gives the fixed-rho prefactor; mixed terms decay exponentially faster, not merely numerically. The fixed-d thin-shell calculation uses Q_d(1-h)~c_d2^((d-1)/2)h^((d-1)/2)/(d-1), consistently reproducing the stated constant. Only specified fixed-parameter or critical-window limits are proved.

## originality

PASS

PASS (best-of-knowledge). The published Oct11 result concerns volume-uniform interior endpoints with radial integration. Its all-odd-dimensional rational formula cannot imply the boundary mixture with a different weight rho^(d-1), high-dimensional Gaussian critical window, or surface-only thin shell constant. Sidiropoulos concerns endpoints on one sphere and supplies prior angular density, not the two-component mixture; full text of this older paper was not inspected. Exact targeted searches found no covering surface theorem, but no worldwide-priority assertion is made.

## value

PASS

PASS. A two-boundary surface sampling model is a natural contrast to volume Beer-index sampling. Its exact all-dimensional visibility law, sharp dimension-dependent phase boundary, and inverse-radius identifiability form a nonroutine probabilistic geometric classification; the Gaussian window and rare-tail prefactor give independent quantitative uses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
