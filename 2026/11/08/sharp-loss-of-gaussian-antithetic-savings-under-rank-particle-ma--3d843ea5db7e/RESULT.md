# Sharp loss of Gaussian antithetic savings under rank particle matching

## Finding

In one-dimensional Gaussian particle diffusion, sorting two particle ensembles and pairing equal ranks is optimal for *total distance* but can discard essentially all of the **available integrated antithetic variance reduction**. This remains true with equal strictly positive particle masses, where the sign-switched antithetic rule is simply Gaussian reflection. The exact sharp normalized single-stage variance-savings ceiling is \(\sqrt2-1\); a shifted lattice makes rank matching lose all its savings asymptotically while a cyclic matching approaches that ceiling as the number of particles grows.

More precisely, for every \(N\ge2\), equal positive mass \(m>0\), scale \(\sigma>0\), and arbitrary finite real starting positions, every bijective independent-pair reflected coupling has integrated variance reduction \(G_\pi\) satisfying
\[
0<G_\pi\le (\sqrt2-1)I,\qquad I=\frac{Nm^2\sigma}{2\sqrt\pi}.
\]
Equality in the upper bound holds when matched starting positions coincide. For the ordered translated grids
\[
a_i=(i-1)L,\quad b_i=iL,\qquad 1\le i\le N,\quad L>0,
\]
rank pairing yields \(G_{\rm rank}=Nm^2 h_\sigma(L)/4\), whereas matching the \(N-1\) common grid points and pairing the two unmatched endpoints gives
\[
G_{\rm cyc}=\frac{m^2}{4}\bigl((N-1)h_\sigma(0)+h_\sigma(NL)\bigr),\quad
h_\sigma(d)=\mathbb E|d+2\sigma Z|-\mathbb E|d+\sqrt2\sigma Z|.
\]
The cyclic matching is the unique maximizing matching if \(h_\sigma(L)<h_\sigma(0)/2\), and hence
\[
\lim_{L/\sigma\to\infty}\frac{G_{\rm rank}}{I}=0,\qquad
\lim_{L/\sigma\to\infty}\frac{\max_\pi G_\pi}{I}=
\left(1-\frac1N\right)(\sqrt2-1).
\]
Thus the difference in achievable savings, **as a fraction of the original integrated variance**, is nonvanishing; the limit approaches \(41.42\%\) on taking large \(N\). The Gaussian gain kernel also changes from concave to convex at the exact positive separation \(2\sigma\sqrt{\log2}\), explaining why minimizing total separation is not the appropriate variational principle.

## Assumptions and scope

Fix an integer \(N\ge2\), real \(a_1,\ldots,a_N,b_1,\ldots,b_N\), equal positive masses \(m\), and \(\sigma>0\). In the first simulation set \(X_i^A=a_i+\sigma Z_i\), with independent standard Gaussians; in the second set \(X_j^B=b_j+\sigma W_j\). With no coupling between simulations, all \(Z_i,W_j\) are independent. A matching is a bijection \(\pi:\{1,\ldots,N\}\to\{1,\ldots,N\}\) matching particle \(j\) of simulation B with particle \(\pi(j)\) of simulation A; a reflected coupling sets \(W_j=-Z_{\pi(j)}\). Different matched pairs remain independent.

At observation point \(x\in\mathbb R\), define the pair-average cumulative field
\[
\bar U(x)=u_-+\frac m2\sum_{i=1}^N\mathbf1\{X_i^A\le x\}+\frac m2\sum_{j=1}^N\mathbf1\{X_j^B\le x\}.
\]
Define \(I=\int_{\mathbb R}\operatorname{Var}_{\rm independent}\bar U(x)\,dx\) and \(G_\pi=I-\int_{\mathbb R}\operatorname{Var}_{\pi}\bar U(x)\,dx\). The integrals are finite because each Gaussian indicator variance and matched-pair covariance is integrable. All claims concern the conditional variance over this *one Gaussian diffusion stage*, given the positions, not total unconditional variance after earlier random steps, nor arbitrary correlations among distinct matched pairs. The choice of \(u_-\) does not affect variances.

## Proof

