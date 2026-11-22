# Sharp circular BV contraction and a golden-ratio jump transition for two-harmonic smoothing

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). For nonnegative real \(a,b\), not both zero, assume the two-harmonic density
\[
k_{a,b}(t)=\frac{1+2a\cos t+2b\cos(2t)}{2\pi}\geq0
\quad (t\in\mathbb T).
\]
Let \(T_{a,b}f=k_{a,b}*f\), where convolution uses Lebesgue measure on \(\mathbb T\). For every integer \(r\geq1\), its exact, attained real bounded-variation seminorm on functions modulo constants is \(\kappa_r(a,b)=\sup_{V(f)>0}V(T_{a,b}^{r}f)/V(f)\), as follows.

When \(a>0\), put
\[
A=a^r,\qquad q=4(b/a)^r,\qquad
Q=\sqrt{\frac{11+5\sqrt5}{2}}.
\]
Then
\[
\boxed{\displaystyle
\kappa_r(a,b)=
\begin{cases}
\dfrac{4A}{\pi},&0\leq q\leq Q,\\[5pt]
\dfrac{2A}{\pi}\sqrt{1-s_q}\left(q\sqrt{s_q}+\dfrac1{q\sqrt{s_q}}\right),&q>Q,
\end{cases}
\qquad
s_q=\frac{1+\sqrt{1-8/q^2}}4\quad(q>Q).}
\]
If \(a=0<b\), the coefficient is \(4b^r/\pi\); if \(a=b=0\), it is zero. In every nonzero case the coefficient is strictly below one.

Each sharp coefficient is attained by a characteristic function of one circular arc, after arbitrary translation and nonzero scaling. For \(a>0\), the maximizing arc lengths up to complementation are exactly \(\pi\) when \(q<Q\), and exactly \(2\arccos\sqrt{s_q}\) when \(q>Q\). At \(q=Q\), both \(\pi\) and \(2\arccos\sqrt{(3-\sqrt5)/2}\) are maximizing lengths; no other arc lengths maximize. If \(a=0<b\), the maximizing arc length is \(\pi/2\) up to complementation.

Consequently the complete iteration-dependent transition occurs at the universal multiplier ratio
\[
\boxed{\displaystyle \tau_* = \frac14\sqrt{\frac{11+5\sqrt5}{2}}=0.8325476691\ldots.}
\]
When \(0<b<a\), nonantipodal jump arcs maximize exactly for those positive integers \(r\) satisfying \((b/a)^r>\tau_*\), ties occur at equality, and all later iterations are sharply maximized by semicircles. For example, \(a=1/10\) and \(b=9/100\) give a shorter-arc maximizer for \(r=1\), but a semicircle for every \(r\geq2\). When \(b\geq a>0\), a shorter arc maximizes at every positive iteration.

## Assumptions and scope

The variation seminorm is \(V(f)=|Df|(\mathbb T)\) for real \(f\in BV(\mathbb T)\), and the result is on its quotient by constants. The convolution is normalized as \((k*f)(x)=\int_{\mathbb T}k(x-t)f(t)\,dt\). The parameter condition is the full nonnegative two-harmonic density domain in the closed nonnegative Fourier quadrant, not merely the sufficient subdomain \(a+b\leq1/2\). The two Fourier coefficients of \(k_{a,b}\) are \(a\) and \(b\), so \(k_{a,b}^{*r}=k_{a^r,b^r}\). All assertions are exact for every admissible real pair and integer \(r\geq1\); boundary densities with isolated zeros are allowed.

## Proof

**1. An exact zero-mass measure reduction.** For every real periodic \(f\in BV(\mathbb T)\), \(\mu=Df\) is a finite signed measure of total mass zero. If \(m=|\mu|(\mathbb T)/2\), its Jordan decomposition has the form \(\mu=m(\nu_+-\nu_-)\), where \(\nu_+,\nu_-\) are probability measures. For any real probability density \(k\), integration against the product coupling of these probability measures yields
\[
\|k*\mu\|_{L^1}\leq m\sup_{u,v\in\mathbb T}\|k(\cdot-u)-k(\cdot-v)\|_{L^1}.
\]
Since \(D(k*f)=k*Df\), division by \(2m=V(f)\) gives the upper bound
\[
\frac{V(k*f)}{V(f)}\leq \frac12\sup_{0\leq\phi\leq\pi}
\int_{\mathbb T}|k(t)-k(t-\phi)|\,dt.
\]
For each separation \(\phi\in(0,\pi]\), the indicator of a circular arc of length \(\phi\) has derivative two opposite point masses, variation exactly two, and its smoothed derivative is the difference of those two translates. Thus the upper bound is attained for a maximizing separation: the reduction is an equality, not merely an estimate.

