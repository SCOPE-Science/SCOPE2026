# A universal reentrant positivity law for three-node Gaussian-kernel quadrature

## Finding

Consider a unit-amplitude squared-exponential covariance kernel on the real line,
\[
k_\ell(x,y)=\exp\!\left(-\frac{(x-y)^2}{2\ell^2}\right),\qquad \ell>0,
\]
and a centered Gaussian scale-mixture probability measure
\[
\mu=\int_{[0,\infty)} N(0,s^2)\,\pi(ds),
\]
where \(\pi\) is a probability measure on finite \(s\ge0\) with \(\pi((0,\infty))>0\). This includes ordinary centered Gaussian targets and many heavy-tailed Gaussian variance mixtures. For each \(a>0\) and diagonal regularization \(\eta\ge0\), take the three prescribed, distinct nodes \((-a,0,a)\). Let the (unconstrained) quadrature coefficient vector be
\[
(w_-,w_0,w_+)^\mathsf T=(K_a+\eta I_3)^{-1}m_a,
\]
where \(K_a\) is their kernel Gram matrix and \((m_a)_i=\int k_\ell(x_i,x)\,\mu(dx)\). The same formula is the posterior-mean weight vector if the three function observations have independent centered Gaussian noise of variance \(\eta\).

The two outer coefficients are strictly positive for all \(a>0,\eta\ge0\). Define the probability law \(\nu\) on \((0,1]\) by tilting \(\pi\) with \(c(s)=\ell/\sqrt{\ell^2+s^2}\) and pushing forward through \(\beta(s)=\ell^2/(\ell^2+s^2)\):
\[
m_0=\int c(s)\,\pi(ds),\qquad
\int F(\beta)\,\nu(d\beta)=\frac1{m_0}\int c(s)F(\beta(s))\,\pi(ds).
\]
Set
\[
q=\exp(-a^2/(2\ell^2)),\qquad
H(q)=2\int q^{1+\beta}\,\nu(d\beta)-1-q^4.
\]
There is a **unique** \(q_*\in(0,1)\) satisfying
\[
\boxed{\int(1+\beta)q_*^{\beta-3}\,\nu(d\beta)=2,}
\]
and \(H\) rises strictly from \(H(0)=-1\) to its positive maximum \(\eta_*=H(q_*)\), then strictly decreases to \(H(1)=0\). The sign of the center weight is exactly
\[
\boxed{\operatorname{sgn}(w_0)=\operatorname{sgn}(\eta-H(q)).}
\]
Consequently the coefficients are nonnegative at **every** positive spacing precisely when \(\eta\ge\eta_*\). At \(\eta=\eta_*\), only the center coefficient at the one spacing \(a_*=\ell\sqrt{-2\log q_*}\) vanishes. For \(0<\eta<\eta_*\), the center coefficient is negative on exactly one bounded open interval of spacings, and positive both near collision and for sufficiently wide spacing. For \(\eta=0\), it is negative throughout one initial open interval of positive spacings and positive beyond its unique positive endpoint. No other sign changes occur.

There is also a **sharp target-uniform threshold**, valid simultaneously for every such mixture \(\mu\), every \(\ell>0\), and every \(a>0\):
\[
\boxed{\eta_{\mathrm{univ}}=3\,2^{-4/3}-1=0.190550788976149\ldots.}
\]
All three coefficients are strictly positive whenever \(\eta\ge\eta_{\mathrm{univ}}\). No smaller universal constant works: centered Gaussian targets with standard deviation tending to infinity relative to \(\ell\) have \(\eta_*\uparrow\eta_{\mathrm{univ}}\). For each fixed admissible target, \(0<\eta_*<\eta_{\mathrm{univ}}\).

Finally, the two ends of the negative-weight interval meet in a nondegenerate square-root fold. If \(c_*=-H''(q_*)>0\), then as \(\eta\uparrow\eta_*\) the two roots of \(H(q)=\eta\) obey
\[
\boxed{q_\pm(\eta)=q_*\pm\sqrt{\frac{2(\eta_*-\eta)}{c_*}}+O(\eta_*-\eta).}
\]
Thus the corresponding interval of forbidden spacings shrinks with exponent \(1/2\).

