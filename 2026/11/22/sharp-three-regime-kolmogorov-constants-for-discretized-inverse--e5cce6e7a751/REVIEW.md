# Independent mathematical audit

## correctness

PASS

For fixed positive α,β the incomplete-gamma integral gives the stated smooth tail expansion and linear and quadratic terms of n log F(a_n x). To check uniformity, on a_n x≥y₀ choose the survival S≤1/2 and comparable to (a_n x)^(-α). The error in replacing n log F by −x^(−α) is bounded by a constant times a_n^(-1)x^(−α−1)+n^(-1)x^(−2α), from |nS−x^(−α)| and the nS² bound for the log remainder. Both logs are bounded above by −C x^(−α). After exponentiation, scaling by n for α<1 or a_n for α>1 leaves polynomial-in-x envelopes times exp(−C x^(−α)), vanishing at both ends. The derivative formula likewise gives a uniform bound by C' x^(−α−1)exp(−C x^(−α)) plus the compact convergence. On a_n x<y₀, H_n and its derivative are exponentially small (even with polynomial n factors) by F(y₀)<1, and the Fréchet CDF and derivative have the same required negligible tails. This validates the uniform expansions. The exact floor shift is d_n/a_n with 0<d_n≤1. Integrating the uniform derivative convergence gives the uniform first-order shift, and lattice points approaching the derivative maximum attain d_n=1. Below shape one, this is smaller than 1/n and maximizing (1/2)u²e^(−u) gives 2e^(−2). At shape one the smooth parent maximum is exactly Fréchet, but the floor still contributes 4e^(−2)/β at scale n. Above one, the smooth term equals β/(α+1) times the derivative term, so the two positive errors add at d_n=1, giving exactly the stated constant. At x<0 both CDFs are zero; x=0 has probability F(1)^n and is negligible. check.py was inspected, not executed: its scan samples lattice cells and truncates the range and hence does not certify the global supremum.

## originality

PASS

Pass for the combined sharp global floor-law classification under the specified first-order scaling, including lattice attainment and the shape-one change in the leading mechanism. Neither the floor inverse-gamma model, the first-order domain of attraction, nor the general expansion of a smooth maximum is claimed as new. The closest inspected floor inverse-gamma example addresses exceedances, and the prior continuous rate literature remains an explicit access limitation.

## value

PASS

The sharp uniform constants quantify when discrete observations matter for the error in a Fréchet approximation to maxima. The classification separates an ordinary finite-sample exponent correction, an exact continuous cancellation leaving a pure lattice error, and an additive smooth-plus-lattice regime. This is an all-threshold conclusion that a tail fit or a compact pointwise expansion would not give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
