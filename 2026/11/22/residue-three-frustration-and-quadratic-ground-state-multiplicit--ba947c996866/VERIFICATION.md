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

For N=2n≥6 there are 2N distinct undirected bonds; each trace term for the ordered-pair transfer is one labelled cyclic sequence, counting the two bonds to each newly appended site and that site's marker exactly once. I checked the three required determinant polynomials with a separately written integer cycle-cover computation: each directed simple cycle contributes one minus sign in det(I−tT), collections are vertex-disjoint, and truncating at two defects is exact since costs are nonnegative. It reproduced D_0=(1−q)^2, D_1=−2t^4 y(y+2)(1−q) and D_(2,[2])=t²(2y+1)(−1−4q+4q²), q=t³y. In the formal log the order-one quotient has only t-exponents 1 mod 3, and the square term in order two has only exponents 2 mod 3; combining with D_2/D_0 gives t²[−(2y+1)−4(2y+1)q−(2y²+4)q²]/(1−q)^2 in that residue class. Its coefficient at t^(3m+2) uses multipliers m+1,m,m−1, and −t∂_t multiplies by −N. This recovers all coefficients in the Finding, including positivity and disappearance of lower defects for the allowed lengths. Evaluating at y=1 yields N(21m−3)=N(7N−17) in the quadratic case; dividing log multiplicity by N gives zero limiting entropy density. A separate direct edge-list check confirmed N=6,8,10, including occupancy counts (120,176,16) at N=8. The finite determinant certificates feed the all-N formal-series proof; the enumerations are only spot checks.

## originality

PASS

The distinct supported contribution is the evaluated length-congruence classification and closed fixed-colour coefficient polynomials in the frustrated sectors. A primary paper already gives the full uniform-field transfer for the same strips and hence encodes every coefficient; neither that encoding, the proper-colouring sector, nor the transfer method is credited as new. Extracting and simplifying the lowest nonzero orders uniformly in length is the contribution, not evaluating a known formula at one size.

## value

PASS

The classification links a small geometrically forced defect cost to three sharply different multiplicity scales in a natural frustrated periodic system. The occupancy polynomial gives the exact distribution within the zero-field ground sector, including the response of that sector to infinitesimal colour preference at fixed size, where the unmarked count or an unevaluated transfer does not exhibit it. In particular, the quadratic count despite only two bad bonds is a useful fine-size invariant even though the bulk entropy density vanishes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
