# A uniquely optimal Gaussian sampling scale for positivity of three-node flat-kernel quadrature

## Finding

Take three independent random nodes from \(N(0,\sigma^2)\), with \(\sigma>0\), and integrate against \(N(0,\tau^2)\), with \(\tau>0\). For the unaugmented Gaussian kernel \(k_h(x,y)=\exp[-h(x-y)^2]\), let \(w_h\in\mathbb R^3\) be the exact Bayesian quadrature weights at distinct nodes, where \(h>0\). Define the relative target variance \(q=\tau^2/\sigma^2\). The almost-sure flat limit \(w_0=\lim_{h\downarrow0}w_h\) equals the weights of the unique degree-two-exact interpolatory rule.

Let \(\phi\) and \(\Phi\) be the standard normal density and distribution function. The probability that *all three* limiting weights are strictly positive is exactly
\[
P(q)=12\int_0^\infty\phi(u)\left[\Phi(q/u)-\tfrac12\right]\left[1-\Phi(q/u)\right]du,\qquad q>0.
\]
The function \(t\mapsto P(e^t)\) is **strictly log-concave** on \(\mathbb R\), and tends to zero at both ends. It therefore has exactly one maximizer. More precisely, the uniquely optimal relative variance \(q_*\) is the positive root of
\[
\int_0^\infty\frac{\phi(u)\phi(q/u)}{u}\left[\tfrac32-2\Phi(q/u)\right]du=0.
\]
Numerical quadrature gives \(q_*\approx0.393094362591\), \(P(q_*)\approx0.246970587655\), while \(P(1)\approx0.178147324601\). Thus optimizing the Gaussian proposal scale still makes simultaneous positive weights a roughly one-in-four event in the flat-kernel limit; matching the proposal variance to the Gaussian integration target is suboptimal for this positivity criterion.

For every fixed three distinct nodes and every fixed positive target variance, all three Gaussian-kernel weights are strictly positive for all sufficiently large \(h\). Consequently \(\lim_{h\to\infty}\Pr(w_h>0\text{ coordinatewise})=1\), whereas \(\lim_{h\downarrow0}\Pr(w_h>0\text{ coordinatewise})=P(q)\). The positivity criterion is distinct from numerical integration accuracy or an optimum over kernel shapes.

## Assumptions and scope

All random nodes are independent, exactly Gaussian, and sampled once. The integration target is a centered Gaussian. The kernel has a common strictly positive inverse-squared-lengthscale and no polynomial augmentation, nugget, positivity projection, or additional samples. The weights solve \(K_h w_h=v_h\), with \((K_h)_{ij}=\exp[-h(X_i-X_j)^2]\), and
\[
(v_h)_i=\int k_h(X_i,y)\,dN(0,\tau^2)(y)
=\frac{\exp[-h X_i^2/(1+2h\tau^2)]}{\sqrt{1+2h\tau^2}}.
\]
Almost surely the nodes are distinct, so each kernel matrix is strictly positive definite. All positivity assertions use exact real arithmetic. The flat limit is taken for fixed nodes before sampling probabilities; the high-shape assertion is also pointwise for fixed nodes. No uniform rate in nearly-colliding nodes is asserted. The source of the flat-limit theorem is acknowledged below, rather than presented as original.

## Proof

**1. Flat-limit reduction and exact signs.** For any fixed distinct three nodes, the established flat Gaussian-kernel quadrature theorem [3] makes \(w_h\) converge to the unique interpolatory rule integrating \(1,x,x^2\) exactly. Divide all nodes by \(\sigma\), sort them as \(a<b<c\), and put \(q=\tau^2/\sigma^2\). The degree-two-exact Lagrange weights are
\[
W_a=\frac{q+bc}{(a-b)(a-c)},\quad
W_b=\frac{q+ac}{(b-a)(b-c)},\quad
W_c=\frac{q+ab}{(c-a)(c-b)}.
\]
Here the first and last denominators are positive and the middle one is negative. Therefore all three weights are positive if and only if
\[
q+bc>0,\qquad q+ac<0,\qquad q+ab>0.
\]
The strict middle inequality forces \(a<0<c\). If \(a=-u\) and \(0<b<c\), the other conditions reduce to \(0<b<q/u<c\). Reflecting all nodes yields the analogous case of two negative nodes and one positive node. Weight zeros occur only on algebraic hypersurfaces and therefore have probability zero under the joint Gaussian density.

