# Joint tangent-polygon fluctuations detect Euclidean disks

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body whose support function \(h\) is \(C^4\), with curvature radius \(r(\theta)=h(\theta)+h''(\theta)>0\). Sample oriented outward support-normal angles from a homogeneous Poisson process on the angular circle with intensity \(\lambda\) per radian; intersect the corresponding tangent halfplanes. Condition on having at least three angles and on all successive angular gaps being at most \(\pi/2\); the conditioning event has probability \(1-O_K((1+\lambda)e^{-\pi\lambda/2})\). Denote the resulting tangent polygon by \(Q_\lambda\), and its area and perimeter excesses over \(K\) by \(X_\lambda\) and \(Y_\lambda\).

As \(\lambda\to\infty\), jointly,
\[
\lambda^{5/2}\begin{pmatrix}
X_\lambda-\frac{1}{4\lambda^2}\int_0^{2\pi}r(\theta)^2\,d\theta\\
Y_\lambda-\frac{1}{2\lambda^2}\int_0^{2\pi}r(\theta)\,d\theta
\end{pmatrix}
\Longrightarrow N_2(0,\Sigma_K),
\]
where
\[
\Sigma_K=\begin{pmatrix}
\frac78\int_0^{2\pi}r^4 & \frac74\int_0^{2\pi}r^3\\
\frac74\int_0^{2\pi}r^3 & \frac72\int_0^{2\pi}r^2
\end{pmatrix}.
\]
The conditional mean excesses equal the displayed deterministic centerings up to \(O_K(\lambda^{-3})\); the conditional covariance matrix, multiplied by \(\lambda^5\), converges to \(\Sigma_K\).

The covariance determinant is
\[
\det\Sigma_K=\frac{49}{16}\left[\left(\int_0^{2\pi}r^4\right)\left(\int_0^{2\pi}r^2\right)-\left(\int_0^{2\pi}r^3\right)^2\right].
\]
It vanishes **if and only if \(K\) is a Euclidean disk**, allowing arbitrary translation and radius. Thus the joint second-order tangent-polygon law distinguishes disks from every noncircular smooth strictly convex body, although the individual area and perimeter fluctuations are Gaussian in both cases.

## Assumptions and scope
Angles are points of a Poisson process of intensity \(\lambda\,d\theta\) on \(\mathbb R/(2\pi\mathbb Z)\), not a fixed-number sample. The polygon is defined only on the stated good-gap event; conditioning is part of the definition. Each tangent halfplane is \(\{x:x\cdot(\cos\theta,\sin\theta)\le h(\theta)\}\). The smoothness \(h\in C^4\) and positivity of \(r\) ensure uniform local expansions. Every angular integral uses unnormalized Lebesgue measure in radians. A bivariate normal with singular covariance is interpreted as a Gaussian law supported on a line.

## Proof
**1. Geometric local expansion.** Write the sampled angles in cyclic order \(\theta_i\), with gaps \(d_i\in(0,2\pi)\). When the largest gap is at most \(\pi/2\), each selected support line contributes a genuine edge. Let \(x(\theta)=h(\theta)n(\theta)+h'(\theta)t(\theta)\) be the support contact, where \(n=(\cos\theta,\sin\theta)\) and \(t=(-\sin\theta,\cos\theta)\). Since \(x'(\theta)=r(\theta)t(\theta)\), the two tangent segments from consecutive contacts to their intersection have total length
\[
T(\theta,d)=\frac1{\cos(d/2)}\int_0^d r(\theta+s)\cos(s-d/2)\,ds.
\]
Subtracting the curve-arc length \(\int_0^d r(\theta+s)\,ds\) and Taylor expanding the explicitly nonnegative kernel gives, uniformly over \(\theta\) and \(0<d\le d_0<\pi/2\),
\[
T(\theta,d)-\int_0^d r(\theta+s)\,ds=\frac{r(\theta)}{12}d^3+O_K(d^4).
\]
The area between the tangent corner and the intervening convex arc is \(\frac{r(\theta)^2}{24}d^3+O_K(d^4)\). To verify the coefficient directly, replace the arc in contact coordinates by its osculating parabola \(y=x^2/(2r)\); the tangent-contact triangle contributes \(r^2d^3/8\), and the curved cap removes \(r^2d^3/12\). Uniform \(C^4\) Taylor bounds give the stated remainder. These corner regions have disjoint interiors, so summing produces
\[
X_\lambda=\frac1{24}\sum_i r(\theta_i)^2d_i^3+O_K\left(\sum_i d_i^4\right),\qquad
Y_\lambda=\frac1{12}\sum_i r(\theta_i)d_i^3+O_K\left(\sum_i d_i^4\right).
\]

