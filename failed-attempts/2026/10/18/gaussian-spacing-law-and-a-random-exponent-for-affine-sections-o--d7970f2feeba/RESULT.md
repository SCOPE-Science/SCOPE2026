# Gaussian-spacing law and a random exponent for affine sections of regular simplices

## Finding

Let \(m\ge3\) and let \(S_m\) be a regular \((m-1)\)-simplex with \(m\) vertices. Sample an oriented affine hyperplane from Euclidean-motion-invariant measure in the affine span of \(S_m\), conditional on meeting the simplex. Let \(N_m\) be the number of vertices of its generic \((m-2)\)-dimensional section. Let \(Z_1,\ldots,Z_m\) be independent standard Gaussian variables, \(Z_{(1)}<\cdots<Z_{(m)}\) their ordered sample, \(R_m=Z_{(m)}-Z_{(1)}\), and \(\Phi\) the standard normal cumulative distribution function.

There is a rank \(K_m\in\{1,\ldots,m-1\}\) such that \(N_m=K_m(m-K_m)\), with **exact probabilities**
\[
\Pr(K_m=k)=\frac{\mathbb E[Z_{(k+1)}-Z_{(k)}]}{\mathbb E R_m}
=\frac{\binom mk\displaystyle\int_{-\infty}^{\infty}\Phi(x)^k[1-\Phi(x)]^{m-k}\,dx}
{\displaystyle\int_{-\infty}^{\infty}\left[1-\Phi(x)^m-(1-\Phi(x))^m\right]dx},
\quad 1\le k<m.
\tag{1}
\]
Each displayed integral is finite and strictly positive; the probabilities sum to one. When \(k\ne m-k\), the section-vertex probability at \(k(m-k)\) is the sum of the two symmetric rank probabilities. Thus (1) specifies the complete finite-dimensional law.

More strikingly, as \(m\to\infty\),
\[
\boxed{\frac{\log N_m}{\log m}\ \Longrightarrow\ 2-U^2,\qquad U\sim\operatorname{Uniform}[0,1].}
\tag{2}
\]
The limiting cumulative distribution function is \(0\) below \(1\), \(1-\sqrt{2-x}\) on \([1,2]\), and \(1\) above \(2\); in particular,
\[
\lim_{m\to\infty}\mathbb E\frac{\log N_m}{\log m}=\frac53.
\tag{3}
\]
This random polynomial exponent contrasts with a uniformly oriented **centroid-passing** simplex section, whose number of vertices has deterministic leading exponent \(2\). The statement concerns random *affine offsets*, not uniformly selecting a combinatorial type or a centroid-passing hyperplane.

## Assumptions and scope

The simplex is nondegenerate and regular; its scale and Euclidean placement do not affect the law. An oriented affine hyperplane is parameterized by a uniform unit normal \(u\) in its \((m-1)\)-dimensional direction space and a signed offset \(t\in\mathbb R\) with Lebesgue measure \(dt\); the resulting measure \(du\,dt\) is normalized conditional on intersection with \(S_m\). Choosing unoriented hyperplanes instead gives the same section law. Hyperplanes through simplex vertices form a null set and are ignored. The minimum count is \(m-1\) and the maximum is \(\lfloor m^2/4\rfloor\), so \(\log N_m/\log m\) is well-defined.

## Proof

**1. Face counting for a fixed plane.** Model the simplex by \(\operatorname{conv}(e_1,\ldots,e_m)\) in \(H=\{x\in\mathbb R^m:\sum_i x_i=1\}\). Normals are vectors \(u\in H_0=\{u:\sum_i u_i=0\}\) of Euclidean norm one. For a generic offset \(t\in(\min_i u_i,\max_i u_i)\), precisely \(k\) values \(u_i\) lie below \(t\) for some \(1\le k\le m-1\). Each of the \(k(m-k)\) simplex edges whose endpoints lie on opposite sides is intersected at exactly one relative-interior point. Those points are exactly the vertices of the section, proving \(N_m=k(m-k)\).

