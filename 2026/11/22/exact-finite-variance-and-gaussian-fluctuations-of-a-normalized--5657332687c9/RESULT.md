# Exact finite variance of a normalized random Fourier fourth moment

## Finding
Let \(n\ge 1\), and let \(g_0,\ldots,g_{n-1}\) be independent standard circular complex Gaussian variables, normalized by \(\mathbb E|g_j|^2=1\). On the circle with probability Haar measure \(m\), put
\[
P_n(e^{it})=\sum_{j=0}^{n-1}g_je^{ijt},\qquad
Y_n=\frac{\int_{\mathbb T}|P_n|^4\,dm}{\left(\int_{\mathbb T}|P_n|^2\,dm\right)^2}.
\]
The denominator is strictly positive almost surely. For **every** integer \(n\ge1\),
\[
\boxed{\mathbb E Y_n=\frac{2n}{n+1},\qquad
\operatorname{Var}(Y_n)=\frac{4(n-1)(2n^2-2n-1)}{3(n+1)^2(n+2)(n+3)}.}
\]
In addition, as \(n\to\infty\),
\[
\boxed{\sqrt n\left(Y_n-\frac{2n}{n+1}\right)
\ \xrightarrow{\ \mathrm d\ }\ \mathcal N\!\left(0,\frac83\right).}
\]
Equivalently, the centering may be replaced by \(2\). The contribution is the exact finite-size moment formula for the fourth power of the random \(L^4/L^2\) Nikolskii factor. The Gaussian limit is included for context: after removing the radial fluctuation, it is also a consequence of a general Gaussian triangular-array limit theorem, as explained below.

## Assumptions and scope
The variables are *proper complex* Gaussians: \(g_j=(X_j+iY_j)/\sqrt2\) for independent real standard normal \(X_j,Y_j\). This is an analytic, one-sided consecutive-frequency polynomial, not a real symmetric trigonometric polynomial or a random polynomial with unimodular coefficients. All norms use normalized Haar measure. The result is exact for each finite \(n\), including the deterministic \(n=1\) case \(Y_1=1\); the central limit theorem only concerns \(n\to\infty\). No assertion of a quantitative normal-approximation rate is made.

## Proof
**1. Exact Gaussian moment identities.** Let \(S=\sum_{j=0}^{n-1}|g_j|^2\) and \(T=\int|P_n|^4\,dm\), so \(Y_n=T/S^2\) and \(S\sim\operatorname{Gamma}(n,1)\). Writing \(g=\sqrt S\,u\), the direction \(u\) is uniform on the complex unit sphere and independent of \(S\). Hence \(Y_n\) is independent of \(S\). In particular,
\[
\mathbb E S^2=n(n+1),\qquad
\mathbb E S^4=n(n+1)(n+2)(n+3).
\]
At each \(t\), \(P_n(e^{it})\) has variance \(n\), so \(\mathbb E T=2n^2\). For two jointly proper circular complex Gaussians \(X,Z\) of common variance \(n\) and cross-covariance \(c=\mathbb E(X\overline Z)\), the exact Wick expansion gives
\[
\mathbb E\bigl(|X|^4|Z|^4\bigr)=4n^4+16n^2|c|^2+4|c|^4.
\]
Here \(c\) equals a phase choice of \(D_n(t-s)=\sum_{j=0}^{n-1}e^{ij(t-s)}\). By character orthogonality,
\[
\int|D_n|^2\,dm=n,\qquad
\int|D_n|^4\,dm
 =\sum_{k=-(n-1)}^{n-1}(n-|k|)^2=\frac{2n^3+n}{3}.
\]
Integrating the joint moment formula therefore yields
\[
\mathbb E T^2=4n^4+16n^3+\frac{4(2n^3+n)}3
=4n^4+\frac{56n^3+4n}{3}.
\]
Independence of \(Y_n\) and \(S\) now implies
\[
\mathbb E Y_n=\frac{\mathbb E T}{\mathbb E S^2}=\frac{2n}{n+1},\qquad
\mathbb E Y_n^2=\frac{\mathbb E T^2}{\mathbb E S^4}.
\]
Subtraction and rational simplification give the claimed finite variance. The formula is nonnegative, vanishing only for \(n=1\).

