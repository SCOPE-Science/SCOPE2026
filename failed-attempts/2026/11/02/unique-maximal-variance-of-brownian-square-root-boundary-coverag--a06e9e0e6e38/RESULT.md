# Unique maximal variance of Brownian square-root-boundary coverage occupation

## Finding

For standard one-dimensional Brownian motion \(B\), the limit of the fraction of conventional Gaussian-calibrated confidence intervals covering their target is the square-root-boundary occupation fraction
\[
Z_z=\int_0^1 \mathbf 1\{|B_t|\le z\sqrt t\}\,dt,\qquad z>0.
\]
Its variance has the exact one-dimensional formula, with \(a=z^2\),
\[
\boxed{V(a)=\operatorname{Var}(Z_{\sqrt a})
=\frac1\pi\int_0^1\sqrt{1-r^2}\left(e^{-a/(1+r)}-e^{-a/(1-r)}\right)\,dr.}
\]

**The variance has exactly one global maximum** over all \(z>0\). Put
\[
A(a)=\int_{1/2}^{1}\frac{\sqrt{2s-1}}{s^2}e^{-as}\,ds,\qquad
D(a)=\int_{1}^{\infty}\frac{\sqrt{2s-1}}{s^2}e^{-as}\,ds.
\]
There is exactly one \(a_*>0\) satisfying \(A(a_*)=D(a_*)\); it is the unique maximizer of \(V\). Numerical quadrature gives
\[
\begin{aligned}
a_*&=0.68810970320346721766\ldots,\\
z_*&=\sqrt{a_*}=0.82952378097524559013\ldots,\\
\operatorname{Var}(Z_{z_*})&=0.08135656185520381043\ldots,\\
\operatorname{sd}(Z_{z_*})&=0.28523071688582877877\ldots.
\end{aligned}
\]
The corresponding **nominal** two-sided Gaussian coverage is \(2\Phi(z_*)-1=0.59319191415401940057\ldots\), i.e. about 59.32%, and the noncoverage level is about 40.68%. Furthermore,
\[
\boxed{V(z^2)\sim\frac2\pi z^2\ (z\downarrow0),\qquad
V(z^2)\sim4\sqrt{\frac2\pi}\,z^{-3}e^{-z^2/2}\ (z\to\infty).}
\]
In particular the large-coverage variance decays at a Gaussian-exponential rate with a cubic prefactor.

## Assumptions and scope

Brownian motion starts at zero, has independent centered increments and \(\operatorname{Var}(B_t)=t\). The value of the indicator at \(t=0\) is irrelevant. The threshold \(z\) ranges over all fixed positive real numbers, and \(\Phi\) denotes the standard normal cumulative distribution function. The variance is of the **random time-occupation fraction**, not of an individual coverage indicator or of a finite-sample coverage proportion.

Fischer and Glynn (arXiv:2610.24668v1, Section 2, Theorem 1) establish \(P_{n,z}\Rightarrow Z_z\) under a functional central limit theorem and consistent estimated scale; the classical sample-mean and sample-standard-deviation construction with independent identically distributed observations of finite positive variance is an example. Their coverage proportions obey \(0\le P_{n,z}\le1\). For any such convergence, bounded-continuous mapping for the first two moments yields \(\operatorname{Var}(P_{n,z})\to V(z^2)\) **for each fixed \(z\)**. This statement does not interchange the supremum over \(z\) with the sample-size limit.

## Proof

**1. Correlation reduction.** For \(0<s<t\le1\), the pair \((B_s/\sqrt s,B_t/\sqrt t)\) consists of standard normals with correlation \(r=\sqrt{s/t}\). Let \(p_z=2\Phi(z)-1\) and
\[
q_z(r)=\Pr\{|X|\le z,\ |Y|\le z\}
\]
for standard bivariate normal \((X,Y)\) with correlation \(r\). Fubini's theorem, followed by \(s=tr^2\), gives
\[
\mathbb E Z_z=p_z,\qquad \mathbb E Z_z^2
=2\int_0^1\!\int_0^tq_z(\sqrt{s/t})\,ds\,dt
=2\int_0^1r q_z(r)\,dr.
\]
Since \(q_z(0)=p_z^2\),
\[
\operatorname{Var}(Z_z)=2\int_0^1r[q_z(r)-q_z(0)]\,dr
=\int_0^1(1-r^2)q_z'(r)\,dr.
\]
The integration by parts is justified first on \(r\in[0,1-\epsilon]\) and then by bounded convergence; the bivariate normal probabilities converge continuously as \(r\uparrow1\).

**2. Exact derivative and variance.** For \(|r|<1\), the bivariate normal density \(f_r(x,y)\) satisfies the correlation heat equation \(\partial_r f_r=\partial_x\partial_y f_r\). This may be checked by direct differentiation of
\[
f_r(x,y)=\frac{\exp[-(x^2-2rxy+y^2)/(2(1-r^2))]}{2\pi\sqrt{1-r^2}}.
\]
Integrating over the square \([-z,z]^2\) yields the four corner terms, hence
\[
q_z'(r)=2[f_r(z,z)-f_r(z,-z)]
=\frac{e^{-z^2/(1+r)}-e^{-z^2/(1-r)}}{\pi\sqrt{1-r^2}}.
\]
Substitution proves the claimed formula for \(V(a)\). The integrand is strictly positive for \(a>0\), \(0<r<1\); thus the variance is nonzero.

