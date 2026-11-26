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

The length-m orbit has total probability m^(-s)/zeta(s) and positive mass at every phase. Two forward marks recover the orbit and phase and occur for every point by length 2m, proving generation. A two-mark atom is a singleton of return time m; a single mark at i is one point per compatible orbit with minimum length max(i+1,n-i); two consecutive phases on an orbit of length at least n+2 witness overlap one for the zero word. The word with a mark at position zero only attains n, so the maximum is exactly n. Counting phases in these three cases also gives the exact moment identity. The lower sum over m<=floor(n/2) and the upper bound from min(m,n) give the stated powers and critical logarithmic coefficients; pointwise monotone convergence gives the finite limits. Subtracting the squared mean does not cancel the leading divergent second moment. Singleton entropy is finite by summability of m^(-s) log m, the increasing forward-join entropies tend to it, and the generating entropy rate is zero. This yields infinite system-level mean for 1<s<=2 and infinite system-level variance through s=3; the finite mean asserted for the intermediate regime concerns this partition. The packaged checker.py and VERIFICATION.md were read, not run; their rational finite-truncation checks are supplementary to the infinite argument.

## originality

PASS

The distinct finding is an admissible binary generator with addressed moment thresholds for the specific positive-overlap invariants in Question 6.8, not a new definition of recurrence or an exhaustive classification of variance values. No inspected prior result supplies the countable admissible construction and divergent normalized quantities.

## value

PASS

Answers a stated existence question using one explicit binary generator with the smallest growth order needed for the reference's admissibility condition. Bounded entropy and exact linear maximum coexist with tunable, different mean and variance thresholds; the full critical-moment calculation makes the example reusable rather than just a divergent-series witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
