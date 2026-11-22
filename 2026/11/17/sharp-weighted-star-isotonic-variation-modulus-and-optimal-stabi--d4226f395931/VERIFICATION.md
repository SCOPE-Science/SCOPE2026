---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Given m>=2 and all masses μ0..μm and edge weights v1..vm positive, strict convexity produces unique rooted-star isotonic fit. On an active set S of pooled leaves, hub c=(μ0 x0+Σ_{S}μ_i x_i)/(μ0+Σ_S μ_i) and leaves max(x_i,c), with every S realized on an open chamber. In quotient d_i=x_i-x0, active columns have weighted norm μ_i Σ_{j notin S}v_j/[(μ0+Σ_S μ_j)v_i], bounded above by the singleton S={i}, which is strictly attainable; no-pooling yields norm 1. Finite segment integration proves sharp global Lipschitz. With Σ v=1, t_i=μ_i/(μ0+μ_i), R(v)=max_i t_i(1-v_i)/v_i, hence R<=ρ iff v_i>=t_i/(ρ+t_i); unique decreasing root of Σ t_i/(ρ+t_i)=1, threshold Σ μ_i/(μ0+2μ_i)<=1 and stated optimizers. Equal leaf mass μ_i=1 gives μ0>=m-2. Independent rational active-face checks cover m=2..8 and 105 instances, not arbitrary parameters.

## originality

PASS

A full relevant prior published tree-variation theorem determines the unweighted isotonic star special case L=max(1,(m-1)/2) and is correctly not reclaimed. Its hypothesis explicitly fixes unweighted vertex least squares and unweighted edge TV, so it cannot imply the mass-dependent singleton ratio, exact stabilizing region, or minimax edge weighting without new weighted optimization. Two primary isotonic papers address algorithmic and order-preserving concerns.

## value

PASS

Optimally choosing variation edge penalties to stabilize a weighted isotonic estimator is a natural and nontrivial graph-filter design problem. The exact root-mass threshold and all weighted equality regions give sharp, interpretable decisions beyond the already established uniform star coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
