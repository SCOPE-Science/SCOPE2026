---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a prescribed center \(c\), every centrally symmetric subset of \(K\) lies in \(S(c)=K\cap(2c-K)\), which is itself centrally symmetric. The submitted Brunn--Minkowski argument correctly shows \(|S(c)|^{1/2}\) is concave, so averaging a center over the regular polygon's rotation orbit proves the polygon center is optimal. For odd \(n\), the outward normals of \(P_n\) and \(-P_n\) interlace into \(2n\) equally spaced normals with the same inradius, hence the centered overlap is a regular \(2n\)-gon. The standard inradius area formula then gives \(2\tan(\pi/(2n))/\tan(\pi/n)=1-\tan^2(\pi/(2n))\); even \(n\) is already centrally symmetric.

## originality

FAIL

The classical centrally symmetric kernel theorem already gives a unique maximum-volume centrally symmetric subset for every convex body, and Moszyńska--Żukowski explicitly state that its pseudo-centre is equivariant under affine automorphisms. For a regular polygon, rotational equivariance therefore forces the unique pseudo-centre to be the polygon center. Once the center is fixed, the maximal symmetric subset is immediately \(P_n\cap(-P_n)\); for odd \(n\) its edge normals visibly interlace to a regular \(2n\)-gon, and the displayed measure is the standard area ratio. Thus the all-\(n\) formula is a routine specialization of the classical uniqueness/equivariance theorem plus elementary regular-polygon geometry, even if the exact tangent expression was not located verbatim.

## value

FAIL

The regular-polygon profile is natural, but once the classical unique affine-equivariant kernel theorem is brought to bear, the optimizer is forced by symmetry and the value is a standard regular-polygon area ratio. The residual work is a textbook-level specialization rather than a substantive new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
