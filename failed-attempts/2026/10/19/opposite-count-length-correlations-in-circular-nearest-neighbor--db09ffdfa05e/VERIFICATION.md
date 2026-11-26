---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Anchor the cyclic gaps at a tagged sample point (not at the gap containing an independently fixed origin) to get uniform Dirichlet spacings. The nearer adjacent point realizes min(G[i−1],G[i]); a strict local-minimum gap is reciprocal and its length equals the geodesic distance. With iid Exp(1) gaps the only shared minimum indicators occur at offsets 0, ±1, ±2, including at n=5. Splitting the distance-two integral into the two orders of a,b gives E[J_i J_{i+2}]=2/15, E[J_i B_{i+2}]=11/225 and E[B_i B_{i+2}]=22/1125. For two adjacent directed minima their conditional mean given the shared X is 1−exp(−X), giving covariance 1/12. Conditioned on J_i=1, the inner and outer directed minima have means 1/3 and 5/8; their respective covariance contributions are −1/18 and 1/24, each twice. Gamma–Dirichlet independence supplies the factors n and n(n+1) for mixed and second moments. This yields both reported length variances, both correlations, and the nonreciprocal covariance by subtraction. Independently used exact uniform-simplex moments in ordered chambers for n=5,6,7, also checking the directed variance. Replay: python3 /workspace/branches/reproduce_discrete.py.

## originality

FAIL

Verified current coverage of both mixed moments and a mechanical derivation of the remaining weighted variance from published local moment tables. In the 11/8 interval proof, all interior Exp(1) mean and covariance rows are the identical kernels for each circle site. For n≥5 the circle has n diagonal, n adjacent and n distance-two unordered pairs; applying the published interior rows gives Var(T)=n(5/81−2/81+146/10125) and E[T]=n/9. Substituting the circle's Gamma(n,1) total gives exactly Var(W)=44/[1125(n+1)], without any new integral or boundary case. The 10/27 and 11/22 circle records cover the negative and positive mixed moments directly. The frozen comparison and its other constants then follow by linearity and normalization. This is a finding of demonstrated coverage at audit, not a claim that the later-dated catalogue items have historical priority over the frozen manuscript.

## value

FAIL

The opposite-sign question is natural and the exact covariance values are useful. But for a distinct exact-invariant finding at audit, the sign comparison puts two already verified mixed moments side by side, the nonreciprocal moment is their linear combination, and the remaining finite second moment is a cyclic recount of published local rows. No independently new structural result remains after those implications. This is not a judgment against the usefulness of the original computation on its own date.

The dated certificate retains the supplied scientific assessment, sources and limitations.
