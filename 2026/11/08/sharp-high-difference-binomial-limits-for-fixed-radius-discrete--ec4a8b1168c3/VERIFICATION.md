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

For a real even radius-n symbol, y=(1-cos θ)/2 gives all degree-at-most-n polynomials r with r(0)=1; Fourier positivity is exactly r≥0 on [0,1]. Plancherel gives 2^k times the weighted y^{k/2} norm. Setting K=k/2 and Q(z)=K^n r(1-z/K) yields the endpoint constraint Q(K)=K^n. Vandermonde evaluation at fixed distinct bounded z controls every coefficient of every minimizer: the weights at those points stay positive, and a rescaled monic limiting competitor gives a uniform upper bound using (1-z/K)^K≤e^(-z). The endpoint constraint forces limiting monicity, pointwise evaluation gives the lower bound, and positivity persists on every bounded interval. Alternation on the half-line is legitimate: the nonzero norm contact set is compact, and if there are at most n ordered sign groups one can subtract a small polynomial of degree ≤n-1 with a root in each sign gap; the exponentially decaying tail stays strictly below the norm. Uniqueness follows by applying alternation to the midpoint of two minimizers, which forces agreement at n+1 contacts. Hence the signed minimizer changes sign and the attained positive minimum is strictly larger. The leading coefficient tends to 1 and all lower rescaled terms vanish in r, giving (1-y)^n and the centered binomial. The uniform bound C(1+z)^n e^(-z) excludes all distant maximizing points, yielding the stated Nyquist scale. For n=2 the weighted derivative has just the two roots t,t+d; matching the three signed contacts gives the stated uniquely solvable equations. In the positive class every monic quadratic with intercept b≥0 dominates (z-√b)^2 on the half-line; minimizing the maximum of its endpoint and right hump gives the Lambert-W value. The extraneous remark about an additional critical point for s>2 is not needed: the endpoint alone excludes s>2. Independent bisection gives d=2.399357280515468, t=0.610348711840214, c₂=0.2169154712561674, c₂⁺=0.3101700063005356 and ratio 1.429911866149182. The frozen checker was inspected, not executed; finite grids are not evidence for the infinite-order limits.

## originality

PASS

The supported distinct contribution is the fixed-radius n≥2 high-difference limit with its limiting-kernel and worst-frequency statements and the unrestricted radius-two evaluation. The signed finite-order variational formulation, alternation tools, and positive radius-two constant via squaring are not independent novelty claims. No inspected prior statement covered the supported fixed-radius limit or supplied the unrestricted radius-two value.

## value

PASS

This resolves a natural regime of the discrete smoothing minimax problem left out by finite low-order formulas. The minimizers in two genuinely distinct classes share a binomial kernel limit, yet their normalized worst-case errors have a strict gap; a kernel limit alone consequently misses the sharp smoothing loss. The rescaled invariant and frequency window explain this and the signed five-tap evaluation makes the gap concrete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
