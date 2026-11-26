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

The frozen coefficient, the near-vertex example and nonattainment are correct, but the last sentence of frozen proof Step 3 says the only possible sharp limit is toward a vertex. For b=(3,2,1), the midpoint (5/2,5/2,1) of an edge gives a counterexample: interior approximants have the same third-coordinate limiting derivative 2(1−1/6). The replacement proves sharpness along interpolations to any minimum-coordinate face and removes the exclusivity assertion. It also treats boundary segments explicitly. Along every affine segment the sorting and pool comparisons have finitely many changes, because each candidate comparison is an analytic function on a neighborhood of the compact interval, with identically zero comparisons settled by fixed tie conventions. Each active block has derivative row sum 2(1−μ_i/B_I). For a proper block B_I<B, and for a full block with μ_i>m the bound is also strict. At differentiability times with μ_i=m the corresponding logged coordinate is at its global minimum and its tangential derivative is zero. Integration gives strictness in every coordinate for any distinct inputs. Positive interior interpolants toward a minimum coordinate allow the total-mass softmax derivative to attain the limiting bound. Euclidean block centering gives the quadratic comparison, and b=e^ρ gives m/B=(e−1)/(e^n−1).

## originality

PASS

The exact map, pool formulas, and block Jacobians are already in Blondel et al., and the soft-rank specialization by indexing and scaling is not separate novelty. The assessed distinction is the sharp all-input coordinate modulus and the strict finite-pair inequality. These require the feasible minimum-to-mass bound and a realizing limit, plus control on boundary segments. No matching sharp global result was identified in the statement-level comparison, which does not claim historical priority.

## value

PASS

A sharp coordinate perturbation budget for a natural differentiable ranking map is directly useful: the modulus depends only on minimum relative mass, converges to a very different value from local behavior on many pool patterns, and yields a strict comparison to quadratic rank at the same scale. The finite-pair strictness explains why testing moderate finite pairs will not recover the worst-case modulus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
