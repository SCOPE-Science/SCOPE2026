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

Normalize by z=au+ibv on the unit disk. The squared disk radius has the Beta(1,α+1) law; angular averaging gives second moments 1/(2s), single-coordinate fourth moments 3/[4s(s+1)] and the mixed fourth moment 1/[4s(s+1)]. Central symmetry and subtraction of c²/(2s) in degree two give the orthogonal basis and squared norms c²R/(2s) and c⁴D/[4s²(s+1)]. In the resulting quartic diagonal, the angular penalty B−A is positive and the coefficient A of x² has the sign of P. If P≥0 only the origin achieves the lower bound, and when P=0 the real-axis expansion starts with a positive quartic. If P<0, completing the square gives C(x²+y²−x_*²)²+(B−A)y² above the minimum, with x_*²=−A/(2C). This vanishes only at the two real sites; −P<2(s+1)R puts both strictly inside the ellipse. Subtracting A²/(4C) gives the stated minimum. P(1)=−3, P has exactly one positive root, and R increases with b/a; the stated critical examples follow by substitution. The reciprocal has the same maximizing sites. This proof applies to the complex analytic space through degree two, not the real bivariate or infinite Bergman kernel. Inspected VERIFICATION.md and CHECK.py without executing the supplied checker; its rational checks do not prove the all-parameter statement.

## originality

PASS

The weighted Gegenbauer basis is known and yields the kernel by summation. The supported distinct claim is the sharp global diagonal-minimum and equality-site phase classification as aspect ratio varies, not a new orthogonal polynomial or a new general kernel formula. The closest distinct catalogue records either change the optimization objective or study a different slice of a kernel. The exact catalogue hit is 35600b425e72 itself. Priority is best-of-knowledge only.

## value

PASS

The result describes the location of best reciprocal Christoffel values on a standard domain and identifies the first polynomial degree at which symmetry can break. It determines both sharp interior equality sites and a quartic-flat critical case uniformly in the admissible weight, a genuine shape effect not read off from positivity or symmetry of the kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
