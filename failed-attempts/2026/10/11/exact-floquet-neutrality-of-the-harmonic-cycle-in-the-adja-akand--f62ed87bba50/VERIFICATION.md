---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For all n>=0, the source equation gives F=(y,-x(R+yS_n)y-x^(2n+3)) with R=x^2+y^2-1 and S_n=sum_{l=0}^n x^(2l). The finite geometric identity (1-x^2) S_n=1-x^(2n+2) implies exactly Rdot=-2xy(y+S_n)R, so the unit circle is invariant. On gamma=(cos t,-sin t), the normal log multiplier is -2 integral_0^(2π) xy(S_n+y)dt=0: the S_n term is integral of exact xS_n(x) dx along a closed path and the other is integral cos(t)sin^2(t)dt=0. The normal multiplier is 1, and the tangential autonomous multiplier is 1. A separate direct parity/reversibility proof also forces the same value. Independently expanded the complete polynomial defect identity for n=0,1,2,3,5 using symbolic exact arithmetic; these finite checks are corroboration only. Poincaré map may have nontrivial Jordan/shear in full 2D, and no exponential hyperbolicity is inferred.

## originality

FAIL

Decisive covered corollary. The 2022 primary source gives the exact harmonic orbit of its polynomial family. Every member is reversible under sigma(x,y)=(-x,y), because S_n is even and the vector field obeys F(sigma z)=-D sigma F(z). The orbit intersects Fix(sigma)={x=0} transversely. Classical reversibility theory explicitly states sigma P sigma=P^{-1} on a symmetric periodic orbit Poincaré map (Vanderbauwhede 2012, Sections 2,4) and reciprocal Floquet eigenvalue pairing. On the 1-dimensional section x=0 the involution sigma acts identically, so P=P^{-1}; since a planar flow first-return map preserves order, P is locally identity, and its derivative is 1. The tangential autonomous Floquet multiplier is 1. Indeed a local annulus of symmetric cycles is forced, a statement stronger than the submitted neutrality. The normal-defect identity is an elementary special-purpose algebraic verification and cannot distinguish this claim from the general known theorem. The exact indexed Resultary copy is not counted as independent prior literature.

## value

FAIL

Although Floquet multipliers are mathematically natural invariants for a displayed oscillator, the submitted value is an immediate established reversible-systems consequence of the introducing paper's exact known symmetric orbit. The entire main theorem follows by checking even/odd parity of the coefficients and applying standard return-map conjugacy; the claimed exact polynomial normal-defect law is short routine geometric-series algebra that adds no independently motivated new invariant, classification, or structural boundary not already forced by the broader theorem. Rechecking a known corollary in custom coordinates, even for all n and with correct code, does not satisfy the required nontrivial-value standard. The stronger local periodic annulus is also a generic reversible-flow consequence and cannot rescue the original claim as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
