---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The domain is ALL binary overlap-free linear words of length 0..96 having exactly nine nonempty square factors. Every root has length <=40 because eight other squares require at least 16 positions; the block generator therefore exhausts 154 eligible square blocks. The inductive nine-level search retains all overlap-free products and ordered recipes, while independent full-prefix search tests all overlap-free words to length 96 and all square-suffix decompositions. The two finite approaches give counts {48:2,76:2,86:4,92:2,96:2}, zero at all other lengths <=96, and one nine-block recipe per word. No claim for n>96.

## originality

PASS

The minimum-length result implies the two 48-letter cases with unique decompositions. The 10-square exclusion is used only to bound dynamic-program counts. Neither entails 76/86/92/96 counts or nonattainable intermediate lengths; obtaining those needs the complete length-bounded census. Shallit proves 10 concatenated squares force an overlap, and gives nine-square witness; the published sharp minimum-spectrum for k<=9 gives the minimum at k=9 (48) and its two minimizers. Neither enumerates every nine-square overlap-free product of lengths 49..96.

## value

PASS

Completes a first morphic doubling window, from the established extremal length 48 to the natural Thue-Morse image length 96; the sparse attainable-length spectrum and uniqueness at the intermediate lengths are natural unknown exact invariants of extremal overlap-free square concatenations, useful for extremal word structure rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