**1. The exact pairwise kernel.** Set \(g_t(d)=\mathbb E|d+tZ|\), where \(Z\sim N(0,1)\). For \(t>0\), with \(\phi\) and \(\Phi\) denoting the standard Gaussian density and distribution,
\[
g_t(d)=2t\phi(d/t)+d(2\Phi(d/t)-1),\qquad
\frac{\partial g_t}{\partial d}=2\Phi(d/t)-1.
\]
For an independent partner \(Y'=b+\sigma Z'\), the distance \(X-Y'\) has law \(d+\sqrt2\sigma Z\), where \(d=a-b\). Under reflection, \(X-Y\) has law \(d+2\sigma Z\). The integrated indicator-covariance identity
\[
\int_{\mathbb R}\operatorname{Cov}(\mathbf1\{X\le x\},\mathbf1\{Y\le x\})\,dx
=\frac12\left(\mathbb E|X-Y'|-\mathbb E|X-Y|\right)
\]
follows from integrating \(\mathbf1\{X\le x<Y\}+\mathbf1\{Y\le x<X\}\) and subtracting the corresponding independent quantities. Consequently, each reflected matched pair lowers the integrated variance of the pair-average field by \(m^2h_\sigma(d)/4\), with
\[
h_\sigma(d)=g_{2\sigma}(d)-g_{\sqrt2\sigma}(d).
\]
Independence between distinct pairs makes reductions additive: \(G_\pi=(m^2/4)\sum_jh_\sigma(a_{\pi(j)}-b_j)\). This also independently reconstructs the Gaussian specialization of the pair-gain formula in Abkin–Daripa, Corollary 4.8.

**2. Positivity, sharp maximum and curvature.** For \(d>0\),
\[
h_\sigma'(d)=2\bigl(\Phi(d/(2\sigma))-\Phi(d/(\sqrt2\sigma))\bigr)<0,
\]
so \(h_\sigma\) is even, strictly decreasing in positive separation and tends to zero at infinity. Its maximum is
\[
h_\sigma(0)=(2-\sqrt2)\sigma\sqrt{2/\pi}.
\]
It is strictly positive for finite \(d\): for fixed \(d\), the map \(t\mapsto\mathbb E|d+tZ|\) increases strictly for \(t>0\), with derivative \(2\phi(d/t)>0\). Its second derivative in separation is
\[
h_\sigma''(d)=\frac1\sigma\left[\phi(d/(2\sigma))-\sqrt2\phi(d/(\sqrt2\sigma))\right].
\]
This is strictly negative for \(|d|<2\sigma\sqrt{\log2}\), vanishes on the boundary and is strictly positive for larger \(|d|\); in particular the distance-optimization cost \(h_\sigma(0)-h_\sigma(d)\) is not globally concave.

For one Gaussian indicator \(\chi_x=\mathbf1\{a+\sigma Z\le x\}\), let \(X'\) be an independent copy. Then
\[
\int_{\mathbb R}\operatorname{Var}\chi_x\,dx=\tfrac12\mathbb E|X-X'|=\sigma/\sqrt\pi.
\]
There are \(2N\) independent indicators, each with coefficient \(m/2\), giving \(I=Nm^2\sigma/(2\sqrt\pi)\). Bounding each kernel term by \(h_\sigma(0)\) yields
\[
\frac{G_\pi}{I}\le\frac{h_\sigma(0)\sqrt\pi}{2\sigma}=\sqrt2-1.
\]
Equality holds for coincident matched positions, and strict inequality holds if any pair has nonzero separation. This is a sharp ceiling *within the stated reflected independent-pair class*.

**3. Shifted grids and asymptotic optimality.** Take \(a_i=(i-1)L\) and \(b_i=iL\). Rank matching pairs distances all equal to \(L\). The cyclic bijection \(\pi(j)=j+1\) for \(j<N\), \(\pi(N)=1\), pairs \(N-1\) identical locations and one pair distance \(NL\), giving the two claimed exact formulas. There are at most \(N-1\) coincident pairs under any bijection: location zero in the first ensemble has no identical partner in the second. The cyclic matching is the **only** bijection with \(N-1\) coincidences. A different matching has at most \(N-2\) coincidences, and all noncoincident grid separations are at least \(L\). Thus, if \(h_\sigma(L)<h_\sigma(0)/2\), its total kernel reward is at most
\[
(N-2)h_\sigma(0)+2h_\sigma(L)<(N-1)h_\sigma(0),
\]
strictly below the cyclic reward. This proves uniqueness. Since \(h_\sigma(L)\to0\) and \(h_\sigma(NL)\to0\) for fixed \(N\), the rank and optimal asymptotics follow on dividing by \(I\). The double regime (first large \(L/\sigma\), then large \(N\)) approaches the universal sharp savings ceiling, whereas rank matching has limiting savings zero.

## Verification

The standalone `verify.py` computes the gain kernel from Gaussian absolute moments, compares its analytic integral-covariance identity with independent numerical integration, and exhaustively checks all permutations for several small lattice sizes and separations. It also verifies the sharp constant, the numerical sufficient uniqueness threshold, and the curvature sign change. Run using a standard Python 3 interpreter with no external dependencies: `python verify.py`. These finite checks are supplementary; the universal quantifiers and optimality are proved above, not inferred from enumeration.

For instance, at \(\sigma=m=1\), the per-pair maximal kernel reward is \(h_1(0)\approx0.4673899545\), the curvature transition is \(2\sqrt{\log2}\approx1.6651092223\), and the sufficient uniqueness condition \(h_1(L)<h_1(0)/2\) begins at \(L\approx1.994115508\). For \(N=2\), the optimal asymptotic savings are \((\sqrt2-1)/2\approx0.20710678\) of the independent integrated variance while rank savings vanish.

## Relationship to prior work

Abkin and Daripa (2026), Proposition 3.1 and Corollary 4.8, establish the optimal reflection/sign rule **for a fixed matched pair** and its integrated variance contribution. Their Remark 4.7 shows rank matching minimizes total absolute partner distance. The present result changes the optimization variable to the **permutation of partners** and shows that distance-optimal rank pairing is not variance-optimal, in fact may lose a sharp nonvanishing fraction of potential savings. Their paper compares rank switching with within-sign pairing but does not state this adversarial shifted-grid matching law or the exact \(\sqrt2-1\) ceiling for the equal-mass all-positive reflected class.

Nüsken and Pavliotis (2018/2019) formulate coupling optimization via transport for interacting samplers and treat mirror couplings; they do not specialize to the Gaussian cumulative-field one-stage kernel and rank-vs-cyclic finite assignment law. Delon, Salomon, and Sobolevski (2011) analyze line matchings with **concave** distance-type costs; the present variance reward corresponds to a cost that changes curvature sign, so their concavity hypotheses do not directly establish this result. Classical maximum-weight bipartite assignment theory supplies the general computational framework, not the sharp Gaussian loss construction or variance constant.

## Limitations

This is not a claim that rank matching is always inferior, that the shifted configurations are typical, or that changing pairing at one diffusion step necessarily improves *unconditional full-trajectory* variance for nonlinear fluxes. All particles have identical positive masses, the two simulations share the same diffusion scale, the estimator is a pair-average cumulative field integrated over the full real line, and different reflected matched pairs are independent. The sharp upper bound is for this restricted coupling class; richer couplings could have different limits. A strict uniqueness condition is supplied, not an exact threshold for every finite \(N\) and \(L\). Priority risk remains that a general older rearrangement theorem or a different representation of the same Gaussian assignment law may subsume the statement.

## References

1. S. Abkin and P. Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection–diffusion equations*, arXiv:2610.01120v1 (first public version: 2026-10-01); see also v2 (2026-10-12), Proposition 3.1, Remark 4.7, and Corollary 4.8. https://arxiv.org/abs/2610.01120
2. N. Nüsken and G. A. Pavliotis, *Constructing sampling schemes via coupling: Markov semigroups and optimal transport*, arXiv:1806.11026 (2018), SIAM/ASA Journal on Uncertainty Quantification 7 (2019), 324–382. https://arxiv.org/abs/1806.11026
3. J. Delon, J. Salomon, and A. Sobolevski, *Minimum-weight perfect matching for non-intrinsic distances on the line*, arXiv:1102.1558 (2011), Journal of Mathematical Sciences 181 (2012), 782–791. https://arxiv.org/abs/1102.1558