**2. Exact removal of the fluctuating quadratic component.** Define the unit-variance stationary complex Gaussian field
\[
Z_n(t)=n^{-1/2}P_n(e^{it}),\quad
U_n=\int|Z_n|^2\,dm-1=\frac{S-n}{n},
\]
and the fourth Wick polynomial \(h(z)=|z|^4-4|z|^2+2\), with
\[
H_n=\int h(Z_n(t))\,dm(t).
\]
Then, by direct rearrangement,
\[
\frac{T}{n^2}=2+4U_n+H_n,\qquad
Y_n-2=\frac{H_n-2U_n^2}{(1+U_n)^2}.
\]
Since \(\operatorname{Var}(S)=n\), we have \(U_n=O_{\mathbb P}(n^{-1/2})\). Consequently, once \(\sqrt n H_n\) is known to be tight, the last display shows
\[
\sqrt n(Y_n-2)-\sqrt nH_n\xrightarrow{\mathbb P}0.
\]
In particular, the random quadratic normalization cancels the Gaussian second-chaos fluctuation; only the fourth Wick chaos contributes at leading order.

**3. Variance and connected-diagram central limit theorem.** The covariance function is
\[
r_n(u)=\mathbb E[Z_n(t)\overline{Z_n(t+u)}]
=\frac1n\sum_{j=0}^{n-1}e^{-iju}.
\]
The complex Wick pairing rule (two unbarred and two barred legs at each vertex, with internal contractions removed) implies
\[
\mathbb E[h(Z_n(t))h(Z_n(s))]=4|r_n(t-s)|^4.
\]
Therefore
\[
\operatorname{Var}(H_n)
=4\int|r_n(u)|^4\,dm(u)
=\frac{4(2n^3+n)}{3n^4},\qquad
n\operatorname{Var}(H_n)\longrightarrow\frac83.
\]
We verify asymptotic normality rather than infer it from this variance. The elementary Dirichlet-kernel estimate
\[
|r_n(u)|\le\min\left\{1,\frac1{n|\sin(u/2)|}\right\}
\quad\text{implies}\quad
\int|r_n(u)|\,dm(u)\le\frac{1+\log n}{n}
\]
for every \(n\ge1\), using \(|\sin(u/2)|\ge |u|/\pi\) on \([-\pi,\pi]\).

For each fixed integer \(q\ge3\), expand the joint cumulant of \(q\) fourth Wick polynomials by the connected Wick-pairing formula. Every summand corresponds to a connected multigraph on \(q\) labeled vertices, with four contracted Gaussian legs at each vertex and no internal contractions. Every edge contributes a covariance factor whose modulus is bounded by \(|r_n(t_i-t_j)|\). A spanning tree has \(q-1\) edges. The remaining edge factors have modulus at most one; integrating tree leaves successively against normalized Haar measure gives at most \(\|r_n\|_1^{q-1}\). Since the number of Wick pairings depends only on \(q\),
\[
|\kappa_q(H_n)|\le C_q\left(\frac{1+\log n}{n}\right)^{q-1}.
\]
It follows that for \(q\ge3\),
\[
|\kappa_q(\sqrt nH_n)|\le C_q n^{q/2}
\left(\frac{1+\log n}{n}\right)^{q-1}\longrightarrow0.
\]
The first cumulant is zero and the second tends to \(8/3\). Hence all fixed moments converge to those of \(\mathcal N(0,8/3)\). Gaussian moment determinacy and bounded second moments yield \(\sqrt nH_n\Rightarrow\mathcal N(0,8/3)\). Applying the preceding probabilistic approximation and Slutsky's theorem proves \(\sqrt n(Y_n-2)\Rightarrow\mathcal N(0,8/3)\). The difference \(2-2n/(n+1)=2/(n+1)\) is negligible at scale \(n^{-1/2}\), completing the proof.

