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

For w=x+iy, differentiating w^3 gives 3|w|^4 in original time; u=Re(w^3) increases and v=Im(w^3) is conserved. At fixed v≠0 the forward integral from u to infinity converges and reaches infinite |w|, giving the maximal lifespan. At v=0 the negative real u half-axis approaches zero in infinite time and the positive one blows up; their cubic preimages give the stable and unstable rays respectively. The z-coordinate cannot shorten the existence time. The pushforward of planar area under the cubic map has density 3/(9|w|^4)=1/[3(u²+v²)^(2/3)]; hence on each v-slice it is exactly absolute remaining-time measure in u. The slice extends from 0 to c|v|^(-1/3) with c=B(1/2,1/6)/3. Integrating its excess above t over |v|<(c/t)^3 gives c³/t². This gives the exact ratio for uniform area on D_s. Quadratic homogeneity gives D_t=t^(-1)D_1; boundedness of f and finite area of D_1 justify dominated convergence, and the tail integral gives the moment threshold and log coefficient (subtracting L²Pr(T>L) for indicator truncation affects only O(1)). The Gaussian substitution is for the centered isotropic Gaussian. On the radius-R circle the time integral scaled by |sin(3θ)| has lower endpoint tending to minus infinity at each stable angle, giving R T ∼ B/3^(4/3) |θ-θ_j|^(-1/3) on each side, and is bounded away from those angles. Squeezing the angular level sets by the two-sided asymptotic gives three intervals of total length ∼6(B/(3^(4/3)Rt))³ and thus the stated coefficient and moment threshold. This requires neither monotonicity of the angular lifetime profile nor extrapolation from sampled trajectories.

## originality

PASS

Qualified originality is supported for the exact physical-time area and for the two sharp sampled lifetime laws for this single flow, not for the existence of a cubic potential, invariants/orbit geometry in broadly related gradient flows, or the classical integral and tail techniques. The closest inspected records and primary passages concern other flows, other events, or qualitative dynamics; they do not supply the stated distributional laws as an implication.

## value

PASS

For a natural homogeneous cubic gradient with explicitly identifiable stable rays, the exact finite-measure but unbounded survivor set gives a normalizable area ensemble and an exact Pareto law. Comparing it with a fixed-radius ensemble exposes a real change of lifetime exponent and moment threshold in the same deterministic flow. The explicit constants and contrasting laws provide a useful calibrated example beyond the homogeneity exponent or qualitative blow-up picture alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