## Assumptions and scope

The kernel amplitude is normalized to one; accordingly \(\eta\) is dimensionless noise variance or diagonal nugget relative to the kernel variance. The same conclusion for an amplitude \(\sigma_k^2\) follows after dividing the physical noise variance by \(\sigma_k^2\). The nodes are required to be symmetric and distinct; no optimization over asymmetric locations is asserted. The mixing distribution \(\pi\) is arbitrary on finite standard deviations, may have an atom at zero and need not have a finite moment. Its positive mass at nonzero standard deviations ensures the integration target is not a point mass at zero.

For \(\eta=0\), coincident nodes are excluded because the unregularized Gram matrix is singular. For \(\eta>0\), the limiting case \(a\downarrow0\) is well defined by continuity. The statement is about signs of *unmodified* posterior-mean or regularized kernel weights, not a constrained positive-weight estimator, an optimal selection of nodes, or the sign of a noisy realized function value.

## Proof

**1. Exact kernel means and the three-by-three reduction.** Gaussian convolution gives
\[
m(x)=\int k_\ell(x,y)\,\mu(dy)
=\int c(s)\exp\!\left(-\frac{x^2}{2(\ell^2+s^2)}\right)\pi(ds).
\]
Hence \(m(a)/m_0=\int q^\beta\,\nu(d\beta)\). With outer weight \(u=w_-=w_+\) and central weight \(v=w_0\), symmetry reduces the regularized kernel system to
\[
\begin{pmatrix}1+\eta+q^4&q\\2q&1+\eta\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}
=\begin{pmatrix}m(a)\\m_0\end{pmatrix}.
\]
Its determinant is
\[
\Delta=(1+\eta+q^4)(1+\eta)-2q^2>0.
\]
For \(\eta=0\), \(\Delta=(1-q^2)^2>0\); for \(\eta>0\), it is positive because it is the determinant of the symmetric even-coordinate block of a positive-definite regularized Gram matrix. Cramer's rule gives
\[
u=\frac{(1+\eta)m(a)-qm_0}{\Delta},\qquad
v=\frac{m_0(1+\eta+q^4)-2qm(a)}{\Delta}.
\]
Since \(q^\beta\ge q\) for \(0<q<1\) and \(\beta\le1\), with strict inequality on the positive-\(\nu\) set \(\{\beta<1\}\), we have \(m(a)>qm_0\). Therefore \(u>0\), and \(v\) has the asserted exact sign.

**2. A nonparametric one-maximum lemma.** Differentiation under the integral is valid locally on \((0,1)\), since \(0<\beta\le1\). The derivative is
\[
H'(q)=4q^3\left[\frac12\int(1+\beta)q^{\beta-3}\,\nu(d\beta)-1\right].
\]
The bracket is strictly decreasing in \(q\), because each derivative contribution is proportional to \((\beta-3)q^{\beta-4}<0\). It tends to \(+\infty\) as \(q\downarrow0\) (every integrand is at least of order \(q^{-2}\)) and equals \((\int\beta\,\nu(d\beta)-1)/2<0\) at \(q=1\). Hence there is exactly one zero \(q_*\), and \(H\) strictly increases before it and strictly decreases after it. Because \(H(1)=0\), the maximum is positive. Because \(H(0)=-1\), the stipulated one- or two-crossing descriptions follow by continuity and strict monotonicity on the two branches. The change from \(q\) to \(a\) is a strictly decreasing bijection between \((0,1)\) and \((0,\infty)\).

**3. Sharpness of the universal nugget.** For \(q\in(0,1)\) and \(\beta>0\), \(q^{1+\beta}<q\). Therefore
\[
H(q)<2q-1-q^4\le 3\,2^{-4/3}-1,
\]
where the last maximum is uniquely attained by \(q=2^{-1/3}\). The strict inequality gives \(\eta_*<\eta_{\mathrm{univ}}\). When \(\mu=N(0,s^2)\), \(\nu\) is a point mass at \(\beta=\ell^2/(\ell^2+s^2)\); as \(s/\ell\to\infty\), \(\beta\downarrow0\) and \(H(q)\) tends uniformly on \([0,1]\) to \(2q-1-q^4\). Thus its maximum converges to the stated universal constant, proving sharpness.

