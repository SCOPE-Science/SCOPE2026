# Weibull near-regularity threshold for maximal cyclic spacing among random circular subsets

## Finding

Fix an integer \(m\ge2\). For each \(n\ge m\), let \(U_1,\ldots,U_n\) be independent points on the circle \(\mathbb T=\mathbb R/\mathbb Z\) with a common strictly positive, periodic Lipschitz probability density \(f\). For each \(m\)-point subset, take its \(m\) clockwise circular spacings; let \(S_{n,m}\) be the maximum, over all subsets, of the smallest spacing, and set \(\Delta_{n,m}=1/m-S_{n,m}\). Define
\[
J_m(f)=\int_0^1\prod_{j=0}^{m-1}f(u+j/m)\,du,
\qquad
\Lambda_m(x)=\frac{m^{m-1}J_m(f)}{m!}x^{m-1}.
\]
Then for every fixed \(x\ge0\),
\[
\boxed{\lim_{n\to\infty}\Pr\{n^{m/(m-1)}\Delta_{n,m}>x\}=e^{-\Lambda_m(x)}.}
\]
Equivalently, the rescaled optimal-spacing deficit converges to the Weibull distribution with survival function \(e^{-\Lambda_m(x)}\). More precisely, let \(W_{n,m}(x)\) count all \(m\)-point subsets with every clockwise gap at least \(1/m-xn^{-m/(m-1)}\). Then
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(W_{n,m}(x)),\operatorname{Poisson}(\Lambda_m(x))\bigr)
=O_{m,f,x}\bigl(n^{-1/(m-1)}\bigr).}
\]
For uniformly distributed points the probability that one specified \(m\)-point subset satisfies the threshold \(1/m-\varepsilon\), for any \(0\le\varepsilon\le1/m\), is **exactly** \((m\varepsilon)^{m-1}\); consequently the finite-sample expected number is exactly \(\binom nm(m\varepsilon)^{m-1}\).

The nonuniform constant distinguishes sampling environments with the same one-point support. For \(f_{a,k}(u)=1+a\cos(2\pi k u)\), \(0<|a|<1\), \(k\) a positive integer, the leading constant is suppressed below its uniform value if \(m\nmid k\) and enhanced above it if \(m\mid k\). For \(m=3\), explicitly,
\[
J_3(f_{a,k})=\begin{cases}1+\tfrac32a^2,&3\mid k,\\1-\tfrac34a^2,&3\nmid k.\end{cases}
\]
This harmonic-product identity is a known form of circular sampling resonance and is not asserted to be new in isolation; the new claim concerns its appearance in the **growing-sample optimal-subset Weibull law**.

## Assumptions and scope

The circle has circumference one. The integer \(m\) is fixed before \(n\to\infty\). The density \(f:\mathbb T\to(0,\infty)\) is Lipschitz, normalized by \(\int_0^1f=1\), and is independent of \(n\). Any \(m\) distinct sampled points have clockwise gaps \(G_1,\ldots,G_m>0\) summing to one. Their smallest gap is at most \(1/m\), with equality exactly for a rotated regular \(m\)-gon. Sample collisions have probability zero. The count and scaling refer to **arbitrary selected subsets**, not to \(m\) consecutive observations among the circular order statistics. The rate is for each fixed \(x\), with a constant depending on \(m,f,x\); no claim uniform in growing \(m\) is made.

## Proof

**1. A small-simplex identity for one subset.** Fix \(0<\varepsilon<1/m\) and a labelled \(m\)-point sample. Start at its first labelled point \(U_1=u\), and write the clockwise ordered positions of the remaining points as \(u+s_1,\ldots,u+s_{m-1}\), with \(0<s_1<\cdots<s_{m-1}<1\). Put \(s_0=0\), \(s_m=1\), and \(g_j=s_j-s_{j-1}\). In these coordinates the joint density, integrated over the circle and ordered positions, is
\[
(m-1)!\prod_{j=0}^{m-1}f(u+s_j).
\]
The event \(g_j\ge1/m-\varepsilon\) for all \(j\) is equivalent to
\[
g_j=1/m-\varepsilon+m\varepsilon v_j,
\qquad v_j\ge0,\quad\sum_{j=1}^m v_j=1.
\]
The Jacobian on the first \(m-1\) coordinates is \((m\varepsilon)^{m-1}\), and the uniform Dirichlet simplex has coordinate density \((m-1)!\). Consequently, with \(V\sim\operatorname{Dirichlet}(1,\ldots,1)\),
\[
\Pr\{\min_jg_j\ge1/m-\varepsilon\}
=(m\varepsilon)^{m-1}
\mathbb E_V\int_0^1
\prod_{j=0}^{m-1}f\left(u+\frac jm+m\varepsilon\sum_{i=1}^j\left(V_i-\frac1m\right)\right)du.
\]
(The empty sum for \(j=0\) is zero.) Uniform continuity gives a leading factor \(J_m(f)\), while Lipschitz regularity makes the relative error \(O_{m,f}(\varepsilon)\). For \(f\equiv1\) the expectation is identically one, proving the exact uniform identity for all \(\varepsilon\) in its stated range.

