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

With A=U_n, B=U_(n+1), D=U_(n+2), the sign of the usual hazard increment is the sign of S_(n+1)^2-S_n S_(n+2). Clearing positive factors gives B^2-AD-cB[B(A+D)-2AD]; B^2-AD=e^(-2(n+1)t)t^2 and B(A+D)>2AD. The failure-odds convention preserves all signs and ties. Independently expanding with r=1+z+t gives P=r[2(cosh(t)-1)r^2-2t sinh(t)r+2t^2], and yields the displayed cubic coefficients. The constant coefficient of P-P' is negative, the leading coefficient positive; when q>=1/2 both middle coefficients are nonpositive (the linear coefficient is strictly negative using 1-q>=qt and 5-4/q+1/q^2<=2), and when q<1/2 the quadratic coefficient is positive, allowing only one sign change irrespective of the linear coefficient. The positive root is unique and the continuous threshold strictly decreases then increases; comparing its two neighboring grid points gives the exact minimum, strict sublevel sets give one finite block, and C_0<1 follows from E-(B^2-AD)=D(1-B)^2 at A=1. For t approaching zero, the scaled cubic tends to z(z^2-2z-1); fixed positive brackets on either side of 1+sqrt(2) trap its unique positive root despite the limiting root at zero. Local uniform convergence, strict transverse limiting level crossings and lattice unimodality trap both extreme indices for the stated fixed c, and prove the critical-tilt limit. A separate rational certificate verifies the six strict signs in the example; the infinite tail follows from unimodality, not the finite computation.

## originality

PASS

The same-model survival, discrete failure odds and qualitative hazard illustrations are known. The supported distinct contribution is the exact lattice-age threshold and finite global minimization, the all-parameter contiguous-block theorem, and the associated discrete fine-resolution limits. Inspected same-model and analogous results do not give that combination or imply the exact discrete decision rule.

## value

PASS

For an existing fitted lifetime family, the cubic gives a sharp finite decision procedure in place of arbitrary finite-age plots, identifies a certified regime with two reversals, and rules out hidden decreasing blocks on infinite support. The limiting turn separation explains a feature that a fixed observation window can miss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
