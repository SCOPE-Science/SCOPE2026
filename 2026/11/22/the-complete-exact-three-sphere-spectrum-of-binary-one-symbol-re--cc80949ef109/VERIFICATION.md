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

Track the descendants of the prefix x and the appended symbol b in separate consecutive blocks. In one step two positions i<j give different symbols at output position j+1. Writing c for the complement of b, the word xbc is reachable from x in two steps exactly when x is not all b: append bc if x ends in c, or insert a b at the last cb transition then append c; from an all-b source the initial b-run cannot grow. This gives the stated exact-two recurrence, whose base size is 2. At three steps the ending classes b, bc and cc isolate the three disjoint main families, and D_1(x)bcb lies in D_3(x)b because every one-step descendant is nonconstant. Of the four final single-symbol-block outputs, xbccc is always new; the other three are old if x is not all b by the two-step criterion plus one duplication, and new otherwise because they start with n+1 copies of b (and the bc-ending word would require xbc in D_2(x)). Thus the size increase is binom(n+2,2)+r+3·1_(x=b^n), the increase of the displayed formula. The n=1 base, strict difference n+2−r, binary frequency count, and extrema agree. Fresh direct enumeration, not the frozen scripts, checked all 510 binary sources of lengths 1–8; that is corroboration, not the proof. Both frozen checkers were inspected.

## originality

PASS

The supported distinction is the exact source-dependent three-duplication sphere law. The closest indexed formulas give the source-dependent two-duplication count or an exact-two maximum. Published results on common descendants, single-symbol descendants, and correcting multiple errors have materially different conclusions from counting distinct exact-three descendants of an arbitrary fixed source. No assertion of priority is made for the embedded two-step formula.

## value

PASS

Distinct received-word counts are basic sphere-packing data for the existing multiple reverse-complement error model. The fixed-source law gives every attainable three-error volume, not just a larger constant-source example: code-size arguments sensitive to source-dependent volume can now distinguish all initial run lengths. The nontrivial overlaps first appearing beyond the established exact-two enumeration make this a natural exact case, without claiming a new optimal code bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
