# Independent mathematical audit

## correctness

PASS

The killed process is reset to empty at every hub fire, and independent future Poisson increments give iid cycles. The finite chain is irreducible: an occupied hub can clear the system, and from empty any configuration is reachable by a chosen finite sequence of births before strikes. Conditional on hub growth at h, the pre-hub birth/death chain has leaf occupation p_h=(1−e^{−(1+λ)h})/(1+λ). For a post-hub leaf, vacancy weighted by survival is (1−p_h)e^{−u}; surviving occupation is p_h e^{−λu}+(1−p_h)∫₀ᵘe^{−s−λ(u−s)}ds. The latter integral is (V−U)/(1−λ) and is u e^{−u} at λ=1. These weights and the independent hub survival e^{−λu} factorize before the marked kill; multiply the k coefficient by λ(k+1), then integrate in h and u. Both monomial denominators and the algebraic expression for B follow, including continuity at one by domination for λ in a compact positive interval around one using hub survival. Hub lightning ensures total probability one; every k is attainable with positive probability. Independent finite cross-check by first-event conditioning: n=1 gives P(F=1)=λ/(λ+2). For n=2, λ=1, the hub-growth occupancy probabilities are (7/15,2/5,2/15); post-growth birth/kill total rate is 3 in each count state. This gives P(F=1,2,3) as the vector (7/45,64/135,10/27). The supplied checker was inspected, not run; it omits λ=1 and checks finite formula versus generator only. For λ_n=c/n, deleted pre-hub leaf lightning marks up to t have expected count ≤ct, which bounds the discrepancy in leaf fraction from independent growth paths by a quantity tending to zero in probability, uniformly over a compact interval. The empirical CDF of independent Exp(1) birth times converges uniformly. An independent Exp(1) threshold for integrated terminal hazard gives time convergence on compacts since the limiting hazard is strictly increasing after h and diverges; tightness and uniform leaf control give joint convergence, also using the left-limit count just before the fire. Averaging the conditional survival gives S_c, and differentiation cancels the boundary term against the derivative of e^{−t}; the changes y=1−e^{−t}, s=e^{−h} give the displayed density. For stationarity the worst initially vacant leaf survival is (e^{−λu}−λe^{−u})/(1−λ) when λ≤1/2. The uniform conditional product bound e^{2c−cu} holds for all h; it can be integrated against e^{−h}, without assuming the actual post-growth wait independent of H₀. Splitting at H₀=t/2 directly gives an integrable bound e^{−t/2}+e^{2c−ct/2} for the full cycle survival. Dominated convergence in the renewal-reward numerator and denominator yields the stationary age mixture and its fraction. Exchangeability plus bounded first two moments gives the covariance; positivity follows from nondegenerate age. At small c, post-growth hazard ≤c gives M_c≥1/c and P(A_c≤a)≤a/M_c→0. At large c the post-growth wait tends to 0 for each h>0 and S_c≤S_1 for c≥1, giving age Exp(1) and uniform fire and stationary fractions. Their stated endpoint variance follows by bounded moments.

## originality

PASS

The elementary regenerative principle and conditional-mixture covariance are established tools, not new results. The surviving claim is a model-specific all-size hub-fire distribution, critical state-gated hazard and explicit law, and its stationary correlation limit. The closest actually checked model families and statements do not prescribe that growing-degree star law.

## value

PASS

The hub naturally selects fires that reset the entire labelled star, making regenerative cycles observable. The c/n scale keeps the total leaf ignition rate competitive with regrowth. The result gives a usable all-size marked law, a nondegenerate critical size density, and a mechanism and magnitude for persistent pair correlation despite diverging leaf count, distinguishing event-time from stationary sampling. These are quantitative benchmarks rather than mere stationarity or a finite generator computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
