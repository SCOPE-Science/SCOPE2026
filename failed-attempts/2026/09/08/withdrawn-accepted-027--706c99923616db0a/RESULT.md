# Exact mean demerit factor over the skew-symmetric Littlewood ensemble

## Context
Low-autocorrelation binary sequences (LABS) / Golay merit-factor optimization
habitually restricts odd lengths to the skew-symmetric subclass to halve the
search dimension. Unrestricted-ensemble demerit moments are known
(Katz–Ramirez), and heuristic work shows the skew restriction can be strictly
suboptimal at large odd lengths (Zhang et al.: 99, 107, 109, 113, 119) without
giving any distributional explanation. No prior source gives the
skew-conditional mean/variance.

## Definitions
Let n = 2m − 1 be odd (m ≥ 2), indices 0..n−1, center c = m−1.
s ∈ {+1,−1}^n is skew-symmetric if s_{c+t} = (−1)^t s_{c−t} for t = 1..m−1.
The uniform skew ensemble (size 2^m) takes free variables x_0..x_{m−1} i.i.d.
Rademacher. Aperiodic autocorrelations, energy, demerit factor:
C_k = Σ_{j=0}^{n−k−1} s_j s_{j+k}, E = Σ_{k=1}^{n−1} C_k^2, D = E/n^2.
Unrestricted uniform mean: M_unrest(n) = (n−1)/(2n).

## Result
Theorem (proved, all odd n = 2m−1):
(a) C_k ≡ 0 pointwise for every odd k.
(b) E[C_k^2] = 2(n−k) − 1 for every even k.
(c) Mean energy E[E] = (m−1)(2m−3); mean demerit
    M_skew(n) = (m−1)(2m−3)/(2m−1)^2.
(d) Strict bias vs unrestricted mean at same n:
    M_skew(n) − M_unrest(n) = −2(m−1)/n^2 < 0 (m > 1);
    the skew restriction lowers expected demerit.

Verified table (exact exhaustive skew-subspace enumeration, no closed form claimed):

| n | m | E[E] | Var(E) | Var(D) |
|---|---|---|---|---|
| 3 | 2 | 1 | 0 | 0 |
| 5 | 3 | 6 | 16 | 16/625 |
| 7 | 4 | 15 | 144 | 144/2401 |
| 9 | 5 | 28 | 480 | 160/2187 |
| 11 | 6 | 45 | 1248 | 1248/14641 |
| 13 | 7 | 66 | 2544 | 2544/28561 |
| 15 | 8 | 91 | 4464 | 496/5625 |
| 17 | 9 | 120 | 7232 | 7232/83521 |
| 19 | 10 | 153 | 10816 | 10816/130321 |
| 21 | 11 | 190 | 15696 | 1744/21609 |

Var(E) fits no low-degree polynomial in m (degrees 4–6 tested, all fail), so
only the table is claimed.

## Proof / evidence
Reversal g(i) = n−1−i; T_j = s_j s_{j+k}, j′ = (N−1)−j, N = n−k.
Skew symmetry gives T_{j′} = (−1)^k T_j. For odd k, N is even, the involution
is fixed-point-free, summands cancel in pairs: C_k ≡ 0.
For even k, T_j = T_{j′} pointwise. With fold map r(i) = c−|i−c| and signs
σ_i, E[T_j T_l] ≠ 0 requires even fiber multiplicity; diagonal gives N ones,
mirror pairs l = j′ ≠ j give N−1 ones (N odd, one fixed point
j* = (N−1)/2 with constant summand ±1 since j*+k = g(j*)), all other ordered
pairs give 0 (fiber-pair uniqueness; confirmed by exact pairwise-expectation
matrices = identity plus anti-identity for every even k). Hence
E[C_k^2] = 2N−1. Summing over even lags gives (m−1)(2m−3); gap algebra gives
−2(m−1)/n^2. Exhaustive exact-rational replay over all 2^m skew sequences for
m = 2..11 (4092 sequences) confirms odd-lag vanishing, even-lag second
moments, mean energies, gap, and the variance table.

## Limitations
Variance is a verified finite table for n ≤ 21 only; no closed-form variance
is claimed. Proof covers the mean only; higher skew moments are open.
Mean-bias direction does not imply extremal (optimum) ordering and coexists
with Zhang et al.'s finding that unrestricted optima beat optimal skew optima
at 99, 107, 109, 113, 119.

## Reproducibility
Stdlib only: `python3 output/artifacts/verify_skew_moments.py` (seconds;
Fraction arithmetic, exact integer autocorrelations). Exits ALL CHECKS PASSED.

## References
- D. J. Katz, M. E. Ramirez, Moments of Autocorrelation Demerit Factors of Binary Sequences, arXiv:2307.14281.
- D. J. Katz, M. E. Ramirez, Limiting Moments of Autocorrelation Demerit Factors of Binary Sequences, arXiv:2307.14566.
- Z. Zhang et al., New Improvements in Solving Large LABS Instances Using Massively Parallelizable Memetic Tabu Search, arXiv:2504.00987.
- B. Bošković et al., Low-Autocorrelation Binary Sequences: On Improved Merit Factors and Runtime Predictions, arXiv:1406.5301.
- OEIS A102780, Ground states of the Bernasconi model (optimum table, not moments).
