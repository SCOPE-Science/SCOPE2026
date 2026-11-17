---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For all 0<beta<pi/2 and beta<=alpha<=pi/2, direct Fourier integration yields Gram diag a=2beta/pi, off-diagonal u=2 sin(beta)cos(alpha)/pi and v=sin(2beta)cos(2alpha)/pi. Reflection splits an antisymmetric eigenvalue a-v and a symmetric 2x2 block. At antipodal separation the minimum is a-B; at t=cos(alpha)>0 the shifted symmetric block determinant is 2t^2(B^2-C^2)<0 (C=2sin(beta)/pi>B), proving strict unique optimality; exact loss and Taylor series follow from the closed eigenvalues. Small-window comparator is a single arc of total length 4beta, giving leading 64beta^5/(135pi). Independently integrated Gram spectra and tested analytic identity; finite checks do not prove all real parameters.

## originality

FAIL

FAIL: The published 1 November three-mode antipodal-maximin theorem is exactly the same mathematical statement, after unit-modulus modulation of its Fourier span. It gives the same arc domain, sharp minimum eigenvalue, and unique equality. Its further frame-potential bifurcation is stronger in a second criterion. A same-date 8 November larger-band theorem also gives the m=1 exact result, although no intraday priority inference is made. The candidate exact loss and contiguous-arc expansion follow directly from the already known 3x3 eigenvalues and do not rescue this covered headline.

## value

FAIL

FAIL: The main unique maximin theorem and exact optimal value are already published for identical objects and parameters. The leftover algebraic rationalization, local quadratic loss and routine same-length single-arc Taylor expansion are simple consequences of the known Gram spectral formula, not a separately motivated unknown classification or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
