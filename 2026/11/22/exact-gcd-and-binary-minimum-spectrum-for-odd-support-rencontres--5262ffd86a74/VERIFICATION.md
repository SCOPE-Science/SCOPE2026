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

The two-term derangement recurrence and alternating parity give v2(D_m)=v2(m-1) for odd m>=3. The factorial identity leaves only odd divisors m and m-2 in the denominator, proving the full binary formula; m=3 attains the minimum. With N=n-3, Lucas gives precisely the even submasks j<N of N. When N is odd they omit the low bit and are automatically proper; when N is even exclude only N. For an odd p<=n outside a pure p-power row, take m=p^j at a nonzero positive-position digit of n: both factors are p-units by Lucas and the derangement recurrence modulo p. Primes p>n are excluded by m=3. On n=p^a every selected binomial coefficient is divisible by p; the m=p^(a-1) coefficient has exactly one base-p carry and a p-unit weight for a>=2. This includes n=9, m=3: the proof's phrase 'strictly between 3 and n' is an endpoint slip, since 3 is admissible. For a=1, m=3 gives exactly exponent one. Independent inclusion–exclusion produced derangements and checked 1,675 exact assertions on n=4..80 (after a 43-assertion pilot), including each binary valuation and the minimizing columns.

## originality

PASS

The factorization, Lucas/Kummer inputs, and exact dyadic derangement valuation are prior art. The distinct contribution supported by the comparisons is their weighted odd-support row content and complete binary refinement, including the minimum count.

## value

PASS

The odd moved-support slice has uniform dyadic structure in its derangement weights, while the positive-fixed-point cutoff is decisive for the prime-power obstruction. The result supplies the primitive row factor and exactly locates the least-divisible columns, information not provided by the classical entries or an unweighted binomial row gcd.

The dated certificate retains the supplied scientific assessment, sources and limitations.