**2. The rare-subset intensity.** Put \(\varepsilon=xn^{-m/(m-1)}\). For \(x>0\) and sufficiently large \(n\), the preceding formula gives
\[
p_n:=\Pr\{\min_jg_j\ge1/m-\varepsilon\}
=(m\varepsilon)^{m-1}\bigl[J_m(f)+O_{m,f}(\varepsilon)\bigr].
\]
Thus the mean \(\lambda_n=\binom nm p_n\) satisfies
\[
\lambda_n=\Lambda_m(x)+O_{m,f,x}(n^{-1}),
\]
since the factorial-ratio correction is \(O(n^{-1})\), and \(\varepsilon=o(n^{-1})\) when \(m\ge2\). Positivity of \(J_m(f)\) makes the limit nondegenerate.

**3. Joint events for overlapping subsets.** Let \(A_I\) be the threshold event for an \(m\)-subset \(I\). If \(A_I\) holds, every circular gap of \(I\) lies in
\[
[1/m-\varepsilon,\;1/m+(m-1)\varepsilon],
\]
because the gaps sum to one. Fix any point of \(I\) as an angular anchor. Every other point of \(I\) must lie within \((m-1)^2\varepsilon\) of one of the \(m-1\) non-anchor regular vertices at offsets \(j/m\). Hence, for two distinct subsets \(I,J\) sharing exactly \(k\) labels, where \(1\le k<m\), conditioning on a shared anchor forces all \(2m-k-1\) remaining independently sampled points into a deterministic union of arcs of total length at most \(C_m\varepsilon\). Boundedness of \(f\) then gives
\[
\Pr(A_I\cap A_J)\le C_{m,f}\varepsilon^{2m-k-1}.
\]
The bound is deliberately not claimed sharp for individual overlap types; it is sufficient for Poisson approximation.

**4. Dependency-graph Poisson approximation.** In \(W_{n,m}(x)=\sum_{|I|=m}\mathbf1_{A_I}\), events for disjoint label sets are independent. Give each \(I\) the dependency neighborhood of subsets intersecting \(I\). The two standard Arratia--Goldstein--Gordon terms satisfy
\[
\begin{aligned}
b_1&=O_{m,f,x}(n^{2m-1}\varepsilon^{2m-2})=O(n^{-1}),\\
b_2&\le\sum_{k=1}^{m-1}O_{m,f,x}(n^{2m-k}\varepsilon^{2m-k-1})
=O_{m,f,x}(n^{-1/(m-1)}).
\end{aligned}
\]
The last equality follows because the exponent of \(n\) for overlap size \(k\) is exactly \(-(m-k)/(m-1)\). There is no conditional-dependence remainder: independent label sets carry independent coordinates. The classical dependency-graph Poisson inequality therefore yields
\[
d_{\mathrm{TV}}\bigl(\mathcal L(W_{n,m}(x)),\operatorname{Poisson}(\lambda_n)\bigr)
\le C_{m,f,x}(b_1+b_2).
\]
Combining with \(|\lambda_n-\Lambda_m(x)|=O(n^{-1})\) and the standard Poisson coupling bound proves the displayed rate. For \(x=0\), every event has probability zero, so \(W_{n,m}(0)=0\) almost surely and the same conclusion is immediate.

**5. The optimal-deficit distribution.** The defining maximum implies, for \(x\ge0\),
\[
\{n^{m/(m-1)}\Delta_{n,m}>x\}=\{W_{n,m}(x)=0\}
\quad\text{almost surely},
\]
since equality to a deterministic threshold has probability zero under the continuous density. Taking zero-count probabilities in step 4 gives the limit \(e^{-\Lambda_m(x)}\).

