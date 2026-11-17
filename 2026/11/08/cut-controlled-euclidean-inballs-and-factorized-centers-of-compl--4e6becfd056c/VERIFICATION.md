---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For complete-graph incidence B, BB^T=nI−J, hence each edge-coordinate restriction to ker B has norm sqrt((n−2)/n). Thus an intrinsic ball centered at x has radius sqrt(n/(n−2))*min_e x_e. Every prefix cut has k(n−k) crossing edges and conserved total beta_k, giving min_e x_e≤τ=min beta_k/[k(n−k)]. The explicit feasible x_e=τ+1_{e=(k,k+1)}(beta_k−k(n−k)τ) achieves equality; proper prefix conditions guarantee full-dimensional positive feasible flows. For every tight cut, y=x−τ1≥0 has zero crossing sum and therefore zero individual crossing values. The remaining edges decompose across contiguous blocks, each with positive internal prefix netflows; their relative affine dimensions are (d−1)(d−2)/2. With b=e1−en, central cuts maximize k(n−k), recovering the stated radius and center dimension. No general metric equivalence to alternate Birkhoff-face embeddings assumed.

## originality

PASS

PASS best-of-knowledge for the all-prescribed-positive-prefix-netflow complete-DAG metric inradius and the exact tight-cut factorized incenter locus/dimension. The published general unit-flow antichain theorem covers CRY special radius and center inequalities, which are treated as prior work, not the novel remainder.

## value

PASS

The all-prescribed-real-netflow complete-DAG family is a natural parametrization of network-flow polytopes. The exact optimal-radius geometry and entire space of incenters can undergo cut-controlled dimension transitions; identifying its product decomposition and dimension for every positive prefix vector gives more than a routine scalar max-min LP value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
