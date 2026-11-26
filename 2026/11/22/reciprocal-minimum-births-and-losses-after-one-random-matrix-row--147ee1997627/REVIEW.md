# Independent mathematical audit

## correctness

PASS

Atomlessness removes ties and the probability-integral transform preserves the joint rank law, so independent mean-one exponentials may be used. A loss is the deleted row's first entry beating the surviving minimum in its column. An arrival is a surviving column minimum that also beats its other row entries and is beaten by the deleted entry in that column. Integration gives the stated means. The mixed moment counts same-column events (n/[2(3n−2)] in total) and distinct-column events. In the latter integrand the crossing entry constrained by both events is counted only once, at the larger threshold y. Changing variables to x,z−x,y−z gives factors with rates 4n−4, 2n−1, 2n−2; multiplying by n−1 row choices and n(n−1) column pairs gives n/[8(2n−1)]. The covariance identity and positivity then follow. For a rigorous marking check, select all columns with nU_j≤M using only deleted-row data, so their number is tight and the unselected surviving array is still independent. The selected minima rescaled by n are tight and have independent uniform minimizing row labels, distinct with probability tending to one. Restrict their scaled minima to a fixed bounded range temporarily. Conditional on their minima and labels, each crossing surviving entry has an exponential residual above its column minimum; the chance any crossing changes a mark is O(1/n) with the count and range bounded. Outside the selected columns the tested rows are distinct and independent, and each mark has probability exp(−(n−number selected)y/n) before crossings, tending to exp(−y). The scaled strip has the stated limiting Poisson intensity. The expected number of potential arrivals with x>M is exactly e^(−M), and the first x lies outside with that same probability, so truncation can be removed. Independent marking gives arrival intensity (1/2)e^(−2x); conditional on the first x, loss probability is e^(−x), joint loss/arrival probability (1/2)e^(−2x), and later arrivals have independent Poisson mean e^(−2x)/4. Integration with u=e^(−x) and the derivative of u exp((t−1)u²/4) give the stated joint PGF. Arrival counts are dominated by the number of columns where U_j<Y_j, a Binomial(n,1/n), giving uniform higher moments and justifying the limiting covariance, conditional means, and variance of A_n−L_n. Frozen checker read but not run.

## originality

PASS

The supported distinct claim is the dependence between lost and born reciprocal minima for a single deleted row, including its exact mixed moment and limiting joint PGF. Whole-array reciprocal-minimum laws and first moments of total counts are established comparisons, and the two elementary marginal expectation computations are not the basis for this decision. Same-day refresh results overlap in technique and one Poisson mean but concern different couplings and observables. The historical full-text limitations below are not treated as absence of prior coverage.

## value

PASS

One row deletion is a natural local perturbation of a classical mutual-nearest-choice count. Its effect is an order-one random increment with a nontrivial dependence between losses and births: assuming independence from the marginal limits gives the wrong variance and misses the conditional arrival means 11/24 versus 1/24. The exact mixed moment and dependent joint law quantify that sensitivity, which the known single-matrix distributions cannot predict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
