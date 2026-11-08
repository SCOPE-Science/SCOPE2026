# A rare-switching staircase and logarithmic transition windows in analytic correlations of random expanding circle maps

## Finding

For integers \(2\le a<b\), set \(\rho=b/a>1\), choose any \(s>0\), and write
\[
T_d(x)=dx\pmod 1,\qquad f_s(x)=2\sum_{m\ge1}e^{-sm}\cos(2\pi m x),\qquad d\in\{a,b\}.
\]
For each integer \(n\ge1\), independently choose the slower map \(T_a\) with probability \(p_n\in(0,1)\), and \(T_b\) with probability \(1-p_n\), for exactly \(n\) steps, beginning with Lebesgue-uniform \(X_0\). Let \(C_n\) be the **annealed** stationary lag-\(n\) covariance of \(f_s\), averaged over both \(X_0\) and the map selections. The exact finite-time formula is
\[
C_n=2e^{-s}\sum_{k=0}^{n}\binom nk p_n^{n-k}(1-p_n)^k
\frac{e^{-s a^n\rho^k}}{1-e^{-s(1+a^n\rho^k)}}.
\tag{1}
\]

Consider the rare-switching scaling \(p_n=e^{-\tau a^n}\) for fixed \(\tau>0\), and define
\[
F_\tau(k)=s\rho^k-\tau k\quad(k=0,1,2,\ldots),
\qquad \tau_j=s(\rho-1)\rho^j\quad(j=0,1,2,\ldots).
\]
The following infinite **dominant-itinerary staircase** is exact asymptotically:

* If \(0<\tau<\tau_0\), the dominant number of faster-map selections is \(k_*=0\). If \(\tau_{j-1}<\tau<\tau_j\), for \(j\ge1\), it is \(k_*=j\).
* At the threshold \(\tau=\tau_j\), the exponential costs for \(j\) and \(j+1\) selections coincide, but the binomial multiplicity selects \(k_*=j+1\).

In both cases, with the specified \(k_*\),
\[
\boxed{\displaystyle C_n\sim 2e^{-s}\binom n{k_*}
\exp\bigl(-a^n[\tau n+F_\tau(k_*)]\bigr).}\tag{2}
\]

The actual finite-\(n\) competition occurs in a shifted window, rather than exactly at \(\tau_j\). For any fixed \(j\ge0\) and real \(\xi\), put
\[
\tau_n=\tau_j-\frac{\log n-\xi}{a^n},\qquad p_n=e^{-\tau_n a^n}
\]
(for all sufficiently large \(n\) so that \(\tau_n>0\)). Then
\[
\boxed{\displaystyle
\frac{C_n}{2e^{-s}\binom nj\exp\{-a^n[\tau_n n+F_{\tau_n}(j)]\}}
\longrightarrow 1+\frac{e^{\xi}}{j+1}.}\tag{3}
\]
Thus a universal logarithmic finite-time shift and an explicit two-itinerary crossover occur at every threshold of the staircase. In particular, the dominant number of rare *fast* selections takes every nonnegative integer as \(\tau\) increases, despite each individual fast selection being typical and each slow selection having probability exponentially small in \(a^n\).

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/\mathbb Z\), equipped with normalized Lebesgue measure \(m\). Every integer map \(T_d\) preserves \(m\); therefore the one-time marginals are stationary within each fixed-\(n\) experiment. The observable \(f_s\) is real analytic and centered, equal to the usual Poisson-kernel boundary function minus one. The random choices are independent of each other and of \(X_0\). The probability \(p_n\) is **constant within the row of length \(n\)** but changes with the observation horizon: equations (2) and (3) are *triangular-array* asymptotics, not the correlation sequence of a single fixed transition kernel. No assumption of coprimality of \(a,b\) is necessary.

All limiting statements fix \(a,b,s\) and the displayed \(\tau\) or \(j,\xi\), and send the integer \(n\to\infty\). The phrase “dominant number of faster-map selections” denotes the unique leading term after summing all words with equal numbers of \(T_b\) uses, not a probabilistic statement that typical random words contain only finitely many faster maps. All covariance values here are positive.

