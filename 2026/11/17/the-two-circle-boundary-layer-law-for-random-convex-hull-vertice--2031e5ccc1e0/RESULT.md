# The two-circle boundary-layer law for random convex hull vertices

## Finding

Let \(n\) independent angles be uniform on \([0,2\pi)\), giving \(n\) points on the unit circle. Independently sample \(m_n\) uniform angles on the concentric circle of radius
\[
r_n=1-\frac{\lambda}{2}\left(\frac{2\pi}{n}\right)^2,
\]
where \(\lambda>0\) and \(m_n/n\to\alpha\in(0,\infty)\). Denote by \(V_n\) the number of inner-circle samples that are vertices of the ordinary Euclidean convex hull of all \(n+m_n\) samples. Then
\[
\frac{V_n}{m_n}\longrightarrow p(\lambda,\alpha)\quad\text{in }L^2,
\]
where the explicit positive crossover profile is
\[
p(\lambda,\alpha)=
\int_0^\infty\!\int_{\lambda/a}^\infty
\exp\!\left[-a-b-\alpha\left(\left(\frac\lambda a-a\right)_++\left(\frac\lambda b-b\right)_+\right)\right]\,db\,da,
\qquad (x)_+=\max(x,0).
\]
Every outer-circle sample is always a vertex. Consequently the entire hull vertex count, divided by \(n\), tends in probability to \(1+\alpha p(\lambda,\alpha)\). The profile is continuous, strictly decreasing in each positive argument, and satisfies
\[
\begin{split}
p(0,\alpha)&=1,\quad \lim_{\lambda\to\infty}p(\lambda,\alpha)=0,\\
\lim_{\alpha\downarrow0}p(\lambda,\alpha)&=2\sqrt\lambda\,K_1(2\sqrt\lambda),\\
\lim_{\alpha\to\infty}p(\lambda,\alpha)&=e^{-2\sqrt\lambda},
\end{split}
\]
where \(K_1\) is the modified Bessel function of the second kind. More generally, for any positive radii \(r_n=1-\delta_n\) with \(\delta_n\to0\), the fraction of surviving inner samples tends to one if \(n^2\delta_n\to0\), and to zero if \(n^2\delta_n\to\infty\). Thus radial separation at scale \(n^{-2}\) is the sharp transition window.

## Assumptions and scope

Both clouds have independently sampled, continuously distributed, uniform polar angles; sample counts are fixed, not Poisson-distributed. The geometry is the ordinary Euclidean convex hull in \(\mathbb R^2\), rather than a ball-convex hull or a hull of regular polygons. In the main limit \(\alpha\) and \(\lambda\) are fixed positive constants; the displayed radius is positive for all sufficiently large \(n\). The count \(V_n\) includes only samples from the smaller-radius circle. For the off-window conclusions, \(m_n/n\to\alpha\in(0,\infty)\) remains assumed. All probability statements refer to the joint law of the two independent angle samples. The value of \(p\) at \(\lambda=0\) is defined by continuity, and in that case all points are in convex position almost surely.

## Proof

**1. A finite configuration criterion.** Fix one inner candidate and rotate it to \((r,0)\). Write every competitor as \((R\cos\phi,R\sin\phi)\), \(-\pi<\phi<\pi\), with \(R\in\{r,1\}\). On the event that the outer points surround the origin (equivalently, their maximum circular gap is less than \(\pi\)), any supporting normal exposing the candidate has the form \((\cos\psi,\sin\psi)\) with \(\cos\psi>0\). Indeed the support function of the outer hull is strictly positive in every direction. The support inequality becomes
\[
\tan\psi\begin{cases}
\le (r/R-\cos\phi)/\sin\phi,&\phi>0,\\
\ge (r/R-\cos\phi)/\sin\phi,&\phi<0.
\end{cases}
\]
For either radius \(R\), the bounding function is strictly increasing in \(\phi\), since its derivative is \((1-(r/R)\cos\phi)/\sin^2\phi>0\) away from \(\phi=0\). Hence just the nearest outer and inner neighbors on either angular side determine whether the candidate is exposed. If their four signed angular gaps are \((-A_n,B_n)\) and \((-U_n,W_n)\), respectively, the strict necessary and sufficient condition is
\[
\max\left\{-\tan(U_n/2),\frac{\cos A_n-r}{\sin A_n}\right\}<
\min\left\{\tan(W_n/2),\frac{r-\cos B_n}{\sin B_n}\right\}.
\]
The exceptional surrounding failure has probability exponentially small: a fixed sampled outer point can start an empty semicircle with probability \(2^{-(n-1)}\), and a union bound gives at most \(n2^{-(n-1)}\). The analogous exceptional gap event for inner neighbors also vanishes exponentially.

**2. The local Poisson limit.** Put \(h_n=2\pi/n\). For a uniformly selected inner candidate, the vector of normalized gaps
\[
(A_n/h_n,B_n/h_n,U_n/h_n,W_n/h_n)
\]
converges in distribution to four independent variables \((A,B,U,W)\), where \(A,B\) have exponential rate one and \(U,W\) have exponential rate \(\alpha\). This follows directly by computing joint void probabilities in disjoint angular arcs of lengths \(h_n\) times fixed constants. With \(r=1-\lambda h_n^2/2\), divide both sides of the support criterion by \(h_n\); the four bounds converge to
\[
\max\{-U/2,-A/2+\lambda/(2A)\}
<\min\{W/2,B/2-\lambda/(2B)\}.
\]
Equivalently,
\[
AB>\lambda,\qquad A(A+W)>\lambda,\qquad B(B+U)>\lambda.
\]
The boundary of this event has probability zero. Conditioning on the independent \(A=a,B=b\) therefore yields its probability as
\[
\mathbf 1_{\{ab>\lambda\}}\exp\!\left[-\alpha\left(\left(\frac\lambda a-a\right)_++\left(\frac\lambda b-b\right)_+\right)\right].
\]
Integrating against the rate-one exponential densities of \(A,B\) gives exactly \(p(\lambda,\alpha)\).

