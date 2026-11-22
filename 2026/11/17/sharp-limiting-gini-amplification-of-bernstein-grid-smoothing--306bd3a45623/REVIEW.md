# Independent mathematical audit

## correctness

PASS

For row-stochastic B_n and complete-pair Gini seminorm, the coarea identity for arbitrary real vectors reduces relevant inequalities to binary cuts. For a probability vector q, q(S)(1-q(S)) <= qmax s(N-s)/N gives a weighted Gini comparison; pairwise Jensen with independent draws gives operator norm <= maximum column mass. Bernstein columns are unimodal: grid-point count <= n integral+sup, and basis-mode bound <=(1−1/n)^(n−1) proves every interior column mass strictly smaller than endpoint U_n. Endpoint input e0 yields R_n=U_n−(2/n)sum k(1−k/n)^n, positive >1 for n>=3 by symmetric pairing; n=1 identity and n=2 Gini=2 oscillation gives norm one. Since (1−k/n)^n<=exp(−k), dominated convergence and geometric derivative sum show e/(e−1) sharp with gap <=2e^−1/[n(1−e^−1)^2]. Fresh rational exact exhaustive binary-cut computation for n=2..7 checked 492 cuts, with Lambda3=88/81 and endpoint witness maximal on tested dimensions only. Inspected actual checker.py; no all-n finite exact norm beyond sandwich is asserted.

## originality

PASS

Heitzinger et al 2004 Theorems 2.7–2.8 prove ordinary adjacent-interval total-variation diminution and sign-variation diminution for Bernstein polynomial; it cannot imply complete-pair Gini contraction, which indeed fails here. Kozyra and Rychlik 2016/17 use Bernstein basis to bound expectations of L-statistics relative to Gini scale of random variables; this is not a deterministic grid collocation operator Gini quotient. Same-day published exact Cesaro prefix Gini norm grows logarithmically under a different stochastic matrix. Nothing inspected entails the Bernstein e/(e−1) endpoint asymptotic, though historical priority is provisional.

## value

PASS

Bernstein grid smoothing is a canonical approximation matrix. The finding precisely separates classical path-variation contraction from global all-pairs dispersion amplification in every n>=3, supplies an explicit first threshold and sharp limiting amplification constant with an O(1/n) certificate. These are natural exact stability quantities for numerical smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