**2. Exact probability.** In the first sign pattern, choose the negative node from three labeled observations (three choices), place the two positive observations one below and one above \(q/u\) (two assignments), and integrate the magnitude \(u>0\) of the negative node against its standard normal density. The reflected sign pattern doubles this probability. This yields the displayed factor \(3\cdot2\cdot2=12\) and the integral formula for \(P(q)\). The integral is positive and continuous for every \(q>0\). Pointwise its integrand tends to zero at both \(q\downarrow0\) and \(q\to\infty\), with integrable bound \(\phi(u)/4\), proving \(P(q)\to0\) at both ends by dominated convergence.

**3. Strict log-concavity and uniqueness.** Let \(Z\sim N(0,1)\) and \(Y=\log|Z|\). Its density and CDF are
\[
g(y)=\sqrt{2/\pi}\,\exp[y-e^{2y}/2],\qquad F(y)=2\Phi(e^y)-1.
\]
Write \(S=1-F\). Substituting \(u=e^v\) in the preceding integral gives the *exact convolution identity*
\[
P(e^t)=\frac32\int_{\mathbb R}g(v)F(t-v)S(t-v)\,dv.
\]
The density \(g\) is positive on the real line and strictly log-concave because \((\log g)''(y)=-2e^{2y}<0\). Both \(F\) and \(S\) are strictly log-concave as well. Here is a direct verification of the relevant strict hazard monotonicity: for \(u>0\), the ratio \(g(y-u)/g(y)\) strictly increases with \(y\), since \((\log g)'(y-u)>(\log g)'(y)\). Integrating this ratio over \(u>0\) proves \(F(y)/g(y)\) strictly increasing, so the reversed hazard \(g/F=(\log F)'\) strictly decreases. Similarly \(g(y+u)/g(y)\) strictly decreases with \(y\), proving \(S/g\) strictly decreasing and the hazard \(g/S=-(\log S)'\) strictly increasing. Thus \(F\), \(S\), and their product \(FS\) are strictly log-concave and positive. Their product is integrable, since it decays as the smaller of the two tails. The standard strict convolution property for positive full-support log-concave functions (the one-dimensional Prékopa–Leindler inequality, with strictness from the factor densities) makes \(g*(FS)\) strictly log-concave. Therefore \(t\mapsto P(e^t)\) is strictly log-concave. Its vanishing at both ends and positivity ensure a unique global maximizer.

**4. Critical equation and endpoint limits.** Differentiation under the integral, first for \(q\) in a compact subinterval of \((0,\infty)\), gives
\[
P'(q)=12\int_0^\infty\frac{\phi(u)\phi(q/u)}{u}\left[\tfrac32-2\Phi(q/u)\right]du.
\]
The integrand is integrable near zero by Gaussian decay in \(q/u\) and near infinity by the \(u^{-1}\phi(u)\) factor. Uniqueness of the maximizer proves the derivative equation has a unique positive solution, and the reported decimals follow by one-dimensional numerical quadrature. For fixed distinct nodes, \(K_h\to I_3\) as \(h\to\infty\) and every component of \(v_h\) remains positive. More quantitatively \((K_h)_{ij}\to0\) for \(i\ne j\) while \((v_h)_i>0\) and these components share the same polynomial-order \(h^{-1/2}\) decay for fixed nodes, so the corrections \((K_h^{-1}-I_3)v_h\) are negligible relative to each component of \(v_h\). Consequently \(w_h>0\) for all sufficiently large \(h\). At the flat endpoint, almost surely the limiting polynomial weights have nonzero entries, so their signs eventually agree with those of \(w_h\); bounded convergence then yields the two stated probability limits.

