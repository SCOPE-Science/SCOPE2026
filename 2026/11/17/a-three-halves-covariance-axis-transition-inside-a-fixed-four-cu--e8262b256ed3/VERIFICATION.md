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

For each real t>=1 the orthogonal coordinates x=(a-tB,-a-tB,B+b,B-b) give constant intrinsic Jacobian and exact rectangular fibers |a|<=1-t|B|, |b|<=1-|B|. Independently integrated I0=(3t-1)/(6t), IA=(5t-1)/(20t), IB=(10t^3-10t^2+5t-1)/(20t^3), I2=(5t-3)/(60t); conditional symmetry removes all mixed moments. This yields the three claimed rational intrinsic-volume covariance eigenvalues. Symbolically checked three pairwise differences, their positivity, unique least-eigenaxis crossing t=3/2 with both eigenvalues 13/35 and condition number 142/117, and volume derivative vanishing at t=2. The claimed polytope face-lattice constancy for t>1 follows from coordinate-face intersections; t=1 is a distinct octahedral endpoint. The supplied rational triangulation check was inspected, and the all-real assertion rests on the analytic integrals.

## originality

PASS

PASS, best of knowledge: natural two-block four-cube central sections have known volume critical points and there exist general parametric moment algorithms, but the inspected primary results do not supply the explicit three covariance eigenvalue functions, their crossing at t=3/2, or the strict separation from volume minimum t=2. No implication from the recorded general moment method to this computed family without a nontrivial instantiation and diagonalization was identified. Historical unnoticed calculations remain possible.

## value

PASS

PASS: an exact uniform-intrinsic-volume covariance spectrum in a geometrically natural symmetry class, with a sharp crossing of least-inertia directions entirely inside a constant combinatorial chamber, contrasts with a known and different volume critical normal. The parameter t is the ratio of the two equal coordinate pairs, not an arbitrary unmotivated numeric slice; the classification may be used to study isotropy and inertia transitions in cube sections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
