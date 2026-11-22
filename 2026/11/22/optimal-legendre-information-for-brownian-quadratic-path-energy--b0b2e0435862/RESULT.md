# Optimal Legendre information for Brownian quadratic path energy

## Finding

Let \(B\) be standard Brownian motion on \([0,1]\), and let \(Q=\int_0^1 B_t^2\,dt\). Fix the orthonormal shifted Legendre family \(p_j(t)=\sqrt{2j+1}\,P_j(2t-1)\), \(j\geq0\), and its independent Gaussian white-noise coordinates \(Z_j=\int_0^1p_j(t)\,dB_t\). Among *all* subsets of exactly \(m\geq1\) of these coordinates, the unique subset minimizing the unconditional squared error of the conditional-mean estimator of \(Q\) is
\[
S_m=\{0,1,\ldots,m-1\}.
\]
Its exact minimum mean-square error is
\[
R_1=\frac19,\qquad
R_m=\frac{2m^2-m+1}{4(2m-3)(2m-1)^2(2m+1)^2}\quad(m\geq2),
\qquad R_m\sim\frac{1}{64m^3}.
\]
Over the larger class of *any* \(m\) independent noiseless Gaussian linear measurements of the Brownian driving white noise, the globally minimum error is
\[
R_m^{\mathrm{KL}}=\frac{2}{\pi^4}\sum_{k=m+1}^{\infty}\frac{1}{(k-1/2)^4}
\sim\frac{2}{3\pi^4m^3}.
\]
The Legendre-restricted error is strictly larger for every finite \(m\), and its sharp asymptotic cost against unrestricted linear sensing is
\[
\lim_{m\to\infty}\frac{R_m}{R_m^{\mathrm{KL}}}=\frac{3\pi^4}{128}=2.2830255711\ldots.
\]

## Assumptions and scope

The driving process is a single standard real Brownian motion on \([0,1]\); observations are exact Gaussian coefficients of its white-noise derivative, and the estimator is the exact Bayes conditional expectation in squared loss. Coordinate selection is nonadaptive and restricted to the specified normalized Legendre family for \(R_m\). The unrestricted comparison allows any deterministic \(m\)-dimensional subspace of \(L^2(0,1)\), observed through independent normalized Wiener integrals; it does not permit nonlinear measurements of the entire path. All claims are for integers \(m\geq1\). Neither arbitrary nonlinear path functionals nor finite observation noise are covered.

## Proof

**1. Conditional quadratic information.** Write \(f_j(t)=\int_0^t p_j(u)\,du\) and \(G_{ij}=\int_0^1 f_i(t)f_j(t)\,dt\). Orthonormality and the Itô isometry give independent \(Z_j\sim N(0,1)\) and the convergent Hilbert-space expansion \(B_t=\sum_{j\geq0}f_j(t)Z_j\). For a finite index set \(S\), Gaussian conditioning yields exactly
\[
\widehat Q_S=\mathbb E[Q\mid (Z_j)_{j\in S}]
=\sum_{i,j\in S}G_{ij}Z_iZ_j+\frac12-\sum_{j\in S}G_{jj}.
\]
As \(\operatorname{Cov}(B_s^2,B_t^2)=2\min(s,t)^2\), \(\operatorname{Var}(Q)=1/3\). Orthogonality of Gaussian second-chaos terms therefore gives
\[
R(S)=\mathbb E[(Q-\widehat Q_S)^2]
=\frac13-2\sum_{i,j\in S}G_{ij}^2.
\tag{1}
\]
This holds for every finite subset, without assuming consecutiveness.

**2. Exact Gram structure.** For every \(j\geq1\), the antiderivative is explicitly \(f_j(t)=[P_{j+1}(2t-1)-P_{j-1}(2t-1)]/[2\sqrt{2j+1}]\), while \(f_0(t)=t\). The ordinary Legendre orthogonality \(\int_0^1P_j(2t-1)P_k(2t-1)\,dt=\mathbf1_{j=k}/(2j+1)\) then gives the *complete* list of nonzero Gram entries:
\[
G_{00}=\frac13,\qquad G_{01}=G_{10}=-\frac{1}{4\sqrt3},
\]
\[
G_{jj}=\frac1{2(2j-1)(2j+3)}\quad(j\geq1),\qquad
G_{j,j+2}=G_{j+2,j}=-\frac1{4(2j+3)\sqrt{(2j+1)(2j+5)}}\quad(j\geq0).
\tag{2}
\]
All other off-diagonal entries vanish. Thus the squared information \(\sum_{i,j\in S}G_{ij}^2\) is a weighted vertex-and-edge reward on two decreasing-weight parity chains, plus the positive special edge connecting indices \(0\) and \(1\).

**3. Unique optimal subset for every budget.** Define \(d_j=G_{jj}^2\) and \(e_j=G_{j,j+2}^2\). These are strictly decreasing in \(j\), with \(d_0=1/9\), \(d_1=1/100\), and \(e_0=1/720\). Compress any finite selected set to the smallest indices within each parity, preserving its number of even and odd indices. Each selected vertex moves earlier, strictly improving its diagonal contribution whenever any movement occurs; an existing parity-chain edge becomes an edge at an earlier index (and any new edges add positive information). The special \(0\)-\(1\) edge can only be created, never destroyed. Consequently every optimum must consist of an initial segment of each parity chain.

