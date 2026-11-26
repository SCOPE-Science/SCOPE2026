---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Unitary invariance gives orthogonal monomials with norm squared α! m_L/(d)_L in degree L and hence the radial diagonal kernel B_L |z|^(2L)/m_L. The argument includes surface mass and mass at the origin (the degree-zero kernel is one), and full radial reach gives positive moments. Bounded holomorphic multiplication preserves A²: approximate first by f(ρz) and its polynomials, then let ρ tend to one using bounded radial convergence on the surface component and ordinary interior convergence. The identity H*H=M_f* M_f−M_f M_f* follows by orthogonal projection. On an input of degree L the homogeneous outputs of M_f are orthogonal, and on degree L the adjoint retrieves exactly the blocks of degrees L−k for k≤L. Thus the norm sums give a first trace B_L a_k m_(L+k)/m_L and the same trace shifted by k for the second term. The positive component sums are finite at any fixed cutoff for bounded f, so cancellation is legitimate and leaves exactly the stated boundary shells. Tilting by |z|^(2L) concentrates near radius one and gives fixed-k moment ratios tending to one. The normalized shell factor tends to k and is bounded by k, giving the finite-energy case by dominated convergence and divergence in the infinite-energy case by Fatou. For d≥2, B_M grows unboundedly, so positive energy implies failure of Hilbert–Schmidt membership. For d=1 the same cutoff increases to the full squared Hilbert–Schmidt norm in the extended sense. The beta moment ratio and a_1=1/d give the claimed coordinate benchmark. The frozen CHECK.py was inspected, not run. An independently written replay at branches/5f119ab4-0584-4776-b88d-86f22ebeef78/reproduce_trace.py passed 173 exact rational assertions comparing direct monomial energies to shell traces; this is a bounded diagnostic, not proof of the infinite result.

## originality

PASS

The supported distinction is the exact first-power, total-degree compressed trace and its normalized full-radius radial-measure universality for bounded analytic symbols. The commutator identity, one-dimensional consistency case, established rigidity results and critical-power boundary trace methods are not treated as new. The accessible prior statements do not establish this cutoff law; the older full-text gap remains explicit.

## value

PASS

The natural degree filtration turns an infinite Hilbert–Schmidt energy into exact finite quantities. Their sharp leading coefficient is shared by standard Bergman, sphere and singular full-radius radial measures, while their finite values retain measure dependence. This determines a quantitative invariant that is not answered by qualitative Schatten nonmembership, with a precise benchmark and a clear divergent-energy regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
