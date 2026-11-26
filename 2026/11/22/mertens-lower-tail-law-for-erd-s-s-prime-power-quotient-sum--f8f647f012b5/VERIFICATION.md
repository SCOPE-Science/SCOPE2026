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

For fixed prime sets the Chinese remainder theorem gives independent geometric exact valuations (first truncate the allowed exponents); the omitted-prime mean is uniformly bounded by ∑_{p>P}p⁻² for integers up to X and for the independent-prime model. E Z_p=1/[p(p+1)], so the model sum is finite almost surely and the same tail bound gives weak convergence. Atomlessness also follows directly: distinct assignments of reciprocal powers or zero at a finite prime set have distinct sums, since multiplying their difference by the common denominator and reducing modulo a prime where the valuations differ leaves a nonzero residue. The largest possible mass of that finite sum is therefore ∏_{p≤P}(1−1/p)→0, an upper bound on the largest mass after adding the independent tail. Full support follows by greedily selecting reciprocals of sufficiently large primes to approximate any u≥0, imposing finitely many valuations (positive probability), then using Markov's inequality for the unassigned tail. In particular the CDF limit exists also at 0. For y→∞ the no-prime-through-y cylinder has mass M(y). Its independent tail has mean O(1/(y log y)) by the prime-counting upper bound and partial summation, giving relative loss O(1/log y). Conversely each p≤y must be absent or have valuation at least the first a with p^a≥y, a constraint of probability 1−1/p+p⁻ᵃ. Summing the exception terms contributes O(y⁻¹ᐟ²), by bounding each by 1/y through √y, each by p⁻² for √y<p<y, and treating prime y separately. Dividing their product by M(y) proves the matching relative bound. Mertens supplies e^(−γ); the CDF ratio is exactly the conditional logarithmic survival probability for fixed α≥1 and 0<t<1. This is an iterated endpoint limit after natural density, not a joint cutoff claim. The supplied finite checker was inspected but not run; the analytic proof covers the limits.

## originality

PASS

The exact sharp lower endpoint for the normalized exact-prime-power statistic is distinct on the inspected evidence. Existence and atomlessness are classical, the Mertens product is classical, and the Pareto ratio law adds no independent novelty. The supported increment is the arithmetic-to-prime-cylinder comparison for this specific lower endpoint, including the exact-valuation exceptions.

## value

PASS

The normalized Erdős statistic is a natural arithmetic observable with a known general distribution-existence mechanism but no tail constant in that mechanism. Identifying the small-value frequency to sharp relative order explains quantitatively why rough-number avoidance dominates despite the possibility of small prime powers with high valuation. The conclusion is useful beyond finite examples and gives precise conditional thresholds as a consequence, without treating the Pareto rephrasing as a second contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
