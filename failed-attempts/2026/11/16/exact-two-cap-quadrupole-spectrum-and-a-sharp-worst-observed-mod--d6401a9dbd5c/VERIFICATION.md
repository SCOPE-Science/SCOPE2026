---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For two disjoint equal caps centered on orthogonal x and z axes with c>=1/sqrt2, the pure degree-two spherical-harmonic basis q=(x²-z²,x²+z²-2y²,xz,xy,yz) is globally and regionally orthogonal. Independent normalized monomial integrations using the uniform sphere measure reproduce exactly polynomial eigenvalues A,B,C,D,D and trace 5(1-c); symbolic factorization gives B-D=(5/32)c(1-c)(1+c)(9c²-5) and B-C=(5/32)c(1-c)(1+c)(15c²-11). Thus the least eigenvalue has the claimed 1→3→2 dimensional eigenspace at sqrt(5)/3, secondary B=C crossing at sqrt(11/15), and A remains greatest; asymptotic Gram condition number ~1/(1-c) follows. Independently verified the entire result as exact specialization of previously published arbitrary-center-angle five-sector spectrum. Correct mathematics is not evidence of originality.

## originality

FAIL

Decisive mathematical prior coverage. Published November 8, 2026 full result gives the five eigenvalues at EVERY allowed separation theta, not just its title optimal-placement theorem. Setting q=cos(theta)=0, t=c in its proof yields A=2mu2+beta+gamma, B=2mu2+(beta+gamma)/3, C=2mu2+beta, D=2mu2+beta/2 (twice), where mu2=1/2-15c/16+5c³/8-3c⁵/16, beta=15c(1-c²)²/8, gamma=15c(1-c²)(7c²-3)/32. Independent exact symbolic subtraction gives zero against all four proposed polynomials. Both crossing thresholds and eigenspace multiplicities follow as factorization corollaries of those published same-operator eigenvalues. The current final claim is therefore a covered restriction, not original.

## value

FAIL

Although the cap localization problem is inherently motivated and formulas are correct, this submitted theorem adds only a restriction to perpendicular centers of an earlier full arbitrary-angle five-eigenvalue result. Its most substantial claimed worst-mode phase transition is explicitly in the prior theorem; the secondary internal branch crossing is routine exact algebra from already published formulas. As a separate new finding, the claimed increment is not mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
