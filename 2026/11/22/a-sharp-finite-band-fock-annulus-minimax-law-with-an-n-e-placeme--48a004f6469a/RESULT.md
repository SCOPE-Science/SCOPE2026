# A sharp finite-band Fock annulus minimax law with an \(N/e\) placement scale

## Finding
Let \(N\ge1\) be an integer and \(L>0\). In the analytic Bargmann–Fock space with normalized Gaussian measure \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\), let \(E_N=\operatorname{span}\{z^j/\sqrt{j!}:0\le j\le N\}\). For the concentric annulus \(\Omega_{a,L}=\{z\in\mathbb C:a\le |z|^2\le a+L\}\), \(a\ge0\), its Euclidean area is \(\pi L\). Define its guaranteed energy capture
\[
B_N(a,L)=\inf_{f\in E_N,\ \|f\|_{\mathcal F}=1}\int_{\Omega_{a,L}}|f(z)|^2\,d\gamma(z).
\]
Put \(\lambda_j(a,L)=\frac1{j!}\int_a^{a+L} t^j e^{-t}\,dt\). The complete finite-band minimax placement law is
\[
\boxed{B_N(a,L)=\min\{\lambda_0(a,L),\lambda_N(a,L)\},\qquad
\sup_{a\ge0}B_N(a,L)= (1-e^{-L})e^{-a_N(L)},}
\]
where \(a_N(L)>0\) is the **unique** solution of
\[
\boxed{\sum_{k=1}^N\frac{a^k}{k!}
=e^{-L}\sum_{k=1}^N\frac{(a+L)^k}{k!}.}
\]
The unique maximizing annulus has squared radii \(a_N(L)\) and \(a_N(L)+L\). At that location, precisely the vacuum and the highest included degree, \(0\) and \(N\), are least observed; for \(N\ge2\) all interior degrees have strictly greater captured energy. For \(N=1\), \(a_1(L)=L/(e^L-1)\); for \(N\ge2\), \(0<a_N(L)<L/(e^{L/N}-1)\).

For every fixed \(L>0\), as \(N\to\infty\), set
\[
J(L)=\frac{e^{(e-1)L}-1}{(e-1)(1-e^{-L})}.
\]
Then the sharp large-bandwidth law is
\[
\boxed{a_N(L)=\frac Ne+\frac{\log(2\pi N)}{2e}-\frac{\log J(L)}e+o(1),}
\]
\[
\boxed{\sup_{a\ge0} B_N(a,L)
\sim (1-e^{-L})(2\pi N)^{-1/(2e)}J(L)^{1/e}e^{-N/e}.}
\]
For fixed \(N\) and \(L\downarrow0\), the complementary thin-annulus law is \(a_N(L)=(N!)^{1/N}-L/2+O_N(L^2)\).

## Assumptions and scope
The measure, normalization, and domain are as above; \(a\ge0\), \(L>0\), and \(N\ge1\) are arbitrary, with no discrete-grid restriction. The optimization is over **one concentric connected annulus of prescribed Euclidean area**, not arbitrary measurable sets, unions of annuli, or arbitrary translates. The objective is the smallest eigenvalue of the localization compression on the full consecutive-mode space \(E_N\), so it controls every normalized superposition, not just a pair of specified states. The asymptotic in \(N\) holds at fixed positive \(L\), and the thin-annulus expansion at fixed \(N\).

## Proof
**1. Exact diagonalization.** Angular orthogonality of distinct monomials and polar substitution \(t=|z|^2\) yield, for \(f=\sum_{j=0}^{N}c_j z^j/\sqrt{j!}\),
\[
\int_{\Omega_{a,L}}|f|^2d\gamma=\sum_{j=0}^{N}|c_j|^2\lambda_j(a,L),\qquad \|f\|^2=\sum_{j=0}^{N}|c_j|^2.
\]
Therefore \(B_N=\min_{0\le j\le N}\lambda_j\). Integrating by parts gives the exact neighbor identity
\[
\lambda_j-\lambda_{j-1}=\frac{a^j e^{-a}-(a+L)^j e^{-(a+L)}}{j!},\quad j\ge1.
\]
When \(a>0\), its sign is the sign of \(L/\log(1+L/a)-j\). Thus the finite sequence of eigenvalues increases and then decreases (with at most one adjacent equality); at \(a=0\) it decreases throughout. Its minimum is necessarily at one of the two endpoint indices, proving the first boxed equality. This unimodality itself is classical and is not asserted to be new.

**2. Unique optimizer.** The zeroth-mode mass is \(\lambda_0=e^{-a}(1-e^{-L})\), strictly decreasing in \(a\). The ratio
\[
\frac{\lambda_N(a,L)}{\lambda_0(a,L)}=\frac{1}{N!(1-e^{-L})}\int_0^L e^{-s}(a+s)^Nds
\]
is continuous and strictly increasing in \(a\), from a value below one at \(a=0\) (by the neighbor identity there) to infinity. Hence there is exactly one crossing \(a_N\). The equality \(\lambda_N=\lambda_0\), on using \(\int_a^{a+L}t^N e^{-t}dt/N!=e^{-a}\sum_{k=0}^N a^k/k!-e^{-(a+L)}\sum_{k=0}^N(a+L)^k/k!\), is equivalent to the displayed degree-\(N\) polynomial equation.

