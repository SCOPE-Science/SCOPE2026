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

The optimum enumeration is complete: the length-ten word 0001011100 covers all eight trigrams, and testing all 2,040 binary words of lengths 3–10 covers every possible shorter witness. Each greedy step branches over all ordered pairs at the global maximum overlap and reduces the active multiset by one, which proves the worst-length recurrence by induction. An independently written exact checker covered all 255 input sets and 7,405 memoized greedy states. It reproduced 10/7, exactly masks 31, 87, 234 and 248, and the eight size maxima 1, 1, 7/5, 4/3, 10/7, 11/8, 4/3, 7/5. For the explicit five-trigram witness the window count alone rules out length six, and 0100011 attains seven; the listed merges realize ten using overlaps 2, 2, 1, 0, each globally maximal.

## originality

FAIL

A distinct indexed Resultary record states the same binary-trigram sharp ratio, four equality cases and symmetry orbit, and contains a complete 255-mask census that gives the same eight size maxima. No distinct mathematical content in the declared finding survives that comparison. The comparator's displayed November 8 date is later than the frozen record's October 18 date; this is demonstrable equivalent coverage, not evidence of earlier discovery or priority by the comparator.

## value

FAIL

The sharp binary restriction, small sharpness witness and complete equality classification are mathematically well motivated. But the audited finding provides no additional invariant, classification or independently useful unknown case beyond the existing exact coverage. The census reproduction corroborates those numbers; it is not a distinct valuable result under this audit standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
