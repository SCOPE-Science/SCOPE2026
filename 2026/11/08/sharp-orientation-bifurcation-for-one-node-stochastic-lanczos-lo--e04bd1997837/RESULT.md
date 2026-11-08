# Sharp orientation bifurcation for one-node stochastic Lanczos log-determinants

## Finding
Let \(\theta>0\), let \(u\in\mathbb R^3\) satisfy \(\|u\|_2=1\), and let \(A_{\theta,u}=I_3+\theta uu^{\mathsf T}\). Given a uniformly random Rademacher vector \(\varepsilon\in\{-1,1\}^3\), the one-node stochastic Lanczos quadrature (SLQ) estimate of \(\log\det A_{\theta,u}\) is
\[
T_{\theta,u}=3\log\!\left(1+\frac{\theta}{3}(\varepsilon^{\mathsf T}u)^2\right).
\]
Set \(\alpha=\theta/3\) and \(\theta_*=5\sqrt{10}-14\). Its **sharp expected-estimate range over every orientation** is
\[
\boxed{\frac34\log\min\!\left\{\left(1+\frac\alpha3\right)^3(1+3\alpha),\ (1+2\alpha)^2\right\}
\ \le \ \mathbb E T_{\theta,u}\ \le\ 3\log(1+\alpha).}
\]
The minimum is attained **only** when the absolute coordinates of \(u\) are \((1/\sqrt3,1/\sqrt3,1/\sqrt3)\), up to permutation and independent signs, for \(0<\theta<\theta_*\). For \(\theta>\theta_*\), it is attained **only** when these absolute coordinates are \((1/\sqrt2,1/\sqrt2,0)\). At \(\theta=\theta_*\), exactly these two families tie; there are no other minimizers. The maximum is attained **only** at signed coordinate vectors, for every \(\theta>0\). The exact target is \(\log\det A_{\theta,u}=\log(1+\theta)\); accordingly the one-node expected estimate is strictly upward biased for every orientation.

In particular, two matrices with **identical eigenvalues** \(1,1,1+\theta\) can have different one-node Rademacher SLQ bias, and the orientation minimizing that bias undergoes a genuine support transition at \(\theta_*\approx1.8113883008419\). This is an expectation result, not an optimization of estimator mean-squared error or runtime.

## Assumptions and scope
All quantities are real; \(\theta>0\), \(u\in\mathbb R^3\) is a unit vector, and the three signs are independent and equally likely. The probe has deterministic squared norm \(\|\varepsilon\|_2^2=3\). One-node SLQ means one Lanczos step with initial normalized vector \(\varepsilon/\sqrt3\), followed by the one-point Gaussian quadrature of the natural logarithm, multiplied by the probe squared norm. Results concern a single probe's expected estimate; averaging independent copies does not change its expectation.

The permitted optimization is orientation of the fixed rank-one spike, including arbitrary signs and zeros, not eigenvalues or probe distribution. The first motivating numerical method was publicly available by 2017-10-03; the present exact threshold is a separately derived finding.

## Proof
**Step 1: Exact reduction to a four-factor product.** Put \(\alpha=\theta/3\) and \(s_\varepsilon=\varepsilon\cdot u\). The first Lanczos Rayleigh quotient is \(1+\alpha s_\varepsilon^2\), proving the stated estimator. The eight sign vectors come in four opposite pairs, with identical squared dot products. Consequently
\[
\mathbb E T_{\theta,u}=\frac34\log P(u,\alpha),\qquad
P(u,\alpha)=\prod_{\varepsilon\in\{(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)\}}
\bigl(1+\alpha(\varepsilon\cdot u)^2\bigr).
\]
Write \(x_i=u_i^2\), so \(x_i\ge0\), \(\sum_i x_i=1\), and introduce
\[
q=x_1x_2+x_1x_3+x_2x_3,\qquad r=x_1x_2x_3.
\]
Expanding the four factors and collecting even monomials gives the exact algebraic identity
\[
\boxed{P=\left[(1+\alpha)^2-4\alpha^2q\right]^2+64\alpha^3r.}\tag{1}
\]
All sign or coordinate permutations leave \(P\) unchanged. The feasible range is \(0\le q\le1/3\).

