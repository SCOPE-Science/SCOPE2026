# Sharp spectral-tail extremizers for monotone multipliers of the real-variable Cesàro operator

## Finding
Let \(C\) be the bounded operator on complex \(L^2(0,1)\) defined by
\[
(Cf)(x)=x^{-1}\int_0^x\frac{f(t)}{1-t}\,dt.
\]
For every real \(g\in C^1([0,1])\) put \(K_g=M_gC-CM_g\). The commutator is compact and has the exact second-order singular-value law
\[
\lim_{n\to\infty}n^2s_n(K_g)=\mathcal W(g):=\frac1{\pi^2}\left(\int_0^1\sqrt{\frac{|g'(x)|}{x(1-x)}}\,dx\right)^2.\tag{1}
\]
For a prescribed Lipschitz budget \(L\ge1\), let
\[
\mathcal G_L=\{g\in C^1([0,1];\mathbb R):g(0)=0,\ g(1)=1,\ 0\le g'\le L\}.\tag{2}
\]
The exact extremal values of the spectral-tail coefficient \(\mathcal W\) are as follows. For \(L=1\), the only admissible function is \(g(x)=x\), and \(\mathcal W(g)=1\). For \(L>1\), let \(\beta_L\in(0,1/2)\) be the unique solution of
\[
2L\left[\beta+\beta(1-\beta)\log\frac{1-\beta}{\beta}\right]=1.\tag{3}
\]
Then
\[
\boxed{\sup_{g\in\mathcal G_L}\mathcal W(g)=\frac1{\pi^2}\left[4\sqrt L\arcsin\sqrt{\beta_L}+2\sqrt{L\beta_L(1-\beta_L)}\log\frac{1-\beta_L}{\beta_L}\right]^2.}\tag{4}
\]
The supremum is attained by exactly one \(g\), given by \(g(0)=0\) and
\[
\boxed{g'(x)=\min\left\{L,\frac{L\beta_L(1-\beta_L)}{x(1-x)}\right\}\quad (0<x<1),\qquad g'(0)=g'(1)=L.}\tag{5}
\]
The opposite extremum is
\[
\boxed{\inf_{g\in\mathcal G_L}\mathcal W(g)=\frac{4L}{\pi^2}\arcsin^2(1/L).}\tag{6}
\]
For \(L>1\) this infimum is not attained in \(C^1\); it is approached by smooth derivatives tending to \(L\) on the centered interval \([(1-1/L)/2,(1+1/L)/2]\) and zero elsewhere. As \(L\to\infty\),
\[
\sup\mathcal W(g)\sim \frac{2}{\pi^2}\log L,\qquad \inf\mathcal W(g)\sim\frac4{\pi^2L}.\tag{7}
\]
Thus the worst high-index singular-value tail is produced by a boundary-saturated but interior-tapered multiplier, whereas the best tail is approached by concentrating its permitted derivative centrally. This constrained classification, rather than the general one-operator Weyl principle behind (1), is the principal finding.

## Assumptions and scope
Singular values \(s_n\) are arranged in nonincreasing order with multiplicity. Multiplication \(M_g\) is pointwise multiplication by \(g\). For formula (1), the derivative is real and continuous but need not be nonnegative; the complex-valued extension follows by the same kernel argument with \(|g'|\). The displayed optimization concerns real nondecreasing \(C^1\) functions exactly, with an \(L^\infty\) derivative cap \(L\) and normalized endpoint gap one. If \(L<1\), the admissible class is empty. Every singular-value asymptotic is as the index tends to infinity with \(g\) and \(L\) fixed; no uniformity across unbounded \(L\) is asserted. The maximum statement includes uniqueness up to equality of functions, not just of derivatives.

## Proof
**1. Exact convolution factorization.** Write \(x(s)=e^s/(1+e^s)\), and use the unitary map \((Uf)(s)=\sqrt{x(s)(1-x(s))}\,f(x(s))\) from \(L^2(0,1)\) to \(L^2(\mathbb R)\). Direct substitution in the kernel yields
\[
UCU^{-1}=R,\qquad (Rh)(s)=\int_{-\infty}^s e^{-(s-t)/2}h(t)\,dt.
\]
Let \(w(s)=g(x(s))\) and \(\rho(s)=w'(s)=x(s)(1-x(s))g'(x(s))\). Thus \(|\rho(s)|\le C_g e^{-|s|}\), and
\[
UK_gU^{-1}=[M_w,R]=RM_\rho R=:T_\rho.\tag{8}
\]
Indeed, the kernel of the right-hand side is
\[
\mathbf 1_{t<s}e^{-(s-t)/2}\int_t^s\rho(u)\,du
=\mathbf 1_{t<s}e^{-(s-t)/2}(w(s)-w(t)),
\]
which equals the kernel of the commutator. In particular \(T_\rho\) is compact, as follows also from the localized estimates below. The change of variables gives the exact identity
\[
\int_{\mathbb R}|\rho(s)|^{1/2}\,ds=\int_0^1\sqrt{\frac{|g'(x)|}{x(1-x)}}\,dx.\tag{9}
\]

**2. Localization and the second-order spectral coefficient.** We prove the auxiliary asymptotic
\[
\lim_{n\to\infty}n^2s_n(T_\rho)=\pi^{-2}\left(\int_{\mathbb R}|\rho(s)|^{1/2}\,ds\right)^2\tag{10}
\]
for any continuous \(\rho\) with \(|\rho(s)|\le C e^{-c|s|}\). An elementary finite-interval estimate is central. If \(\rho\) is bounded and supported on an interval of length \(h\), then for every positive integer \(m\), subdividing that interval into \(m\) equal cells and separating the three exterior rectangles and the off-diagonal cell rectangles gives an approximation to \(T_\rho\) of rank at most \(2m+3\). For an off-diagonal pair of cells, the kernel has the form \(e^{-(s-t)/2}[F(s)-F(t)]\), with \(F'=\rho\); the sum of all such blocks has rank at most \(2m\), since the first term factors through the output cell and the second through the input cell. The three exterior pieces are rank at most one each. On an individual diagonal cell the triangular kernel is bounded in absolute value by \(\|\rho\|_\infty(s-t)\), and its Hilbert--Schmidt norm is at most \(\|\rho\|_\infty h^2/(\sqrt{12}m^2)\). The diagonal-cell errors are orthogonal direct sums, so their operator norm is their maximum. Hence
\[
s_{2m+4}(T_\rho)\le\frac{\|\rho\|_\infty h^2}{\sqrt{12}\,m^2}.\tag{11}
\]
The crude norm estimate \(\|T_\rho\|\le4\|\rho\|_\infty\) (Young's convolution inequality) handles small indices, establishing \(s_n(T_\rho)\le C_0(1+h)^2\|\rho\|_\infty n^{-2}\), with an absolute \(C_0\). The constant is independent of the location of the interval.

If \(\rho\) is stepwise constant on finitely many intervals \(I_j\), all off-diagonal blocks have finite rank by the same factorization. On \(I_j\) itself, the diagonal block is \(\rho_j\) times the triangular kernel \(e^{-(s-t)/2}(s-t)\) for \(t<s\), up to reflection. The difference from the ordinary double Volterra kernel \((s-t)\mathbf 1_{t<s}\) has singular values \(O(n^{-3})\): its second-order Taylor cancellation gives a third-order Volterra factorization with bounded remaining convolution kernel, and three Volterra singular-value bounds \(s_n(J)=O(n^{-1})\) combined with the singular-value product inequality yield the stated order. More explicitly, the Taylor defect \(d(v)=v(e^{-v/2}-1)\) vanishes to order two at zero; its second derivative is bounded on the finite cell, so the defect is \(J^2\) composed with a bounded-kernel Volterra operator, or equivalently a third-order Volterra convolution with bounded amplitude, which is \(O(n^{-3})\). The standard fourth-order boundary problem for \(J^2\) has eigenfrequency roots \(\cos\kappa\cosh\kappa=-1\) and thus \(s_n(J^2)\sim h^2/(\pi^2n^2)\). (This is a classical integration-operator fact; it is also derived by the elementary clamped/free beam equation.) Consequently each nonzero diagonal block has \(s_n\sim |\rho_j||I_j|^2/(\pi^2n^2)\). Adding finitely many blocks and observing that finite-rank perturbations do not alter the coefficient gives
\[
\lim_{n\to\infty}n^2s_n(T_\rho)=\pi^{-2}\left(\sum_j|I_j|\sqrt{|\rho_j|}\right)^2.\tag{12}
\]
Here a finite direct sum of sequences with coefficient \(a_j/n^2\) has counting function asymptotic \(t^{-1/2}\sum_j\sqrt{a_j}\), which proves (12) without an implicit spectral-equidistribution assertion.

For continuous compactly supported \(\rho\), uniform approximation by step functions and (11), combined with the singular-value counting inequalities \(N_{A+B}(t)\le N_A((1-\theta)t)+N_B(\theta t)\) and their reverse versions, yield (10) by first taking \(n\to\infty\), then the step-mesh to zero, and finally \(\theta\to0\). These inequalities keep track of the coefficient: an approximation whose \(\|\rho-\rho_{\mathrm{step}}\|_\infty\) tends to zero has uniformly vanishing weak \(n^{-2}\) coefficient.

For exponential tails, partition each of the two half-lines outside \([-R,R]\) into unit cells \(I_j\), and let \(a_j=\|\rho\|_{L^\infty(I_j)}\le Ce^{-c|j|}\). By (11), each cell contributes \(s_n(T_{\rho 1_{I_j}})\le C_1a_j/n^2\). Subadditivity of ranks (the Ky Fan inequality), allocating ranks in proportion to \(a_j^{1/3}\), gives the tail estimate
\[
\limsup_{n\to\infty}n^2s_n(T_{\rho 1_{|s|>R}})
\le C_2\left(\sum_{|j|>R}a_j^{1/3}\right)^3.\tag{13}
\]
To justify the countably infinite sum, first truncate to \(|j|\le C_3\log n\), give each active cell an additive rank overhead, and bound the remaining operator norm by a geometric series \(o(n^{-2})\); the total overhead is \(O(\log n)=o(n)\). The right side of (13) tends to zero with \(R\). Combining (13) with the compact-support result through the counting inequalities proves (10). Equation (1) now follows from (8)--(10).

**3. Exact maximum.** Write \(p=g'\), so \(0\le p\le L\), \(\int_0^1p=1\), and let \(a(x)=[x(1-x)]^{-1/2}\). Maximizing \(\mathcal W\) is equivalent to maximizing the strictly concave functional \(I(p)=\int_0^1a(x)\sqrt{p(x)}\,dx\). A Lagrange multiplier \(\lambda>0\) shows that the pointwise unique maximizer of \(a\sqrt p-\lambda p\) on \([0,L]\) is
\[
p_*(x)=\min\{L,a(x)^2/(4\lambda^2)\}.
\]
Normalization gives the shape (5) and equation (3). Indeed the function \(2L[\beta+\beta(1-\beta)\log((1-\beta)/\beta)]\) is continuous, strictly increasing from zero to \(L\) as \(\beta\) runs from zero to one half; its derivative equals \(2L(1-2\beta)\log((1-\beta)/\beta)>0\). Thus there is a unique \(\beta_L\). For every competing \(p\), integrate the pointwise optimality inequality at the common mass to obtain \(I(p)\le I(p_*)\). Strict concavity gives almost-everywhere equality only for \(p=p_*\). The optimizer is continuous even at the two interfaces \(\beta_L\) and \(1-\beta_L\); integrating it from zero gives a unique admissible \(g\). Integrating \(a\sqrt{p_*}\) on the two end intervals and the center yields (4).

**4. Exact infimum and nonattainment.** Because \(0\le p\le L\), \(\sqrt p\ge p/\sqrt L\), with equality exactly when \(p\in\{0,L\}\). Therefore
\[
I(p)\ge L^{-1/2}\int_0^1 a(x)p(x)\,dx.
\]
The weight \(a\) is symmetric about one half, strictly decreasing toward its unique minimum there and increasing afterward. The bathtub rearrangement principle (or direct mass exchange between any two points of unequal weight) therefore minimizes the linear integral subject to the mass and cap constraints uniquely almost everywhere at \(p=L\mathbf1_{I_L}\), where \(I_L=[(1-1/L)/2,(1+1/L)/2]\). It follows that
\[
I(p)\ge \sqrt L\int_{I_L}\frac{dx}{\sqrt{x(1-x)}}=2\sqrt L\arcsin(1/L).
\]
The square divided by \(\pi^2\) is (6). For \(L>1\) the unique equality profile jumps at both endpoints of \(I_L\), so no continuous derivative attains the infimum. Convolution smoothing and a small symmetric adjustment of the transition endpoints preserve \(0\le p\le L\) and mass exactly, with integrals converging to this value. For \(L=1\) the mass constraint forces \(p=1\) everywhere.

**5. Growing budget.** At \(L\to\infty\), (3) implies \(\beta_L\sim[2L\log L]^{-1}\): divide the equation by \(2L\beta_L\) and use \(\log(1/\beta_L)=\log L+O(\log\log L)\). The interior contribution in (4) is \(\sqrt{2\log L}(1+o(1))\), while the exterior contribution is \(O((\log L)^{-1/2})\). Squaring gives the first estimate (7). The Taylor expansion \(\arcsin(1/L)\sim 1/L\) gives the second.

## Verification
The standalone `verify.py` uses only Python's standard library. It solves the unique normalization equation (3), evaluates the two coefficients independently by quadrature and by the closed forms (4)/(6), and verifies pointwise multiplier optimality and mass normalization for several derivative caps. It tests the asymptotic scalings and the exact \(L=2\) infimum \(2/9\) without approximating the infinite-dimensional operator by a finite matrix. Run `python verify.py`. The proof of (1)--(7) is analytic; finite numerical tests do not certify a singular-value limit.

## Relationship to prior work
Belli, Gül, Ross and Siskakis (arXiv:2606.08600v1) introduce and analyze the real-variable Cesàro operator \(C\), its norm, spectrum and semigroup representation, not derivative-cap spectral-tail optimization. Their related arXiv:2604.19691 gives the Hilbert-space groundwork; the convolution transform is prior work, not a claimed discovery. Tuan and Gorenflo (1996) and Gorenflo and Samko (1997) study weighted Volterra singular-number asymptotics and could imply the generic pointwise Weyl principle (1). This possibility is explicitly acknowledged: the original claim here is the **two opposite sharp constrained extremal coefficients, uniqueness/nonattainment, their incompatible derivative geometries, and the large-cap law**.

An accessible previously published study of oscillatory-multiplier commutators for the same real-variable \(C\), titled *Phase-velocity thresholds for Cesàro commutators with oscillatory multipliers*, proves compactness and Hilbert–Schmidt thresholds for unimodular phases, not the present second-order coefficient and constrained extremizers. Another previously published entire-determinant result concerns a different, unweighted averaging operator \(x^{-1}\int_0^x f(t)dt\), and does not dominate (4)--(7). General bounded-density bathtub and concave-duality arguments inform the proof, but neither alone identifies the spectral objective for this particular singular integral commutator.

## Limitations
The singular-value law is asserted for each fixed \(g\in C^1\), not uniformly over all admissible profiles. The limiting minimizer at \(L>1\) has a discontinuous derivative and is therefore not an admissible \(C^1\) function; equation (6) is an infimum and is not claimed as an attained minimum. Broad pseudodifferential or classical weighted-Volterra results might reproduce (1) and could, in principle, imply the optimization when combined with elementary convexity arguments. The novelty claim is qualified by that bibliographic risk and is not independently priority-certified. No result about individual finite-index singular-value optimizers or about \(L^p\) with \(p\ne2\) is asserted.

## References
1. A. Belli, U. Gül, W. T. Ross and A. G. Siskakis, *Crescents and the real variable Cesàro operator*, arXiv:2606.08600v1 (first public 2026-06-07), DOI:10.1007/s00020-026-02865-7, full open-access article https://link.springer.com/article/10.1007/s00020-026-02865-7.
2. A. Belli, U. Gül, W. T. Ross and A. G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691v1 (2026-04-21).
3. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461, DOI:10.1080/01630569608816704.
4. R. Gorenflo and S. Samko, *On the dependence of asymptotics of s-numbers of fractional integration operators on weight functions*, Integral Transforms and Special Functions 5 (1997), 191–212, DOI:10.1080/10652469708819136.
5. *Phase-velocity thresholds for Cesàro commutators with oscillatory multipliers*, accessible published-finding corpus scientific finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-phase-velocity-thresholds-for-ces-ro-commutators-with-oscillator--b2f67a1e1e7a.
6. *An entire characteristic determinant for the singular spectrum of the Hardy–Volterra commutator*, accessible published-finding corpus scientific finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-entire-characteristic-determinant-for-the-singular-spectrum-o--2a37cf33f373.
