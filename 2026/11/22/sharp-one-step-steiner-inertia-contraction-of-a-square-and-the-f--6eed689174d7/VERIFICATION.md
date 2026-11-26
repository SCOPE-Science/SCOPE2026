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

The moment difference on a section of length L and midpoint m is Lm²; the longitudinal moment cancels. I independently integrated the central and tail pieces in RESULT.md. With c=cos(theta), s=sin(theta), A=ac, B=bs, D=A−B and k=c²−s², the central contribution is 4BsD³/(3c³). Changing tail variable to y=A+B−z gives (2B²P²−16B³Pk/3+4B⁴k²)/(2c³s³), with P=2(c²B−s²A). Expansion at s=tc gives the displayed first branch. Exchange of axes, reflection and continuity cover the other branch, the separating angle and the coordinate axes. For the square the expression is 2h⁴u(1−u)²/3 with a unique maximizing u=1/3. Division by 8h⁴/3 yields 1/27, and the four slopes account for every equality axis. Read the checker and VERIFICATION.md; the 89 assertions are frozen recorded evidence, not a new execution or formal certification.

## originality

PASS

The supported distinct result is the explicit piecewise rectangle profile and sharp single-direction square optimum. General monotonicity and the fiber parallel-axis identity do not count as new. No inspected result supplies the same profile or a stronger theorem giving its exact optimum.

## value

PASS

Quantifying how much one Euclidean Steiner step actually reduces inertia is a natural question for direction selection; qualitative descent does not answer it. The entire directional function covers every aspect ratio and the square supplies a sharp benchmark, with symmetry directions giving zero loss and non-obvious best directions giving positive loss. No iterative convergence rate or optimum for every unequal rectangle is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
