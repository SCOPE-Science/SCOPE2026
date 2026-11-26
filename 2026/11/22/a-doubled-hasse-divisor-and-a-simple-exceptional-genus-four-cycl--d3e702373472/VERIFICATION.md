---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Here smooth family means the squarefree, genus-four family, not that the normalization of a singular model is nonsmooth. At distinct cubic roots and at infinity the tame degree-five map is totally ramified; Riemann–Hurwitz gives genus four. Regularity of the four forms follows from ord∞(x,y,dx)=(-5,-3,-6) and ord at a simple branch point of (y,dx)=(1,4); character separation and the two different x-powers give independence. In the j-block, writing y^(−j)=(y^(−j))^31 f^(6j) and retaining degrees 31(k+1)−1−i yields the ordinary polynomial coefficient matrix (entrywise 31st powers of the semilinear Cartier matrix, not the latter as a polynomial over the parameter space). /workspace/replays/cartier.py independently expands the powers in an exact modular polynomial ring and verifies Disc=4Δ, both scalars, the trailing-block determinant, and det=14H²Δ¹² identically. All Frobenius twists preserve block invertibility, so the stable rank is two exactly where the two scalar blocks vanish, and four elsewhere; first Cartier rank likewise gives the stated a-numbers. On H=0, Δ=6a³ and u=b/(10a) recovers a=u² and b=10u³, proving the reduced-locus isomorphism, finite marked counts, and scaling to the geometric model. Δ=0 also has q points via its analogous cubic parametrization including 0. Independent point replay /workspace/replays/4.py uses separately checked FLINT field presentations and the Euler power criterion, not the submitted counters' enumeration of y^5. The (zero, nonzero fifth-power) counts are (1,6),(3,232),(1,5958),(3,184120); adding the unique rational infinity gives 32,1164,29792,920604. Newton identities and reciprocal symmetry recover all nine numerator coefficients. The submitted mod-7 quartic factors force any rational split into two monic integral quartics, and the absolute value of every root forces their constant terms both +961 or both −961. Comparing degrees 6 and 2 rules out −961 and gives c²=961a². Degrees 5 and 3 force either the odd coefficients to vanish or both quadratic coefficients to match; the first case has nonsquare discriminant 405, the second has nonsquare discriminant 496 or all-positive polynomial in a². Exact independent FLINT factorization also returns the polynomial irreducible. A proper base-field isogeny factor would factor it over Q. No conclusion on all rational twists or absolute simplicity follows or is claimed.

## originality

PASS

The defendable advance is the explicit coefficient equation and exact arithmetic of the distinguished F₃₁ model. The family, geometric Newton possibilities, nonordinary a-number and equality of multiplicity with a-number are covered by prior work. Bounded checks did not establish an earlier explicit marked Hasse equation or Frobenius calculation for this model; impossibility of such coverage is not claimed.

## value

PASS

The natural one-dimensional Shimura-family locus is made explicit in a small split characteristic where it occurs at a single geometric class. The coefficient equation and an independently verified degree-eight Frobenius polynomial yield a concrete test case and a simple nonordinary Jacobian over the base field. Weighted mass and the allowable Newton slopes do not supply the rational model's point counts or simplicity. The value is the explicit finite-field arithmetic and marked description, not re-counting a known weighted mass or classifying twists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