## Proof

**1. Exact Fourier correlation.** Absolute and uniform convergence of the Poisson series gives
\[
f_s(x)=\sum_{m\in\mathbb Z\setminus\{0\}}e^{-s|m|}e^{2\pi i m x},
\qquad \int_\mathbb T f_s\,dm=0.
\]
For a fixed word containing \(k\) copies of \(T_b\) and \(n-k\) copies of \(T_a\), the composition is multiplication by \(M=a^{n-k}b^k=a^n\rho^k\) modulo one. Orthogonality of characters shows exactly
\[
\int_\mathbb T f_s(x)f_s(Mx)\,dm(x)
=\sum_{h\in\mathbb Z\setminus\{0\}}e^{-s(|h|+M|h|)}
=\frac{2e^{-s(M+1)}}{1-e^{-s(M+1)}}.
\]
There are \(\binom nk\) such words, each with probability \(p_n^{n-k}(1-p_n)^k\). This proves (1), including all finite \(n\) and every \(0<p_n<1\).

**2. A uniform harmonic remainder.** Write \(L=a^n\) and \(q_n=1-p_n\). Since every word multiplier satisfies \(M\ge L\),
\[
\frac{1}{1-e^{-s(1+M)}}=1+O_s(e^{-sL})
\]
uniformly in \(n\) and the word. All summands are positive, so this is a *relative* error estimate for the complete sum. If \(p_n=e^{-\tau_n L}\) with \(\tau_n>0\), equation (1) becomes
\[
C_n=2e^{-s}e^{-\tau_n nL}
\left(\sum_{k=0}^n\binom nk q_n^k e^{-L F_{\tau_n}(k)}\right)
\bigl(1+O_s(e^{-sL})\bigr).
\tag{4}
\]
No smallness assumption on the finite summands is needed beyond \(M\ge L\).

**3. Exact minimizers of the exponential cost.** Direct subtraction yields
\[
F_\tau(k+1)-F_\tau(k)=s(\rho-1)\rho^k-\tau=\tau_k-\tau.
\]
The right side increases strictly with \(k\), tending to infinity. Therefore the minimizers are precisely those listed in the finding: one minimizer outside the discrete thresholds, and the adjacent pair \(j,j+1\) at \(\tau=\tau_j\). Every non-minimizing integer has cost at least a strictly positive constant above the minimum, since the cost tends to infinity with \(k\).

**4. Fixed-scale staircase.** Fix \(\tau>0\), and let \(K\) be the one- or two-element minimizer set. For some \(d>0\), every \(k\notin K\) satisfies \(F_\tau(k)\ge\min F_\tau+d\). Hence, by the elementary binomial estimate \(\sum_{k=0}^{n}\binom nk\le 2^n\), the combined contribution outside \(K\) to the bracket in (4) is at most
\[
2^n e^{-L(\min F_\tau+d)},
\]
which is exponentially smaller than any fixed-minimizer contribution because \(L=a^n\) and \(a\ge2\). Furthermore \(q_n=1-e^{-\tau L}\to1\), so \(q_n^k\to1\) for every fixed integer \(k\). At a threshold, the ratio of the two tied leading terms is
\[
\frac{\binom n{j+1}q_n^{j+1}}{\binom nj q_n^j}
=\frac{n-j}{j+1}q_n\longrightarrow\infty.
\]
Therefore the larger integer \(j+1\) controls the prefactor, which proves (2) both on and off thresholds.

