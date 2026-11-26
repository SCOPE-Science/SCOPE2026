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

An independent all-k argument checks the nonequivariant input: for a path on m≥3 vertices, splitting at the next-to-last vertex gives a conical deletion and a link on m−3 vertices, shifting reduced homology by one. Splitting the 3k-cycle at 0 gives deletion P_(3k−1) and link P_(3k−3), with their unique reduced groups Z in degrees k−1 and k−2 for k≥2. The integral exact sequence gives a split extension of Z by Z in degree k−1 and no other groups. At k=1 the complex has three vertices. For all k each join chain z_j is closed by signed omission cancellation, and its support lies in independent sets. The two maximal independent residue-class faces give actual integral cocycles even in the presence of higher simplices. Their evaluation on z_0,z_1 has rows (1,0), ((−1)^k,1) and determinant 1, proving a full basis. On z_2 it is (−1,0), the −1 coming from k negative choices and a cyclic factor reorder of sign (−1)^(k−1). Hence [z_2]=−a+(−1)^k b. Rotation shifts the offsets, and reflection sends factor t of z_j to reversed pair k−1−t of z_(2−j); reversing the k factors and the k directed pairs gives (−1)^(k(k+1)/2). These give exactly the stated column action matrices. With r=1 the relations give a=b and (2−(−1)^k)a=0; for odd k, s acts on the remaining Z/3 by (−1)^(k(k+1)/2). This proves both module-coinvariant assertions, including the triangle boundary case. No finite testing is used to infer the infinite result.

## originality

PASS

The nonequivariant wedge result, the sign-twisted rational character via Alexander duality and one exact order-three restriction at k=2 are established or overlap with inspected results. The compared statements do not give the full all-k integral dihedral lattice in the specified generators or its reflection-sensitive coinvariants. This passes the additional integral content, not those overlapping statements.

## value

PASS

A canonical all-k family gets concrete geometric generators and the full lattice action, not merely an isomorphism after scalar extension. The precise mod-four criterion detects order-three module coinvariants that the rational character cannot distinguish, and supplies useful input for computations with the symmetries of the ordinary cycle matching complex. The sign and integral basis matter: a rational basis or a finite catalogue of examples would not give the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
