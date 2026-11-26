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

With generator d²/dx² the reflected kernels have direct and image terms (4πt)^−1/2 exp(−(x∓y)²/(4t)). The squared commutator norm integrates twice over E×E^c, and row-square bounds give finiteness for every finite-measure E. Subtracting the signed kernel squares gives the product of the two complementary Gaussian masses with prefactor 2/(πt), exactly q(1−q), with equality at q=1/2. Dilation followed by integration of Q from 0 to 2c gives the common interval term and the cross term factors. For the Dirichlet derivative, multiplying by πexp(c²/2) gives H as in the original; H(0)=0 and H′>0. The analogous Neumann G goes from 2sqrt(π/2) to −sqrt(π/2); Q(2c)<exp(−2c²)/(2c) makes G′ strictly negative, proving the unique peak and the direction of both limiting approaches. Taylor expansion yields the cubic coefficient 1/(6sqrt(2π)) for Dirichlet and slope sqrt(2/π) for Neumann, hence the quoted ratio. Independent direct kernel quadrature at c=t=0.7 gives Neumann 0.26939730485051155 and Dirichlet 0.019655636392878425, agreeing with closed forms to about 7e−17. Independent evaluation of the peak equation gives c≈0.7990017881788918 and F_+≈0.2719729564300915. These are finite cross-checks; the derivative proof, not the grid, proves global uniqueness. The original verification file and checker were inspected, not executed.

## originality

PASS

Classical image kernels and error functions are inputs, not contributions. The exact finite-time Gaussian-mass contrast for arbitrary masks combined with a strict global classification for boundary-attached intervals is distinct from the examined heat-content, commutator and Gaussian-interface statements. Exact reduction to a reflecting heat-content term plus the signed boundary correction clarifies the closest equivalent formulation.

## value

PASS

The natural mask-commutator statistic reveals a boundary-condition effect controlled solely by one Gaussian mass despite arbitrary mask geometry. For intervals the exact turnover distinguishes reflecting from absorbing evolution beyond leading small- or large-length asymptotics. Combining that structural identity with the complete strict shape and leading boundary suppression is useful for comparison across both boundary conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
