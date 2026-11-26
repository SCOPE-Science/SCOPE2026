---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Affine reduction preserves length fractions on individual sides and the area ratio. In the unit right triangle the support equations fix the shape matrix, and the two contact equations imply tv=wu and 2vt=2(u+v)-1; solving yields the stated center. Its three barycentric coordinates are in (0,1/2), which gives a positive determinant by Heron's identity. The normalized area is pi sqrt(p q r) with the three stated positive simplex coordinates. Monotone binomial expansion and beta integration give the 3F2 expression, with excess 2+s/2, including s=0. At the exceptional boundary corner (0,0), H>= (t+w)/2 and tw<=(t+w)^2/4 imply A=O(sqrt(t+w)); all other boundary limits are zero directly. Thus the unique AM–GM maximum localizes all upper-tail mass at (1/2,1/2). The independent symbolic Hessian and its determinant give 2 pi/sqrt(det(-D^2 A))=9/4 under unit contact density. The first two moments were also recomputed in /workspace/checks/scalar_checks.py; the frozen script was inspected, not run.

## originality

PASS

Best of checked evidence, the Mellin transform and sharp endpoint coefficient for independent uniform contacts are distinct. Contact geometry, affine shape invariance as a consequence of that geometry, and the Steiner supremum are not credited as new.

## value

PASS

Uniform arclength at each prescribed contact is a natural sampling measure, not an arbitrary slice of the center parameter space. The full compactly supported area law gives an exact calibration for this experiment, distinguishes it from uniform centers, and quantifies the probability of finding near-Steiner ellipses. The value lies in these quantitative results, not the classical maximum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
