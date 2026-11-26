# Exact rare-failure laws for positive-weight quadrature on an antipodally sampled circle

## Finding
Let \(f:\mathbb R\to(0,\infty)\) be a continuous, \(2\pi\)-periodic density with \(\int_0^{2\pi}f(\theta)\,d\theta=1\) and antipodal symmetry \(f(\theta+\pi)=f(\theta)\). For \(N\ge2\), draw independent \(\Theta_1,\ldots,\Theta_N\) from this density and set \(X_j=(\cos\Theta_j,\sin\Theta_j)\). In the reproducing-kernel Hilbert space induced by \(k(x,y)=1+x\cdot y\) on the unit circle, define the **optimal simplex-weight worst-case quadrature error** \(E_N\) as the infimum of worst-case integration error over nonnegative weights summing to one.

For every \(0\le z<1\), the finite-sample distribution is exactly
\[
\Pr(E_N>z)=N\int_0^{2\pi}f(\theta)\left[\frac12-\int_0^{2\arcsin z}f(\theta+u)\,du\right]^{N-1}\,d\theta.
\]
In particular \(\Pr(E_N>0)=N2^{-(N-1)}\), the planar instance of the established Wendel law. Conditional on \(E_N>0\), the unique clockwise starting endpoint of the exceptional gap has density \(f\), exactly for each \(N\). For every \(t\ge0\),
\[
\lim_{N\to\infty}\Pr(NE_N>t\mid E_N>0)=\int_0^{2\pi}f(\theta)e^{-4tf(\theta)}\,d\theta.
\]
Moreover, for **every** real \(p>0\),
\[
\boxed{\lim_{N\to\infty}2^{N-1}N^{p-1}\mathbb E[E_N^p]=\frac{\Gamma(p+1)}{4^p}\int_0^{2\pi}f(\theta)^{1-p}\,d\theta.}
\]
In particular \(\mathbb E[E_N]\sim\pi2^{-N}\) independently of the angular density. Among all strictly positive continuous antipodally symmetric densities, the uniform density uniquely minimizes the leading error moment coefficient for \(p>1\), uniquely maximizes it for \(0<p<1\), and ties all such densities at \(p=1\). Here uniqueness is modulo equality almost everywhere, which by continuity means equality everywhere.

For \(f_a(\theta)=(1+a\cos2\theta)/(2\pi)\), \(|a|<1\), the squared-error law specializes to
\[
\mathbb E[E_N^2]\sim\frac{\pi^2}{\sqrt{1-a^2}\,N2^N}.
\]
Thus the Wendel failure probability and the leading first moment are distribution-free within this class, while the leading squared-error penalty can be arbitrarily large relative to uniform angular sampling.

## Assumptions and scope
The sample size is any integer \(N\ge2\). Samples are independent and identically distributed on the full unit circle with the stated strictly positive continuous, antipodally symmetric angular density; the kernel is exactly \(k(x,y)=1+x\cdot y\), and weights are selected optimally from the probability simplex after observing the pool. The target measure is the same law that generates the pool, so its feature mean is \((1,0,0)\). Statements concern exact arithmetic and the best achievable simplex-weight rule, not the performance of a particular weight-computation algorithm. The tail expression uses strict inequality; the law may have an atom at zero but has no atom at any positive threshold. The asymptotics hold for fixed \(f\) and fixed \(p>0\) as \(N\to\infty\).

## Proof
**Feature-space reduction.** The finite-dimensional feature representation of the kernel is \(\Phi(x)=(1,x_1,x_2)\in\mathbb R^3\), with the standard inner product. Antipodal symmetry gives \(\mathbb E X=0\). For any simplex weights \(w\), the squared RKHS worst-case integration error is \(\|\mathbb E\Phi(X)-\sum_jw_j\Phi(X_j)\|^2=\|\sum_jw_jX_j\|^2\). Minimizing gives
\[
E_N=\operatorname{dist}\bigl(0,\operatorname{conv}\{X_1,\ldots,X_N\}\bigr).
\]

**Gap geometry.** Almost surely the angles are distinct. Order them around the circle and write \(G\) for the longest cyclic angular gap. If \(G\le\pi\), no open semicircle contains the sample and the origin belongs to its convex hull, hence \(E_N=0\). If \(G>\pi\), this gap is unique and the complement is a short arc of length \(2\pi-G<\pi\). The chord connecting its two endpoints supports the convex hull on the side away from the origin; its midpoint realizes the nearest point of the hull, and its distance from the origin is \(\cos((2\pi-G)/2)=\sin((G-\pi)/2)\). Consequently
\[
E_N>z\ \Longleftrightarrow\ G>\pi+2\arcsin z\qquad(0\le z<1).
\]

