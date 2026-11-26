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

Reconstructed the supporting-line argument. The outward normal angle is t+atan(t)-pi/2 and the stationary maximum height t²/sqrt(1+t²) is strictly increasing, so a later stationary maximum at a repeated normal wins. In the candidate interval the cross product F at a zero has derivative -lambda(t²+2)>0, where z(T)-z(t)=lambda z'(t) and lambda=T sin(T-t)/t<0. The lower-end sign is negative, including immediately to the right of zero at T=2pi (F'_T(0)=-2T), while the upper-end sign is positive. A full 2pi normal turn after contact would force a repeated terminal normal with greater height at T, contradicting F>=0 there. Thus the interior of the last arc strictly supports; excluded earlier turns either lose at their unique outward normal or are radially inside, since the retained directions span more than a semicircle and their hull contains the origin in its interior. The contact chord supports, leaves the tangent direction unchanged at u, and the corner at T turns by less than pi; these pieces close the convex boundary. For T<=pi, the radial chord supports since sin(t-T)<=0 on the full interval. The origin at T=pi is on the boundary but is not strictly exposed: its sole supporting line contains the chord. This is consistent with the wording of the Finding; the proof's informal 'exposes the whole arc' is read as boundary membership at this endpoint. The contact u when T>pi likewise shares its supporting line with T.

## originality

PASS

The strongest compared same-day record has the analogous boundary mechanism but exponential radius and a different threshold; neither it nor the older decaying spiral recovers the linear-radius contact equation and intrinsic-volume coefficients. The identical catalogue entry is the reviewed result itself, not independent coverage. No verified equivalent coverage in the inspected statements.

## value

PASS

The exact support transition solves a natural nonlocal convexification problem, not just an integration exercise. Green's theorem gives the stated chord term and length adds the return segment. As additional correctness checks, at T=pi+delta the tangent root has u=delta/2+O(delta²), so the leading area change is (pi/2)u(delta-u) and the perimeter change is -u³/6-u(delta-u)²/2, giving the displayed coefficients. At large T take h=T^(-1/2), d=2pi-epsilon, and set epsilon=h y in (T-d)(1-cos epsilon)-d+d²/T-sin epsilon=0. The regular positive root has y=2sqrt(pi)+O(h²), since the order-h term cancels. In the area, the T²epsilon terms cancel, leaving the sqrt(T) contribution from pi T epsilon - T²epsilon³/12. In the perimeter, the arc and chord terms in T epsilon cancel; the remaining terms of order T^(-1/2) are pi epsilon - T epsilon³/24 + (2pi)²/(2T epsilon). These give precisely the asserted coefficients and distinguish input arclength/sector area from hull measurements, both at first contact and over many turns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
