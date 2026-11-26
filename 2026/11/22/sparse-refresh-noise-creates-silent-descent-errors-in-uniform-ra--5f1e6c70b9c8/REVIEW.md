# Independent mathematical audit

## correctness

PASS

Apply the probability integral transform to the common atomless law. With q=1−p, the centered one-coordinate projection of D is (X_1−1/2)−(X_n−1/2), since the two projections cancel at every interior score. Its variance is 1/6, and the remaining two-coordinate component has variance (n−1)/12: the total variance is (n+1)/12 by the −1/12 covariance of adjacent comparisons and independence at greater distance. Refresh multiplies degree-one and degree-two components by q and q² respectively, giving cross covariance q/6+(n−1)q²/12, equivalent to the claim, and the stated variance of Δ. A comparison flips with probability 1/3 given one replacement and 1/2 given two, yielding E H. For a sole interior replacement, conditional on a=|old−new|, the two flips are independent Bernoulli(a) and contribute opposite signed changes if both occur. E a=1/3 and E a²=1/6 give probabilities 1/2,1/6,1/6,1/6 for the stated four marks. Excluding endpoint hits and replacement pairs within distance two costs at most 2p+2np². Conditional on the remaining mask, disjoint neighborhoods give independent marks, so the ideal iid marked trials can be coupled on the good event. Each site's nonzero mark count is Bernoulli(p/2); coupling to Poisson(p/2) and uniformly coloring points costs at most (p/2)² per site, which is even below the np²/2 term used in the record. Adjusting three independent Poisson means to λ/6 costs at most |np−λ|/2, and the map to (Δ,H) preserves the bound. H=0 iff all three limiting Poisson counts vanish; summing equal positive/negative mark counts gives the Bessel term, and the event of positive double flips alone proves strict positivity. H=0 implies Δ=0 but both H=0 and Δ≠0 have positive marginal probabilities, establishing dependence. Below the critical scale use E H; above it, centered bounded one-dependent comparison changes have kth joint cumulant sum O_k(np) from connected tuples only (each tuple's moments vanish unless one of its O_k(1) relevant refreshes occurs). Since variance is of order np, standardized cumulants of fixed order ≥3 vanish and moment determinacy gives the Gaussian limit. VERIFICATION.md and CHECK.py were inspected but not executed; the reported exact n=2–4 mask/score-order checks and single-site permutations test the local moments and mark law, not the TV bound or Gaussian limit.

## originality

PASS

The supported distinct result is the explicit joint refresh law for descent-count error and comparison Hamming error, its finite total-variation estimate, and the consequent positive probability of count agreement with local change. Classical one-dependent descents, compound-Poisson approximation, and the product-noise covariance mechanism are credited as ingredients, not separately novel general results.

## value

PASS

The natural descent count can agree before and after noise even when local comparisons have changed. The joint approximation detects both single-site double flips and cancellations across sites, phenomena the limiting marginal count difference cannot distinguish. It supplies a probability for these silent changes, a finite error bound in the sparse regime, and a coherent comparison with the many-refresh Gaussian regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
