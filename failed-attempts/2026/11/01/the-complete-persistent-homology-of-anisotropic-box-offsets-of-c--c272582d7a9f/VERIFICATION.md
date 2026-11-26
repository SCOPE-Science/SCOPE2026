---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The analytic proof works for aligned nondegenerate boxes, real inclusive offsets, all ties, and reduced homology over any field. Membership is equivalent to lying in the outer box and having at least d-k endpoint-admissible coordinates. Inactive endpoint slabs cover their coordinate intervals even at equality. For q>k the active saturation homotopy preserves endpoint slabs and lands in the rescaled k-skeleton; restriction to that skeleton is homotopic to the identity. Its reduced cellular rank is the displayed Euler sum; since the skeleton is (k-1)-connected for k>=1, its homotopy type is the stated wedge (and k=0 is a set of vertices). For lambda<=mu at least q(mu)-k surviving coordinates were already saturated at lambda, with the same signs at mu. The normalized maps are therefore homotopic in the target skeleton to coordinate deletion, whose section appends fixed endpoints. This proves surjectivity rather than inferring it from ranks and gives the exact half-open death intervals. The outer box is the convex hull because all its vertices occur in the offset; all-active zero coordinates miss the offset when q>k, and the endpoint condition is automatic when q<=k. The frozen verify.py and its noted finite tests are supplementary, not the general proof; the supplied script was not executed.

## originality

FAIL

A distinct November 8 catalogue record, 6624d08db373, covers the entire mathematical finding after coordinate rescaling, not just a convexification criterion or an isotropic special case. Its inspected Finding has the same strong endpoint membership, wedge type, ranks, all inclusion surjections, tied all-field barcode deaths, and sharp inclusive convexification threshold, and adds a void-volume profile. This is an exact coverage decision in the checked corpus. The November 1 and November 8 record paths do not establish historical priority or dependence, and no claim is made that the later-dated entry preceded the frozen result.

## value

FAIL

The exact tied-width barcode is useful in itself as a benchmark for cubical persistence. However, this submission adds no independent structural or exact result over the verified anisotropic-offset theorem. The coordinate normalization and alternate Betti sum are equivalent descriptions, not a distinct contribution or a surviving repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
