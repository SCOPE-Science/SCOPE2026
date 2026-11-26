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

The binomial formula follows by solving the unfloored row generating functions (2-z)H_a=H_(a-1)+m with H_0=2m/(2-z). The error obeys the linear average recursion with local loss in {0,1/2}, so 0<=L-C<=a+1 by induction. Integer inputs in the row update allow all same-row floors to collapse into one floor. Its correction is the weighted sum 2^(-b) sum_(r=1)^b 2^(r-1)(L-C)(a-1,r). For r<=b-h, h=ceil(2 log_2 b), this is at most a 2^(-h); for the other h terms, substituting the unfloored lower row bounds the contribution by a constant times m h (b+1)^(a-1) 2^(-b), uniformly O(log b/b) on the stated m range. Continuity of floor away from the integers proves the staircase. At the threshold, 1/Lambda is a lower bound and ceil((1+B log b/b)/Lambda) is an upper bound for sufficiently large fixed B: first fix a uniform scaling range containing these candidates eventually, then choose B larger than its rounding-loss bound. This avoids a circular uniformity argument. The leading coefficient of Q gives the threshold and adjacent-row ratio; row zero is exactly floor(m/2^b). Theorem 21 of arXiv:2611.25137v1 verifies the stated reachability correspondence, with the same directions. It is the first positive value of the auxiliary array that gives physical reachability.

## originality

PASS

The recurrence, its interpretation, finite values, and the leading threshold laws for a=0,1 are prior. The contribution supported by the inspected sources is the quantitative fixed-row loss estimate, its noninteger staircase, and the threshold laws for every fixed higher row. Catalogue and primary-source comparisons support that distinction, not global priority.

## value

PASS

The minimum chip crossing the two-coordinate boundary is a natural labeled dynamics invariant, not an arbitrary fitted slice. The exact hierarchy of polynomial factors with row, the adjacent-row ratio, and the full limiting response off integer thresholds answer questions not apparent from finite tables; the proof isolates how path mergers and floor errors affect near-threshold counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
