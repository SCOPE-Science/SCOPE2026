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

The repaired text disambiguates the generating function: C_w/D_w has coefficients indexed by iid block length, not by the number of shifts in the definition of survival. For example, one shift survives with probability 1-p²q^(2k), whereas the length-one avoidance probability is 1. The two series differ by removing the first N-1 terms and shifting the exponent, which preserves their first positive pole. The standard denominator identity and original theorem therefore survive unchanged. I checked the proper border lists and weighted suffix factors. In the V denominator, t=qz gives G=t-q-p t^(2k+1)(1-t); G is strictly increasing on [0,1], its zero is in (q,1), and the zero decreases in p. At an equality of first poles the function (p/q) times the sum of t^(-j) must equal one, and it is strictly increasing. Both denominators start positive at 1 and are negative at 1/q: for U, the remaining factor q²-pq+kp² is positive. At the small-p end C_U<C_V throughout this root interval, and at the large-p end the reverse holds. Evaluating the respective denominators at the other first zero gives opposite strict escape-rate orderings; the finite prefix spectral radius is continuous in p, so the unique candidate is attained. Substituting q=p times the geometric sum into G gives 2t^k-1=t^(3k)(1-t), strictly increasing after bringing all terms to the left. The strict bounds use q<t<1 and k≥3. With c=log 2, t=exp(-y/k), the corrected proof bounds 0<y<c and the right-hand side by c/k. The local implicit solution has y=c-c/(8k)+O(k^(-2)), hence 1-t=c/k-(c/8+c²/2)/k²+O(k^(-3)). The exact formula p=(1-t)/(1-t^(2k+1)(1-t)) adds c²/(4k²), yielding the claimed coefficient. Own direct finite-string enumeration at p=2/9 and k=3,4 agrees exactly with the length-indexed coefficients through N+2; high-precision bisection at k=3,4,8 reproduces the printed thresholds. These are finite cross-checks; the argument above covers the full parameter set. The supplied script was inspected, not run.

## originality

PASS

The isolated k=2 reversal and general autocorrelation formula are prior art. The repaired statement keeps the same substantive claim: the growing k≥3 family, uniqueness over the full bias interval and the sharp threshold asymptotic. These are not established by the compared prior statements.

## value

PASS

For natural equal-mass holes, bias can reverse the escape ordering even with composition fixed. The theorem gives a unique sharp scale, exact threshold, and second-order correction for arbitrarily long words. This goes beyond a numerical table or an example at a fixed length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
