---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproduction
Run `python checker.py` with Python 3 and the standard library. Output must state 671 canonical distinct-letter parameter triples for source lengths at most 11 and 4338 binary repeated-letter controls for lengths at most 6, followed by two excluded-boundary collision checks. Every output word is computed directly using the contiguous-block reversal-and-insertion definition.

## Evidence and limits
The checker is an exhaustive finite regression test only for its stated parameter domains. The infinitely quantified mathematical statement is established by the first-occurrence gap argument in `RESULT.md`, including explicit site recovery in the two-gap case and letter comparisons for all feasible single-gap offsets. The full text of one closely relevant 2026 fixed-block-length source was inaccessible. Independent audit: not performed.
