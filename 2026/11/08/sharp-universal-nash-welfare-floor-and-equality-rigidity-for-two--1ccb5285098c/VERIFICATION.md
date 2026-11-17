---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Sort bundles a<=b. If the larger bundle has one good, its product ab is globally optimal. Otherwise EFX implies b-a<=min_{g in B}v_g<=b/2, so T/3<=a<=T/2, yielding ab>=2T²/9 while P*<=T²/4. Equality in both bounds forces B to have exactly two goods of value u each, A total u, and an exactly balanced global allocation requires a subbundle of A of value u/2. Conversely this is EFX and its optimum is balanced; witness (2,2,1,1) gives squared ratio 8/9. Exhaustive independent rational/integer enumeration of 456 positive-integer item multisets, 2939 EFX allocations, 4 equal cases corroborated. Strict positivity, complete allocation and two identical agents are essential.

## originality

PASS

Best-of-knowledge no inspected prior theorem proves a sharp guarantee for EVERY complete two-agent EFX allocation with common arbitrary positive additive values and its necessary-and-sufficient equality structure. Strongest related work for arbitrary EF1 allocations uses a weaker fairness requirement or restricted bivalued goods; EFX/NSW existence theorems reverse the quantifier.

## value

PASS

The lower guarantee governs every EFX allocation (not just the existence of one selected allocation), and the equality classification determines exact welfare loss witnesses for a central fairness property. The sharp factor and rigid geometric/subset-sum mechanism are mathematically informative for the EFX–efficiency tradeoff rather than a routine restatement of EF1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
