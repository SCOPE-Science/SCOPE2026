---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In W₂=001001110 each binary bigram occurs twice, and the singleton triples start at 1,2,4,5,6. Every length-four interval contains one, excluding longer MUSs. Across 001|001, 001|110, 110|001, 110|110 the crossing triples are respectively (010,100), (011,111), (100,000), (101,011), never image words. A length-five or longer interval must contain a whole aligned block even starting at phase one (two symbols before the next block). Its phase is thus unique, and all nonempty end fragments distinguish the two complementary images. Its occurrences correspond bijectively to those of the covering source factor; a repeated cover always implies a repeated image factor even below length five. Given no unique source factor below r+2, every image length ≤3r+1 covers ≤r+1 letters. At length 3r+2, only phase two can cover r+2 letters; the covers of precisely the five unique source factors lift, at new start 3i+2. If an MUS has length ≥6, each endpoint deletion has length ≥5; retaining either outer image block would leave the same unique cover and contradict the deletion's repetition. Thus it begins on the last symbol of its first block and ends on the first symbol of its last, and its cover is a source MUS since deleting either end removes the corresponding source endpoint. Its length is 3(r+2)−4=3r+2. This also handles the first induction step where length five is the threshold. Exact independent enumeration of all position intervals agreed through m=6 (including length 83, starts 161,242,404,485,566 at m=6). The source checker was inspected, not executed; finite replay is not the reason for the universal conclusion.

## originality

FAIL

A distinct indexed record, 00d0c1e4d8b8, contains the exact five-interval theorem under identical iterate, seed and occurrence conventions, and proves it by the same general mechanism of phase synchronization and endpoint lifting. The indexed record's displayed path date is later than the frozen path date; this is a coverage decision, not a historical priority, attribution, or provenance finding.

## value

FAIL

The five-MUS stabilization is a worthwhile exact invariant of this substitution. As a separate finding, however, this version adds no level, interval, sharper synchronization threshold or distinct implication to the exact indexed classification. The alternate presentation does not supply a surviving incremental contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