**2. Cubic-gap Poisson lemma.** For a \(C^1\) angular weight \(w\), set \(S_\lambda(w)=\sum_i w(\theta_i)d_i^3\). Use all Poisson configurations, setting the sum to zero when there are no angles and setting the sole gap equal to \(2\pi\) when there is one angle. For \(E\sim\mathrm{Exp}(\lambda)\), put \(g_j(t)=\mathbb E[\min(E,t)^j]\). The one-point Palm formula gives
\[
\mathbb E S_\lambda(w)=\lambda g_3(2\pi)\int_0^{2\pi}w=\frac6{\lambda^2}\int_0^{2\pi}w+O(e^{-c\lambda}\operatorname{poly}(\lambda)).
\]
For two distinct forced Poisson points separated clockwise by \(t\), the two outgoing gaps depend on disjoint open arcs and have independent laws \(\min(E,t)\) and \(\min(E',2\pi-t)\). The two-point Palm identity therefore gives the *exact* covariance formula
\[
\begin{split}
\operatorname{Cov}(S_\lambda(w),S_\lambda(v))
={}&\lambda g_6(2\pi)\int_0^{2\pi}wv\\
&+\lambda^2\int_0^{2\pi}\!\int_0^{2\pi}
 w(\theta)v(\theta+t)
 \big[g_3(t)g_3(2\pi-t)-g_3(2\pi)^2\big]\,dt\,d\theta.
\end{split}
\]
The diagonal term, after multiplication by \(\lambda^5\), tends to \(720\int wv\). Each of the two boundary layers \(t\approx0\) and \(t\approx2\pi\) contributes \(-108\int wv\), since
\[
\int_0^\infty\big(g_3(t)-6/\lambda^3\big)\,dt
=-\frac{18}{\lambda^4}.
\]
Consequently,
\[
\lambda^5\operatorname{Cov}(S_\lambda(w),S_\lambda(v))\longrightarrow504\int_0^{2\pi}wv.
\]

For completeness, joint Gaussianity follows by a local Poisson-block argument rather than from covariance alone. Partition the angular circle into \(O(\lambda^{1/3})\) blocks of length \(O(\lambda^{-1/3})\). Discard points within \(10\log\lambda/\lambda\) of block boundaries and truncate outgoing gaps at that distance. The discarded total has \(\lambda^{5/2}\)-scaled \(L^1\) norm \(O(\lambda^{-1/6}\log\lambda)\); the probability of any truncated gap is \(O(\lambda^{-8})\). The remaining block contributions are independent. Partitioning each block further into a bounded-dependence grid of cells of length \(10\log\lambda/\lambda\) shows that the sum of fourth centered moments of the \(\lambda^{5/2}\)-scaled block contributions is \(O(\lambda^{-1/3}\operatorname{polylog}\lambda)=o(1)\). The Lyapunov theorem, the covariance limit above and Cramér–Wold yield, for every finite collection of \(C^1\) weights,
\[
\lambda^{5/2}\left(S_\lambda(w)-6\lambda^{-2}\int w\right)
\Longrightarrow \text{centered Gaussian},
\]
with cross-covariance \(504\int wv\).

**3. Transfer and moments.** The Poisson gap estimates give \(\mathbb E\sum_i d_i^4=O(\lambda^{-3})\) and \(\mathbb E(\sum_i d_i^4)^2=O(\lambda^{-6})\). Therefore the geometric remainders vanish in \(L^2\) when multiplied by \(\lambda^{5/2}\). The good-gap event fails with probability at most \(O((1+\lambda)e^{-\pi\lambda/2})\); on that event's complement the unconditional cubic-gap scores are bounded by a polynomial in the Poisson count. Conditioning consequently does not change any stated limit or moment asymptotic. Substituting \(w=r^2/24\) and \(v=r/12\) into the cubic-gap lemma gives exactly the centerings and entries of \(\Sigma_K\).

**4. Shape rigidity.** Cauchy–Schwarz gives \((\int r^3)^2\le(\int r^4)(\int r^2)\). Equality holds precisely when the positive continuous \(r\) is constant. Then \(h+h''=R\) has the general periodic solution \(h(\theta)=R+a\cos\theta+b\sin\theta\), which is the support function of a translated Euclidean disk. The converse follows immediately.

## Verification
The included standard-library checker `verify_poisson_tangent.py` independently computes sampled tangent intersections and polygon shoelace areas and edge perimeters. For the support function \(h(\theta)=1-\varepsilon\cos(2\theta)/3\), the exact curvature radius is \(r(\theta)=1+\varepsilon\cos(2\theta)\); \(\varepsilon=0\) tests the disk and \(\varepsilon=0.55\) a noncircle. It compares sample means and the rescaled full covariance matrix with the explicit integrals of powers of \(r\), checks the cubic local expansions, and checks the exact disk identities. The run reported `POISSON_TANGENT_GEOMETRY_AND_COVARIANCE_CHECKS_PASSED`. This is a finite numerical consistency test; the unbounded-parameter and Gaussian statements follow from the proof above.

## Relationship to prior work
Bakó-Szabó and Fodor (2024) establish variance upper bounds for mean width in a different circumscribed random-halfspace model, with random hyperplanes located outside \(K\) and a positive offset distribution. The construction here samples *only exact supporting tangents*, so its local angular-spacing scale and joint covariance are not corollaries of that work. Calka, Demichel and Enriquez (2021) study Poisson–Voronoi cells conditioned to contain a convex body, another model involving random hyperplane offsets. Hug and Schneider (2019/2020) likewise study stationary Poisson hyperplanes outside a body rather than a Poisson process supported on its tangent-normal circle. The present claim is the exact two-observable Gaussian covariance and its disk-rigidity determinant for the tangential-normal Poisson model; general random-polytope central limit theorems and standard Poisson-space calculations are not claimed as new. Searches did not identify an identical formula, but unindexed results expressed as circular-spacing functionals remain a priority risk.

## Limitations
The model is homogeneous *Poisson* angular sampling with random sample size, not a fixed number of tangents. Its constant \(504\) would change under fixed-count sampling; substituting a fixed count without reproving the covariance is invalid. The conditioning event prevents heavy-tailed near-unbounded tangential polygons; raw unconditioned area and perimeter moments need not be finite. The result is asymptotic and does not provide a Berry–Esseen rate, finite-sample exact distribution, or analogous classification for nonsmooth bodies or random offset halfplanes. Historical priority is provisional, and no independent mathematical audit has been conducted.

## References
1. A. Bakó-Szabó and F. Fodor, *On the variance of the mean width of random polytopes circumscribed around a convex body*, Mathematika 70 (2024), e12266. First publicly available 17 July 2024. DOI: 10.1112/mtk.12266.
2. P. Calka, Y. Demichel and N. Enriquez, *Large planar Poisson–Voronoi cells containing a given convex body*, Annales Henri Lebesgue 4 (2021), 711–757. DOI: 10.5802/ahl.86.
3. D. Hug and R. Schneider, *Poisson hyperplane processes and approximation of convex bodies*, Mathematika 66 (2020), 713–732; arXiv:1908.09498 (26 August 2019).
4. F. Fodor and V. Vígh, *Variance estimates for random disc-polygons in smooth convex discs*, Journal of Applied Probability 55 (2018), 1143–1157; arXiv:1802.02808 (8 February 2018). This concerns disc-polygon approximation rather than the tangent-normal model.
