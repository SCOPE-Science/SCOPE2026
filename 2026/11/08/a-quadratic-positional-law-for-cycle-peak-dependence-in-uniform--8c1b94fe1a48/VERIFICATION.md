---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS. For any three prescribed distinct images of a uniform permutation, the partial injection splits into forced cycles and paths; contracting paths gives E[cycle_count | images]=H_{n-3}+r for n>=3. Counts of peak-compatible fixed points, transpositions, and the one compatible 3-cycle yield the displayed numerator; subtraction of H_n/3 establishes exact covariance for all i<j<k. Consecutive substitution gives -4 numerator, and (1,n-1,n) gives 3n²-21n+32, positive first n=5. Independent exhaustive exact-rational check for all position triples n=3..6 corroborated the formula, not its infinite proof.

## originality

PASS

Earlier sources give aggregate or consecutive-index peak/cycle relations. No checked source yields the full arbitrary i<j<k quadratic positional law; the nonadjacent event is not a descent-set statistic.

## value

PASS

PASS. Cycle structure versus one-line permutation-pattern comparisons is a natural dependence question. The complete indexed nonconsecutive quadratic profile distinguishes weak negative adjacent peaks from positive long-range peaks and identifies the sharp first sign boundary, a motivated exact finite positional law beyond aggregate peak counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
