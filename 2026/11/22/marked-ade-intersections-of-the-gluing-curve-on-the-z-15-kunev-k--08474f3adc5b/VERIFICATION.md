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

For the stated open abcd(ad-bc) != 0, any stabilizer point on the weighted complete intersection has tau=v=0: a nonzero tau has weight 1, and a nonzero v needs an even-weight nonzero coordinate on the surface, giving coprime weights. At alpha=0 the beta chart has u/beta=±sqrt(b), and nonzero derivatives in u and alpha leave (tau,v) with mu_4 weights (1,3). At alpha!=0 the alpha chart gives beta/alpha^2=-c/d and (u/alpha^2)^2=-c(ad-bc)/d^2, so both points are distinct and the u and beta derivatives leave (tau,v) with mu_2 weights (1,1). The restrictions have disjoint simple branch zeros in the weighted charts; at other points on the boundary the nonvanishing cover derivatives (or the simple branch derivative when one vanishes) give smoothness, and off tau=0 the stated quasismoothness applies. Near each A_(r-1) point, use x=tau^r, y=v^r, z=tau*v, xy=z^r. The first cone of the minimal resolution adjacent to the tau-axis divisor has coordinates y and s=z/y, with x=s^r y^(r-1), z=sy. Here the first exceptional component is y=0 and the strict transform is s=0, so the intersection is transverse with the end only. The adjacent rays of the usual subdivision are (1,0) and ((r-1)/r,1/r); they are a basis of the quotient lattice and the intermediate rays give the -2 chain. For each chain the sole unit endpoint intersection gives correction (r-1)/r by solving the Cartan system. Off the finite alpha=0 locus the curve is the conic u^2=beta(a+b beta) in the alpha=1 slice modulo sign on v, so it is rational and irreducible; the local calculation gives its smooth strict transform. Since tau vanishes once generically, T represents O_Y(1), with square 48/96=1/2; subtracting 5/2 yields -2. The generic-coefficient reading of the cited model is supported by the primary source's explicit four distinct branch points and generic linear systems, not by taking the displayed coefficient-one monomial list literally.

## originality

PASS

The supported contribution is the endpoint marking of the designated double curve on the generic biquadratic tail and its fractional intersection vector. The primary source already gives the normalized branch and gluing model, rationality and family identification; those are not new. Neither the inspected prior passages nor basket data give the marked map to the four exceptional chains, which requires identifying the axis in the actual cover and computing its minimal-resolution intersections. The index's exact hit was the assigned record itself.

## value

PASS

The divisor is selected by an actual KSBA gluing construction. The marked local intersections determine how to augment the exceptional configuration by the double curve, and distinguish an end from a middle in an A3 chain, which the unmarked classification cannot do. The 3/4,3/4,1/2,1/2 correction vector supplies the local numerical data needed to use this divisor on the resolution. The value rests on this complete incidence calculation, not on repeating a K3 family number or applying adjunction in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
