# Arithmetic Gumbel-to-Gaussian crossover for bit-limited stochastic rounding of scalar descent

## Finding
A scalar contraction implemented with a downward-truncated, bit-limited stochastic rounding operation has an exact absorbing-time law. In a natural family where the contraction decrement is one \(q\)-th of a guard-bit probability quantum, its extinction-time fluctuations converge to an average of \(q\) independent Gumbel laws when \(q\) is fixed, but become Gaussian whenever \(q\) diverges. The same finite model supplies exact mean and variance formulas.

More precisely, for integers \(n,q,r\ge1\) with \(n<q2^r\), set \(\varepsilon=(q2^r)^{-1}\). On the integer fixed-point grid, start at \(X_0=n\). At each iteration form the exact real number \(z=(1-\varepsilon)X_t\), first truncate it downward to the refined grid \(2^{-r}\mathbb Z\), and then stochastically round that result to either adjacent integer using distance-proportional probabilities, independently at each iteration. Let \(T_n=\inf\{t:X_t=0\}\). For \(1\le j\le n\), write \(c_j=\lceil j/q\rceil\). Then
\[
 \mathbb P(j\to j-1)=\frac{c_j}{2^r},\qquad
 \mathbb E T_n=2^r\sum_{j=1}^n\frac1{c_j},\qquad
 \operatorname{Var}T_n=2^{2r}\sum_{j=1}^n\frac1{c_j^2}-2^r\sum_{j=1}^n\frac1{c_j}.
\]
The complementary transition is \(j\to j\), and \(0\) is absorbing. The entire distribution is specified by
\[
 \mathbb E z^{T_n}=\prod_{j=1}^n\frac{(c_j/2^r)z}{1-(1-c_j/2^r)z},\qquad |z|\le1.
\]

For any sequence \(n\to\infty\) and \(r=r_n\) such that \(n/2^{r_n}\to0\), the following asymptotic classification holds.

1. If \(q\) is a fixed positive integer, for independent standard Gumbel random variables \(G_1,\ldots,G_q\) with distribution function \(\exp(-e^{-x})\),
\[
 \varepsilon T_n-\log n\ \xrightarrow{d}\ \frac1q\sum_{i=1}^q G_i-\log q.
\]
The limit has mean \(\gamma-\log q\) and variance \(\pi^2/(6q)\). In particular \(q=1\) gives the usual Gumbel law, whereas every fixed \(q\ge2\) gives a genuinely non-Gumbel convolution law.

2. If \(q=q_n\to\infty\), with no restriction on \(q_n/n\),
\[
 \frac{T_n-\mathbb ET_n}{\sqrt{\operatorname{Var}T_n}}\ \xrightarrow{d}\ \mathcal N(0,1).
\]
In the subregime \(q_n\ge n\), the distribution is exactly negative binomial with \(n\) successes and success probability \(2^{-r_n}\).

The theorem concerns the explicitly defined two-stage *downward truncation followed by stochastic rounding* convention; other few-bit conventions can produce different drift and limit laws.

## Assumptions and scope
The grid is a fixed-point integer lattice (a physical fixed-point unit may multiply every state). The exact intermediate contraction is computed before truncating the probability to an \(r\)-bit grid. Random rounding choices are fresh and mutually independent. There is no overflow or saturation; only the states \(0,1,\ldots,n\) are visited. The restriction \(n<q2^r\) ensures that every positive transition is a drop of at most one integer cell. For the limit results, the grid size \(n\) grows and the number \(r_n\) of available probability bits grows fast enough that \(n2^{-r_n}\to0\). The parameter \(q\) is an integer, not a generic real-valued ratio. No floating-point exponent/binade changes are modeled.

## Proof
**1. Exact transition kernel.** At state \(j\ge1\), let \(p=2^{-r}\). Since \(0<\varepsilon j<1\), the real contraction lies strictly between \(j-1\) and \(j\). Downward fine-grid truncation gives the exact identity
\[
 p\lfloor (j-\varepsilon j)/p\rfloor
 =j-p\lceil\varepsilon j/p\rceil
 =j-p\lceil j/q\rceil.
\]
Stochastic rounding from this refined-grid value to neighboring integers goes downward with probability \(p\lceil j/q\rceil=c_j/2^r\). This is positive and at most one; zero is fixed. Thus every positive state is eventually left almost surely.

**2. Exact termination law.** While the state equals \(j\), it remains there with probability \(1-p_j\) and moves to \(j-1\) with probability \(p_j=c_j/2^r\). By independence of future random bits and the strong Markov property, the successive waiting times \(W_j\) are independent geometric random variables on \(1,2,\ldots\) with parameters \(p_j\). Therefore \(T_n=\sum_{j=1}^nW_j\). The generating function, expectation and variance follow from \(\mathbb E W_j=1/p_j\) and \(\operatorname{Var}W_j=(1-p_j)/p_j^2\). If \(q\ge n\), all \(c_j=1\), proving the negative-binomial statement.

**3. Continuous exponential coupling.** Take independent unit-rate exponential variables \(E_j\), set \(\lambda_j=-\log(1-p_j)\), and realize \(W_j=\lceil E_j/\lambda_j\rceil\). The resulting waiting time is exactly geometric with parameter \(p_j\). Since \(p_j\le n2^{-r}+2^{-r}=o(1)\), the uniform estimate \(|1/\lambda_j-1/p_j|\le C\) holds for all sufficiently large \(n\). Consequently, with \(\varepsilon=(q2^r)^{-1}\),
\[
 \mathbb E\left|\varepsilon T_n-\frac1q\sum_{j=1}^n\frac{E_j}{c_j}\right|
 \le Cn\varepsilon+n\varepsilon\le C' n2^{-r}\longrightarrow0.
\]
Here the final bound is uniform in \(q\ge1\). Only this explicit coupling, rather than an unproved Gaussian approximation, is used in the fixed-\(q\) limit.