**6. Dependence on sampling density.** For \(f_{a,k}(u)=1+a\cos(2\pi k u)\), if \(m\nmid k\), the arithmetic mean of \(f_{a,k}(u+j/m)\) over \(j\) is exactly one, while the factors are not almost everywhere identical. Strict arithmetic--geometric mean yields \(J_m<1\). If \(m\mid k\), all factors coincide, and strict Jensen yields \(J_m=\int_0^1 f_{a,k}(u)^mdu>1\). For \(m=3\), expanding the trigonometric product and integrating gives \(1+3a^2/2\) in the resonant case and \(1-3a^2/4\) otherwise. These are formulas for the already-known regular-polygon density product; the Poisson theorem establishes their role in the present growing-sample optimization problem.

## Verification

Run `python3 check.py` with the Python 3 standard library. The script checks rotational invariance and exact event/count equivalence on finitely many deterministic configurations, verifies the harmonic coefficient for fifteen frequencies against numerical circle integration, tests finite-sample intensity algebra, and compares the one-subset exact uniform probability with 390,000 seeded Bernoulli observations. Its recorded status is `PASS: 321 deterministic assertions, plus 390000 seeded Bernoulli trials`. These checks validate implementation details, not the all-\(n\) Poisson approximation, which follows from Steps 1--5.

## Relationship to prior work

Cunden, Cuppone, Gramegna and Vivo (2026) study maximizing minimum spacing among a selection of random points **on a line**, with fixed extreme endpoints and a renewal/reset-walk formulation. Their open-access paper does not state a growing-sample, fixed-subset-size, near-regular cyclic-packing limit, nor the independent-label overlap estimate here. Nikitin and Simarova (2022) prove broad Weibull limits for smooth circular U-max kernels with nondegenerate Hessians; the minimum-angular-gap kernel in this theorem is only piecewise linear at its regular-polygon maximum, so their differentiability Condition A5 fails and their quadratic-Hessian scaling does not imply the present \(n^{m/(m-1)}\) rate. Their general Poisson-approximation framework is classical prior technique and is explicitly credited.

A prior exact random-circle Rips-loop result (identifier `2026/11/1/SCOPE-quadratic-onset-and-harmonic-resonance-of-nonuniform-random-circ--d6f6950242b9`) already identifies the density product \(J_m(f)\) and its harmonic resonance in a **fixed-number-of-points** coverage/topology event with an upper gap bound. Neither its fixed-size probability nor its conditional gap-shape limit asserts the \(n\to\infty\) Poisson count of near-regular **chosen subsets**, or the min-gap optimum studied here. The harmonic-product phenomenon itself is not claimed as new. A related circular scan result (identifier `2026/10/12/SCOPE-first-signed-finite-size-correction-for-rare-circular-scan-clust--01f619f9c5ed`) treats tight clusters of \(k\) **consecutive** circular sample points, minimizing their arc span; its rare event is the opposite spatial geometry from a well-separated optimal \(m\)-subset. Classical Poisson approximation and earlier geometric U-max results remain the technical basis, not new ingredients.

## Limitations

The subset size \(m\) and density \(f\) are fixed, with \(f\) Lipschitz and strictly positive. The rate statement is for fixed \(x\), with unspecified constants; it is not a nonasymptotic universal bound over all parameters or a growing-\(m\) limit. The exact subset probability requires uniform sampling; under nonuniform sampling only its small-deficit asymptotic is asserted. No full point-process limit for orientations, no optimal algorithm, and no universality for singular sampling laws is claimed. General geometric U-max and circle-coverage literature is extensive; a historically implicit equivalent may remain unlocated. This theorem has not received an independent mathematical audit.

## References

1. F. D. Cunden, N. Cuppone, G. Gramegna, P. Vivo, *Maximal Minimal Spacing for Random Points*, arXiv:2606.04837v1, first posted 2026-06-03, https://arxiv.org/abs/2606.04837; Journal of Statistical Physics **193** (2026), article 118, https://doi.org/10.1007/s10955-026-03680-5.
2. Ya. Yu. Nikitin, E. N. Simarova, *Generalized Limit Theorems For U-max Statistics*, arXiv:2010.04460 (2020); Journal of Applied Probability **59** (2022), 825--848, https://arxiv.org/abs/2010.04460.
3. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen--Stein method*, Annals of Probability **17** (1989), 9--25, https://doi.org/10.1214/aop/1176991491.
4. *Quadratic onset and harmonic resonance of nonuniform random-circle Rips loops*, published mathematical record (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-quadratic-onset-and-harmonic-resonance-of-nonuniform-random-circ--d6f6950242b9.
5. *First signed finite-size correction for rare circular scan clusters*, published mathematical record (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-first-signed-finite-size-correction-for-rare-circular-scan-clust--01f619f9c5ed.
