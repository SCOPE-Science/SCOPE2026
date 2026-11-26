---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The root-count pgf is det(qzI+L)/det(qI+L), so R_q is a sum of Bernoulli variables in distribution, with parameters t_j=q/(q+λ_j). The orthogonal Gaussian moments give V_G=2Σt_j². Connectedness gives t_1=1 and contributes −2 to the forest excess; every remaining summand t_j−3t_j² equals 1/12−3(t_j−1/6)². The bound and certificate follow, and equality forces λ_j=5q for all j≥2. The Laplacian is then exactly 5q times the orthogonal projector away from the constant vector, which gives the unique uniform complete conductance matrix and realizes all equality conditions simultaneously. At n=26 the variances are 125/36 and 122/36; the numerator of the complete-graph difference at general n is −2x²+(n−5)x−2n, with discriminant (n−1)(n−25) and positive roots for n≥26. The strict excess persists on an open neighborhood of the complete graph in the positive conductance and q parameters.

## originality

FAIL

The 2019 paper already compares the same unmodified one-draw estimators and gives both exact variances on these graphs. The frozen result is a mechanical sharp corollary: complete the same scalar square in each nonconstant mode, realize its equality with a uniform complete graph, and solve the resulting quadratic on that graph. This judgment is based on positive prior-coverage evidence, not a claim that the literal number 25 appears in the paper.

## value

FAIL

A sharp one-draw variance boundary is a natural benchmark, but this particular certificate and cutoff are a scalar square completion and an elementary equality realization from the already published comparison. The complete-graph window adds only the roots of that same quadratic. There is no independently nonmechanical invariant here, nor does the result resolve computational efficiency, correlated probes, or general-graph crossover sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
