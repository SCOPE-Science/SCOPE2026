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

For distributional BV modulo constants, integrate unit-step residuals against Df; the upper bound by the best single step is attained at the level of the supremum. Integral preservation follows from the Bernstein basis integrals 1/(n+1), so the error of a jump at s equals twice the integral of its sampled response on (0,s). On cell j with u=(n+1)s−j the response is the Bernstein tail above j plus (1−u)p_{n,j}. Differentiating the basis-integral binomial tail gives (n+1) integral_0^s p_{n,j}=sum_{k>j}p_{n,k}(s)+s p_{n,j}(s). This reduces the error derivative to 2p_{n,j}(s)[j+1−(n+2)s]. As a separate check of the exact peak heights, this derivative is that of 2s(1−s)p_{n,j}(s). These primitives match at cell boundaries because successive Bernstein masses coincide there, and they vanish at 0, so this is the entire cell profile. Thus each cell's strict peak lies at (j+1)/(n+2), and every interior cell boundary is a strict minimum. At its peak the height is proportional to a_j a_(n−j), a_k=(k+1)^(k+1)/k!. The ratio a_(k+1)/a_k strictly decreases because d[(t+1)log(1+1/t)]/dt=log(1+1/t)−1/t<0. This gives the precise central parity maxima and the formulas by substitution, also C_0=1/2. Every norming derivative measure is concentrated on winning jumps; both odd-degree jumps together lead to opposite residual signs on (a,b) for coefficients of the same sign or on (0,a) for coefficients of opposite signs, so only a single nonzero jump can attain equality. Stirling at j=n/2+O(1), s=1/2+O(1/n) gives the claimed 1/sqrt(2 pi) limit. The uploaded verification notes and checker were read, not executed. Their finite tests are not used to certify all degrees or all BV inputs.

## originality

PASS

The one-step L1 asymptotic, single-step norm reduction and existence of one-jump attainment are not distinct from the inspected fixed-iterate result. The supported contribution is the exact evaluation by parity, the positions and strict cell-wise extrema, and the necessity of a single jump even when two sites are optimal. These finite statements go beyond the verified overlap. Historical exact overlap is a real residual risk, in particular Hoeffding (1971) and Grundmann (1976).

## value

PASS

The exact finite-degree budget for classical average-cell reconstruction distinguishes odd and even degrees even though their first-order constant agrees. The strict extrema on every cell pinpoint a grid effect not observable from a rate, and the no-mixture equality result determines exactly when two equally bad discontinuity locations can or cannot coexist in a worst-case input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
