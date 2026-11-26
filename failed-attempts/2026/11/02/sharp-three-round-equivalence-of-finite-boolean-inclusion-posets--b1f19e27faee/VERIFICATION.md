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

The six-class theorem is correct in the stated inclusion-only language. After choosing X and Y, the final choice Z can test the common cell X∩Y only for whether all of it lies in Z, and the cell outside X∪Y only for whether none of it lies in Z. Each of those two cells can therefore be capped at one for final-move types. The two cross cells need a cap of two, since their chosen and unchosen parts can affect different inclusions. When a first-move region has size at least three, its second-move split into a cap-two cell and a cap-one cell has the same four possible capped pairs (0,1), (1,1), (2,1), (2,0), independent of its size. Thus first-move types depend only on the two side sizes capped at three; all n≥6 attain the same pairs. For sharpness, relative to X, rank at most two expresses |X|≥1 by a strict predecessor, |X|≥2 by a two-step descending chain, and |X|≥3 by a Y strictly below X that has a strict predecessor and admits a strict intermediate element between Y and X. Dual formulas test |[n]\X|≥j for j≤3. Existentially quantifying X with both tests expresses n≥i+j for thresholds through six. An independent exact bounded replay also matched all 18 stated local comparisons and the finite equality pattern through n=7. No uploaded script was executed.

## originality

FAIL

The distinct 2026-10-26 Resultary record already states the identical iff in the identical relational signature on the wider domain n,m≥0, explicitly stating the six positive-parameter classes and the least 64-element tail representative. The frozen Finding is wholly covered; this is a statement-level duplicate, not conjectured overlap or a date-order inference about two same-day records.

## value

FAIL

The sharp finite cutoff is mathematically useful, but as a contribution this record re-establishes the same exact classification, representative, and boundary already in a distinct record. It does not state an additional useful theorem or method with a new scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
