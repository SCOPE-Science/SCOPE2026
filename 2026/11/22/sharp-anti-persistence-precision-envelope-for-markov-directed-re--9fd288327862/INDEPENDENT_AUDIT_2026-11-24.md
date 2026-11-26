# Independent mathematical audit

## correctness

PASS

Conditioning on the entire iid sequence of bounded cycle marks freezes the completed-cycle count and leaves the stationary signs unchanged. The centered binary sign is a transition eigenfunction of eigenvalue ρ, so the conditional variance uses lag covariances (1−m²)ρ^k. The strong law for the k-dependent products R_i R_{i+k}, the renewal count limit ν(t)/t→1/b, and the deterministic bound ν(t)≤t/n₋ allow the diagonal and each off-diagonal limit, then summation by geometric domination. For the conditional mean term, Y_i=R_i−aN_i/b has zero mean and variance d, and ν(t)+1 is a bounded stopping time at each fixed t. The stopped sum has zero mean and second moment d E(ν(t)+1). Undoing the one extra increment and the renewal undershoot adds a bounded variable, hence changes the variance by at most O(√t)+O(1). This gives the asserted variance; the mean follows from the bounded marked renewal law of large numbers. Stationarity balances the two switching flows. The smaller stationary mass caps that flow, attained when the minority always leaves, yielding ρ_min=−(1−|m|)/(1+|m|) and (1+ρ_min)/(1−ρ_min)=|m|. The matrix remains irreducible and aperiodic for 0<|m|<1; monotonicity is strict for a>0, and a=0 forces zero reward. The unit-cycle example has j=1/2 and σ²=3/8, so 2/3>(√3−1)/2; this refutes only the memory-blind extrapolation. For the separate N=1 or 2 equiprobable, R=1 example the unsigned term has d=1/9 and substitution gives 29/108. RESULT.md lines 33–83 are independently supported by these checks. The supplementary verify.py was inspected, not executed.

## originality

PASS

Credit the iid marked-renewal variance and information bound, standard Markov-renewal covariance theory, and the elementary two-state occupation covariance calculation. The supported contribution is the sharp fixed-marginal precision/variance envelope with the renewal clock and arbitrary within-cycle dependence, accompanied by an explicit counterexample to using the iid marginal-reversal expression unchanged. The inspected statements do not already give this combined conclusion. This is a bounded comparison, not a priority guarantee.

## value

PASS

The iid uncertainty bound motivates a concrete question: how much variance can sign memory remove without changing the stationary sign proportions or the cycle marks? The exact attained envelope answers it despite reward-duration dependence. The deterministic witness shows a real failure of a tempting extrapolation and identifies temporal correlation, not any claimed physical entropy accounting, as the missing ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
