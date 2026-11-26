---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For positive a,b,c every nonempty palindrome uses zero, one or two ones. The unique unary factor must be the unique longest run (its length-two trim is empty or repeats). At a marker the allowed radii are 0 through min(a,b) or min(b,c); the first radius absent at the other marker is the only minimal unique one. The two-marker palindrome is always unique, but positive padding leaves both markers in its trim; with zero padding the central zero run repeats iff an outer run is at least as long. These give the three indicators and the four cases b≤a, a<b<c, b=c, b>c for a<c (reversal handles a>c). Equality a=c yields one, and the minimum sum for a strict ordering is 1+2+3, giving length eight. Positive-composition summation gives all three series and the six strict order chambers have equal counts, with O(n) ties amongst Θ(n²) words. The condition on the central trim agrees with the standard MUPS definition, including overlapping occurrences and nonunique empty trim. The independent bounded literal replay matched every string/interval for 3,375 triples and every coefficient for 17,296 triples at lengths 5–50, including exactly the two claimed length-eight witnesses. At n=50 the counts were (23,720,338).

## originality

PASS

Best-of-knowledge pass for the parameterized identity/census and length statistics, not for the MUPS predicate, run-based candidate reduction or ability to compute MUPSs of a given word. The open author version of the 2024 paper was accessible and its relevant sections were inspected, closing the specific access limitation recorded in the frozen self-review at the preprint level. The general RLE antecedent is closer than the maximal-palindrome index and should be cited in a future exposition.

## value

PASS

A canonical sparse test family for MUPS indexing now has exact positional witnesses and output counts at all lengths. The limit distribution distinguishes this palindrome-specific statistic from both ordinary uniqueness and a single query's SUPS multiplicity. The contribution is modest but reusable as a sharp exact benchmark, not a claimed speedup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
