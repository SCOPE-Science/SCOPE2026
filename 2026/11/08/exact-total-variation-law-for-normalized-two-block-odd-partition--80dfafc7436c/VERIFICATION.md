---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Using the actual two-size odd-partition signed coefficient identity of Merca, for n=2^t m (m odd) the normalized coefficient equals r_t - lambda(m)/(4(2^{t+1}-1)sigma(m)). Positive lambda corresponds to sums of two squares by the prime-factor criterion. If t>=1, a different limiting atom would force lambda/sigma>2; if t=0, the 2-adic valuation equality for lambda(m),sigma(m) contradicts an even numerator 2/C_s. Therefore representable indices are outside the discrete limiting support. Every nonempty valuation layer contains n=2^t (sum of two squares), so the finite empirical atom masses are each at most 2^{-t-1}; the entire positive mass off support equals B(N)/N. TV is exactly that value for all N>=1, and Landau--Ramanujan gives the sharp K/sqrt(log N) asymptotic. Independent rational re-enumeration yielded B(256)=97 and TV=97/256; the finite check supplements the universal parity argument.

## originality

PASS

PASS: Merca derives the coefficient and dyadic identities, Landau the two-square asymptotic, but the exact finite-cutoff total-variation equality depends on the separately proved atom rigidity and mass-domination argument. These are not restatements of Merca positivity or an OEIS tabulation.

## value

PASS

An exact finite-sample total-variation distance at EVERY N from a natural signed partition statistic to a countable dyadic atomic distribution is mathematically substantive, with nontrivial parity rigidity and a surprising bridge to the classical sum-of-two-squares exceptional set. Sharp rate and exact support identification make the invariant useful beyond a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
