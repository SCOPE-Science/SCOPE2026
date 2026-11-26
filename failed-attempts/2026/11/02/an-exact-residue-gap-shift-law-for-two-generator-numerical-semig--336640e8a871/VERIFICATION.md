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

The simultaneous shift and all stated consequences hold under the two endpoint coprimality hypotheses, without any coprimality assumption on an intermediate pair. An independent algebraic check uses (1-z^a)P_{a,b}(z) = sum_{i=0}^{a-1}z^i - sum_{i=0}^{a-1}z^{ib}, where P is the gap polynomial. Subtract the corresponding identity at (a+m,b+m) in the polynomial ring modulo z^m-1. The increment profile f satisfies f(t)-f(t-a)=1-e*1_{e|t}; exchanging a,b yields f(t)-f(t-b)=1-d*1_{d|t}. The proposed sawtooths satisfy both cyclic differences, since a is -k modulo e and b is k modulo d. The two differences determine f up to a constant because gcd(a,b)=1; the difference of the Sylvester genera fixes its mean to a+(k+m-2)/2. CRT yields the asserted product-uniform multiplicities, range and variance, and t=0 counts exactly the quotient gaps. The source's Fourier recurrence is understood as a change of -1, rather than a decrease by -1. The frozen verifier was inspected, not executed.

## originality

FAIL

A distinct indexed result gives a stronger exact formula for every static residue count. Subtracting this formula at the two endpoints recovers the entire frozen increment; its CRT statistics are immediate consequences. This is demonstrated mathematical coverage, not a priority determination based on catalog dates.

## value

FAIL

A full transition histogram can be useful, but here the asserted translation law is a direct subtraction of a stronger available residue formula. The remaining spread, variance and balance criterion are routine computations for the two CRT uniforms, not a distinct surviving advance worth a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
