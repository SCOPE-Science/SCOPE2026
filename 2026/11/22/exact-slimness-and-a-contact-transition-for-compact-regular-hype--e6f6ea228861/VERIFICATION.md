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

For the central right triangle, the sine and cosine rules give sinh(L/2)=s sinh R, tan(theta/2)=cot(a)/cosh R, and tanh r=c tanh R for midpoint distance r and interior angle theta. For a point at distance u from one end of a side, the hyperbolic cosine rule along its incident neighboring side gives cosh d(v)=cosh u cosh v-sinh u sinh v cos(theta). If theta>=pi/2 the unique minimizer is the shared vertex; otherwise tanh v=tanh u cos(theta), yielding an interior foot for u>0 because v<u<=L, and distance asinh(sinh u sin(theta)). The resulting one-neighbor distance is strictly increasing in u. The minimum over both neighbors therefore has a unique maximum at the midpoint. This is the actual maximum over the union of all other sides: at the midpoint a nonneighbor contact candidate has absolute polar angle at least 3a. Match its radial distance on an adjacent side using the same absolute angular offset from that side's midpoint ray, choosing the offset toward the fixed side. The matched absolute angle is at most 2a, so the hyperbolic cosine law gives strictly smaller distance. For n=3 all other sides are neighbors. Thus there are exactly the claimed two nearest points. Independently the Lorentz inner product of the midpoint with an adjacent unit side normal gives sinh of the supporting-line distance as 2s^2 sinh(r) cosh(r)=T, which is the segment distance on the acute branch. On the other branch the segment distance is L/2. The angle crosses pi/2 only for n>=5 at cosh R=cot(a). At the crossing theta'=-tanh R_n and B^2=cos(2a); the first derivatives match, and differentiating B sin(theta) twice versus B contributes -B(theta')^2/sqrt(1+B^2), the stated negative jump. The derivative of T as a function of y=sinh^2 R has positive sign from 1+(2-s^2)y. Expanding T=2c[1+(1/2-1/s^2)/y+O(y^-2)] gives the claimed approach coefficient after applying asinh. The frozen numeric checker was inspected, not executed.

## originality

PASS

The ideal endpoint and its midpoint maximizer are already given in a separate indexed record and are not credited as distinct. The compact finite-segment profile, the change of nearest contact from endpoint to interior foot, and the differentiability boundary and approach rate remain distinct from that result and from the inspected thin-polygon and hyperbolic-width work.

## value

PASS

The regular compact family gives an exact benchmark for a standard metric invariant. The endpoint-constrained phase is a genuine geometric feature invisible from ideal polygons or support-line distances; the sharp contact threshold and derivative jump quantify it. The unique midpoint and the exact two-contact classification provide more than plugging a radius into a known limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
