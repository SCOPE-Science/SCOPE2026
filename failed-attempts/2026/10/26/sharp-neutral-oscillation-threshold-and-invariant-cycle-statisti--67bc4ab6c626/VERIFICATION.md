---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The asymmetric payoff difference in Jiang's Appendix C reduces to the frozen equations at N=2. For D=δ_s+δ_d, q(p)=δ_s−Dp, a=r/2−1, use the physical-time coordinates u=log(x/(1−x))−1/x and v=log(p/(1−p)). Each is an increasing diffeomorphism onto R. The transformed system satisfies u̇=a/x+(r/2)q(p), v̇=ε[(1+θ)x−1], and its divergence in (u,v) is −a(1−x), of strict sign off r=2. Thus Bendixson–Dulac excludes every nonconstant periodic interior orbit there, irrespective of equilibrium existence. At r=2 the separated Hamiltonian in (u,v) has derivatives H_u=ε[(1+θ)x(u)−1], H_v=Dp(v)−δ_s, with u̇=−H_v and v̇=H_u. Each derivative strictly increases and tends to nonzero limits of opposite signs, so H is strictly convex, proper and has a unique minimum at the stated coexistence point. Its other levels are smooth compact circles with a nowhere vanishing tangent flow, hence form a family of periodic orbits. Integrating v̇, u̇, and d log(x/(1−x))/dt=xq(p) over each full period gives respectively the stated mean x, mean p, and mean xp; these are physical-time identities and give zero covariance. The PDF version inspected numbers the general model Eq. (7) and gives the asymmetric formula in Appendix C; the frozen Eq. (11) locator was not confirmed in that version, but the stated vector field is correct.

## originality

FAIL

The entire critical center and its first integral are equivalent to those of a distinct catalogue finding for the same model. Its displayed Dulac identity immediately gives the off-critical exclusion when the original payoff constant is retained at N=2. The physical-time moments are not printed in that finding, but follow by applying the previously stated conditional-generator calculation for separable growth rates with the positive one-coordinate factors replaced by the ones already displayed in the model. This is partial exact overlap plus direct implication for the remaining claims, not a finding that all formulas appeared verbatim or that one record had chronological priority.

## value

FAIL

The neutral boundary and amplitude-independent averages are natural dynamical questions. In this record, the full critical orbit geometry is already covered, while the off-critical conclusion is a direct readout from the same model's displayed divergence identity and the moments are routine stationary tests of the separated velocity factors on those known orbits. No independently nonmechanical gap is established by combining them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
