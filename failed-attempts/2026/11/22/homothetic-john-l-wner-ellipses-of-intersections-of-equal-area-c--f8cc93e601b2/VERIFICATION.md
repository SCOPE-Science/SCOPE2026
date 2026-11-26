---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Let D=(A-B)/2 and C=M^(-1/2)DM^(-1/2). In dimension two det(I+C)-det(I-C)=2 tr C, so equal determinants give tr C=0 and eigenvalues ±s with 0<=s<1 by positivity. The normalized intersection has quadratic gauge ||z||^2+s|z_1^2-z_2^2|. By uniqueness, quarter-turn symmetry fixes each unrestricted optimizer; its center must be the origin and its symmetric quadratic matrix scalar. The radial minimum and maximum are 1/sqrt(1+s) and 1, so pulling the disks back gives the two claimed ellipses. For s>0 equality occurs at the four axial inner contacts and four diagonal outer contacts; each rescaled four-point set has zero first moment and second moment 2I. When s=0 the body is a disk in these coordinates and the boundary contact set is continuous, as allowed by the Finding. Expanding det(A+B)/4 gives det M=d(1+delta^2/4), while det A=det M(1-s^2), yielding the spectral formula. Area scales as radius squared, so the ratio and its inverse follow; diagonal input matrices diag(t,t^(-1)) and diag(t^(-1),t) give the strict sharp limit. The frozen checker is numerical corroboration only and was not executed. The analytic proof is valid for all stated inputs and imposes no restriction on the competing centers or orientations.

## originality

FAIL

The full result is mechanically implied by exact earlier catalogue passages together with the classical uniqueness/affine equivariance of extremal ellipses. The October equal-area two-ellipse reduction supplies the complete affine class and mismatch; the November perpendicular-lens calculation supplies the exact sector radial function and square symmetries for that same class. These already fix both radii and all their equality directions. Kahan also directly covers the outer matrix. This finds equivalent mathematical coverage by implication, not a previously printed verbatim statement of the joint pair or a claim of absolute historical priority.

## value

FAIL

The family and fitting problem are natural, and this is a useful explicit exposition. As an independent new finding, however, the whole exact pair, contact pattern, sharp profile and inverse follow mechanically from already known affine normalization and exact radial data: uniqueness gives disks, and two endpoints of a one-variable sector formula give their radii. The invariant inversion adds only algebra. No distinct surviving mathematical claim beyond that covered consequence is established; a broader new theorem would be a different finding, not a bounded repair of this one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