**Exact finite-sample distribution.** For a fixed sample angle \(\theta\) to be the clockwise starting endpoint of a gap longer than \(\pi+w\), all remaining \(N-1\) samples must lie in \((\theta+\pi+w,\theta+2\pi)\) modulo a full turn. Antipodal symmetry implies that this complementary arc has probability \(1/2-\int_0^w f(\theta+u)\,du\). Two different sample points cannot each start gaps longer than \(\pi\), so these events are disjoint. Summing over the \(N\) possible anchors and integrating \(\theta\) yields the claimed exact tail with \(w=2\arcsin z\). At \(z=0\), each conditional complement has probability exactly \(1/2\), giving \(N2^{-(N-1)}\). The joint law of the failure event and its anchor has density \(N2^{-(N-1)}f(\theta)\), establishing the conditional anchor law.

**Conditional scaling limit and all positive moments.** Dividing the exact tail by \(N2^{-(N-1)}\), for \(0\le t<N\) one obtains
\[
\Pr(NE_N>t\mid E_N>0)=\int_0^{2\pi}f(\theta)\left[1-2\int_0^{2\arcsin(t/N)}f(\theta+u)\,du\right]^{N-1}d\theta.
\]
Uniform continuity of \(f\) and \(2\arcsin(t/N)=2t/N+o(N^{-1})\) yield the pointwise limit \(\int f(\theta)e^{-4tf(\theta)}d\theta\). Let \(m=\min f>0\). Since \(\int_0^{2\arcsin(t/N)}f(\theta+u)du\ge2mt/N\), the displayed conditional tail is at most \(\exp(-2mt)\) for every \(N\ge2\), with the tail identically zero for \(t\ge N\). For any real \(p>0\), apply dominated convergence to the positive-moment identity \(\mathbb E[Y^p]=p\int_0^\infty t^{p-1}\Pr(Y>t)\,dt\). Integration of the exponential mixture yields the conditional moment limit \(\Gamma(p+1)4^{-p}\int f^{1-p}\). Multiplying by the exact failure probability and dividing by \(N^p\) proves the boxed formula.

**Sampling-law extremum and explicit family.** Jensen's inequality for \(u\mapsto u^{1-p}\) on the circle, with mean density \(1/(2\pi)\), is strict convexity for \(p>1\), strict concavity for \(0<p<1\), and constancy for \(p=1\). This gives the claimed extremizers and uniqueness. For the cosine family, elementary integration gives \(\int_0^{2\pi}f_a(\theta)^{-1}\,d\theta=4\pi^2/\sqrt{1-a^2}\); insert this at \(p=2\).

## Verification
Run \(\texttt{python3 verify.py}\) with standard-library Python. The independent segment-distance calculation and the longest-gap calculation agreed over \(504\) deterministic pseudorandom polygons. Additional checks reconstruct the exact uniform-density tail, the Wendel zero-threshold probability across cosine densities, the conditional exponential-mixture limit, and the first two mixture moments, totaling \(578\) assertions. These are finite checks: the all-sample-size, all-positive-moment statements rely on the proof above. Numerical integration uses periodic midpoint and ordinary midpoint rules and is not claimed to be exact for nonconstant densities.

## Relationship to prior work
Hayakawa (2026, arXiv:2605.05705v1) provides the convex-hull interpretation for positive-weight kernel quadrature and broadly applicable high-probability error bounds. The present result specializes to a first-harmonic circle kernel to resolve **the exact rare-failure distribution, conditional severity, and all positive-moment asymptotics**, including their nonuniform-density dependence; it does not claim the general convex-hull reduction as new. Wendel (1962) already proves the exact distribution-free probability that a centrally symmetric random planar sample misses the origin. Schlemm (2014) studies the maximal circular spacing for **uniform** angles, and Liu and Yang (2014) derive a related disk-hitting probability for points **uniform in a planar disk**. Their stated sampling models and results do not directly provide the nonuniform antipodally symmetric boundary-density moment law. Jewell and Romano (1982) study random arc coverage and convex hulls; its full text was not available in the literature comparison and remains a relevant possible source of earlier coverage.

## Limitations
No general RKHS or higher-dimensional version is asserted. The law requires an exactly optimized convex combination, not a particular iterative quadrature solver, and requires a fixed strictly positive continuous antipodally symmetric density. The finite-sample tail can be regarded as a consequence of angular-gap geometry; the claim of novelty concerns its precise interpretation as positive-weight quadrature risk and the density-sensitive limiting mixture, moment spectrum and optimization phase reversal. Historical priority is not independently certified; specialized earlier circular-coverage work, especially Jewell and Romano (1982), was not fully accessible. Full independent mathematical review is not performed.

## References
1. S. Hayakawa, *Convex-Geometric Error Bounds for Positive-Weight Kernel Quadrature*, arXiv:2605.05705v1 (first public 7 May 2026), https://arxiv.org/html/2605.05705v1.
2. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111, DOI:10.7146/math.scand.a-10655.
3. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114 (2014), https://arxiv.org/abs/1405.6114.
4. Z. Liu and X. Yang, *Probabilities of hitting a convex hull*, Comptes Rendus Mathématique 352 (2014), 935–940, DOI:10.1016/j.crma.2014.08.015, https://www.numdam.org/item/CRMATH_2014__352_11_935_0.pdf.
5. N. P. Jewell and J. P. Romano, *Coverage problems and random convex hulls*, Journal of Applied Probability 19 (1982), 546–561, DOI:10.2307/3213513.
