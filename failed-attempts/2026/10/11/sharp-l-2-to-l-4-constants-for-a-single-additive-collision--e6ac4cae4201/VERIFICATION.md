---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Parseval applied to F² gives collision-free baseline 2S²−Σ|c_a|⁴. Exactly one off-diagonal/off-diagonal fiber adds 8Re(c_a c_b conjugate(c_c c_d)), bounded by 8√(x_ax_bx_cx_d); AM–GM gives fourth power 9/4 with four equal squared moduli. A diagonal/off-diagonal collision adds 4Re(c_v² conjugate(c_uc_w)), bounded by 4y√xz; optimizing x=z, y:(x,z)=3:2:2 gives 15/7. Equality in localization, AM–GM and phase inequalities yields precisely asserted supports and phases. Torsion-freeness eliminates diagonal/diagonal collisions. Inspected all exact identities in assigned RESULT.md; finite checker does not supply infinite proof.

## originality

FAIL

Published distinct Resultary general theorem for compact abelian groups and arbitrary finite character sets with exactly one repeated pair-product fiber gives the same 9/4,15/7 constants, complete amplitude/phase extremizers, plus a third torsion-type diagonal/diagonal case. Pontryagin duality identifies additive Γ frequencies with characters on compact dual Γ-hat; torsion-free restriction removes a case, so the audited theorem is strictly implied by a broader published result. Another published finite odd-order theorem independently duplicates the two cases after measure scaling.

## value

FAIL

The abstract single-collision Λ(4) optimization is a worthwhile invariant in itself, but this particular package contributes no independently useful precise fact beyond an already published strictly stronger theorem with exactly the same constants and all extremizers. Repackaging under torsion-free additive notation and repeating the same AM–GM proof provides neither a motivated new structural refinement nor an unknown natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
