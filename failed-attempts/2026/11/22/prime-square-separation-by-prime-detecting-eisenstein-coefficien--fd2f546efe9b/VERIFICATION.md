---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The frozen domain is n≥2 and odd 1≤r<s. The end-divisor terms cancel, and a proper divisor of composite n is at most n/2, so for h=s−r≥2 its contribution T_n(d) is at least d^r(1+11n^s/16)>n^s d^r/2. Primes have an empty sum. For n=p² the sole interior divisor gives p^r(p^{s−r}−1)(p^{r+s}−1), with normalized ratio (1−p^{−(s−r)})(1−p^{−(r+s)}) strictly between zero and one and tending to one. Otherwise the least prime p and n/p are distinct interior divisors, and AM–GM gives A_{r,s}(n)>n^s(p^r+(n/p)^r)/2≥n^{s+r/2}. The envelope lies below the threshold for all n>1 and equals the exact value at squares. The G normalization and the published partition-detector identity have the stated signs and factor n+1. The prime statement would be false at n=1, which the original explicitly excludes. Exact independent tests corroborate rather than prove the infinite claim.

## originality

FAIL

The threshold is a direct corollary of a previously published proper-divisor bound, even though the checked texts do not print the trichotomy with that threshold. Craig–van Ittersum–Ono's Lemma 2.1 proof bounds each term below by d^r[1+n^s(1−2^{1−(s−r)})] (i.e. as a lower bound for the term). This is already strictly greater than n^s d^r/2 on the entire frozen odd-exponent domain, including r=1. Allen–Craig explicitly retains the two terms p,n/p on nonsquares and evaluates the sole term on prime squares. Substituting the older bound in that two-term estimate and taking the arithmetic–geometric mean yields exactly the claimed strict nonsquare threshold. The exact prime-square value and the partition normalization are also prior. This is demonstrated implication, not a failure due to lack of access or an assumption of priority from a similar title.

## value

FAIL

The prime-square normalization is a clear arithmetic interpretation, but the claimed exact result as a standalone contribution is obtained directly from the already studied complementary-divisor pair and known term estimate, with the equality case and detector identity already available. The frozen proof's slight sharpening of the intermediate coefficient is neither necessary for the claim nor motivated as an independently useful new bound. No substantial surviving finding is established by narrowing this record to its envelope or its partition specialization, so no repair is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