## Verification

Run \(\texttt{python verify.py}\) with Python 3, NumPy, SciPy, and mpmath installed. The standalone checker independently integrates the one-dimensional Gaussian probability and derivative, checks moment-exact Lagrange weights, compares exact event inequalities with direct independent Monte Carlo draws, verifies approximate root and probability values, and checks high-precision convergence of four fixed-node Gaussian-kernel rules to their polynomial limits. It passed 30,122 finite assertions. These experiments are reproducibility checks, not a proof of global uniqueness, strict log-concavity, or any infinite-parameter assertion.

## Relationship to prior work

Huszár and Duvenaud [1] connect optimally weighted kernel herding with Bayesian quadrature; the kernel-weight framework and possibility of signed weights are established prior art. Karvonen, Kanagawa, and Särkkä [2] analyze Bayesian-quadrature weight positivity, including numerical tests with randomly sampled points; their results do not give this exact Gaussian three-node, variable-proposal-scale probability. Karvonen and Särkkä [3] prove the fixed-node flat-kernel-to-polynomial convergence, including Gaussian integration on an unbounded domain; that essential reduction is entirely pre-existing. Their scaled Gauss–Hermite-node work [4] studies deterministic scaled nodes rather than independent Gaussian nodes.

Published mathematical notes on uniform random-node *feasibility* of positive quadratic rules [5], Gaussian three-node *affine least-norm* weight positivity [6], and three symmetric fixed nodes on a *bounded* interval with Gaussian kernel [7] address different event definitions, solver choices, integration targets, or node laws. In particular, [5] allows any strictly positive representation, whereas here all three weights of the *unique degree-two-interpolatory rule* must be positive. Their methods and statements do not imply the present exact Gaussian proposal-scale optimization or uniqueness result. General log-concavity and polynomial interpolation facts are standard and not claimed as original.

## Limitations

The maximal probability concerns simultaneous positivity only in the flat-kernel limit, not the finite-bandwidth optimum, integration error, robustness near colliding nodes, or higher numbers of nodes. The reported numerical optimum is approximate; the derivative integral defines the exact optimum. The theorem uses independent one-dimensional Gaussian sampling and Gaussian integration and does not assert distribution-free universality. Although closest known published texts and mathematical records were compared, an unindexed equivalent result remains a historical-priority risk. No independent external mathematical audit has been performed.

## References

[1] F. Huszár and D. Duvenaud, *Optimally-Weighted Herding is Bayesian Quadrature*, arXiv:1204.1664, first public 2012-04-07. https://arxiv.org/abs/1204.1664

[2] T. Karvonen, M. Kanagawa, and S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, arXiv:1812.08509, first public 2018-12-20. https://arxiv.org/abs/1812.08509

[3] T. Karvonen and S. Särkkä, *Worst-case optimal approximation with increasingly flat Gaussian kernels*, arXiv:1906.02096, first public 2019-06-05, Theorem 2.4 and subsequent Gaussian-integration example. https://arxiv.org/abs/1906.02096

[4] T. Karvonen and S. Särkkä, *Gaussian Kernel Quadrature at Scaled Gauss–Hermite Nodes*, arXiv:1803.09532, first public 2018-03-26. https://arxiv.org/abs/1803.09532

[5] *Exact random-node feasibility and a two-mechanism phase transition for positive quadratic quadrature* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-random-node-feasibility-and-a-two-mechanism-phase-transiti--03159ea86990

[6] *A density-universal collision law and exact Gaussian positivity benchmark for affine least-squares quadrature* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-density-universal-collision-law-and-exact-gaussian-positivity--c97a80bc1618

[7] *A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-one-crossing-positivity-diagram-for-symmetric-three-node-gauss--bf59562e8e52
