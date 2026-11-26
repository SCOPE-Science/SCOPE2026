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

In A=kQ/J², J denotes the image of the arrow ideal and is the radical. Since J²=0, the Peirce action on J only depends on idempotents modulo J. Thus the induced vertex permutation must preserve all block dimensions; conversely any such permutation lifts by block isomorphisms. For an automorphism in the kernel, f_v=φ(e_v) are orthogonal lifts; u=Σ_v f_v e_v≡1 mod J is invertible and f_vu=ue_v. After conjugating by u⁻¹ only the independent GL actions on the arrow blocks remain. Conjugation by 1+J is normal and has kernel 1+(Z(A)∩J). Projecting along the Peirce blocks shows that Z(A)∩J is exactly the diagonal loop subspace, including for arbitrary loop combinations; a map from 1+J fixing all e_v acts trivially. This gives the stated semidirect product and order, including disconnected and isolated vertices and the GL_0 convention. Hand checks include one vertex with r loops, giving GL_r with no additive factor, and one arrow, giving q(q−1). The frozen verifier was inspected, not executed.

## originality

FAIL

No assertion is made that the exact displayed formula was found verbatim for all quivers. The claimed structure and order are a direct specialization of classical conjugacy of semisimple complements: here the semisimple quotient is k^V, whose bimodule category is just vector spaces indexed by ordered pairs. After complement conjugacy there is no additional classification problem, and each factor is fixed by that observation. The cited papers on other quiver invariants are not the decisive comparison.

## value

FAIL

The finite-field order is a legitimate and natural invariant, but in this split square-zero case every factor is obtained directly from conjugacy of complements and linear algebra on independent blocks. The report adds no further structural constraint, nonroutine count or motivated boundary phenomenon beyond those deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