**4. Fixed \(q\): Gumbel convolution.** Write \(n=qM+s\) with \(0\le s<q\). For \(j=(m-1)q+i\), \(1\le i\le q\), the ceiling \(c_j=m\). The initial \(qM\) terms of the coupled exponential sum thus equal
\[
 \frac1q\sum_{i=1}^q\sum_{m=1}^M\frac{E_{m,i}}m,
\]
where all exponentials are independent. The remaining \(s\) terms have expectation at most \(1/(M+1)\), which vanishes by Markov's inequality. By the independence and memorylessness of exponential order-statistic spacings, \(\sum_{m=1}^M E_{m,i}/m\) has the distribution of the maximum of \(M\) independent unit-rate exponentials. Its distribution function after subtracting \(\log M\) tends to \(\exp(-e^{-x})\). Since \(\log n-\log M\to\log q\), Slutsky's theorem proves the asserted convolution. Harmonic-number moments and \(\sum_{m\ge1}m^{-2}=\pi^2/6\) give the limit mean and variance. For \(q\ge2\), the variance differs from that of a standard shifted Gumbel; more decisively, its standardized third cumulant is the Gumbel skewness divided by \(\sqrt q\), so the shape is genuinely different.

**5. Diverging \(q\): normal law.** For each geometric summand, \(\mathbb E|W_j-\mathbb EW_j|^3\le C p_j^{-3}\) when \(p_j\le1/2\), and \(\operatorname{Var}W_j\ge\tfrac12 p_j^{-2}\). Thus the Lyapunov ratio is bounded by a constant multiple of
\[
 \frac{\sum_{j=1}^n c_j^{-3}}{(\sum_{j=1}^n c_j^{-2})^{3/2}}.
\]
If \(q\le n\), each positive integer appears among the \(c_j\) at most \(q\) times, and \(c_j=1\) for the first \(q\) states. Therefore this ratio is at most \(\zeta(3)/\sqrt q\). If \(q>n\), every \(c_j=1\), and it equals \(1/\sqrt n\). Both bounds vanish whenever \(q_n,n\to\infty\), so Lyapunov's central limit theorem proves the second limit. The exact moment formulas provide its centering and scaling.

## Verification
Run \(\texttt{python3 check.py}\) with Python 3 and NumPy. The checker executes exact-fraction comparisons of the fine-grid rounding rule against \(c_j/2^r\), exact absorbing-chain dynamic programming against the geometric convolution, exact mean/variance and block harmonic identities, and bounded numerical checks of the Gumbel-profile moments and the standardized normal regime. In the supplied execution, 6,961 checks passed. These tests confirm finite identities and numerical consistency; the weak convergence statements rest on the analytic proof above.

## Relationship to prior work
El Arar, Fasi, Filip and Mikaitis (2026, arXiv:2603.24161) formulate downward-truncated limited-precision stochastic rounding and analyze Horner evaluation and pairwise summation. Their 2026 survey (arXiv:2603.06060) also covers fixed-point applications and the impact of finite random bits. Fitzgibbon and Felix (2025, arXiv:2504.20634) examine few-bit bias and corrections. Xia, Massei and Hochstenbach (2025, DOI 10.1007/s10589-025-00656-1) analyze convergence of stochastic-rounding fixed-point gradient descent, including biased variants. Hathcock and Strogatz (2021, arXiv:2103.08522) establish general Gaussian, Gumbel and convolution universality classes for extinction-prone Markov processes. These are important antecedents: neither elementary Gumbel convergence nor the existence of low-precision rounding bias is claimed as new. The present specific contribution is the exact bit-quantized transition kernel and the all-integer-\(q\) absorbing-time classification, including the \(q\)-fold Gumbel averaging and its normal crossover, for this explicitly stated scalar computation.

## Limitations
This is an exactly solvable one-dimensional model, not a convergence theorem for arbitrary finite-precision optimization or non-scalar iterative methods. Its special relation \(\varepsilon=(q2^r)^{-1}\), the single-cell restriction, and the truncation convention are essential. The Gumbel-to-normal crossover is a statement for the specified triangular sequence, not a universal prediction for all bit-limited implementations. The general theory of birth-death extinction already provides related universality classes, so independent historical-priority review of specialized quantization literature remains warranted. No independent mathematical audit has been performed.

## References
- E.-M. El Arar, M. Fasi, S.-I. Filip, M. Mikaitis, *Probabilistic Error Analysis of Limited-Precision Stochastic Rounding: Horner's Algorithm and Pairwise Summation*, arXiv:2603.24161, first posted 2026-03-25, https://arxiv.org/abs/2603.24161.
- E.-M. El Arar, M. Fasi, S.-I. Filip, M. Mikaitis, *What is New in Stochastic Rounding: a Survey on Theory, Hardware, and Applications*, arXiv:2603.06060, first posted 2026-03-06, https://arxiv.org/abs/2603.06060.
- A. Fitzgibbon, S. Felix, *On Stochastic Rounding with Few Random Bits*, arXiv:2504.20634, first posted 2025-04-29, https://arxiv.org/abs/2504.20634.
- L. Xia, S. Massei, M. E. Hochstenbach, *On the convergence of the gradient descent method with stochastic fixed-point rounding errors under the Polyak–Łojasiewicz inequality*, Computational Optimization and Applications 90 (2025), 753–799, https://doi.org/10.1007/s10589-025-00656-1.
- D. Hathcock, S. H. Strogatz, *Asymptotic absorption-time distributions in extinction-prone Markov processes*, arXiv:2103.08522, https://arxiv.org/abs/2103.08522.
