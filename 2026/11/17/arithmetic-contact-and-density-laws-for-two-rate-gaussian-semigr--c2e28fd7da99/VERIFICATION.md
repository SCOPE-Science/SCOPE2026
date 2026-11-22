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

C PASS: For 1<p<infinity, p!=2, two independent Gaussian coordinates and rates alpha,beta>0, Janson's complex second-quantization criterion/Epperson's one-variable region gives boundedness iff |sin(alpha s)|<=k_p sinh(alpha t) and |sin(beta s)|<=k_p sinh(beta t), t>=0; coordinate restriction gives necessity and Fubini tensorization sufficiency including the boundary, operator norm exactly one from constants. The threshold h(s) is max of the two inverse-asinh sine heights. Imaginary periods must map zero to simultaneous sine zeros, hence exactly the common pi-lattice for rational beta/alpha and {0} otherwise. Kronecker equidistribution of irrational torus flow gives product normalized arcsine interval lengths, with quadratic small-t asymptotic. Coprime integer rates yield a unique shrinking common zero arc modulo pi/omega, producing first-order coefficient 2k_p omega/pi. For irrational theta, distance to the two zero lattices and midpoint choice make minimal max-distance half their separation; selecting nearest integer pairs along best approximations establishes liminf |s|h(s)=pi^2 lambda(theta)/(2k_p alpha beta). The liminf is not an all-s estimate; rational small-t errors are fixed-rate, not denominator-uniform. Independently checked several rational and irrational small-t constants numerically. Finite checks cannot replace the boundary theorem or equidistribution.

## originality

PASS

O PASS (qualified): Janson 1997 Theorem 2 already covers diagonal multirate Gaussian boundedness/contractivity, so no novelty is assigned to the Epperson-region intersection itself. Perelmuter 2026 Proposition 5 proves imaginary-periodicity for common-rate OU via reflection, not a rational/irrational dichotomy for unequal rates and not vertical-density/contact constants. The additional precise arithmetic geometry—linear versus quadratic small-time density and exact Lagrange-constant liminf—was not found as a consequence stated in these works or the nearest published Resultary records; it is an explicit model-specific quantitative refinement. General equidistribution/continued-fraction facts are prior tools.

## value

PASS

V PASS: Complex-time boundedness beyond analytic sectors is a natural operator-semigroup invariant. In a genuinely anisotropic two-rate product model, the exact imaginary-period group, rationality-sensitive order of vertical allowed times and Lagrange-constant cusp contact quantify distinct geometric regimes not described by norm contractivity alone. These are reproducible sharp analytic formulas with a clear standard base operator, not an arbitrary frequency slice or merely reformulated norm-one bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
