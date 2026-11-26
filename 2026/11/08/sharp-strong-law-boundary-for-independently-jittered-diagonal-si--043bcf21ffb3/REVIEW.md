# Independent mathematical audit

## correctness

PASS

An independent truncation check verifies the full threshold, including equality. For each fixed level c>0, summing cell probabilities of an entry greater than c n² gives exactly A_n=n² μ{f>c n²}, by equal cell areas. Since f is integrable, A_n tends to zero; by within-row independence the probability of such an entry is asymptotic to A_n when it is positive. By interchanging nonnegative sums and integrals, Σ_n A_n is finite exactly when E f^(3/2) is finite, since Σ_{n<sqrt(f/c)} n² grows as f^(3/2). Truncate entries at c n² by discarding larger ones: the normalized row variance is at most n^(−2)∫f² 1_{f≤c n²}, summable under the same moment condition by summing n^(−2) over n≥sqrt(f/c). Truncated expectations approach I. A union bound, Chebyshev and first Borel–Cantelli give convergence in the finite-moment regime. Otherwise fresh-row independence and second Borel–Cantelli at each positive integer level give limsup infinity. For any fixed bounded truncation the n^(−2) variance bound gives almost-sure convergence to its integral; monotone approximation from below yields liminf≥I. Fixed bounded truncation and the integrable tail also give convergence in probability, hence an almost-sure convergent subsequence and liminf=I. Finally the gap density is 2(1−t); the moment integral has t-power −3α/2 and log-power −3β/2, giving strict β>2/3 at α=2/3. This agrees with the frozen band, truncated critical moment, and one-entry divergence estimates. The almost-sure conclusions are for each fixed pair, not a uniform parameter limit; the converse uses the fresh redraw assumption. The inspected checker.py gives finite diagnostics, not a proof, and was not executed.

## originality

PASS

The supported distinction is the sharp boundary and both almost-sure limits for this fresh one-point-per-square sequence. Standard stratified-sampling truncation makes the rate of row cardinalities central: a new diagonal-specific probability inequality is not required. The inspected comparison statements do not cover the exact n²-row moment boundary, its endpoint, and the infinite excursions together.

## value

PASS

For an integrable singularity on a natural grid, unbiasedness and convergence in probability hide a sharp almost-sure failure even at the pure critical power and logarithmic equality. The threshold distinguishes algorithms that converge on almost every full sequence of fresh grids from those that produce unbounded sporadic estimates. The exact lower limit additionally shows that these excursions do not reflect a persistent upward shift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
