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

Euler's identity identifies the logarithmic tangent bundle with the kernel of O(1)^3→O(2r+1) given by the three gradient monomials. Chern classes follow by division and twisting: c₁(F_r)=0 and c₂(F_r)=3r². There is no degree-r coefficient syzygy, since monomial supports are disjoint below coefficient degree 2r; H⁰(F_r)=0 implies slope stability by extending a rank-one subsheaf to its double dual. The fiberwise square restriction map has rank-3r source and target bundles; its cokernel is the first higher direct image of the restricted F_r(−1), so its zeroth Fitting divisor is the canonical first determinant scheme. For c≠0, deleting the two pivot blocks leaves the middle binomial minor: all determinant terms carry A^(r²)B^(r²), and the remaining binomial matrix is PPᵀ of full row rank by Vandermonde and triangular pivots. Permuting coordinates verifies the remaining chart and gives the global Cartier equation. On a coordinate line in the dual plane a constant gradient syzygy splits off, and the other two restricted gradient forms have disjoint zeros, giving O(r)⊕O(−r) after twisting. The determinant is invertible on the remaining lines, forcing the degree-zero splitting O⊕O.

## originality

FAIL

No inspected primary source was found to print the entire all-r formula as a Fermat example. Nevertheless it is an immediate specialization of the established first Barth determinant on the graded Jacobian quotient and the characteristic-zero weak Lefschetz theorem. On the smooth Fermat Jacobian quotient R=C[x,y,z]/(x^(2r),y^(2r),z^(2r)), diagonal scaling preserves the ideal and acts transitively on linear forms with all coefficients nonzero. WLP therefore gives invertibility everywhere on abc≠0. The determinant is homogeneous of degree dim R_(3r−2)=3r², and a homogeneous polynomial nonzero throughout that torus is a monomial. Coordinate permutation symmetry forces that monomial to be (abc)^(r²) up to a scalar. Generic balanced splitting extends to the entire open orbit; at the complementary lines, two independent coordinate powers and their redundant third generator give the exact order r by restriction. Thus the complete splitting and nonreduced multiplicities are mechanically forced even without the published special-case equation.

## value

FAIL

A thickened first jumping scheme is a natural invariant and the proof is an accurate explicit illustration. But once the existing determinant and Lefschetz theorems are applied, coordinate scaling and permutation symmetry alone force the exact exponents, and the remaining splitting follows from a redundant generator on a line. No independently useful new invariant or claim remains; the finite tests and computational presentation do not alter that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
