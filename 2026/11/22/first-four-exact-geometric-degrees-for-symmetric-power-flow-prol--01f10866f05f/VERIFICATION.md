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

Repeated substitution of the ODE expresses every jet through the two retained initial conditions, so the affine prolongation is exactly the graph of the homogeneous D-iterates. Differentiating the monomials gives the stated top jets. Removing the visible coordinate factors, the two order-three residual linear forms have determinant 1−2n; for order four the swapped residual quadratics differ by −2(n−1)(u²−v²) and are nonzero at both candidate projective roots u=±v. Thus base points on the infinity line are only the coordinate points when 1<=m<n, and none for m=0 or m=n=3. At [1:0:0], r=n−m and M=m(n−1); the leading t-orders of the normalized top jets are r and r+1. For j=2 through m, both earlier jets have t-order at least n−j+1>=r+1. The degree-n jet B1 supplies z^M; A1 has positive t-order and constants and order-zero jets carry z-powers >M. Hence with wt(t)=M and wt(z)=r the leading forms are ct^r+uz^M and vz^M, with c,v nonzero generically. The regular sequence gives the associated graded quotient by (t^r,z^M): possible leading-term cancellations in a combination lift using the Koszul syzygy, increasing weight until the initial term is exposed. The local length is rM, also at the other point by symmetry. Generic codimension-two linear sections avoid the graph closure's boundary of dimension at most one and meet the smooth affine graph transversely. In the parametrizing plane the two degree-d curves have no component, either affine or at infinity. Bézout minus the two local lengths gives d²−2rM=(m²+1)n²−m²; d² alone gives n² and 81 at the two zero-correction regimes. A separate symbolic check tested the gcd and all allowed lower-jet weight inequalities for n=3 through 12, but the conclusion for all n rests on the analytic comparisons above.

## originality

PASS

The graph framework, elementary order-zero degree, general predicted formula and predicted infinity multiplicities are prior. The nontrivial contribution supported here is their uniform proof at orders 1–3 for n>=3. The exact formula is indeed a specialization of Puddu’s conjecture, but the prior computational evidence and his available transversality criterion do not prove this range.

## value

PASS

This proves a substantive initial-order range of a proposed two-parameter formula and explains exactly the lost Bézout degree at nontransverse infinity points. Uniform control in the exponent and the local length formula answer a specific obstruction in prior work; the elementary order-zero case only anchors the profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
