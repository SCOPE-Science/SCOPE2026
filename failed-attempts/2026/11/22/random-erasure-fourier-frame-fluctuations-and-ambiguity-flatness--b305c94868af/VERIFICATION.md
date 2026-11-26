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

The full shift orbit sums to N I, so the off-diagonal weights have row sum N−1 and mean mu=1/(N+1). Centering the weights by mu gives a symmetric edge kernel with zero row sums. If A is its sum of squares over unordered edges, the sum of products of distinct edges sharing an endpoint is −A; the corresponding disjoint sum is A/2 since the total edge sum is zero. Thus the variance of the centered edge sum is A(p_2−2p_3+p_4), with p_j=(m)_j/(n)_j. The factor is (m)_2(n−m)_2/(n)_4; covariance under label translations gives A=n D(g)/2, and trace-square uses twice the unordered sum. This yields the asserted mean and variance, also for n=4 and all four zero-variance masks. The Weyl squared ambiguities are in [0,1] and sum to N including the identity. The minimum centered dispersion is zero exactly for constant off-origin ambiguities, the SIC case. For the upper endpoint every ambiguity is 0 or 1; the unit-ambiguity labels form a subgroup of size N because their shifts fix the ray of g. Their scalar commutators equal one. The perfect commutator pairing then gives H=H^perp in every cyclic dimension, with no primality requirement. Conversely N unit entries exhaust the full sum and force all other entries to vanish. For the Alltop cubic the nonzero translation differences have a nondegenerate quadratic phase for p≥5, giving squared modulus 1/p; zero-translation, nonzero-modulation weights vanish. Inserting these values gives the claimed p^(-2) scaling of the maximum. That is a multiplicative identity even at trivial masks, not a quotient of two nonzero variances there.

## originality

PASS

Credit only the explicit identification of the all-window fixed-cardinality Gabor trace-square variance with the centered Weyl ambiguity moment. No inspected statement gives that identification at this scope. The sampling calculation is generic, the strongest endpoint is the same Weyl fourth-moment extremum as in stabilizer Rényi entropy, and the Alltop mask statistic is prior. The bounded pass on the explicit identification is not credit for a new sampling law, an ambiguity rigidity theorem in isolation, or a new Alltop formula.

## value

FAIL

The observable is natural, but the supported distinction is a routine specialization, not a substantive advance for it. After centering, the orbit gives a zero-row-sum kernel and its squared norm is exactly nD(g)/2: two- to four-label inclusion probabilities then mechanically read off all mask-size dependence. Optimizing it adds no new extremal analysis beyond the known Weyl fourth-moment statistic, interval equality, and the elementary ray-stabilizer condition; the Alltop comparison already follows from the known MUB frame-potential formula. There is no separate nonroutine estimate, parametrically new equality mechanism, or useful unknown case requiring more than these observations in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