**2. The measure of rank events.** For any fixed \(u\), write its sorted coordinates as \(u_{(1)}<\cdots<u_{(m)}\). The offsets yielding rank \(k\) form an interval of length \(u_{(k+1)}-u_{(k)}\). The total eligible offset length is \(u_{(m)}-u_{(1)}\). By the motion-invariant measure,
\[
\Pr(K_m=k)=\frac{\mathbb E_u[u_{(k+1)}-u_{(k)}]}{\mathbb E_u[u_{(m)}-u_{(1)}]}.
\tag{4}
\]
Take iid standard Gaussians and set \(G=(Z_1-\bar Z,\ldots,Z_m-\bar Z)\), \(Q=\|G\|\), and \(u=G/Q\). The Gaussian \(G\) is isotropic in \(H_0\); \(u\) is Haar-uniform and independent of \(Q>0\). Its ordered gaps are precisely Gaussian gaps divided by \(Q\); hence the numerator and denominator of (4), after multiplication by the same \(\mathbb E Q\), are the corresponding unscaled expected Gaussian gaps and range. This proves the first equality in (1).

For the second equality, use the nonnegative random spacing identity
\[
Z_{(k+1)}-Z_{(k)}
=\int_{\mathbb R}\mathbf1\{\#\{i:Z_i\le x\}=k\}\,dx.
\]
Tonelli's theorem and independence give the binomial integral in (1). Summing over \(k=1,\ldots,m-1\) gives \(\mathbb E R_m\), whose integrand is the probability that at least one sample lies on each side of \(x\). This proves the denominator formula and normalization.

**3. An exactly equivalent size-biased Gaussian construction.** On the space of iid Gaussians \(Z\) and an independent \(V\sim\operatorname{Uniform}[0,1]\), replace the ordinary Gaussian law by one weighted with density \(R_m/\mathbb E R_m\), then set
\[
T_m=Z_{(1)}+V R_m,\qquad K_m=\#\{i:Z_i<T_m\}.
\tag{5}
\]
The conditional chance that \(T_m\) falls in the \(k\)-th sample gap equals that gap divided by the range. Integrating under the range-weighted law gives the first ratio in (1), and the preceding radial decomposition shows that the full oriented affine-hyperplane measure has precisely this construction. The range weight is essential: selecting a Gaussian sample without it would not represent motion-invariant section sampling exactly.

**4. Removing the range bias asymptotically.** Put \(s_m=\sqrt{2\log m}\). Standard elementary Gaussian-tail estimates imply
\[
Z_{(m)}/s_m\longrightarrow1,\quad Z_{(1)}/s_m\longrightarrow-1
\quad\text{in probability},\qquad
\mathbb E R_m/s_m\longrightarrow2.
\tag{6}
\]
For clarity, the upper-tail bound is \(\Pr(Z_{(m)}> (1+\delta)s_m)\le m\exp(-(1+\delta)^2s_m^2/2)\); for the lower tail use \(\Pr(Z_{(m)}\le(1-\delta)s_m)=\Phi((1-\delta)s_m)^m\to0\). Reflect the sample for the minimum. The bound \(\Pr(\max_i|Z_i|>t)\le2m e^{-t^2/2}\), integrated over \(t\), gives uniform square-integrability of \(\max_i|Z_i|/s_m\), establishing the expectation assertion. Thus \(R_m/\mathbb E R_m\to1\) in \(L^1\). The total variation distance between the range-biased joint law of \((Z,V)\) and the original product law is exactly
\[
\frac12\mathbb E\left|\frac{R_m}{\mathbb E R_m}-1\right|\longrightarrow0.
\tag{7}
\]
Consequently, it suffices to prove the logarithmic limit under the simpler *unweighted* iid Gaussian construction.

**5. Exponents of the two tail counts.** Under the unweighted law, (5)–(6) imply \(T_m/s_m\to 2V-1\) in probability. Fix any \(v\in(0,1)\) and condition on \(V=v\); put \(c=2v-1\in(-1,1)\). The Gaussian tail formula for any \(0<q<1\) gives \(\Phi(-q s_m)=m^{-q^2+o(1)}\). At deterministic thresholds \(q s_m\) or \(-q s_m\), the smaller of the upper and lower sample counts is binomial with expectation \(m^{1-q^2+o(1)}\); Chernoff's inequality makes its logarithm divided by \(\log m\) converge in probability to \(1-q^2\). Since, conditionally on \(V=v\), \(T_m/s_m\to c\), one may bound each random count by those at two deterministic thresholds \((c-\delta)s_m\) and \((c+\delta)s_m\), then let \(\delta\downarrow0\). This establishes
\[
\frac{\log\min(K_m,m-K_m)}{\log m}
\ \longrightarrow\ 1-c^2
\quad\text{in probability for every fixed }v\in(0,1).
\tag{8}
\]
For \(c=0\), both counts are \(m^{1+o_p(1)}\), giving the same conclusion. The exceptional endpoints \(v=0,1\) have probability zero. Integrating the conditional convergence over \(v\) shows that (8) holds after replacing \(c\) with \(2V-1\), in the joint-probability sense.

Since \(\max(K_m,m-K_m)\in[m/2,m]\), its logarithm divided by \(\log m\) tends to \(1\) uniformly. Therefore (8) gives
\[
\frac{\log[K_m(m-K_m)]}{\log m}\longrightarrow 2-(2V-1)^2
\quad\text{in probability under the unweighted law}.
\]
Transfer back using the total variation bound (7). Because \(|2V-1|\) is uniform on \([0,1]\), (2) and the explicit CDF follow. Finally, \(0\le \log N_m/\log m\le2\), so bounded convergence of expectations under weak convergence proves (3).

## Verification

The standalone `verify.py` evaluates the Gaussian-spacing integrals by adaptive quadrature, verifies their denominator identity, positivity, reflection symmetry and normalization, and compares the resulting probabilities against a **separately sampled motion-invariant affine-plane experiment**. That experiment chooses Gaussian directions in the sum-zero normal space, normalizes them, samples offsets uniformly from a fixed interval, and rejects planes that miss the simplex. Across \(m=4,5,7,12\), the run checked \(24\) ranked probabilities and passed, with the largest observed absolute discrepancy below \(0.003\). Its final line is `AFFINE_SIMPLEX_CHECK_OK comparisons=24`. Finite sampling checks only the exact finite law; the asymptotic limit is established analytically above, not inferred from numerical convergence.

## Relationship to prior work

Dirksen [1] studies extrema and formulas for **volumes** of regular-simplex sections, including noncentral hyperplanes, rather than the distribution of vertices under motion-invariant affine-hyperplane sampling. Baryshnikov [2] gives the Gaussian/regular-simplex correspondence for random **projections**; neither the present Crofton offset bias nor the logarithmic section-vertex law is implied by a projection-geometry statement without additional work. De Loera–Lopez-Campos–Torres [3] study **possible** vertex counts, maxima, and gaps of affine sections; their full 22-page preprint does not supply the measure-weighted probabilities or their asymptotic distribution. The earlier result [4] establishes an exact Gaussian sign reduction and chi-square fluctuations for **centroid-passing** regular-simplex sections, explicitly excluding randomly translated hyperplanes. It therefore has a distinct probability measure and a different limiting exponent. General Gaussian order-statistic and Gaussian-tail estimates are treated here as established tools; only their measure-biased geometric consequence is assessed as a possible new contribution.

## Limitations

The claim does not apply unchanged to nonregular simplices, arbitrary orientation-offset sampling schemes, randomly *projected* simplices, or hyperplanes constrained through the centroid. The limit describes the logarithm of the number of section vertices, not its finite-dimensional expectation or a uniform error bound in dimension. Independent mathematical validation and definitive historical-priority confirmation have not been performed; another paper could encode an equivalent affine section law in Gaussian-spacing terminology.

## References

[1] H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates*, first publicly submitted 21 September 2015, arXiv:1509.06408v1; https://arxiv.org/abs/1509.06408 .

[2] Y. M. Baryshnikov, *Gaussian Samples, Regular Simplices, and Exchangeability*, Discrete Comput. Geom. 17 (1997), 257–261; https://doi.org/10.1007/PL00009292 .

[3] J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first posted 17 December 2024, 22-page revised preprint https://arxiv.org/pdf/2412.12419 .

[4] *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90 .

[5] F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete Comput. Geom. 7 (1992), 219–226; https://doi.org/10.1007/BF02187839 .
