# Exact finite variance and Gaussian fluctuations of a normalized random Fourier fourth moment

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
Equivalently, the centering may be replaced by \(2\). Thus the fourth power of the random \(L^4/L^2\) Nikolskii factor has an exact finite-size variance and a nondegenerate Gaussian fluctuation scale of order \(n^{-1/2}\).

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
Ling, Geng, Li and Wang (first publicly available March 21, 2025) study random Nikolskii factors for real Gaussian trigonometric polynomials and prove constant *order* for their expectations at finite exponents. Their stated ensemble is a real trigonometric basis, and their main theorem does not give the displayed finite rational variance or a Gaussian central limit theorem for the complex one-sided \(L^4/L^2\) factor. Borwein and Lockhart establish expected random polynomial norm asymptotics and convergence in probability, rather than this self-normalized finite variance or fluctuation law. A published logarithmic Mahler-measure variance expansion does use the same proper-complex-Gaussian coefficient ensemble, but its observable is \(\int\log|P_n|\,dm\), not the normalized fourth power, and its theorem has no central limit statement. A published exact variance computation for random **unimodular** coefficients concerns a different coefficient distribution, a deterministic \(L^2\) denominator, and no central limit theorem. That result shares the leading unnormalized \(8n^3/3\) variance scale but neither implies this finite formula nor this Gaussian limit. The comparison is of claims and hypotheses, not titles or matching leading constants.

## Limitations
This result concerns independent circular complex Gaussians on a one-sided *consecutive* frequency set. Its exact variance and fourth-Wick cancellation need not persist for real coefficients, fixed-magnitude phases, nonconsecutive spectra or non-Gaussian distributions. The central limit theorem is qualitative; it does not give Berry–Esseen or moderate-deviation estimates. An older equivalent statement in Gaussian chaos or random polynomial literature cannot be excluded solely from accessible index and full-text comparisons.

## References
1. Y. Ling, J. Geng, J. Li and H. Wang, “Average Nikolskii factors for random trigonometric polynomials,” arXiv:2503.16786 (first posted March 21, 2025); *Journal of Inequalities and Applications* 2026, article 78, DOI:10.1186/s13660-026-03484-x.
2. P. Borwein and R. Lockhart, “The expected \(L^p\) norm of random polynomials,” *Proceedings of the American Mathematical Society* 129 (2001), 1463–1472; first published online October 25, 2000.
3. “Two-term variance law for the logarithmic Mahler measure of Gaussian polynomials,” public result at https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-two-term-variance-law-for-the-logarithmic-mahler-measure-of-gaus--0d5fa733eb8c/RESULT.md (2026).
4. “Exact finite variance of the fourth moment of a random unimodular polynomial,” public result at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-finite-variance-of-the-fourth-moment-of-a-random-unimodula--2ac4e1c327c6/RESULT.md (2026).
