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

In a basis with A=[[0,I],[0,0]], a commuting B has blocks [[P,Y],[0,P]]; B²=0 is exactly P²=0 and PY+YP=0. A rank-k P has image U, homology complement of dimension s=r−2k, and a complement on which P maps isomorphically onto U. Multiplication then forces the triangular pattern for Y with opposite corner diagonal k-blocks and an unrestricted s-by-s block Q on ker(P)/im(P). For fixed Q there are 2k²+2ks free scalar entries. Projecting the image of B onto the bottom r coordinates contributes k; the upper part over zero is im(P)+Y(ker(P)), which contributes k+rank(Q). The rank-k square-zero P's are counted by choosing the image, a containing kernel, and an isomorphism from the kernel quotient of the ambient space to the image. Counting Q by its image and a surjection gives R_{s,h}; all allowed strata are nonempty, including the dimension-zero blocks. The leading exponent is 4k(r−k)+h(2s−h)=r²−(s−h)² with leading coefficient one, giving maximal rank concentration and both uniform limits at fixed r. Nothing divides by 2, so characteristic two is included.

## originality

FAIL

The full finite-field joint census is an exact reparameterization of the earlier dual-number Smith census, Resultary 9ce1162ea15b. The fixed-r large-field limit is not the prior record's stated fixed-field asymptotic, but is an immediate leading-term consequence of its identical stratum formula. The failure is positive evidence of coverage, not a paper-access or proof issue.

## value

FAIL

The joint census is a natural and useful invariant, but this record duplicates an exact existing calculation in another notation. Its only distinguishable statement, the fixed-r large-q law, follows by selecting the monic maximal-degree terms of the same formula. No new mechanism, parameter range, or independently useful unrecovered invariant remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