## Verification
The accompanying standalone script `check_random_fourier.py` constructs the Gaussian-coefficient polynomial for \(T\) directly, performs exact Wick evaluation of its first and second moments for \(1\le n\le7\), checks the Dirichlet-kernel additive-energy count for \(1\le n\le9\), verifies the rational variance identity and its asymptotic coefficient, and separately checks the two-coefficient beta-distribution case. It executed successfully with 46 assertions. These finite checks are supplementary. The all-\(n\) formulas follow from the exact Gaussian identities, and the central limit theorem follows from the connected-diagram estimate, not from the finite tests.

## Relationship to prior work
Ling, Geng, Li and Wang study random Nikolskii factors in a real Gaussian trigonometric basis and prove order bounds for their expectations at finite exponents, rather than the exact finite variance for the proper-complex analytic ensemble. The expected random polynomial norm asymptotics considered by Borwein and Lockhart concern a different claim from the exact self-normalized variance here. A logarithmic Mahler-measure variance expansion uses the same proper-complex Gaussian coefficient ensemble but a different observable, \(\int\log|P_n|\,dm\). An exact variance computation for random **unimodular** coefficients uses the fourth-norm observable but a different coefficient law and deterministic squared \(L^2\) norm. Agreement of its leading variance after normalization does not fix the finite-size Gaussian formula.

The Gaussian limit is covered by a broader method. Specifically, Theorem 1(ii) of Bardet and Surgailis applies to the fourth Wick sum on the \(M=2n\) equispaced nodes: this average equals \(H_n\) exactly because the integrand has frequencies of absolute value at most \(2n-2\). Take the standardized real vector of real and imaginary parts (multiplied by \(\sqrt 2\)) at each node and the fixed rank-four Wick polynomial as the function of this vector. For distinct indices \(j,k\), each component covariance is bounded by \(1/d\), where \(d=\min(|j-k|,M-|j-k|)\), by the sine bound in the proof. The row sums of fourth powers are uniformly bounded. For the ordinary-index tail in their condition (3.2), pairs with \(|j-k|=d>K\) contribute at most \(2\sum_{d>K}d^{-4}\) after division by \(M\); the other pairs contribute at most \((2/M)\sum_{d\ge1}d^{-3}\), since there are \(2d\) ordered pairs with separation \(M-d\). The tail is empty if \(M\le K\), so it vanishes uniformly as \(K\to\infty\). The variance for \(\sqrt M H_n\) tends to \(16/3\) by the kernel computation above. This verifies the array theorem's hypotheses; rescaling to \(\sqrt n\) and using the exact cancellation in the proof gives the same limit for \(Y_n\). The general array theorem does not give the finite moments of the ratio \(T/S^2\).

## Limitations
This result concerns independent circular complex Gaussians on a one-sided *consecutive* frequency set. Its exact variance and fourth-Wick cancellation need not persist for real coefficients, fixed-magnitude phases, nonconsecutive spectra or non-Gaussian distributions. The central limit theorem is qualitative; it does not give Berry–Esseen or moderate-deviation estimates. An older equivalent statement in Gaussian chaos or random polynomial literature cannot be excluded solely from accessible index and full-text comparisons.

## References
1. Y. Ling, J. Geng, J. Li and H. Wang, “Average Nikolskii factors for random trigonometric polynomials,” arXiv:2503.16786 (first posted March 21, 2025); *Journal of Inequalities and Applications* 2026, article 78, DOI:10.1186/s13660-026-03484-x.
2. P. Borwein and R. Lockhart, “The expected \(L^p\) norm of random polynomials,” *Proceedings of the American Mathematical Society* 129 (2001), 1463–1472; first published online October 25, 2000.
3. “Two-term variance law for the logarithmic Mahler measure of Gaussian polynomials,” https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-two-term-variance-law-for-the-logarithmic-mahler-measure-of-gaus--0d5fa733eb8c/RESULT.md (2026).
4. “Exact finite variance of the fourth moment of a random unimodular polynomial,” https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-finite-variance-of-the-fourth-moment-of-a-random-unimodula--2ac4e1c327c6/RESULT.md (2026).
5. J.-M. Bardet and D. Surgailis, “Moment bounds and central limit theorems for Gaussian subordinated arrays,” arXiv:1104.4732, Theorem 1(ii), https://arxiv.org/abs/1104.4732.