**Step 2: Boundary with at most two positive coordinates.** If \(q\le1/4\), equation (1), \(r\ge0\), and
\((1+\alpha)^2-4\alpha^2q\ge1+2\alpha>0\)
yield
\[
P\ge\left[(1+\alpha)^2-4\alpha^2q\right]^2\ge(1+2\alpha)^2=:P_2.
\]
Equality forces \(q=1/4\) and \(r=0\), hence exactly two squared coordinates are \(1/2\), with the third zero. This also proves global optimality among the entire boundary of the simplex.

**Step 3: Interior with \(q>1/4\).** Here all \(x_i>0\). For each fixed \(q\), the expression (1) increases strictly with \(r\), so minimize \(r\) subject to \(\sum_i x_i=1\) and fixed \(q\). Compactness gives a minimum. A constrained stationary point has at least two equal coordinates (subtract the Lagrange equations for the elementary symmetric product). Define \(d=\sqrt{1-3q}\in[0,1/2)\). The two permitted nontrivial stationary triples have
\[
\left(\frac{1+d}{3},\frac{1+d}{3},\frac{1-2d}{3}\right)
\quad\text{and}\quad
\left(\frac{1-d}{3},\frac{1-d}{3},\frac{1+2d}{3}\right),
\]
where the second has \(r\) larger by \(4d^3/27\). Thus the first uniquely minimizes \(r\) except at the triple-balanced point \(d=0\). Write its smaller coordinate as \(z=(1-2d)/3\in(0,1/3]\), so \(x_1=x_2=(1-z)/2\), \(q=(1+2z-3z^2)/4\), and \(r=z(1-z)^2/4\). Equation (1) becomes
\[
P(z)=(1+\alpha z)^2\bigl(9\alpha^2z^2-12\alpha^2z+4\alpha^2-2\alpha z+4\alpha+1\bigr).
\]
Direct differentiation gives
\[
P'(z)=4\alpha^2(3z-1)(1+\alpha z)(3\alpha z-2\alpha+1).\tag{2}
\]
On \(0<z<1/3\), the first nonconstant signed factor \(3z-1\) is negative while the last factor is strictly increasing; hence \(P'\) either has constant sign or changes from positive to negative. There is therefore **no interior minimum**, and every interior value is bounded below by the smaller endpoint. At \(z=0\) and \(z=1/3\), respectively, the endpoint values are
\[
P_2=(1+2\alpha)^2,\qquad P_3=(1+\alpha/3)^3(1+3\alpha).
\]
For \(1/4<q<1/3\), the bound is strict unless at a covered boundary; all minimizers are therefore the two-coordinate or three-coordinate equal-square families.

**Step 4: Sharp switch.** Expansion and cancellation show
\[
P_3-P_2=\frac{\alpha^2}{27}(3\alpha^2+28\alpha-18).
\]
The polynomial has one positive root \(\alpha_*=(-14+5\sqrt{10})/3\), so \(\theta_*=3\alpha_*=5\sqrt{10}-14\). Below this threshold \(P_3<P_2\), and above it \(P_2<P_3\). This proves the lower bound and its complete equality classification.

**Step 5: Upper bound and strict positive bias.** Since \(\mathbb E (\varepsilon\cdot u)^2=1\), strict concavity of the logarithm yields
\[
\mathbb E T_{\theta,u}\le3\log(1+\alpha).
\]
Equality requires \((\varepsilon\cdot u)^2\) constant across all signs, i.e., all off-diagonal products \(u_i u_j\) vanish, exactly the signed coordinate axes. For each sample, scalar Jensen applied to the spectral measure of \(A_{\theta,u}\) under \(\varepsilon/\sqrt3\) gives
\[
3\log\!\left(\frac{\varepsilon^{\mathsf T}A_{\theta,u}\varepsilon}{3}\right)
\ge \varepsilon^{\mathsf T}(\log A_{\theta,u})\varepsilon.
\]
Taking expectations recovers \(\mathbb ET\ge\operatorname{tr}\log A=\log(1+\theta)\). Strictness holds because, for any \(u\), some sign vector has nonzero but not full overlap with \(u\); the two distinct eigenvalues make logarithmic Jensen strict on that vector. This completes the proof.

## Verification
`verification/check.py` uses Python 3 and SymPy 1.14.0 to verify the four-sign identity, endpoint factorization, derivative formula, threshold polynomial, exact rational random triples and finite integer grids against the two sharp endpoint bounds. Run from the extracted package root using `python verification/check.py`. The recorded output is `verification/run_output.txt`. The analytic argument in **Proof**, not the numerical or finite enumeration, establishes the result for every real admissible parameter.

## Relationship to prior work
Ubaru, Chen and Saad (2017) define stochastic Lanczos quadrature for matrix-function traces, including log-determinants, and give general probabilistic error guarantees. Dong et al. (2017) use Lanczos log-determinant estimation in Gaussian-process computations. Chen, Trogdon and Ubaru (2021) and Chen et al. (2022) analyze spectral and uniform quadrature errors; Li et al. (2023) study asymmetric quadrature nodes. These results motivate the estimator and address different claims; the present finding resolves an exact **orientation-dependent** expected one-node estimate for a fixed three-dimensional rank-one spectrum. It is not a claim that one-node Gauss quadrature, rank-one spectral reduction, or Jensen's inequality is new.

A related existing two-dimensional result computes a one-node Rademacher SLQ **mean-squared error** as a function of a rotation and sample count, and classifies its worst and best angles. That does not determine this three-dimensional **expectation** envelope or its sparsity-changing threshold. Publication precedence for the specific three-dimensional logarithmic extremum is not independently established; an equivalent result could exist in specialized extremal Rademacher-sum literature under different terminology.

## Limitations
The dimension is exactly three; the spectrum is exactly \(1,1,1+\theta\); the probes are independent-coordinate Rademacher signs; the quadrature uses exactly one node; only expectation is optimized over orientation. The result does not establish optimal probe design, least mean-square error, high-probability tails, performance for general spectra, or a runtime advantage. A two-node Lanczos step already captures the two-point spectral support exactly in exact arithmetic, so the effect is specific to aggressive one-node truncation. Independent scientific evaluation and exhaustive publication-precedence verification have not been performed.

## References
1. S. Ubaru, J. Chen, and Y. Saad, *Fast Estimation of \(\operatorname{tr}(f(A))\) via Stochastic Lanczos Quadrature*, SIAM J. Matrix Anal. Appl. 38(4), 1075–1099 (2017), DOI https://doi.org/10.1137/16M1104974; online 2017-10-03. Authorized full text: https://www.cs.cornell.edu/courses/cs6241/2020sp/readings/Ubaru-2017-fast.pdf.
2. K. Dong et al., *Scalable Log Determinants for Gaussian Process Kernel Learning*, arXiv:1711.03481 (2017), https://arxiv.org/abs/1711.03481.
3. T. Chen, T. Trogdon, and S. Ubaru, *Analysis of stochastic Lanczos quadrature for spectrum approximation*, arXiv:2105.06595 (2021), https://arxiv.org/abs/2105.06595.
4. T. Chen et al., *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and kernel polynomial method*, arXiv:2204.01941 (2022), https://arxiv.org/abs/2204.01941.
5. X. Li et al., *An analysis on stochastic Lanczos quadrature with asymmetric quadrature nodes*, arXiv:2307.00847 (2023), https://arxiv.org/abs/2307.00847.
