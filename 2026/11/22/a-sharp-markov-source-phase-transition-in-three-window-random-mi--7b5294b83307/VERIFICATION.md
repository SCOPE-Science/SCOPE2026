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

For a fixed order, leftmost selected indices are nondecreasing as the window slides, so changes count newly selected positions up to end effects. Ergodicity gives the stationary charge frequency; conditional on a context, the smallest of d present types is uniform. A charge occurs when this type is first at index 0 or is unique at index 3, giving the two stated probabilities. For k≥2, a collision at gap 1 forces k+1 zeros with two free flanking symbols in total, giving exactly the six listed words. A nonconstant gap-2 overlap alternates over k+2 positions with just one end symbol free, giving four words. A nonconstant gap-3 overlap covers the whole block; its seed must be cyclically legal and thus has exactly one 1, giving the last three words. These families are disjoint: the alternating block has two 1s at distance 2, and the legal period-3 words cannot have a run of k+1 zeros. At k=2 they still consist of distinct words. Reversal cancels the two alternating defects by detailed balance. In the zero family the unmatched excess is π₀p^k[p²/2+pq/2+q²/6]=π₀p^k(1+p+p²)/6, q=1−p. Counting 00 and 01 transitions for the three cyclic starts gives π₀q(1+2p)t^m, π₀(3−p)t^(m+1), and t^(m+1) for k=3m,3m+1,3m+2. Their common charge excess is −1/6. At k=1 the eight legal contexts have excess only at 0000 and 0001, both +1/2. The crossover compares p with t^(1/3); at p²=q both scales match, with the three periodic weights divided by p^k equal to p, (3−p)p²/(2−p), p, giving the two stated positive coefficients. The stationary entropy rate derivative has sign of log(q/p²), identifying the maximum at the same p. Reviewed VERIFICATION.md and verify.py without executing the upload; the all-length proof is structural, not extrapolation from those finite checks. The comparison is of order averages, not individual orders.

## originality

PASS

The closest primary paper supplies the charge/periodicity method for iid full-alphabet input. Its uniform frequency of contexts gives no Markov-weighted residue term or crossover. The distinct same-source indexed theorem gives a fixed lexicographic order with a different limit; the identical indexed submission is not independent priority evidence. The exact weighted theorem is distinct on the bounded record examined.

## value

PASS

For the first width permitting a distinct period-three collision, correlation in a natural binary source changes the sign of the random-order finite-length bias. The exact formula distinguishes its two competing mechanisms and resolves their resonance at the maximal-entropy source, where using only the exponential rate would miss the persistent residue effect. It gives a tractable benchmark for order averaging under a dependent source without asserting a real-data or fixed-order result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