**3. Self-averaging.** Let \(I_{n,j}\) be the indicator that inner candidate \(j\) survives. Exchangeability gives \(\mathbb E V_n/m_n\to p\). For two distinct candidates, their angle difference stays bounded away from zero on the \(1/n\) scale with probability tending to one. Nearest-neighbor events are determined, up to a probability exponentially small in a chosen truncation width, by the two independent angle clouds restricted to bounded \(1/n\)-neighborhoods of the candidates. These neighborhoods are disjoint with probability tending to one; multinomial local counts converge to independent Poisson counts. Thus \(\mathbb E[I_{n,1}I_{n,2}]\to p^2\), and
\[
\operatorname{Var}(V_n/m_n)=\frac{\operatorname{Var}I_{n,1}}{m_n}+\frac{m_n-1}{m_n}\operatorname{Cov}(I_{n,1},I_{n,2})\longrightarrow0.
\]
This proves \(L^2\) convergence. Every outer point is exposed by its own radial tangent to the unit disk, so the total hull-vertex statement follows.

**4. Sharp window and parameter limits.** At fixed positive \(\lambda\), monotonicity of the integral is immediate because each of its three inequalities becomes harder as \(\lambda\) grows. Strictness follows from positive continuous exponential densities. For positive \(\lambda\), the factors involving \(\alpha\) strictly decrease on a positive-measure subset. Dominated convergence gives \(p(0,\alpha)=1\), \(p(\infty,\alpha)=0\), and the two stated \(\alpha\) limits. For \(\alpha\downarrow0\), integrate \(\mathbb P(AB>\lambda)\) to obtain
\[
\int_0^\infty e^{-a-\lambda/a}\,da=2\sqrt\lambda\,K_1(2\sqrt\lambda).
\]
For \(\alpha\to\infty\), only \(A,B\ge\sqrt\lambda\) remain, of probability \(e^{-2\sqrt\lambda}\). Finally, at fixed angular configuration, moving the entire inner circle inward can only increase the left outer support bounds and decrease the right outer bounds; the inner-vs-inner support bounds do not change. Thus an inner point's vertex indicator is nonincreasing as its radius decreases, whenever the surrounding event holds. Monotone squeezing between fixed \(\lambda\) values proves the two off-window statements.

## Verification

The companion Python checker evaluates the integral by independently nested one-dimensional adaptive quadrature, tests the nearest-neighbor criterion against a direct numerical convex-hull oracle, and simulates several finite sample sizes, separations and inner-to-outer sampling ratios. In particular, at \(\lambda=1,\alpha=1\) it obtains \(p(1,1)\approx0.210403810531257\), compared with simulation fractions near \(0.21\). At \(\lambda=0\), it checks that all samples are vertices. The checker also verifies that the integral lies between its sparse- and dense-inner-layer endpoints. A finite simulation is not used as the proof of the infinite-sample limit; that proof is given above.

Run from this package directory with Python 3, NumPy, SciPy:

```bash
python check_two_circle_hull.py
```

## Relationship to prior work

Böröczky–Fodor–Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body* (first public arXiv version March 25, 2011), proves intrinsic-volume approximation rates for samples from a **single** fixed convex boundary. Its curvature-based boundary scale motivates the present question, but it does not treat two concentric sample layers with radius separation shrinking as the sample sizes grow. The reviewed full-text portions include its principal theorems and boundary-cap argument.

Majumdar–Comtet–Randon-Furling, *Random Convex Hulls and Extreme Value Statistics* (arXiv 2009), develops support-function methods for mean area and perimeter of hulls of independently sampled planar points. It does not give the marked inner-layer vertex proportion or the critical two-circle limiting profile. Har-Peled's 2011 *On the Expected Complexity of Random Convex Hulls* treats interior-uniform sampling and expected hull complexity; its estimates do not determine this singular two-boundary-layer count. The concentric-regular-polygon vertex laws concern deterministic vertex grids with random relative rotation, not two independent clouds of uniform angles.

## Limitations

The theorem concerns two perfectly concentric circles and independent uniform angular sampling; it does not establish universality for arbitrary smooth curves or nonuniform densities. The convergence is qualitative, without a finite-sample rate or a central limit theorem. The exact crossover integral is not claimed to have an elementary closed form. Numerical checks corroborate only finite cases. Unindexed or inaccessible historical literature could affect priority; there has been no independent mathematical audit.

## References

1. K. J. Böröczky, F. Fodor and D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978, first posted 2011-03-25. https://arxiv.org/abs/1103.4978
2. S. N. Majumdar, A. Comtet and J. Randon-Furling, *Random Convex Hulls and Extreme Value Statistics*, arXiv:0912.0631, first posted 2009-12-03. https://arxiv.org/abs/0912.0631
3. S. Har-Peled, *On the Expected Complexity of Random Convex Hulls*, arXiv:1111.5340, first posted 2011-11-22. https://arxiv.org/html/1111.5340v1
4. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672, first posted 2015-05-18. https://arxiv.org/html/1505.04672v1
5. H. Carnal and J. Hüsler, *On the convex hull of n random points on a circle*, Journal of Applied Probability 28 (1991), 231–237, https://doi.org/10.2307/3214754 (abstract inspected; complete text not verified).
