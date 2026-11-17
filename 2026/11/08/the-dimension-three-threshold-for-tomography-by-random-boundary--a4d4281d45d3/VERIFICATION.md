---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Conditioning on IID opposing facet-pair indices gives singular mass ∑wi² and interior product mixture f=2∑_{i<j}wi wj∏_{k≠i,j}t(zk), t(u)=4min(u,1-u), ∫t=1. Tensor psi=t-1 satisfies ∫psi=0, ∫tpsi=1/3: gamma_ij=2wiwj/(s3^(d-2)), allowing vi=sqrt(bij bik/bjk)=wi/sqrt(s) and normalization for d>=3. In d=2 conditional f/s=1. Cube TV integrals independently computed with SymPy piecewise Irwin–Hall density: 13/96 and 521/1536. Reconstruction identifies weights, not nonorthogonal angles; singular component could distinguish rectangles even in d2.

## originality

PASS

Related inverse box theorem reconstructs squared edge lengths from volume-point distance moments, which do not determine this conditional midpoint law or its 2D/3D invertibility transition. Clement studies surface-endpoint chord length and exit statistics; author abstract inspected, but entire original paper not retrievable. Older Mathai cube paper concerns scalar distances, not this conditional tensor inverse in available abstract. Best-of-knowledge PASS with specific full-text risk, not an assertion of exhaustive absence.

## value

PASS

A sharp identifiability threshold for a naturally defined geometric sampling model, explicit finite bounded moments, and exact TV bias benchmarks distinguish what geometric information remains after conditioning. Labels/affine normalization and statistical population measurements are necessary; no claim of physical shape reconstruction for skew boxes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
