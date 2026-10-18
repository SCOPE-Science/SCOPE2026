---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Zapletal 2026 states Con(ZFC)⇒Con(ZF+DC+BPI+no E0-selector), where a Vitali set is an eventual-equality selector. Larson–Zapletal, Observation 3.13, establishes under ZF+DC: existence of a Hamel basis R/Q ⇒ a total E0-selector. By modus tollens within Zapletal’s model, no Hamel basis can exist there. BPI⇒Hahn–Banach is standard. This correctly proves a relative consistency/nonimplication, not that BPI entails no basis. Zapletal full 2026 preprint was inaccessible, so exact construction was not checked; its directly relevant published theorem statement and the fully read older implication suffice for this conditional corollary.

## originality

FAIL

FAIL: The new separation is an immediate corollary of Zapletal’s stronger published model theorem plus the explicit already published Hamel-basis⇒E0-selector implication. Neither a new model nor a new bridge theorem is established. Prior implication logically dominates the exact submitted result even though no source need print this derived Hamel sentence verbatim.

## value

FAIL

FAIL: Although the independence/separation question is inherently important, the package adds only a one-step textbook contraposition to two prior theorems, and the Hahn–Banach statement is another routine implication. The claim contains no independent structural lemma, novel construction, or new method beyond mechanically combining established published statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
