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

Independent splitting proof: for X²=0 choose columns W lifting a reduced complement to ker(A), A=X mod π, and set U=XW. The columns (U,W) are independent mod π and extend to an R-basis. Take a coordinate map λ with λU=I and λW=0. Then P=Uλ+WλX is a projection onto the span of (U,W) and XP=PX=UλX. The complementary summand is free over the local ring and has residual X=0, since im(A) is contained in the reduction of the first summand. Its restriction is therefore π times a uniquely determined residue matrix B. This proves existence without a coefficient field. For uniqueness, on ker(A) a lift changes the divided image by a vector in im(A); a change of representative by Av is lifted by X applied to a lift of v and has zero further image. The divided image is in ker(A) by X²=0 and ann(π)=πR. This gives the k-linear, conjugacy-equivariant homology map, equal to B in the splitting. Conversely any similarity of B lifts to a change of complementary basis. A different generator uπ changes the homology label by the residue of u inverse. For each r, s=n−2r, the partitions indexed by monic irreducibles count B, giving the rational-canonical Euler product by unique factorization. Summing over r multiplies it by (1−z²)^{-1}; expansion through z³ gives q, q²+q+1, and q³+q²+2q. This also handles r=0, s=0 and residue characteristic two. The recorded finite checks are not needed for the proof and were not rerun.

## originality

PASS

Credit the length-two extension-orbit reduction, the labeled Bockstein and Smith statistics, and the standard finite-field similarity Euler product. The supported distinction is the actual all-size square-zero conjugacy quotient by residue rank and homology similarity, valid including mixed characteristic, with its resulting class series. The checked statements do not give that quotient without the extra square-zero splitting or an equivalent computation.

## value

PASS

This classifies all free square-zero differentials up to isomorphism over the short local rings in scope. Residue rank and Smith data can coincide while the homology maps are nonsimilar: already X=πI_2 and X=π times a size-two Jordan block at eigenvalue 1 have the same Smith data and different classes. Giving the missing complete invariant and an all-dimension orbit series uniform in ring characteristic is structurally useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
