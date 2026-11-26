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

Every equilibrium solves z=(1+ε)sin z and has x=y=sin z. With 0<1+ε<π, every root is in (−π,π), and sine divided by its argument strictly decreases from 1 to 0 on (0,π). This proves the global one/three count and Taylor expansion z_±²=6ε+O(ε²). At ε=0 the characteristic polynomial factors as (λ−1)(λ²+(1+s)λ+r); the quadratic Schur conditions are 1−r>0, r−s>0 and 2+r+s>0. The unit root is simple, with q=(1,1,1) and normalized left functional W/D. Direct substitution gives W∘F−W=sin z−z. The center graph has z=u+O(u³) in u=W/D: the quadratic jet vanishes by invariance, since the map has no quadratic term and the stable block has no unit eigenvalue. Thus u' = u−u³/(6D)+O(u⁵). Small nonzero center points keep their sign and tend to zero; differences of 1/u² tend to 1/(3D), yielding n u_n²→3D by averaging. The map is a smooth local diffeomorphism (det DF=r cos z near zero), and the strict spectral gap with the two Schur-stable directions allows the local strong-stable tracking theorem. The small center interval is forward trapping, so a sufficiently small stable-fiber neighborhood tracks it exponentially, including the two-dimensional fiber over zero. All other fibers track nonzero center iterates; the tracking error is negligible against n^(−1/2), giving all three sign and square-limit claims. The origin multiplier derivative in ε is 1/D. For a branch equilibrium, P(1)=1−(1+ε)cos z=2ε+O(ε²) and ∂_λP=D+O(ε), yielding the −2/D slope. Continuity retains both stable multipliers on each branch. The example gives D=11/4 and n z_n²→33/4 (and the same for x,y).

## originality

PASS

Credit the exact family and scalar fixed-point reduction to earlier work. The matched catalogue record covers the full fixed-point census, and the same scalar equation gives the elementary branch-size expansion. Neither that coverage, the primary sources' linear analysis, nor the related leafwise pitchfork supplies the normalized critical cubic drift or the quantified three-coordinate critical decay off a strong-stable surface. The pass is for this distinct nonlinear result in the fixed wedge, not for the equilibrium count taken alone.

## value

PASS

The unit-multiplier boundary of a previously studied recurrence leaves linear stability inconclusive. The critical coefficient and exceptional surface distinguish exponential relaxation from a sharp, parameter-dependent n^(−1/2) decay in the same system. This supplies a useful nonlinear classification at a natural boundary beyond the known equilibrium census or purely numerical bifurcation plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