For any such parity-prefix set, its information score is
\[
\sum_{j\in S}a_j+\frac1{24}\mathbf1_{\{0,1\}\subseteq S},\qquad
a_0=\frac19,\quad a_1=\frac1{100},\quad a_j=d_j+2e_{j-2}\ (j\geq2).
\]
The sequence \(a_0>a_1>a_2>\cdots>0\) is strictly decreasing: for \(j\geq2\) both component sequences decrease, and \(a_2=1/1764+1/360<1/100\). The largest possible sum of exactly \(m\) entries is therefore uniquely obtained by \(S_m\). Its special-edge bonus is also maximal (equal to \(1/24\) when \(m\geq2\)). Equations (1) and (2) prove the stated global unique optimality, including \(m=1\).

**4. Exact risk and asymptotics.** For \(m\geq2\), omission of Legendre indices \(m,m+1,\ldots\) leaves precisely
\[
R_m=2\sum_{j=m}^{\infty}d_j+4\sum_{j=m-2}^{\infty}e_j.
\]
Set \(T_j=d_j+2e_j\), and use the exact partial-fraction identity
\[
T_j=\frac1{64}\left(\frac1{(2j-1)^2}-\frac1{(2j+3)^2}\right)
+\frac1{128}\left(\frac1{2j+3}-\frac1{2j-1}+\frac1{2j+1}-\frac1{2j+5}\right).
\]
The series telescopes, giving
\[
\sum_{j=m}^{\infty}T_j=\frac1{64}\left(\frac1{(2m-1)^2}+\frac1{(2m+1)^2}\right)
+\frac1{128}\left(\frac1{2m+3}-\frac1{2m-1}\right).
\]
Substituting \(R_m=2\sum_{j=m}^{\infty}T_j+4(e_{m-2}+e_{m-1})\) yields the claimed rational formula. Its leading term is \(1/(64m^3)\). Formula (1) directly gives \(R_1=1/9\).

**5. Best unrestricted linear sensing.** Regard \(Kf(t)=\int_0^t f(u)\,du\) as a Volterra map on \(H=L^2(0,1)\), and set \(T=K^*K\). Any \(m\)-dimensional white-noise sensing subspace with orthogonal projection \(P\) captures information \(2\operatorname{tr}((PTP)^2)\). The positive compact operator \(T\) has simple, strictly decreasing eigenvalues \(\lambda_k=[\pi^2(k-1/2)^2]^{-1}\), obtained by the Sturm–Liouville boundary problem \(u'(0)=0\), \(u(1)=0\). The min-max principle bounds each eigenvalue of \(PTP\) by \(\lambda_k\), so the top \(m\) eigenspace uniquely minimizes the risk, giving \(R_m^{\mathrm{KL}}=2\sum_{k>m}\lambda_k^2\). Strict inequality for the finite-degree Legendre span follows because the leading cosine eigenfunction is not a polynomial. An integral comparison gives \(\sum_{k>m}(k-1/2)^{-4}\sim1/(3m^3)\), and the stated limiting ratio follows.

## Verification

Run `python3 verify.py` with only the Python standard library. The program independently constructs the normalized Legendre Gram squares by exact rational polynomial integration through degree 13, checks every possible subset of degrees 0–12 with budgets 1–7 against the unique prefix optimum, tests the telescoped risk identity at every integer budget from 2 to 100, and brackets numerical KL comparison ratios using positive integral-test bounds. Representative exact values are \(R_1=1/9\), \(R_2=7/900\), and \(R_3=4/3675\). The all-budget theorem and asymptotic conclusions rest on the proof above, *not* on finite tests.

## Relationship to prior work

Foster, Lyons and Oberhauser (arXiv:1904.06998, first posted 15 April 2019) introduce the independent polynomial Brownian coordinates and obtain the conditional estimator and variance for the first **two** coefficients (Theorems 2–3 and Section 3). In particular their result is consistent with the already-known \(m=2\) case, which is **not** presented here as novel. Their weighted-path approximation optimality does not settle optimal selection of arbitrary Legendre coefficient subsets for the nonlinear quadratic functional, nor the complete all-budget risk and its optimal-linear-sensing efficiency limit.

Kuznetsov (arXiv:1801.01079, first posted 3 January 2018), especially Theorem 2 and the double-integral case, gives a broad generalized-Fourier mean-square error apparatus for iterated Itô integrals; this can underlie calculations of the present quadratic error. The distinctive assertions here are the unique global Legendre-subset allocation for every budget and the sharp comparison with unrestricted Karhunen–Loève Gaussian sensing. Neither inspected source states those assertions. Grebenkov (arXiv:1307.0185) minimizes the variance of a chosen quadratic statistic by varying its matrix, rather than selecting observed Gaussian coordinates for a fixed quadratic path energy. General spectral compression principles used in the comparison are classical and are not claimed as new.

## Limitations

Only exact coefficients from the specified Legendre bank, a quadratic Brownian path-energy payoff and nonadaptive linear Gaussian observations are considered. The result is not an optimality claim among nonlinear measurements or general Gaussian processes. The exact finite-budget Bayes risks can be derived from established Gaussian-chaos and Fourier-error identities; the claim of distinct contribution is the global subset selection and quantified efficiency frontier. Historical priority beyond inspected sources and accessible result records is not independently certified.

## References

1. D. F. Kuznetsov, *Exact Calculation of the Mean-Square Error in the Method of Expansion of Iterated Ito Stochastic Integrals Based on Generalized Multiple Fourier Series*, arXiv:1801.01079 (initial submission 2018-01-03), https://arxiv.org/abs/1801.01079 .
2. J. Foster, T. Lyons and H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998 (initial submission 2019-04-15), https://arxiv.org/html/1904.06998v3 ; SIAM Journal on Numerical Analysis 58 (2020), 1393–1421, https://doi.org/10.1137/19M1261912 .
3. D. S. Grebenkov, *Optimal and Sub-optimal Quadratic Forms for Non-centered Gaussian Processes*, arXiv:1307.0185 (2013), https://arxiv.org/abs/1307.0185 .