For \(c_N=L/(e^{L/N}-1)\), the neighbor identity shows \(\lambda_j(c_N,L)>\lambda_{j-1}(c_N,L)\) for \(1\le j<N\), while \(\lambda_N(c_N,L)=\lambda_{N-1}(c_N,L)\). Hence \(\lambda_N(c_N,L)>\lambda_0(c_N,L)\) for \(N\ge2\), so \(a_N<c_N\); when \(N=1\) the crossing equals \(c_1\). The derivative \(\partial_a\lambda_N=e^{-(a+L)}(a+L)^N/N!-e^{-a}a^N/N!\) is positive for \(a<c_N\). Therefore \(B_N=\lambda_N\) increases strictly up to \(a_N\), while \(B_N=\lambda_0\) decreases strictly after \(a_N\), proving unique global optimality and its value. Strict unimodality and equality of endpoints at \(a_N\) imply that no index strictly between them is also a minimizer.

**3. Fixed-area large-bandwidth expansion.** Write \(S\) for a random variable supported on \([0,L]\) with density \(e^{-s}/(1-e^{-L})\). The optimizer equation becomes \(\mathbb E(a_N+S)^N=N!\). With \(c=(N!)^{1/N}\), monotonicity gives \(c-L\le a_N\le c\). Stirling's formula implies \(a_N=N/e+O(\log N)\). Moreover,
\[
1=\frac{a_N^N}{N!}\mathbb E(1+S/a_N)^N,
\qquad \mathbb E(1+S/a_N)^N\longrightarrow\mathbb E e^{eS}=J(L),
\]
by bounded convergence, since \(N/a_N\to e\) and \(S\in[0,L]\). Taking logarithms and using Stirling with \(a_N=N/e+O(\log N)\) yields
\[
e(a_N-N/e)-\tfrac12\log(2\pi N)+\log J(L)=o(1).
\]
This is the asserted radius expansion. Substitute it into \(\lambda_0(a_N,L)=(1-e^{-L})e^{-a_N}\) for the displayed sharp minimax-energy equivalent.

**4. Thin-area limit.** For fixed \(N\), the optimizer equation is \(\mathbb E(a_N+S)^N=N!\), with the truncated exponential random variable \(S\in[0,L]\) satisfying \(\mathbb E S=L/2+O(L^2)\). Since \(a_N\to(N!)^{1/N}\), Taylor expansion of the moment gives \(a_N=(N!)^{1/N}-L/2+O_N(L^2)\).

## Verification
Run `python check.py` with Python 3, NumPy and SciPy. The code independently integrates each eigenvalue and checks the neighbor identity, the equality of the two limiting modes, all-interior-mode lower bounds, global placement comparisons over finite test grids, and representative large-\(N\) and small-area approximations. It prints `PASS: 1319 deterministic exact-identity/numerical consistency assertions`. These finite checks supplement rather than replace the analytic argument for all \(N,L,a\).

## Relationship to prior work
Classical radial Gaussian localization diagonalization gives the incomplete-Gamma/Hermite eigenvalue formula. Dewage and Ólafsson (2021) establish general quasi-radial Toeplitz eigenvalue formulas, not the optimal least-eigenvalue placement for a finite consecutive Hermite band. Knutsen (2022) investigates Gaussian short-time Fourier localization on porous masks and corresponding operator-norm bounds, rather than this fixed-area smallest-eigenvalue design. Galbis (2021) proves a universal upper bound for any individual radial Toeplitz eigenvalue; an upper bound on one state does not determine the maximized worst-mode capture.

Published published-finding corpus results on Gaussian annuli give the **largest** Hermite eigenvalue's complete mode staircase and its asymptotics; their adjacent-eigenvalue identity supplies the classical unimodality used in Step 1 but does not state the fixed-area, finite-band *smallest*-eigenvalue optimization, its unique exact polynomial-root placement, or the \(N/e\) minimax scaling. A separate published-finding corpus result optimizes the *vacuum and one excited mode* over arbitrary measurable masks in the vanishing-area regime, showing why connected-annulus restriction is essential; its asymptotic single-annulus comparison agrees with the thin-area limit above, but it does not imply the stated finite-area all-band classification. The distinguishing question is robust simultaneous observation of the entire consecutive Hermite band under a one-annulus budget, including location and bandwidth dependence.

## Limitations
The finding makes no global optimality claim among disconnected or nonradial masks; such masks can outperform a single annulus even for two modes. It does not give uniform error control for the large-bandwidth expansion if \(L\) grows with \(N\). The adjacent-mode recurrence, spectral unimodality, and standard diagonalization are already known; the proposed contribution is the exact finite-band minimax placement plus its sharp asymptotic scaling. The absence of an indexed identical optimization statement cannot establish historical uniqueness; an equivalent may be recorded in design or Fock sampling literature not found in the searches.

## References
1. H. Knutsen, *A Fractal Uncertainty Principle for the Short-Time Fourier Transform and Gabor Multipliers*, arXiv:2204.03068 (first public 2022-04-06), https://arxiv.org/abs/2204.03068 .
2. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public 2021-07-03), https://arxiv.org/abs/2107.01465 .
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public 2021-02-03), https://arxiv.org/abs/2102.02031 .
4. *Exact Hermite-mode staircase and oscillatory norm correction for Gaussian annular localization*, published published-finding corpus research, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-hermite-mode-staircase-and-oscillatory-norm-correction-for--0c0c5a98ddf3 .
5. *A two-band concentration law for vacuum and excited Gaussian Fock modes*, published published-finding corpus research, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-band-concentration-law-for-vacuum-and-excited-gaussian-foc--c54df82037bb .
6. *Exact Gaussian-annulus eigenmode crossings and a Bernoulli second-order concentration law*, published published-finding corpus research, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-gaussian-annulus-eigenmode-crossings-and-a-bernoulli-secon--57fcc645d909 .
