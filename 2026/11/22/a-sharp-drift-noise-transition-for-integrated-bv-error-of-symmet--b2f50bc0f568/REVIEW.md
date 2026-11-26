# Independent mathematical audit

## correctness

PASS

For trace-normalized right-continuous real BV, the signed derivative represents f as a constant plus an integral of unit upward steps, including the values at all sampled knots. Constants are preserved. The triangle inequality and Fubini bound the operator ratio by the supremum of single-step errors, and testing single steps supplies the reverse inequality. With first sampled index k at or above the jump, its response is the CDF of the kth uniform order statistic; integration on the two sides of the step gives E|U_k-s|. Since this is convex in s for fixed k, the supremum is among the stated one-sided nodal candidates and the point-mass outer-cell candidates; when b=0, the formal zero-width outer candidates have error zero and do not alter the maximum. For indices j/n→u in (0,1), represent the Beta order statistic as the ratio of its independent gamma block to the sum of both gamma blocks. The two central limit theorems and the ratio derivative give variance u(1-u) after scaling by sqrt(n). At u=0 or 1 the scaled variance tends to zero, including deterministic end laws. The centered mean shift tends to b(u-1/2), and the uniform second-moment bound gives convergence of the absolute-deviation means. Compactness then reduces the norm to maximizing this folded-normal profile. With t=|2u-1| and a=bt/sqrt(1-t²), differentiation yields b(2Phi(a)-1)-2phi(a)t/sqrt(1-t²); dividing by 2a phi(a)/b yields b²R(a)-1 with strictly increasing R from 1 to infinity. Thus any interior critical point is a minimum, and the endpoint objective values are sqrt(2/pi) and b before division by two. This gives the asserted branches and equality case. A minor wording error in the final localization sentence is that the inter-knot mesh 1/(n+beta_n) is not a bound on an outer cell. Within an inter-knot cell the error is 1-Lipschitz, so that mesh controls the scaled error by o(1); within a left or right outer cell the error is exactly s or 1-s, bounded by beta_n/[2(n+beta_n)], and the locations approach the appropriate boundary. In particular those cells cannot be norming when b<sqrt(2/pi); this completes the stated localization without changing the theorem. Inspected check.py and VERIFICATION.md; did not run the frozen checker. The checker docstring's alternate filename does not affect the documented replay via check.py.

## originality

PASS

The strongest explicit indexed overlap is an exact Beta-deviation norm and midpoint localization for classical Bernstein, already covering b=0. Its date is the same as the frozen record and does not establish relative priority. The Stancu sampling operator and its moment/parameter sensitivity are also established. The surviving claim is the sharp norm competition in the nonzero symmetric square-root-displacement regime, including the exact critical coefficient and the boundary versus midpoint location dichotomy. The closest distinct literature and exact catalogue formula do not supply this determination. The prior BV Stancu source was not independently accessible, so the priority judgment is qualified.

## value

PASS

The discontinuous-input sharp norm measures the worst integrated bias from a standard sampling approximation. Inward grid shift and binomial spreading contribute at the same scale, but the worst discontinuity switches sharply from midpoint below the exact threshold to boundary above it, with no other limits allowed at equality. That competition and the calibrated leading constant are useful for choosing or assessing a symmetric grid, unlike simply reusing the zero-displacement norm. The theorem does not claim finite-degree equality classification, other parameter scalings, or nonsymmetric extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
