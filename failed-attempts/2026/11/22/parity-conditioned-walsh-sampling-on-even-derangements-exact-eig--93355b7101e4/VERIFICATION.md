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

The signed derangement count is det(J−I)=s(n−1); the single-edge signed count is s by conjugation and the deterministic n occupied edges. The reciprocal signed count is minus the residual derangement determinant. Four distinct endpoints give zero determinant because two unrestricted rows coincide, and summing over the other occupied edges then gives the chain signed count s. Combining with ordinary completion counts yields the stated even joint probabilities. On the zero-row/column subspace the reciprocal, chain and disjoint coefficient sums are H_ji, −2H_ji and H_ij+H_ji; this gives covariance αI+β transpose. The symmetric and skew sector dimensions use unsigned and oriented complete-graph incidence ranks. Walsh coordinates multiply centered covariance by four; the outer product of the mean vector (including the constant coordinate) gives τ and the remaining deterministic directions are null. At n=4 the skew eigenvalue is zero, giving nullity ten. For n≥5 the derangement recurrence gives the claimed positive levels; β changes sign only at the two odd exceptions n=5,7 because the odd-size numerator is D_(n−4)−(n−1), negative at 5 and 7 and strictly positive from 9 onward. To obtain the stated O(n^−4) remainder for the squared condition number, use the alternating inclusion-exclusion bound D_m=m!/e+O(1), not just D_m/m!→1/e. It gives α=n^−1+O(n^−2) and β=n^−4+O(n^−5).

## originality

FAIL

The earlier Ewens record 85125daabf20 gives the necessary cycle-weight polynomial counts and covariance action. An explicit two-evaluation parity projection recovers all the even-conditioned pair data, after which its covariance decomposition and the elementary conversion to the Walsh basis give the claimed Gram spectrum. One need not assume an Ewens probability law at negative parameter. The n=4 kernel, tightness, ordering and condition asymptotic are elementary consequences of those explicit inherited formulas.

## value

FAIL

Parity-restricted sampling is a natural problem, and rank loss and sector reversal are meaningful phenomena. Here the exact phenomena are already readable from the cycle-weight polynomials by a two-point parity filter and from the existing sector decomposition. The Gram scaling, isolated small sizes, and elementary sign checks do not supply an independently new exact invariant beyond that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
