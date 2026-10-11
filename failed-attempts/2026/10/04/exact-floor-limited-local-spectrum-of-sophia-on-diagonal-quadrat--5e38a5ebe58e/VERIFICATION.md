---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

FAIL

The EMA formula, limiting mode matrix, determinant \(\beta_1\), trace, Jury stability frontier, and flat-curvature expansion all reconstruct correctly. But the final theorem includes the plateau boundary with \(\lambda_i\ge\varepsilon\chi_-/\eta\) and calls every such mode a complex-conjugate pair. At equality, the floor branch gives exactly \(\chi_i=\chi_-\); by the package's own discriminant condition \(T_i^2<4\beta_1\), equality has zero discriminant and a repeated real root \(\sqrt{\beta_1}\), not a nonreal conjugate pair. The supplied verifier also avoids asserting nonzero imaginary part exactly at the threshold. The rate modulus remains correct at equality, but the stated root-type claim is false on an explicitly included boundary, so the submitted final claim fails correctness.

## originality

PASS

The Sophia source introduces the practical momentum/Hessian-EMA optimizer, clipping, and the max-with-epsilon denominator, and gives a condition-number-independent theorem only for a substantially simplified theoretical method. No inspected source or Resultary hit gives the practical exact diagonal-quadratic characteristic polynomial, floor threshold, or modal plateau. The originality of the intended theorem survives, but the submitted final claim is scientifically false at one included boundary.

## value

PASS

A corrected strict-boundary version would give a useful exact local phase diagram for the practical Sophia recurrence, isolating the denominator floor as the curvature-dependent slow regime and distinguishing Hessian-EMA transients from limiting optimization modes. That mathematical value does not permit acceptance of the false inclusive boundary statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
