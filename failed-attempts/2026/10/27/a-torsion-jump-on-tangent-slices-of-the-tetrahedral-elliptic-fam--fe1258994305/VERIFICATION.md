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

Independent exact calculations in /workspace/review_checks/check_5.py verify the Weierstrass discriminant 4096 Q²(P³−27Q²)³, the parameter discriminant −19683r³(m²r−4), and both torsion-section substitutions (including ψ₃ for the order-three section). The generic fiber is nonsingular, and a finite y=0 point has exact order two. The invariant c₄=16P(P³+216Q²) is nonzero at all finite discriminant zeros under the stated assumptions; at infinity its degree-four leading term is nonzero and the Weierstrass discriminant has degree eleven. Thus the finite vanishing orders give the stated multiplicative fibers, together with I₁ at infinity. The bundle has degree one, so the surface is rational. The trivial lattice root ranks give ranks 1 and 0 by Shioda–Tate. In the generic case the height formula excludes two-torsion and forces each nonzero 3-torsion point to map nontrivially into all three I₃ component groups, excluding a second independent 3-torsion point. The rank-one height determinant is 9/54. In the tangent case the determinant 36 gives torsion order six. These calculations are over C(t), not assertions about points on every specialized fiber.

## originality

FAIL

The abstract torsion jump, Mordell–Weil groups and generic height follow from the published fiber rows and the standard rational-elliptic-surface formulas. The displayed coordinate is not identified as a printed formula in the inspected source, but the whole m≠0 family is one published tangent slice up to weighted scaling, and its unique 2-torsion coordinate is the sole linear factor of that known cubic. This is strong implication evidence, not a negative verdict based on inability to retrieve the classification paper.

## value

FAIL

The tangent locus is natural, but the torsion jump and height are already determined by the known fiber classification. The only candidate additional invariant is the coordinate of the unique point recovered by a single rational factorization of the normalized published slice, then rescaled. The record does not establish a further nonmechanical invariant such as a new comparison of inequivalent slices. The concrete computer-algebra result is correct but does not supply a distinct scientifically valuable remainder under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
