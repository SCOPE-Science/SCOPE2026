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

The definition counts nonempty distinct linear complete returns, allowing overlapping occurrences. Unary powers contribute the two respective maximum run lengths. A nonunary border must match its first transition at different transitions in its two occurrences; this excludes two-run closed factors and forces a two-run border in a four-run factor. Three-run factors are closed only with equal terminal lengths, and their zero-ended families overlap exactly when b=d. For five-run factors a border containing a 1 must center on different full 1-runs, hence requires b=d and both outer zero lengths at most c. Otherwise a unary zero border occurs just twice precisely when both outer lengths equal that border length and exceed c. The summed run counts give the formula. With x=max(u,v), y=min(u,v), the zero-run total is at least 2x+y; substitution in the equal-one-run branch and completing the square give the n^2/8 excess bound, and the unequal branch gives at most (n-1)^2/12. The stated witness yields 8t^2+6t, and padding its final zero run gives the lower limit at all lengths. The equality correction can vanish when u=v=1. The supplied enumeration was inspected, not run: its 9,592 count includes repeated tuples across two loops, and the ten witness checks in lines 45–50 are formula evaluations, not fresh direct counts. The all-parameter proof does not depend on these checks.

## originality

FAIL

Distinctness in the catalogue is not established: a separate Resultary record contains the same exact formula and the same sharp five-run asymptotic and witness, and adds rigidity. This is a verified statement-level overlap, not a suspected match or a conclusion from a failed lookup. The 2026-10-25 path does not show that its result preceded the 2026-10-18 frozen record, nor establish which was independently obtained first. The older identified literature does not give the full result. No mathematically distinct part of the frozen Finding survives the exact match.

## value

PASS

The mathematical question is worthwhile independently of priority: the exact low-run formula isolates the effect of equal interior runs and the restricted sharp extremum discriminates run complexity from unrestricted quadratic growth. The submission does not add a distinct result to the matched catalogue theorem, as recorded under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
