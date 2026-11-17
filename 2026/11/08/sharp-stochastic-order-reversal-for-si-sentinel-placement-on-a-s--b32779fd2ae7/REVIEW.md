# Independent mathematical audit

## correctness

PASS

For uniform initial infected seed on the directed-rate star and k perfect monitors, leaf symmetry leaves exactly layouts H (hub monitored, k−1 leaves) or L (k leaves, hub unmonitored). H has atom k/(m+1) at 0 and Exp(α) with weight (m−k+1)/(m+1). L has same atom and Exp(kβ) with weight 1/(m+1), or independent Exp(α)+Exp(kβ) with weight (m−k)/(m+1). Survival difference equals [(m−k+1)α−kβ]/(m+1) times strictly positive convolution ∫_0^t e^{−αu}e^{−kβ(t−u)}du for every t>0, including equal-rate limit. This gives exact stochastic ordering, full-law ties at kβ=(m−k+1)α, and budget boundary k_c=(m+1)α/(α+β). Direct independent symbolic calculation confirms Laplace difference s[kβ−(m−k+1)α]/[(m+1)(s+α)(s+kβ)] under the correct sign convention. The proof covers all m≥1,1≤k≤m,α,β>0; finite CTMC checks only corroborate.

## originality

PASS

The exact two-class all-time stochastic-order phase diagram for continuous-time directed SI on a star, including equality of entire detection-time laws at the sharp budget, is not stated in the primary surveillance works inspected. Leskovec et al give general expected-detection reward and submodular placement, Ciccolini et al optimize expected detection on hospital movement networks by heuristics, and Colman et al simulate SIR sentinel strategies. Related SCOPE cycle and path sentinel results use different topology and/or objective. The result is a best-of-knowledge original exact solvable boundary.

## value

PASS

The highest-degree star hub need not be stochastically optimal for monitoring when many vertices can be observed. The precise budget-driven rank reversal and whole-law tie form a meaningful, fully classified stochastic-order result, strengthening mean-only design criteria for a natural exactly solvable epidemic-network benchmark. It does not purport to recommend clinical allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
