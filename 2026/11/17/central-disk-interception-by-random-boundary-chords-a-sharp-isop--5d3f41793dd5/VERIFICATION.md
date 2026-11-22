---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For radial parametrization x(θ)=r(θ)e_θ, Lipschitz r>0 and q=sqrt(r²+(r′)²), boundary arclength density q/P. A segment passing arbitrarily near the origin must have nearly antipodal endpoint angles; central symmetry makes second radius r(θ+δ) and q periodic by π. Its exact distance ab|sin δ|/sqrt(a²+b²+2ab cos δ) is r(θ)|δ|/2+O_K(δ²) uniformly, and for sufficiently small |δ| the foot lies inside the finite segment. Thus the allowed second-angle interval has width 4ε/r(θ)+O_K(ε²); Lebesgue differentiation and dominated convergence yield κ=4/P²∫q²/r. Subtract 4/P=4/P²∫q to find exact deficit (4/P²)∫(r′²/r) q/(q+r). Since 1/2≤q/(q+r)<1 where r′ finite, obtain sharp coefficient 2/P² and rigidity r′=0 a.e. A strictly convex perturbation r=1+η cos2θ makes q/(q+r)→1/2 uniformly where r′≠0, proving optimality of constant 2. Square has r=secθ on each side, q=sec²θ, κ=4/64×4∫_{−π/4}^{π/4}sec³θ dθ=(√2+log(1+√2))/4. Independently evaluated this integral and a separate opposite-side endpoint-coordinate Jacobian. Finite simulations in source are not used as proof.

## originality

PASS

Existing circular chord hitting probabilities and motion-invariant random line results do not imply boundary-endpoint arclength law for arbitrary centrally symmetric convex K. The recent published random chord midpoint and moving-boundary target laws use distinct rare events or fixed circular K. A highly relevant historical surface-generated secants paper (Ehlers–Enns 1981) was not accessible in full text; its abstract emphasizes secant distributions and remains an explicit priority risk. No exhaustive originality proof is asserted.

## value

PASS

The sampling convention is natural and materially different from Crofton lines. The exact intensity identifies a radial derivative-energy invariant, its strict perimeter extremizer, a quantitatively sharp stability constant, and explicit nonround square benchmark. This is a geometrically motivated isoperimetric law and reproducible comparison, not just a fixed-disk chord probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
