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

Proper completed part palettes are disjoint. A part with at least two colours in the completion can never have a forced vertex, since its neighbours use at most Q−2 colours. The first force witnesses Q−1 outside colours and completes that palette with the remaining colour, so any successful non-total seed has a surjective completion, with all parts containing blanks monochromatic. Two wholly empty monochromatic parts would leave at least two colours absent and prevent even the first step. Conversely, when exactly one such part is empty it is forceable first, and once every part is represented every remaining blank sees exactly the other Q−1 colours. The forced colour is necessary in any extension, giving uniqueness and ensuring the enumerator does not double count across completions. Partition into unlabelled nonempty colour classes and injectively label them for the falling-factorial Stirling count. For each surjective completion factor the allowed seed restrictions by part, with at most one constant-term omission among the monochromatic factors, and subtract the total term already counted by P_G(Q). Multiplying powers by the independent assignment probabilities gives the probability transform including its polynomial endpoint. In the balanced case, the number j of nonsingle-colour parts among non-total successes must satisfy j≤r−1 and j≤d≤j(t−1). Their least seed size is jt+r−j−1; since it increases with j the first admissible j is k, attained by the one omitted monochromatic part and singleton seeds in the others. Summing colour-class partitions over the bounded positive compositions of d gives the claimed leading coefficient; above the capacity cutoff only total seeds remain, also for Q>N. Independently checked the K_(2,2,2) coefficients for Q=4,5,6 and the total-only Q=7 case by counting partial assignments with exactly one proper full extension (replay python3 /tmp/opencode/nov02-independent-checks.py 4). For this graph class unique completion implies forcing: one can otherwise recolour a blank vertex in a multicolour part or with an unused palette colour, or interchange the colours of two wholly unseeded monochromatic parts. The local process was also independently simulated on the three displayed examples. The uploaded checker was inspected, not executed; finite tests corroborate rather than establish the theorem.

## originality

FAIL

Two exact October 2026 Resultary records cover the full surplus range. 2d913e8a2a13 gives the identical classification and all-coefficient enumerator for Q≥r+2, and a stronger arbitrary-part-size minimum formula. 5336d2e3f828 gives the remaining Q=r+1 classification, all coefficients, minimum, and multiplicity. The balanced staircase and leading term are direct specializations or coefficient extractions from these results, not a new surviving claim.

## value

FAIL

The full surplus census is a useful mathematical object, but this record consolidates two already covered ranges and adds only a balanced specialization and direct coefficient extraction. It does not supply a substantively new forcing phenomenon, extension, or independently informative extremal calculation beyond the existing work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
