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

Verified geometric completeness, not just the F5-rational cases. On the torus the three scaled gradient entries are A-C, B-A, C-B for A=XY^4, B=YZ^4, C=X^4Z. Their simultaneous vanishing would give F=3A≠0; the three coordinate points are also smooth. In local coordinates putting a smooth point at (0:0:1) and tangent Y=0, the Hessian determinant at the point is −2a(4c)^2, where a is the tangent-direction quadratic coefficient and c is the nonzero normal linear coefficient. Hence Hessian vanishing characterizes flexes here even though the characteristic divides the degree. Direct Hessian expansion and substitution of Z=1, X=t, Y=λt^4 give the stated cubic and thirteenth-power equation; the change to s=t^13 gives the stated degree-39 polynomial and inverse λ=4+4s+2s². In a separate FLINT implementation using a different irreducible degree-12 modulus and direct splitting of the degree-39 polynomial, all 39 roots were simple; explicit tangent restriction gave 39 order-three and three order-four contacts. The resulting 42 normalized lines gave 861 different projective pair intersections (which rules out every triple). Exact Frobenius on lines gave {1:3,3:1,12:3}; on nodes it gave {1:3,3:4,6:3,12:69}, with the fixed nodes exactly the axes points and every other flex singly incident. Distinct line pairs cross transversely. The cycle counts give both the reduced support's zeta function and the minimal common field degree 12. Replay: python /workspace/branches/independent_hurwitz.py (python-flint).

## originality

PASS

The 42 flex points and their contact orders are established inputs. The distinct contribution supported by the comparisons is the full flex-tangent incidence and node arithmetic of this particular quintic over F5, not the flex-support classification.

## value

PASS

This is the complete incidence and arithmetic description of the canonical flex-line arrangement of a natural small Hurwitz curve in characteristic dividing its degree. The absence of any higher concurrence is not implied by flex counts or geometry of unrelated arrangements and is needed before an unordered-pair Frobenius calculation is valid. The orbit spectrum gives the exact node counts in every extension and the minimal splitting degree, reusable data for subsequent study of this arrangement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
