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

On the uniquely terminated word every required extension is a suffix of a suffix-maximal one, and two distinct suffix-maximal ones cannot both end at one position; this proves the minimum-set formula. The one-letter domination test is justified because deleting symbols from the left of a right-maximal factor preserves its two distinct followers; the preceding symbol cannot be the terminator. Independently, adjacent LCPs of sorted suffixes recover every branching prefix, including the empty one, and the extension ending-position sets are laminar: if two intersect then one extension is a suffix of the other. Counting distinct inclusion-minimal ending-position sets therefore computes the minimum directly. Enumerating all 32,766 source words and 425,986 directed bit flips by this procedure reproduces (0,1,1,1,2,2,3,4,4,4,4,5,5,6); the 16 length-14 extrema all have values 5 to 11, with exactly the listed one-based positions and source words. No inference is made beyond length 14.

## originality

PASS

The same measure, its right-extension characterization and the substitution-sensitivity question are already known. The supported distinct claim is the exact binary profile through 14 and its complete maximizing-pair classification, not the measure or general sensitivity.

## value

PASS

This resolves the first length at which the edit effect exceeds five for a published compression measure, but the value does not rest on choosing the number six alone: the complete initial profile and all equality cases show exactly how extreme changes emerge in the smallest alphabet. At the first gain of six every source has measure five and the only extremizers are four highly structured words with four flip positions each. This supplies exact short-input benchmarks and concrete constraints on prospective sharp sensitivity bounds; it is not a new asymptotic estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
