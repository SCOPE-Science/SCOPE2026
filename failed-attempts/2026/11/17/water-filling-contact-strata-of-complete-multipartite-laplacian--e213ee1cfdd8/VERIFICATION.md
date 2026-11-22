---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The full columns have class norm squared b_j=(N-a_j)(N-a_j+1) and classwise inner product <Le_v,c>=Nc_v. The scalar F(tau) is strictly decreasing on F>0, so tau exists uniquely. The weighted center c_v=(b_j-tau)_+/(2N)-1 lies in zero-sum hyperplane and is a convex combination of vertex columns with weights (b_j-tau)_+/(2N^2). Direct squared distances give R^2=N+tau+S/(4N^2), clearance (tau-b_j)_+, and all positive barycentric vertices on the sphere. The exact variance identity bounds every rival center by R^2+||z-c||^2, establishing global minimality and uniqueness; affine independence of columns yields uniqueness of certificate. 175 independently generated exact profiles and critical K_(3,3,6) and screened K_(4,17,17) examples agree. Finite tests do not prove unbounded r and part sizes; the displayed algebra does.

## originality

FAIL

A separately published same-date complete-multipartite Laplacian-sphere theorem is mathematically identical after the explicit change of variables m=tau+2N. It has the same domain r>=3, threshold equation, center, radius, all contact/clearance cases, unique certificate, sorted active-prefix construction, and both K_(3,3,6) and K_(4,17,17) examples. This is decisive equivalent-result coverage, not merely a title similarity; within-November-17 priority remains unknown.

## value

FAIL

The convex-geometric contact classification is mathematically meaningful, but as a standalone research finding this precise r>=3 theorem, support certificate, rational thresholds and examples are all restatements of another published theorem. A second proof/checker or variable renaming does not create a new valuable exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
