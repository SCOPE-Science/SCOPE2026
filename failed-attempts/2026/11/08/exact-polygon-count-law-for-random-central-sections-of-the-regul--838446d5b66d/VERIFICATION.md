---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The frozen RESULT specifies the 12 truncation vertices p_ij=2v_i+v_j and Haar-uniform central planes. An independent exact-integer reconstruction enumerated all 18 edges, all 134 sign chambers (from 132 pairwise intersections), and chamber counts 30,72,32 for N=4,5,6. The independently accumulated 528 corner incidences match the eight inverse-cosine classes of the table. Spherical excess and 4π normalization give the exact probabilities, and each of 18 edges has crossing probability arccos(7/11)/π giving E[N]=18 arccos(7/11)/π. This is an exhaustive finite configuration certificate, not a probabilistic Monte Carlo inference. Null vertex-orthogonal normals are excluded correctly.

## originality

FAIL

The complete result was already published on 2026-10-18 for the identical 12-vertex regular truncated tetrahedron and the same Haar-uniform central-plane model. Its full RESULT proof establishes the same three exact arccos probabilities, all 134 normal chambers, a stronger six-class individual chamber-area table, and the identical expected side count. Every submitted statement is implied by that earlier theorem. Later 2026-10-25 and 2026-11-01 findings corroborate coverage. Originality FAIL notwithstanding a correct different enumeration.

## value

PASS

Determining the full central-section polygon law for a natural noncentrally symmetric Archimedean solid is a motivated geometric stereology invariant. Exact shape frequencies, including 5-gon mass above 1/2, contain more information than the first moment, so the problem is intrinsically worthwhile even though solved previously.

The dated certificate retains the supplied scientific assessment, sources and limitations.
