---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Products of degree-3 spherical harmonics have only degrees 0,2,4,6. The icosahedron is a spherical 5-design, suppressing degree 2,4 center sums, so cap averaging gives G_c=I+a6(c)(G_pt-I). The six antipodal representatives yield the exact Seidel/conference S^2=5I and G_pt spectrum {0×4,7/3×3}, using 7P3 reproducing kernel. Funk–Hecke integration gives a6(c)=c(1+c)(429c^4-390c²+65)/208; the two positive nontrivial roots are c±=sqrt((195±26sqrt15)/429). Signs yield 4/3/4 least sectors; strict positivity from real analyticity over open caps; P6 prime at 1=21 implies A~(21/2)(1-c) and kappa~2/[9(1-c)]. Independently rederived polynomial integral/symbolic roots and conference identity; numerical 7-cap checks inspected in packaged script, not used for all c proof.

## originality

PASS

The four-dimensional cubic point-nullspace was already established by Hitchin, and general spherical-design Funk–Hecke filtering is standard. No inspected primary result provides the complete positive-area twelve-cap cubic Gram spectrum or two nontrivial Parseval thresholds.

## value

PASS

The existence and exact algebraic classification of two nonhemispherical cap aperture values yielding an isometry for a natural cubic harmonic representation is a sharp design theorem. The eigenspace switch and near-point conditioning are concrete quantitative stability information beyond the already known point nullspace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
