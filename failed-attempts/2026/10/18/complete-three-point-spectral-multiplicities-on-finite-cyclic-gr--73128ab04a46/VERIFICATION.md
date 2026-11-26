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

Three unit phases sum to zero only when they are a rotated set of cube roots. Applying this to all row differences makes the ternary depths complementary and requires the nonternary products to vanish. For eligible A, putting g=gcd(N,a1-a0,a2-a0) and L=N/(3g), B chooses one point from each of the three residue classes modulo 3L above a chosen residue modulo L. This gives Lg^3 distinct unordered spectra. Independent ternary row lifts and nonternary all-congruent counts give the stated strata, with a single division by six for globally distinct ordered triples; multiplying by the spectrum multiplicity and summing produces the total. Read the frozen RESULT.md, VERIFICATION.md, verify.py and verification_output.txt. Independently tested all three row-pair orthogonalities and fixed-A counts for 13 orders, including 27 and 36, via python /workspace/audit_replay.py 4; complete replay output is /workspace/review-evidence/4.txt.

## originality

FAIL

Covered by direct counting from the stronger pairwise valuation classification in Herr–Wiegand, Theorem 3.6. The closed formulas need not appear there for this conclusion: translating the exact criterion makes the fibers three independent choices in equal-sized residue classes, and the remaining histogram is the elementary census of residue-depth strata. No new compatibility principle or nonmechanical counting step is required. This is implication-based coverage, not evidence that the earlier paper explicitly prints the histogram.

## value

FAIL

The spectrum multiplicity and incidence total are natural and the closed expression is convenient. As a standalone scientific finding, however, this is a mechanically obtainable valuation-stratum tally of the existing full pair classifier: the fixed-A fiber is L equal three-class choices and the row/total sums are routine CRT counting. No separate exact invariant beyond that prior implication is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
