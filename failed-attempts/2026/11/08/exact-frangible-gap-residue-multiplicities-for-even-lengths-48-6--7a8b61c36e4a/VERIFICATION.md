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

Both endpoints force the odd residue mod 2, which covers every odd offset. For an even-offset subset T, asking for all selected offsets to remain uncovered while both endpoints are coprime excludes exactly the distinct residues in {0,-h} union {-j:j in T} at each odd prime less than h. CRT multiplies those local choices and inclusion–exclusion gives the displayed count, also when a prime divides h and the endpoint exclusions coincide. An independent exact computation directly enumerated the endpoint-admissible wheel for primes up to 13 and applied inclusion–exclusion over the even offsets left uncovered, with Gray-code updates for the remaining primes. It completed all 31 even lengths from 4 through 64 and matched every CSV row, including all nine displayed values. Exact fraction summation reproduced 61370211356863231369/29555095284933631875. These are local finite residue classes, not pairs of consecutive primes.

## originality

FAIL

A distinct indexed Resultary result explicitly gives the same nine exact counts for the same residue classes and the same reduced rational S64 as intermediate results of a broader bound. The frozen comparison with the Mossinghoff–Trudgian paper's bounds alone misses this direct catalogue coverage. This is a statement overlap, not a judgment about authorship.

## value

FAIL

Through 64 is a meaningful cutoff set by the published bound table, and exact coefficients and normalization would be useful if unknown. However, the full table extension and rational truncation are already available in an indexed result. Reproducing them by another enumeration is useful corroboration but does not fill a remaining mathematical gap, prove a new efficiency result, or extend the exact range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
