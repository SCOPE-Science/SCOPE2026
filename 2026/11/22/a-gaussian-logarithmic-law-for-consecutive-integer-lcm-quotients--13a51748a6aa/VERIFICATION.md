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

At each power p^j the product-to-LCM exponent counts the multiples in the window minus one if any occur. Above k the count is at most one, whereas at p^j<=k the count is at least one and at most floor(k/p^j)+1. This gives divisibility by k!, periodicity, and (by CRT) exact independence across primes, not across powers of one prime. For p>sqrt(k), counting the start residues with no extra multiple gives deficit probability (p-1-(k mod p))/p, including zero for p|(k+1). The log contribution of the lower primes is bounded by pi(sqrt(k)) log k=O(sqrt(k)), hence its variance is O(k). The large-prime PNT calculation is justified first on p/k in [1/M,1], where log p/log k tends to 1 uniformly and the integrands have finitely many jumps, then by bounding the omitted theta(k/M) mass. Replacing Bernoulli parameters by 1-{k/p} has error at most 1/p also for the variance function. Integration on each unit interval telescopes the mean to Euler's constant and gives the variance partial sum (2M+1)log(M+1)-2log(M!)-2M, whose limit by Stirling is 2-log(2pi)>0. The centered high-prime summands are bounded by log k, so Lindeberg applies; the centered small-prime sum vanishes at the exact standardization scale. The proof does not replace exact centering by its leading equivalent.

## originality

PASS

Best of knowledge: the new claim is the evaluated mean/variance and growing-window Gaussian law for the weighted factorial deficit, not the local valuation or period identities and not a claim to priority for the finite distribution.

## value

PASS

This gives a fluctuation scale with an explicit strictly positive constant for a natural classical periodic quotient, and distinguishes the typical logarithmic deficit from both its extremal value and mere presence of prime factors. The prime weighting is essential and yields a useful evaluated asymptotic not supplied by a fixed-window table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
