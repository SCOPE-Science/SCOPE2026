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

The Hardy multiplier identity reduces the operator norm exactly to max_circle |P|^n |1-P|^k. Positivity plus p0>0 identifies every peripheral root as a gcd-root with P=1 and uniform strict contraction outside finitely many small arcs, so no off-root maximum is neglected. Cumulant expansion log|P|=-v theta^2/2+kappa4 theta^4/24+O(theta^6) and direct moment expansion of log|1-P| to theta^2 yield the first corrected Gaussian profile at x=sqrt(n)|theta|. The leading k log x-vx^2/2 has a unique, nondegenerate maximizer sqrt(k/v), and its O(1/n) displacement affects the log maximum only O(n^-2), giving k^2B. The independent Fraction calculations exactly reproduced B=-1/4, -5/16, and 145661/1401856 for the three specified distributions. The finite identities corroborate rather than replace the analytic localization and stationary-point theorem.

## originality

PASS

Arnold 2026 Section 6.1 already gives an exact equal-weight Bernoulli scalar optimizer, and earlier Katznelson–Tzafriri/Dungey works prove qualitative or rate bounds. The surviving contribution is the full arbitrary finite positive polynomial with a four-moment 1/n coefficient, including sign reversal. No inspected earlier theorem covers that exact two-term formula; this is a qualified best-knowledge finding.

## value

PASS

A natural positive polynomial averaging operator has a sharp quantitative time-regularity profile whose first two coefficients are explicit in the law’s moments. The signed second-order correction distinguishes different convex averages even when leading scaling is the same, providing a precise usable finite-n rate classification beyond qualitative Ritt decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