**5. Logarithmically shifted competition.** Fix \(j\ge0\), \(\xi\in\mathbb R\) and define \(\tau_n\) as in (3). The cost gap between \(j\) and \(j+1\) obeys
\[
F_{\tau_n}(j+1)-F_{\tau_n}(j)
=\tau_j-\tau_n=\frac{\log n-\xi}{L}.
\]
The exact ratio of these two summands in the bracket of (4) is
\[
\frac{n-j}{j+1}q_n\exp[-L(\tau_j-\tau_n)]
=\frac{n-j}{n(j+1)}q_n e^{\xi}
\longrightarrow\frac{e^\xi}{j+1}.
\]
For every other integer \(k\), the cost at \(\tau_j\) has a fixed positive gap from the two tied minima. As \(|\tau_n-\tau_j|=O((\log n)/L)\), its perturbation up to \(k=n\) changes the exponent by at most \(O(n\log n)\), negligible against that fixed gap multiplied by \(L\). Summing at most \(2^n\) binomial weights proves that all remaining terms have vanishing normalized contribution. In addition \(q_n^j\to1\), and the uniform relative harmonic remainder in (4) tends to zero. Dividing by the \(j\)-term normalization now proves (3).

## Verification

The included standalone `check.py` independently enumerates every map-selection word for several integer-slope pairs and rational probabilities, and matches the exact geometric Fourier covariance to its grouped binomial representation using exact Python fractions. It also evaluates the normalized asymptotic sum in log-reduced high-precision arithmetic for three transition indices, three crossover offsets and three finite horizons. These computations execute 195 checks. Run with `python3 check.py` (the exact tests require only Python's standard library; the optional high-precision comparisons require `mpmath`). The finite computations do not prove the infinite limits; Steps 2–5 do.

## Relationship to prior work

Suzuki [1] gives stationary densities and Bernoulli-parameter response formulas for random beta-transformations, including the integer-slope systems here. Those density results are credited; the present claim concerns an annealed analytic observable and a singular noise-to-zero regime, not the stationary density. Stadlbauer–Varandas–Zhang [2] treat general annealed expanding systems and exponential correlation decay, but do not specify the exact rare-selection histories. Shchetka [3] proves sharp double-exponential analytic mixing estimates for finite Blaschke-product semigroups and computes Fourier correlations of a fixed doubling map; these establish the relevant sharp-scale backdrop but not the triangular-array staircase, threshold selection or shifted window in (3).

Related published exact studies of the same integer multiplication family determine the onset of asymptotic variance for fixed noise [4], and arithmetic collapse of a finite rational grid with a Gaussian crossover near balanced switching [5]. Neither determines Poisson-kernel Lebesgue autocovariance, rare-switching cost minimizers, or the logarithmically shifted transition window. The claims here do not assert novelty for Fourier orthogonality, binomial counting, or the abstract discrete Laplace principle, only for their combined sharp correlation phase diagram in this specific dynamical regime.

## Limitations

The result concerns iid selection *within each horizon*, with the choice probability depending on that horizon. It does not describe one process with a fixed switching kernel across all \(n\), quenched correlations, noninteger slopes, arbitrary analytic observables, or a universal phase diagram without Fourier positivity. The amplitude is for the fixed Poisson-kernel observable and can change for other observables. A common general Laplace principle explains the mechanism; the evidence reviewed does not exclude an equivalent calculation in unindexed literature. The infinite asymptotics rely on the analytical bounds rather than the finite reproducibility checks.

## References

1. S. Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, first public 30 March 2023, especially Sections 2–4; *Nonlinearity* **37** (2024), 065013.
2. M. Stadlbauer, P. Varandas and X. Zhang, *Quenched and annealed equilibrium states for random Ruelle expanding maps and applications*, arXiv:2004.04763, first posted 9 April 2020, especially introduction and mixing results.
3. E. Shchetka, *Mixing for Free Semigroup Actions of Blaschke Products on the Circle*, arXiv:2608.13876, first posted 14 August 2026, Sections 1, 2 and 5 (supporting later comparison, not the eligible originating source).
4. *Distinct integer beta maps eliminate zero variance and give an exact noise-onset coefficient*, public result https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-distinct-integer-beta-maps-eliminate-zero-variance-and-give-an-e--c097279b5a2a, `RESULT.md`.
5. *Gaussian crossover of random grid collapse under coprime expanding maps*, public result https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-gaussian-crossover-of-random-grid-collapse-under-coprime-expandi--8b0f31630fa6, `RESULT.md`.
