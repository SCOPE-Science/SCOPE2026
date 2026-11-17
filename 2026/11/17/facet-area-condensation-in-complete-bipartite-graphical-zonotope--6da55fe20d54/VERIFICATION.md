---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof boundary

Run `python verify_k2q.py` after installing `requirements.txt`. This program explicitly enumerates the actual vertices in zero-sum coordinates, uses an orthonormal basis for the affine hull, obtains every exposed facet by a cut normal, computes its intrinsic area with `scipy.spatial.ConvexHull`, and checks the predicted area separately for every facet. It also checks the whole-body surface area and volume for \(q=2,3,4\), and computes stable binomial expectations for \(q=100,1000,3000\).

The recorded checks passed: 74 direct facets, three direct volumes and total areas, and three asymptotic numerical profiles. The finite checks do not certify the infinite family. The exact connected-cut decomposition, spanning-tree Euclidean volume formula, and fourth-moment inequality in `RESULT.md` establish the unrestricted identities and limits. No external independent mathematical audit has been performed.
