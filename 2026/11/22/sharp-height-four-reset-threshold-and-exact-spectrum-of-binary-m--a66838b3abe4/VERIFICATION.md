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

A missing child of any internal vertex would allow appending a new word, so maximality makes the ordered binary prefix tree full; conversely full finite trees give maximal codes. At root depth zero, counting the formal leaf as a tree gives T_0=1 and T_h=1+T_(h-1)^2, with T_4-T_3=677-26=651. Proper prefixes are exactly internal vertices, at most 15; a letter takes the internal child or completes a leaf and returns to the root. A word acts by a path through nonempty image subsets, so the first singleton at breadth-first distance is shortest and exhaustion without a singleton proves nonsynchronization. The supplied scripts were inspected but not executed. They may stop at the first singleton, which is enough in synchronizing cases. An independent implementation, inspected at lines 8–79 and 100–148, was executed and can be replayed as `python3 evidence/5/independent_enum.py --height 4` from the review workspace; `evidence/5/full_height4.log` records 25,689 reachable subsets over the 651 codes, with 19 nonsynchronizing and the exact length counts 1:2, 2:20, 3:44, 4:92, 5:96, 6:56, 7:50, 8:144, 9:118, 10:4, 11:2, 12:2, 17:2. The two length-17 codes have precisely the stated leaves and 14 states each. Direct replay verified the stated reset word and its complement; minimality comes from breadth-first distances, not replay alone. This is computational verification of a bounded census, not a larger-height or formal certification claim.

## originality

PASS

The length-17 examples and their individual shortest lengths are already known. The distinct contribution is the unrestricted exact-height-four maximum, uniqueness within the full family, and complete distribution including nonsynchronization.

## value

PASS

Exact height four is a natural small cutoff at which the known general upper bound and consecutive-depth witness do not fix the unrestricted extremum. Settling the gap from [17,33] to 17 for the literal decoders, including all shallow branches, answers a precise extremal question; the whole spectrum and unsynchronizing count provide independently useful small-case data for subsequent structural bounds and conjectures. The value is not the already-known 17-letter examples or the routine tree-count recurrence in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