**3. Laplace separation and uniqueness.** Under the substitutions \(s=(1+r)^{-1}\) and \(s=(1-r)^{-1}\) in the two integrals,
\[
V(a)=\frac1\pi\left[\int_{1/2}^{1}w(s)e^{-as}\,ds
-\int_1^{\infty}w(s)e^{-as}\,ds\right],\quad
w(s)=\frac{\sqrt{2s-1}}{s^3}.
\]
Since \(s w(s)=\sqrt{2s-1}/s^2\) is integrable on \([1/2,\infty)\), differentiation is valid at \(a=0\) and for every \(a>0\):
\[
V'(a)=\frac{D(a)-A(a)}\pi.
\]
Directly in the correlation integral,
\[
V'(0)=\frac1\pi\int_0^1\sqrt{1-r^2}
\left(\frac1{1-r}-\frac1{1+r}\right)dr=\frac2\pi>0.
\]
Thus \(D(0)>A(0)>0\). For \(a>0\), differentiating logarithms yields
\[
\frac d{da}\log\frac{A(a)}{D(a)}
=\frac{\int_1^\infty s h(s)e^{-as}ds}{D(a)}
-\frac{\int_{1/2}^1 s h(s)e^{-as}ds}{A(a)}>0,
\quad h(s)=\frac{\sqrt{2s-1}}{s^2}.
\]
The first fraction is strictly greater than \(1\) and the second strictly less than \(1\). Also, \(A(a)/D(a)\to\infty\): on any interval \([u,v]\subset(1/2,1)\), \(A(a)\ge c_{u,v}e^{-av}\), while \(D(a)\le e^{-a}\int_1^\infty h(s)ds\). Continuity and strict monotonicity imply exactly one crossing \(A(a_*)=D(a_*)\), and the derivative of \(V\) changes there from positive to negative. Thus \(V\), and equivalently \(\operatorname{Var}(Z_z)\) as a function of \(z>0\), has exactly one global maximum.

**4. Endpoint scales.** Using \(V(0)=0\) and the explicitly computed finite right derivative \(V'(0)=2/\pi\), we obtain \(V(z^2)\sim(2/\pi)z^2\). For \(a\to\infty\), the second Laplace integral is \(O(e^{-a}/a)\), whereas, as \(s\downarrow1/2\),
\[
w(s)\sim8\sqrt{2(s-1/2)}.
\]
The one-sided Laplace endpoint estimate therefore gives
\[
\int_{1/2}^{1}w(s)e^{-as}ds\sim
8\sqrt2\,\Gamma(3/2)a^{-3/2}e^{-a/2}
=4\sqrt{2\pi}\,a^{-3/2}e^{-a/2},
\]
and substitution \(a=z^2\) gives the stated large-threshold asymptotic.

**5. Transfer to conventional intervals.** If \(P_{n,z}\Rightarrow Z_z\) and \(0\le P_{n,z}\le1\), both first and second moments converge, establishing the stated variance limit for each fixed \(z\). The unique worst level is a property of this limiting variance, not an assertion of finite-sample uniformity.

## Verification

The analytic proof supplies the infinite-dimensional statement and unique global optimization. The standalone script `verify_coverage_variance.py` independently integrates the conditional bivariate-normal probability, checks it against the correlation integral, compares two expressions for \(V'\), tests the Gaussian-correlation derivative, and evaluates the unique zero at high precision. Its recorded deterministic output is in `verification_output.txt`. Reproduce with `python verify_coverage_variance.py` after installing `scipy` and `mpmath`. Numerical quadrature supports the displayed decimals but is not a certified interval-arithmetic bound on the last digit.

## Relationship to prior work

Fischer and Glynn, *On the Proportion of Time that a Conventional Confidence Interval Covers*, arXiv:2610.24668v1 (first public 2026-10-17), establish the Brownian occupation limit, provide a three-fold integral for the second moment (Section 2, equation (4)), and tabulate its standard deviation for several nominal confidence levels. They do **not** claim in the inspected manuscript a unique globally maximizing confidence level, a one-dimensional variance representation, or the two endpoint equivalents. These are the contributions assessed here; the Brownian limit itself is not new. Plackett's classical Gaussian-correlation differentiation identity is used only as an established ingredient and is also rederived in Step 2.

## Limitations

The theorem optimizes the variance of the **asymptotic limiting occupation law** over symmetric, two-sided Gaussian thresholds. It does not prove that the same nominal coverage maximizes finite-sample variance, nor does it optimize asymmetric intervals or construct anytime-valid confidence sequences. The quoted decimals are numerical evaluations, not interval-certified digits. Historical priority beyond the identified primary manuscript and compared records requires independent scholarly review; a general Gaussian occupation-covariance optimization theorem could subsume this special case.

## References

1. M. Fischer and P. W. Glynn, *On the Proportion of Time that a Conventional Confidence Interval Covers*, arXiv:2610.24668v1, first posted 2026-10-17. https://arxiv.org/abs/2610.24668
2. R. L. Plackett, *A Reduction Formula for Normal Multivariate Integrals*, Biometrika 41 (1954), 351–360. https://doi.org/10.1093/biomet/41.3-4.351
3. *The Mathematics of Indirect Treatment Comparisons*, Appendix D, Lemma D.3 (a freely accessible proof of the bivariate Gaussian correlation heat equation). https://choxos.github.io/Mathematics-of-ITC/appendices/D-special-functions.html