**2. Reduction to one scalar parameter.** Apply step 1 to \(k_{A,B}\), with \(A=a^r\) and \(B=b^r\). If \(A>0\), set \(q=4B/A\) and \(c=\cos(\phi/2)\in[0,1]\). With \(u=t-\phi/2\), the translated difference factors as
\[
k_{A,B}(t)-k_{A,B}(t-\phi)
=-\frac{2A}{\pi}\sin(\phi/2)\sin u\,(1+qc\cos u).
\]
Using the two-to-one change of variable \(z=\cos u\), the exact half-\(L^1\) distance is
\[
\frac12\|k_{A,B}-k_{A,B}(\cdot-\phi)\|_1
=\frac{2A}{\pi}\sqrt{1-c^2}\int_{-1}^1|1+qcz|\,dz
=\begin{cases}
\dfrac{4A}{\pi}\sqrt{1-c^2},&qc\leq1,\\[4pt]
\dfrac{2A}{\pi}\sqrt{1-c^2}\left(qc+\dfrac1{qc}\right),&qc>1.
\end{cases}
\]
The first branch is at most \(4A/\pi\), with equality only at \(c=0\), representing the semicircle. The second branch is the source of a competing shorter arc.

**3. Global maximization and the sharp threshold.** The derivative of the second branch has the sign of \(q^2c^2(1-2c^2)-1\). If \(q\leq2\sqrt2\), there is no competing interior local maximum. For \(q>2\sqrt2\), its only interior local maximum is at \(c=\sqrt{s_q}\), where
\[
s_q=\frac{1+\sqrt{1-8/q^2}}4.
\]
(The other stationary point is a local minimum.) At this maximum, \(q^2s_q(1-2s_q)=1\), and the ratio of the competing coefficient to the semicircle coefficient, squared, simplifies to
\[
R_q^2=\frac{(1-s_q)^3}{1-2s_q}.
\]
For \(s\in(1/4,1/2)\), this last expression increases strictly: its derivative is \((1-s)^2(4s-1)/(1-2s)^2>0\). Equality \(R_q=1\) therefore occurs exactly when \((1-s)^3=1-2s\), that is, \(s=(3-\sqrt5)/2\). Substitution into \(q^2s(1-2s)=1\) gives the unique threshold \(q=Q\). This proves every branch, equality tie, and asserted maximizing arc length. If \(A=0<B\), the translated distance becomes \((8B/\pi)c\sqrt{1-c^2}\), uniquely maximized at \(c=1/\sqrt2\), giving \(4B/\pi\) and quarter-circle arcs.

**4. Integer powers.** The convolution identity from the Fourier coefficients gives \(A=a^r\) and \(B=b^r\), hence \(q=4(b/a)^r\). Comparing this to \(Q\) proves the complete iteration transition. If \(b/a<1\), the ratio decreases strictly through the threshold at most once; if \(b/a\geq1\), it is always at least four, greater than \(Q\). Finally, a nonzero trigonometric probability density is positive except possibly at finitely many points, so distinct translates overlap on a set of positive measure; their total-variation distance is strictly below one. The same is true of every convolution power, proving strict contraction.

## Verification

A standalone checker, `two_harmonic_bv_check.py`, proves the stated algebraic identities by exact symbolic simplification and compares the translated-kernel formula with independently segmented high-precision \(L^1\) quadrature over 24 parameter-angle pairs. It also compares the global analytic maxima to dense shift grids, verifies the transition for \((a,b)=(1/10,9/100)\) over eight powers, and integrates the attaining arc witnesses. Execute with `python two_harmonic_bv_check.py` using Python with SymPy and mpmath. These finite checks do not certify the universal statement; steps 1–4 provide the all-parameter proof.

## Relationship to prior work

The theory of circular convolution kernels and Fourier-multiplier smoothing is classical. Goodman and Lee (1988) examine trigonometric B-spline kernels, convex preservation, and approximation, rather than the sharp \(BV\) norm for a freely weighted two-harmonic positive density. Kato and Jones (2013) study tractable circular probability densities, trigonometric moments, and convolution representations, not the present variation operator norm or the jump-length phase transition. A related exact real-\(BV\) norm in accessible prior research covers only the signed unweighted degree-two Fourier projector with equal nonzero harmonics; it does not imply the full positive two-parameter threshold or the iteration-dependent change of extremizing arc. Standard zero-mass coupling or Dobrushin reduction yields the translate-distance variational formulation but not the maximization or its sharp spectral threshold.

## Limitations

Only the nonnegative first and second cosine Fourier coefficients are treated; relative phases, negative coefficients allowed by positivity, higher Fourier bands, vector-valued inputs, and alternative variation definitions are not classified. The accessible historical sources do not establish full novelty against every unindexed publication; the exact same coefficient may conceivably occur under different terminology. The transition is for the bounded-variation seminorm, not the \(L^2\), \(L^\infty\), or pointwise error norm.

## References

- S. Kato and M. C. Jones, *An extended family of circular distributions related to wrapped Cauchy distributions via Brownian motion*, Bernoulli 19 (2013), 154–171, first available preprint arXiv:1302.0098v1, posted 2013-02-01, https://arxiv.org/abs/1302.0098.
- T. N. T. Goodman and S. L. Lee, *Convolution operators with trigonometric spline kernels*, Proceedings of the Edinburgh Mathematical Society 31 (1988), 285–299, https://doi.org/10.1017/S0013091500003412.
- J. C. Mairhuber, I. J. Schoenberg, and R. E. Williamson, *On variation diminishing transformations on the circle*, Rendiconti del Circolo Matematico di Palermo 8 (1959), 241–270, https://doi.org/10.1007/BF02843691. Historical background; complete primary text was not obtained in this investigation.
