# Review of second-order recoding fluctuations

## Correctness
PASS. The exact conditional parity mean is \((1-2p_n)^{\binom{S_n}{d}}\). A uniform binomial/log expansion gives its \(L^2\) linearization in the walk position with remainder norm \(O(n^{-1})\). The history statistic has independent-increment harmonic weights and a two-dimensional Lindeberg limit with exact covariance \(\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\). Conditional independence of coefficient rows gives a conditionally Gaussian centered noise component whose characteristic functions converge to a constant, proving asymptotic independence from the history term. The combined CLT and the moments follow with an \(L^2\)-negligible remainder. The quenched first-order Brownian claim follows from the conditional strong law and bounded martingale jumps. Finite exact checks supplement this proof.

## Originality
PASS with historical-priority limits. Hamza--Tournier (arXiv:2610.01658v1) include a general row-independent coefficient setting (Proposition 10) and first-order Brownian criteria, so a bare first-order sparse-degree correlation would not suffice as a new contribution. The final claim instead concerns the \(\sqrt N\) fluctuations of the empirical predictable cross-covariation: their Gaussian law, variance inflation from shared increment history and the degree dependence that persists even when the first-order Brownian correlation is held fixed. The 2020 foundational Brownian criteria do not evaluate this second-order law. Accessible prior claim 962714ec-bc50-4276-a0a6-593cf8a62647 uses a time-invariant cardinality-grouped fair environment with a different fluctuation scale. Targeted searches identified no direct second-order covering result.

## Value
PASS. First-order invariance principles can identify two randomizations as asymptotically equivalent even when their internal mechanisms differ. This result supplies a mathematically natural diagnostic—the empirical cross-covariation of the two walks—whose fluctuations distinguish any two positive degrees at the same limiting Brownian correlation. The explicit additional variance \(2d^2\rho^2(\log\rho)^2\) quantifies the cost of persistent dependence on the shared increment history, rather than giving a routine reparameterization of the first-order CLT.

## Limitations
The second-order law is annealed and assumes independent coefficient rows and a fixed degree; it does not assert quenched second-order behavior. A very broad unlocated historical theorem could imply this special Gaussian decomposition, so independent priority review remains necessary.

Self-review: passed. Independent audit: not yet performed.
