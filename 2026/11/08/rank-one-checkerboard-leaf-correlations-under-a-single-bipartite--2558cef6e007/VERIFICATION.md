---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Deleting the marked leaves leaves a bipartite tree, and the attachments to unmarked opposite-part vertices give exactly the all-marked-leaves probabilities in (1), including when the core is K_{1,1}. An entirely marked part is impossible by the sum of its degrees. Inclusion–exclusion gives independent baseline empty-box vectors and the Stirling laws. For the edge tilt put q=w−1. From the conditional incidences in (3)–(4), r_u−p=−(a−1)α_u/(ab), s_v−p=−(b−1)β_v/(ab), and h_uv−r_u−s_v+p=−α_uβ_v/(ab). The quadratic tilt coefficient ph_uv−r_us_v is the same as the linear coefficient, since p+(a−1)(b−1)/(ab)=1. This yields the stated q(1+q) factor; the denominator is positive even at deletion. Neither contrast vector vanishes, and each has zero sum, giving the signs, ranks and zero sums. Conditioning on both leaf counts preserves symmetry among edges under the uniform law; the number of selected edges remains fixed, so every edge still has inclusion probability p. The tilt consequently leaves the entire joint count law unchanged. This need not preserve independence of the labeled vectors.

## originality

PASS

The unweighted bipartite independence baseline is covered and not credited as a distinct finding. The supported contribution is the explicit nonlinear leaf-indicator checkerboard for a single tilted edge and its coexistence with a completely unchanged joint aggregate law. The closest checked weighted and unweighted results do not already supply this claim.

## value

PASS

A single conductance is a natural minimal perturbation of a graph with independent cross-part leaf vectors. The full covariance matrix resolves where dependence appears, where it reverses sign, and where it disappears; simultaneously the aggregate observers cannot detect any tilt. The exact factor and ranks are useful precisely because invariance of total counts alone misses the local structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
