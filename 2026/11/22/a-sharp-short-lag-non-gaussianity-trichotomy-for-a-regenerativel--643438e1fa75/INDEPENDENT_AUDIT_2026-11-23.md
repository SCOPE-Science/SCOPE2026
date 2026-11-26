# Independent mathematical audit

## correctness

PASS

Physical cycles have positive mean duration d/(a+b); occupation weighting by d exp(−by) gives stationary age Exp(a+b). Stationarity yields EU_t=(a+b)t/(ad) and exact linear MSD. Conditional on initial age, lack of reset for u operational units has probability exp(−au), independently of that age. The physical clock consumed is (d/b)exp(−bY₀)(1−exp(−bu)), producing the stated truncated-power survival for H_t. After the first reset any age is ≤−log(1−η)/b for η<1; this bounds U_t−H_t by t/[d(1−η)] and the second-moment error by O(t²). The exponential tail gives finite second moments at short positive lags, then stationarity and Cauchy–Schwarz give finiteness at every fixed lag. For γ<1, changing to x=exp(−bu) and integrating −log(x) against d[(x/(1−x))^γ]/γ gives B(γ,1−γ)/(γb²); both boundary terms vanish. At γ=1 the tail integrand after removing 2η² is (1/b²u)+O(1) at small u; the lower cutoff is −log(1−η)/b and the below-cutoff integral is O(η²). For γ>1, stationarity, stochastic continuity and uniform integrability of the speed squares yield L² convergence of U_t/t to V₀ with second moment (a+b)/[d²(a−b)]. The exact conditional Gaussian fourth-moment identity supplies all three stated excess-kurtosis constants. The raw fourth moment, unlike normalized kurtosis, stays finite and tends to zero at short lag. The supplied VERIFICATION.md and checker.py were inspected, not executed.

## originality

PASS

Pass for the stationary accelerated-clock short-lag trichotomy and exact constants, not for Brownian subordination, Gaussian-mixture moments, or geometric acceleration by themselves. The checked antecedents use different clock dynamics, a finite-speed-moment superstatistics example, or different kurtosis observables and time regimes.

## value

PASS

An exactly linear MSD here coexists with divergent excess kurtosis even though each finite positive lag has a finite fourth moment. The sharp transition and the model-specific first-reset cutoff explain why the naive instantaneous-speed mixture fails and quantify the short-lag signal in all regimes. The power, logarithm and finite plateau are substantive, not just the standard statement that mixed Gaussian variances can be non-Gaussian.

The dated certificate retains the supplied scientific assessment, sources and limitations.
