---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For pq, the Carmichael exponent is lcm(p-1,q-1), so the defining condition is equivalent to p-1 dividing q-k and q-1 dividing p-k. The relative-size trichotomy is exact, and the prime-k family is counted by primes congruent to one modulo k-1. Fresh bounded comparison found no discrepancy with the direct Carmichael criterion.

## originality

FAIL

The theorem is correct but is a direct two-prime specialization of the classical all-m membership criterion. For a squarefree semiprime, substituting the standard exponent lcm(p-1,q-1) immediately gives the two divisibilities p-1 divides q-k and q-1 divides p-k; the stated cases follow only by comparing p and q with k. The infinitude and asymptotic then apply standard Dirichlet/PNT-in-progressions to the surviving family. Exact wording was not found, but implication-level coverage is decisive.

## value

FAIL

The phase-transition phrasing is neat, but mathematically it is a textbook two-prime substitution into the general Knödel exponent condition followed by standard fixed-progressions prime distribution. Under the common value bar, that is a routine corollary rather than an independently substantive structural advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
