---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent extraction of all nine coefficients from F^4 gives the displayed diagonal and six zero off-diagonal entries. The smoothness factors are obtained by applying the gradient equations to the squared nonzero coordinates, with a 2-by-2 minor for each two-coordinate support and the 3-by-3 determinant for full support. On this open set the Hasse differences force a^2=b^2=c^2=s as equations in the coordinate ring, not just at geometric points. The remaining equation is abc=s^2+2; (abc)^2=s^3 gives (s+1)^2(s^2+2s-1)=0. Since s+1 is a unit, s^2+2s-1=0, so s is invertible. Then r=abc/s has r^2=s and r=3s+4, equivalently r^2-2r-2=0. The three ratios a/r,b/r,c/r square to 1 with product 1, and conversely these relations give all the equations with every smoothness factor invertible. This gives the claimed scheme isomorphism directly over F5: four sign choices and the separable irreducible quadratic of discriminant 2. Each degree-two closed point contributes (1-T^2)^(-1). An independent Gröbner calculation using the inverse variable w=1/Delta additionally gives w+2c^2+2, a+bc^3-bc, b^2-c^2, c^4+2c^2-1, yielding the same reduced ring and degree.

## originality

FAIL

The earlier Resultary characteristic-five p-rank strata result already derives exactly the same marked superspecial triples and all-extension counts from the equal-square and diagonal-polynomial equations. A distinct same-day record gives the same three Hasse polynomials after relabeling and proves independent differentials at all eight triple zeros, covering the very scheme structure singled out here. Disjoint quadratic points and the zeta function then follow directly. The verdict rests on established mathematical coverage, not on an assumption about order within the same UTC day or on the inaccessible Brock dissertation.

## value

FAIL

The transverse marked superspecial intersection is a natural geometric object, but the frozen result does not add a useful new invariant to the exact points, transverse equations, and parity counts already available. The decomposition and Euler product simply repackage that evidence, and the explicit Jacobian scalar is a choice-dependent check, not a new geometric result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
