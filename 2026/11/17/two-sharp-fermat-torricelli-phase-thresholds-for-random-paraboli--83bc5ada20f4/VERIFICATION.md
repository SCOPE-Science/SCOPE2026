---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS. For x<y<z, chord slopes of P(t)=(t,t²) are x+y,x+z,y+z; principal arctangent ordering A<B<C gives vertex angles B−A, π−(C−A), C−B. Classical Fermat criterion identifies interior junction iff every angle<120°, otherwise a sampled angle>=120° is the minimizing hub. The maximum C−A for x>=−a,z<=a is 2 arctan(a), attained only at boundary x=−a,y=0,z=a, yielding a0=1/sqrt3. Maximizing left-end angle over x=−r,y→x,z=a produces F(r,a)=atan(a−r)+atan(2r); differentiating its exact threshold inequality yields unique tangent-contact a1=sqrt3/2+2sqrt6/3 at r=(1/2+sqrt2)/sqrt3; reflection gives right-end. At each unique extremizer the event condition has two linearly shrinking positive endpoint deficits and one quadratically shrinking central variable, hence δ^(5/2) Jacobian. Taylor normal forms give D0: u+w+(sqrt3/2)v²<2, D1: u/2+w+sqrt(3/2)v²<1. Direct integration gives volumes 64/(15*3^(1/4)) and 16/(15*(3/2)^(1/4)); multiplying ordered uniform-triple density 3/(4a³), and both endpoint labels, yields the two reported sharp coefficients. Compact localization around unique strict maxima and normalized indicator L1 convergence prove conditional total variation; numerical small-δ tests only corroborate. All topology scopes and parameter-uniform (not arclength) normalization were respected.

## originality

PASS

PASS best-of-knowledge. Zachos 2014 full primary text gives deterministic floating-versus-absorbed 120° alternative; Jahn–Kupitz–Martini–Richter 2014 full text gives even more general deterministic gauge/convex-set location theory. Neither integrates the ordered measure of three parameter-uniform parabola points, optimizes the arc half-width for new topology, or derives both 5/2-power marked rare-event laws. Related Resultary record treats parabolic tangent triangles with beta–Jacobi slopes, a different random object and event; other 120° near-minimum results treat a fixed triangle, not random three-terminal sampling.

## value

PASS

PASS. Optimal Euclidean three-terminal network type is a natural variational-geometric observable; two distinct sharp geometric thresholds separate middle-vertex hub, interior Steiner junction, and endpoint-hub regimes. Exact onset exponents, constants and complete marked conditional distributions explain how the new topology appears and are mathematically substantive beyond applying the classical pointwise 120-degree test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
