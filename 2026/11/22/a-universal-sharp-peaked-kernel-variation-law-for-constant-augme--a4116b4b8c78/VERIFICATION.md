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

Strict PD makes the augmented system invertible by testing a null vector against its constrained coefficient vector. Constants are reproduced exactly. On the mean-zero coefficient subspace, applying the mean-removal projection P gives PK_εc=Py; PK_ε is identity there up to O_n(φ(εh)). Thus c_i=y_i−mean(y)+O_n(φ(εh)V_d(y)), and the scalar term is mean(y)+O_n(φ(εh)V_d(y)). For the upper TV bound, each monotone translate contributes at most 1 flank for an endpoint and 2 for an interior node. For the lower TV bound use the partition alternating nodes and midpoints. Nodal values are exact; each midpoint differs from the scalar term by at most φ(εh/2)||c||_1, since every node is at least h/2 away. Comparing this partition variation with the endpoint/interior weighted sum confirms the stated uniform rate without differentiation or any assumption on extrema between nodes. Modulo constant input, differences are ℓ¹ coordinates and the unit coordinate vectors are the nodal steps, so subadditivity proves exact finite-ε reduction. A step at j has limiting weighted gain 4j(n−j)/n−1. The integer maximum and strict gap to noncentral steps (when such steps exist) prove the claim; for odd n the theorem does not require both eligible steps to tie. n=2 has norm 1, consistent with directly monotone interpolation. Read VERIFICATION.md and checker.py; the code uses one narrow effective width per grid and sampled partitions, which only lower-approximate continuous TV. It was not executed and is not needed for the proof.

## originality

PASS

The old constant-trend construction and generic ℓ¹ step reduction are not the originality claim. The distinct result supported by the comparison is the uniform fixed-grid localized TV law, hence the sharp norm and eventual central eligibility for all stated monotone profiles.

## value

PASS

The law quantifies a real stability distinction: constants are reproduced and the fixed-grid kernel matrix tends to the identity, yet the sharp variation amplification of the interpolated function grows linearly with the number of nodes. The exact universal coefficient and central perturbations identify a worst-case edge phenomenon not measured by conditioning or sup error. This assesses a fixed-grid peaked limit, not simultaneous scaling with node count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
