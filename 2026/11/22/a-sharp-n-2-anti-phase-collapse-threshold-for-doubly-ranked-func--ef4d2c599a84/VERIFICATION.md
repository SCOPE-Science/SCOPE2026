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

Both pooled rank vectors are permutations almost surely. If the arithmetic summaries are constant, their common value is (N+1)/2, forcing complementary ranks. For the average of the pointwise logit scores, antisymmetry makes the common value zero, and injectivity forces the same complementarity. This is not the logit of the average rank. Ranking the negatives of the noisy X_i shows complementarity iff no pair inverts. For a pair with densities p,q, condition on its positive gap, apply both orientations, and substitute gap=sigma·t. Bounded densities and the integrable N(0,2) upper tail justify the limit; the first moment of its positive part is 1/sqrt(pi), giving 2 sigma∫pq/sqrt(pi)+o(sigma). The fixed equal group counts give N²sigma(∫h²/sqrt(pi)+o(1)). For k distinct inversion edges with v vertices and b connected components, condition on the Gaussian marks and a root in each component; spanning-tree edge constraints confine other X's to intervals of length at most twice sigma times the corresponding absolute mark differences. Integrating leaf by leaf gives O(sigma^(v−b)), since all fixed products of Gaussian differences have finite moments. At criticality each component of size at least three makes the tuple contribution O(N^(2b−v)) vanish. The vertex-disjoint tuples contribute the k-th power of the mean asymptotically by independence: the omitted tuples in the product-of-marginals sum are O(N^(2k−1) sigma^k). This proves the Poisson factorial-moment limit, and an interval around 0 with noninteger endpoints gives convergence of the zero atom. Markov and the shared-vertex second-moment estimate cover the outer regimes. Completing the square gives Lambda=(1+e^(−a²))/(4pi); at a=3 and c=4pi, the collapse probability is 0.36783404404296… and the resulting bound is on limsup power (or on the limiting power if it exists), not an assertion that every test has a limiting power. Replay RESULT.md Steps 1–5. The supplied checker and VERIFICATION.md were inspected, not executed; their simulations are illustrative. The result needs equal fixed group sizes, two raw equally weighted times, the stipulated noise and density hypotheses, and non-rejection on constant scores for the test implication. It does not extend that implication to randomized rejection at ties or order-changing preprocessing.

## originality

PASS

The score definitions, i.i.d. fixed-dimension Gaussian order-error slope, and marked rare-pair Poisson machinery are prior. The supported distinct contribution is the explicit two-fixed-group, joint growing-sample/vanishing-noise collapse law for both raw rank summaries and the resulting nonconsistency bound in a fixed alternative. The closest inspected indexed results have different perturbation models or statistics, not just different names.

## value

PASS

Anti-phase time courses can cancel a pooled-rank reduction even when first-time values separate the groups consistently. The exact nonvanishing tie probability quantifies a failure mode of two existing score choices rather than just giving a noiseless counterexample, with an interpretable conditional ceiling on rejection. This can inform time aggregation and tie handling without purporting to rank arbitrary functional tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
