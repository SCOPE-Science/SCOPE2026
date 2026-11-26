---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Radial orthogonality and angular Parseval give the monomial basis and exact diagonal squared entries M_n(a+ε)/M_n(a). Tilting by r² shifts mass to the right, so its covariance with the strictly decreasing ratio symbol is negative and the entries strictly decrease in n. For a rigorous independent check of the asymptotic input, let f_n(u)=−n^(−δ)log M_n(u) for n≥1, set v=1−r=n^(−1/(β+1))w, and bound the phase from below by n^δ(2w+u w^(−β)) using −log(1−v)≥v. The minimum is F(u)=(β+1)(2/β)^δ u^(1/(β+1)); a matching integral lower bound follows on a fixed small w-interval about its positive minimizer, where the scaled phase converges uniformly and the interval's prefactor is only polynomial in n. Thus f_n→F pointwise on u>0. Each f_n is concave (its second derivative is minus a nonnegative variance times n^(−δ)). Fixed neighboring secants squeeze its derivative to F' at each u, uniformly on compact subintervals because the derivatives are nonincreasing and F' is continuous. This verifies the uniform expectation lemma, including control of the singular observable at the boundary, without differentiating an unexplained error term. Equivalently the secant between a and a+ε lies between the secants over [a,a+h] and [a−h,a] for each fixed h>ε. These converge to the respective F-secants, giving F'(a)/2=2^(δ−1)(aβ)^(−δ), and also a positive lower bound uniform for n large and ε small. At each fixed ε>0, the pointwise leading log-moment difference is positive, proving compactness and all positive Schatten memberships. For the joint limit, integrate the step function with degree floor(t ε^(−1/δ)); its tail is bounded by exp(−K p(t/2)^δ) for t sufficiently large and ε sufficiently small. The finite initial terms contribute zero in the limit, and the gamma substitution gives the stated constant for all real p>0. At a=2, β=1, p=2, the limiting integral is ∫exp(−√t)dt=2. These checks are analytic; no uploaded code was used.

## originality

FAIL

The continuous crossover is a direct consequence of the already published moment asymptotic in Bourass–El-Fallah–Marrhich–Naqos §8, by near-boundary comparison and concavity of the normalized negative log moment. This is coverage by implication, not an assertion that the old paper states the embedding theorem verbatim. In this radial setting it does not require a new uniform saddle or a new spectral asymptotic. The decision does not rely on the inaccessible body of a related indexed fixed-weight embedding record.

## value

FAIL

The effective-rank question is natural and the formula is useful as an expository observation. As a standalone exact finding, however, the claimed quantitative advance is determined by an existing leading all-rate moment asymptotic and elementary monotone secant and summation arguments. The record does not claim a further independently useful invariant such as a second-order or rate estimate beyond that implication. No unproved extension is offered as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
