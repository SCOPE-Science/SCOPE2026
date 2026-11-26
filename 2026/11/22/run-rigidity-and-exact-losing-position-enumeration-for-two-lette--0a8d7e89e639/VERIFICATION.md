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

For a candidate losing word with both letters, each ab prefix deletion leaves a b-to-a word, and each ba suffix deletion leaves an a-to-b word; pure words have no moves. A complementary word beginning in b or ending in b can be moved to a pure b-word, including the empty word. For a complementary word with both ends a, cutting at the first singleton b-run leaves a candidate losing prefix. This proves the P/N classification by length induction. Run minima consume 3j+1 letters; distributing slack among 2j+1 runs gives the binomial sum and the geometric series yields the rational function. The cubic in lambda has discriminant -23, so its root lambda in (1,2) dominates the two conjugate roots of modulus lambda^(-1/2); the simple-pole coefficient equals the stated C. Deletion lowers length by at least two, and even-length prefix cuts of the alternating word realize every smaller Grundy value, including at the empty-word boundary. A fresh length-0-through-17 exhaustive mex and enumeration replay passed, but the all-length claims rest on these proofs.

## originality

PASS

The exact self-match is not distinct prior coverage. The closest primary work poses the general overlap question but studies other concrete games. The distinct checked catalogue comparators do not give the ab/ba transition-pair losing language or its sharp extremum. Assessment is relative to the inspected sources, not historical priority.

## value

PASS

The overlapping opposite transitions are a natural small case of the stated open extension problem. The theorem determines the outcome for every word, gives a regular language contrasting with the one-letter Dyck example, and fixes the true scale of attainable nimbers, rather than sampling short words or claiming the general problem solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
