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

Inclusion-exclusion splits 5040 S(n,7) into the odd-base numerator and -7*2^n*(3^n+3+5*2^n). The squared odd bases give increments 48,24,8. The first two Mahler coefficients on even inputs have valuations 2,4; the first two on odd inputs have valuations 0,3. For j>=3 the coefficients have valuation at least 3j-4. Vandermonde and C(d,i)=(d/i)C(d-1,i-1), with integer d=s-t initially and continuity on the 2-adics, bound C(s,j)-C(t,j) in valuation by at least nu2(s-t)-floor(log2 j). Thus no nonlinear terms tie the linear term; the branch distances are exactly nu2(s-t)+2 (even) and nu2(s-t) (odd). The constants and coefficient valuations give the stated integral branches with the even branch in 4 Z_2. Isometry modulo each power of two makes the normalized branches onto by finite bijection and lifting. Modulo 8 the factor 3^(n-1)+1 has valuation 1 for odd n and 2 for even n, and adding 5*2^n cannot alter that when n>=7. After division by 7!, the remainder valuations are n-3 and n-2. With shift 2^(k+1), the shifted remainder has strictly higher valuation than both competitors. Taking the unique minimum, or gaining at least a power of two on a tie, proves the two formulas and their stated lower bounds. For each k the first parity-compatible cutoff at or above 7 is exactly max(7,k+2+(k mod 2)); when greater than 7 its odd predecessor fails by the strict lower remainder valuation. An odd eventual period would identify an odd input with odd branch residue modulo 2 with an even input, which is impossible arbitrarily far out. Any even period 2d must satisfy 2^k|d by the odd branch distance. This proves both least assertions without extrapolating the tests. The supplied checker and verification notes were inspected, not executed. An independent Stirling recurrence modulo 2^(k+4), for k=1..10 and n=7..160 including shifted indices, matched 1532 nonresonant valuation instances, 8 resonance lower bounds, 1522 tail congruences, and 6 applicable failed predecessor congruences. This finite reproduction checks examples only; no exact resonance value is inferred.

## originality

PASS

Credit the standard fixed-column period comparison, known parity-class behavior, and an exact two-scale seventh-column difference theorem on dyadic-scaled pairs. The distinct supported part is the all-depth least onset with its parity correction and the arbitrary-index full-period shift-defect law (including odd inputs and small/transient even inputs not in the previously covered dyadic pairs). The period alone, the use of odd-base interpolation, and the two-scale mechanism on previously covered subsets are not being credited as new.

## value

PASS

The seventh column is a small Mersenne column with unequal parity scales. Its least onset tells exactly where any finite modular period computation becomes valid; the alternating last failure and the two competing valuations explain where that cutoff comes from. Extending pairwise dyadic estimates to arbitrary starting indices answers a natural fixed-column question without claiming to resolve the two possible resonance valuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
