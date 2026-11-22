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

Derived projection slope B(f)=sum c_k (f_k-f_(k-1)), c_k>0, and exact attained seminorm W max c_k/w_k by single-step jumps. Reproduction of coordinate t yields lower bound 1 and equality iff c_k=w_k/W. Differencing c_i-c_(i+1)=mu_i(t_i-m)/S forces strict rise/possible single peak flat/strict fall. Constructive masses mu_i=(w_i-w_(i+1))/(t_i-m) with endpoint delta values positive and zero-peak free mass give mean m and S=W; completeness up to scaling. Independently checked rational n=4 profile w=(1,2,1), mu=(1,3,3,1): c=(1/4,1/2,1/4), norm 1. Exact one-edge boundary included; examined check_projection.py, which does not replace proof.

## originality

PASS

Published mass-aware isotonic variation theorem classifies a nonlinear cone-constrained projection using concavity in cumulative observation mass; the present linear rank-two affine projector has a distinct inverse positive-mass design criterion in edge-weight order for every grid. TV diffusion/wavelet papers lack this affine projector theorem. The explicit characterization is not a corollary of their different operators.

## value

PASS

A complete all-grid inverse design criterion for turning weighted affine regression into TV-nonexpansive smoothing is a natural stability question. The shape threshold and explicit positive mass construction are useful independent of larger optimization problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