**4. Nondegenerate fold.** Put
\[
\overline\beta_*=
\frac{\int\beta(1+\beta)q_*^\beta\,\nu(d\beta)}
{\int(1+\beta)q_*^\beta\,\nu(d\beta)}\in(0,1].
\]
Using the stationarity equation in the second derivative yields
\[
H''(q_*)=4q_*^2(\overline\beta_*-3)<0.
\]
Taylor's theorem about the strict interior maximum yields
\(\eta_*-H(q)=c_*(q-q_*)^2/2+O(|q-q_*|^3)\). Solving separately on the two monotone branches proves the displayed square-root expansions. The smooth, nonzero derivative of \(a=\ell\sqrt{-2\log q}\) at \(q_*\) transfers the same exponent to physical node spacing.

## Verification

The standalone `verify.py` uses only Python's standard library. It independently solves thousands of regularized three-by-three Gram systems and checks them against the closed weights for random finite Gaussian mixtures, length scales, spacings and nuggets. It also checks the one-maximum geometry and the sharp bound numerically, including ordinary Gaussian targets of increasingly large variance. Run `python verify.py` from the directory containing the file. Its successful recorded result was `PASS 7203 finite direct solves/phase checks; universal bound 0.19055078897615`.

The numerical checks do not establish uniqueness for all mixtures or the sharpness of an infinite-family bound; those statements rely on proof steps 2–4. Values near collisions can be ill-conditioned in floating point even though the mathematical weights are well defined at positive spacing.

## Relationship to prior work

Karvonen and Särkkä [1] study Gaussian-kernel quadrature under Gaussian integration measures, focusing on scaled Gauss–Hermite nodes and approximate kernel weights rather than an all-spacing regularization threshold. Karvonen, Kanagawa and Särkkä [2] develop general positivity conditions based on total positivity and locally optimal nodes; their sufficient condition does not classify these fixed nonoptimal node sets with noise. Glaubitz and Reeger [3] give broad RBF-quadrature stability results using compact support and least-squares constructions, not this precise scale-mixture positivity phase.

A published three-node Gaussian-kernel sign classification on a **bounded uniform** integration interval [4] has a one-crossing transition in kernel *shape* at fixed spacing and no diagonal regularization. Its measure, parameter being varied and assertion differ from the present arbitrary Gaussian scale-mixture, variable-spacing, fixed-kernel regularization theorem. A previously established general symmetric-measure three-node reduction gives a **pointwise** central-weight threshold as a function of spacing; the pointwise matrix inversion is not claimed here as original. The contribution is the global one-critical-point property across every spacing for an infinite-dimensional family of measures, the complete reentrant sign diagram, its universal sharp threshold and the fold law. Generic posterior weight formulas do not alone imply these global extrema without the additional scale-mixture argument.

## Limitations

This proof does not cover arbitrary symmetric non-Gaussian-scale-mixture targets, four or more nodes, asymmetric locations, kernels other than the squared exponential, or optimal node selection for integration error. The target-uniform constant is a supremum, not an attained maximum for a fixed admissible target. The scheme's positivity concerns coefficients; under genuine observation noise, the reported observations can themselves be negative even when their noiseless underlying values are positive. Regularization also changes bias and quadrature accuracy; no optimal accuracy–positivity tradeoff is claimed. An older equivalent global positivity theorem might remain undiscovered, and no independent review has occurred.

## References

[1] T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv:1803.09532, first public 2018-03-26; *BIT Numerical Mathematics* 59 (2019), 877–902. https://arxiv.org/abs/1803.09532

[2] T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, first public 2018-12-20; *Statistics and Computing* 29 (2019), 1317–1333. https://arxiv.org/abs/1812.08509

[3] J. Glaubitz and J. A. Reeger, *Towards stability results for global radial basis function based quadrature formulas*, arXiv:2301.12998, first public 2023-01-30; *BIT Numerical Mathematics* 63 (2023). https://arxiv.org/abs/2301.12998

[4] *A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature*, publicly accessible mathematical result, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-one-crossing-positivity-diagram-for-symmetric-three-node-gauss--bf59562e8e52/RESULT.md
