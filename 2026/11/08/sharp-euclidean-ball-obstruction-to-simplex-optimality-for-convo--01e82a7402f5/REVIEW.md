# Review of the Euclidean-ball versus simplex convolution cutoff

## Correctness

PASS. The exact normalized lens mass is the regularized incomplete beta function with parameters \(((n+1)/2,1/2)\). Spherical symmetry makes the normalized volume ratio of the ball convolution body exactly its half-radius \(r\). The established simplex convolution formula gives \(c_n(1-s)\), so the comparison reduces to one scalar equation. Brunn--Minkowski concavity of the root lens volume is strict because different-separation lenses are not homothetic. The monotonic secant slope and the explicit endpoint bounds prove existence, uniqueness and the sign of the comparison. The published cutoff is strictly inside the ball-beating interval by strict lens containment. Uniform endpoint Laplace asymptotics, Stirling, and a nonvanishing derivative at \(4/5\) prove the stated logarithmic corrections and exact asymptotic constant. Supplementary numerical tests passed; their finite scope is not used as proof.

## Originality

PASS on the examined record, with historical priority provisional. Martín Goñi (arXiv:2610.37066, Section 4.2) proves an elementary ball obstruction at \(s\le(c_n^2-1)/(c_n^2+1)\) and records only the limit \(3/5\) for that upper obstruction. It does not compute the actual ball-versus-simplex crossing, show its uniqueness, or give the sharp polynomial correction. The checked 2023/2024 article of Alonso-Gutiérrez and Martín Goñi and the earlier Alonso-Gutiérrez--Jiménez--Villa preprint establish the convolution-body framework and simplex equality region but not this exact ball comparison. Exact lens integrals are standard known inputs, not claimed discoveries. Public mathematical-record searches disclosed related lens volume, two-ball covering, and simplex distance results without implication of the claimed crossing. Older work on volume distributions of symmetric convolution bodies remains a named priority risk.

## Mathematical value

PASS. The unknown changeover from simplex-optimal to non-simplex behavior in the sharp \(\theta\)-convolution Brunn--Minkowski constant is an explicit motivating gap. The exact two-family threshold provides a rigorously improved *upper exclusion* of simplex optimality, valid in every dimension, not merely an isolated numerical example. For \(n=2\), the threshold in \(s=\theta^{1/n}\) moves from the elementary \(1/5\) to approximately \(0.41078749\). The law \(\theta_n^*\sim(3/5)^n n^{-7/30}(2^{27}/(3^{18}\pi^7))^{1/30}\) quantitatively captures the finite-dimensional boundary layer missing from a leading exponential-limit statement. The construction does not locate the true universal optimality threshold and is not presented as doing so.

## Sources and residual limitations

Principal motivating source: Javier Martín Goñi, arXiv:2610.37066, submitted 2026-10-27, Theorem 1.1 and Section 4.2. Relevant predecessors: Alonso-Gutiérrez and Martín Goñi, Journal of Geometric Analysis 34:58 (2024), and Alonso-Gutiérrez, Jiménez, Villa, arXiv:1112.4757 (2011). The exact standard ball-lens formula is not new. Historical priority may change with discovery of equivalent comparisons in older symmetric convolution literature. The numerical verifier uses SciPy and finite-dimensional sampling only.

Self-review: passed. Independent audit: not yet performed.
