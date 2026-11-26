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

A(y)=(B+y²)/(1+y²)>0 makes (x,y)→(U,y) globally invertible. The real inverse problem is exactly φ_U(y)=V, with φ_U'=1+2Ua y/(B+y²)² and φ_U(y)→±∞ at the two ends. The function r/(B+r²)² has unique maximum at √(B/3), of size 9/(16√3 B^(3/2)); this proves the threshold, strict monotonicity even at equality, and the +,−,+ derivative pattern outside it. At a cusp Ua=−(B+y²)²/(2y), y²=B/3, hence V=U+3y. The third derivative is 9/(2B) and the mixed derivative ∂_Uφ_U' is −1/U, so the cusp is ordinary and the inverse cubic has a triple root. Away from these points the critical roots are simple and give ordinary folds. Writing δ=ε/U_* and η=y−y_* yields the nonconstant terms −δη+3η³/(4B)+O_a(εη²+|η|⁴). At its extrema η=±(2/3)√(Bδ)+O_a(ε), the leading values differ by (8/9)√B δ^(3/2); the errors are O_a(ε²). The original determinant is Aφ_U', and bounded X bounds x, then bounded Y bounds y. The unique regular preimage at U=0 has positive sign, establishing degree +1. The a=0 affine limit is correct.

## originality

PASS

The exact global classification and cusp separation for a>−1 survive the inspected comparisons. The strongest indexed overlap treats exactly the same cubic and map, but states the theorem for a≤−1, with a different pinch and no implication across B=0. Its unnamed reference to an a>−1 calculation leaves priority uncertainty, not established coverage.

## value

PASS

The model is a published rational dynamical system and its first inverse valence is a basic input to backward dynamics. This locates all changes in that valence and quantifies the physical onset of multivalued inversion. It distinguishes the positivity-stratum geometry from the connected-strip and pinch geometry of the same model outside the regime, rather than just reasserting the universal cusp normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
