---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Lücke–Poveda Theorem 1.3 produces a transitive set-sized ZFC model M satisfying that the exacting cardinals are unbounded in its own ordinals. The forward implication of Osinski Corollary 5.9 is a ZFC theorem (with logics and satisfaction definable in the stated sense), and holds internally in every such M. It gives one beth-fixed λ per logic, then a cardinal μ for each α<λ<ζ, with the inequalities and rank-type compactness exactly as stated. The theory-size restriction |T|=λ is Definition 5.3; Definition 3.2 actually defines size-unrestricted μ-chain compactness, while the rank-type definition is in the immediately preceding prose. That is a locator error, not a change in the proved hypothesis or conclusion. Neither an external class quantifier over arbitrary logics nor absoluteness of exactingness/compactness from M is needed. Replay by reading Lücke–Poveda v1 §1 Thm. 1.3 and Osinski v1 §2, §3 before Def. 3.2, §5 Def. 5.3 and Cor. 5.9 in the primary HTML. No lower bound or ambient-universe conclusion.

## originality

FAIL

The claim is a direct corollary of two explicitly published statements, with no new mathematical step: replace the internal conclusion of Lücke–Poveda Theorem 1.3 by its provably equivalent ZFC formulation in Osinski Corollary 5.9. Neither theorem prints the whole sentence, but this is already covered by the prior theorems together. This is an implication assessment, not a claim that the identical sentence was previously published.

## value

FAIL

The connection is useful as an explanatory cross-reference, but the frozen result does not supply new consistency-strength information beyond changing a published model assertion to its known equivalent. No new construction, strengthening, sharpness/lower bound, or nonmechanical step is shown. Correcting the definition locator would not rescue a distinct valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
