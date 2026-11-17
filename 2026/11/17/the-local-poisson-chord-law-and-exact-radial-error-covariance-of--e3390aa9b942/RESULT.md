# The local Poisson-chord law and exact radial-error covariance of random cyclic polygons

## Finding

Let \(K_n\) be the convex hull of \(n\ge3\) independent arclength-uniform points on the Euclidean unit circle. When the origin belongs to \(K_n\), let \(\rho_n(\theta)\) be the radial distance from the origin to its boundary in direction \((\cos\theta,\sin\theta)\); otherwise put \(\rho_n(\theta)=0\). Set \(D_n(s)=n^2[1-\rho_n(s/n)]\) for real \(s\), with angles interpreted modulo \(2\pi\).

Let \(\Pi\) be a stationary rate-\(\lambda=1/(2\pi)\) Poisson point process on the real line. Write \(L_s=s-\sup\{y\in\Pi:y<s\}\), \(R_s=\inf\{y\in\Pi:y>s\}-s\), and \(D(s)=L_sR_s/2\). Then for every fixed finite tuple of real locations, \(D_n\) converges jointly in distribution to \(D\), and its first and second joint moments converge as well. In particular,
\[
\mathbb ED(s)=2\pi^2,\quad \operatorname{Var}D(s)=12\pi^4,
\]
\[
\boxed{\operatorname{Cov}(D(0),D(s))=4\pi^4 e^{-u}\left(3+3u+\frac{u^2}{2}\right),\quad u=\frac{|s|}{2\pi}.}
\]
Consequently the fixed-angular-separation microscopic covariance has an exact, strictly positive, exponentially decaying quadratic profile. For \(x>0\), the one-point inclusion-probability boundary window satisfies
\[
\boxed{\lim_{n\to\infty}\Pr\!\left\{(1-x/n^2,0)\in K_n\right\}=1-\frac{\sqrt{2x}}{\pi}K_1\!\left(\frac{\sqrt{2x}}{\pi}\right),}
\]
where \(K_1(z)=\int_0^\infty e^{-z\cosh t}\cosh t\,dt\) is the modified Bessel function. At \(x=0\), the limit is zero, interpreted continuously.

## Assumptions and scope

Sampling is independent and uniform with respect to angular arclength on the *unit circle*, not area-uniform in its disk. The random hull is the usual Euclidean convex hull. All limits keep real \(s\), \(x\), and every number of query locations fixed while \(n\to\infty\). The choice \(\rho_n=0\) when the origin is absent is a total definition and is asymptotically irrelevant. The covariance is for *centered radial deficits*, not the global Hausdorff error or missing-area variance. Poisson intervals use the nearest points strictly to either side; their equalities at fixed deterministic sites have probability zero.

## Proof

**1. Microscopic point-process limit.** Around angular origin, lift the sampled directions periodically and multiply their angles by \(n\). For any disjoint bounded intervals \(I_1,\ldots,I_m\subset\mathbb R\), the counts are multinomial with each hit probability \(|I_j|/(2\pi n)\). Their joint probability generating function converges to that of independent Poisson counts with means \(\lambda|I_j|\), where \(\lambda=1/(2\pi)\). Hence the rescaled circular samples converge locally to the stationary simple Poisson process \(\Pi\). In any fixed finite collection of locations \(s_j\), the nearest left/right gaps converge jointly to \((L_{s_j},R_{s_j})\); the continuous-mapping theorem applies because fixed sites are almost surely not Poisson points.

**2. Exact chord intersection.** If \(\alpha,\beta>0\) are the angular gaps from a ray to its nearest counterclockwise and clockwise sampled vertices, respectively, and their sum is less than \(\pi\), the intervening edge meets that ray at radius
\[
\rho=\frac{\sin(\alpha+\beta)}{\sin\alpha+\sin\beta}.
\]
This follows either from the two endpoint coordinates or the sine rule for the small triangle bounded by the origin, chord, and ray. For bounded \(A=n\alpha\), \(B=n\beta\), Taylor expansion at zero gives uniformly
\[
n^2\left(1-\frac{\sin((A+B)/n)}{\sin(A/n)+\sin(B/n)}\right)=\frac{AB}{2}+O_{A,B}(n^{-2}).
\]
When all sampled angular gaps are below \(\pi\), the origin is strictly inside the hull and this edge is the unique edge crossing the selected ray. The complementary event has probability \(n2^{1-n}\) by the disjoint long-gap events (the classical central semicircle/Wendel observation). The point-process limit and chord expansion establish finite-dimensional convergence to \(D(s)=L_sR_s/2\).

**3. Convergence of moments.** On the good event, with angular neighbor gaps \(\alpha,\beta\) and \(g=\alpha+\beta<\pi\), the radial chord intersection is at least \(\cos(g/2)\). Thus
\[
0\le n^2(1-\rho_n)\le(n g)^2/8.
\]
For either one-sided rescaled gap \(Z\), \(\Pr\{Z>v\}\le\exp[-v/(2\pi)]\) as long as the relevant arc has length at most one circumference. Consequently all fixed moments of \(ng\) are uniformly bounded, and so are all moments of \(D_n\) restricted to the good event. On the complementary event \(D_n\le n^2\), whose contribution to every fixed moment is bounded by a polynomial in \(n\) times \(n2^{1-n}\). Therefore products of two \(D_n\)'s are uniformly integrable (indeed all fixed polynomial moments are), proving convergence of means, second moments, and covariances.

**4. Exact covariance.** At a stationary Poisson location zero, let \(A=L_0\) and \(B=R_0\). These are independent \(\operatorname{Exp}(\lambda)\) variables, hence \(\mathbb ED(0)=1/(2\lambda^2)\). Fix \(t\ge0\), write \(u=\lambda t\), and split at the first Poisson point to the right of zero. If \(B>t\), both positions lie in the same interval and \(D(t)=(A+t)(B-t)/2\); memorylessness and \(\mathbb E A^2=2/\lambda^2\) give
\[
\mathbb E[D(0)D(t);B>t]=\frac{e^{-u}(u+2)^2}{4\lambda^4}.
\]
If \(B=b\le t\), the process regenerates at \(b\). The expected age at time \(t-b\) is \((1-e^{-\lambda(t-b)})/\lambda\), and the forward waiting time has independent mean \(1/\lambda\). Integrating over the exponential density of \(B\) gives
\[
\mathbb E[D(0)D(t);B\le t]=\frac1{4\lambda^4}\int_0^u v e^{-v}(1-e^{-(u-v)})\,dv
=\frac{1-e^{-u}(1+u+u^2/2)}{4\lambda^4}.
\]
Adding the two cases and subtracting \((1/(2\lambda^2))^2\) yields
\[
\operatorname{Cov}(D(0),D(t))=\frac{e^{-u}}{4\lambda^4}\left(3+3u+\frac{u^2}{2}\right).
\]
Stationarity makes it an even function of \(t\). Substituting \(\lambda=1/(2\pi)\) proves the boxed formula and its zero-lag variance.

**5. Boundary-window distribution.** Because \(A\) and \(B\) are independent exponentials, for \(x>0\),
\[
\Pr(D(0)>x)=\int_0^\infty\lambda e^{-\lambda a-2\lambda x/a}\,da
=2\lambda\sqrt{2x}\,K_1(2\lambda\sqrt{2x}).
\]
The last equality follows from the substitution \(a=\sqrt{2x}\,e^t\) and the defining hyperbolic integral for \(K_1\). The distribution is continuous on \((0,\infty)\) and has no atom at zero. On the event \(0\in K_n\), the inclusion event \((1-x/n^2,0)\in K_n\) is equivalent to \(D_n(0)\le x\) for sufficiently large \(n\). Their unconditional probabilities differ by at most \(n2^{1-n}\); therefore the distributional limit gives the stated inclusion law. At \(x=0\), no nondegenerate random polygon contains the boundary point \((1,0)\), and the limit agrees.

## Verification

Run `python verify_cyclic_radial.py` (Python standard library only). It independently reconstructs exact Euclidean chord intersections from random cyclic polygons, checks the limiting two-point covariance against Monte Carlo renewal trajectories, evaluates the two conditional integrals by quadrature, and compares finite-sample circle-containment probabilities with the boundary-window integral. The saved verifier passed all tests. Finite numerical tests are corroboration, not the proof of convergence; the exact expansions, Poisson convergence, integrability bound, and renewal calculation above supply the proof.

## Relationship to prior work

Ismailov (2026), extending a 2018 calculation of Jeremy Tan Jie Rui, proves the exact *three-vertex* containment probability at a fixed interior radius, involving a dilogarithm; this does not give a growing-sample microscopic two-point radial covariance. The classical Wendel (1962) semicircle probability concerns center containment, not the boundary layer. Sonnleitner (2025) proves a Gumbel law for the *maximum* Hausdorff error of boundary-sampled hulls, on a different scale; the present claim is a fixed-location Poisson chord-product process with an explicit covariance. Published fixed-sample logarithmic boundary-absorption and conditional rare center-clearance results treat different order-of-limits/conditional events. Jewell and Romano (1982) give general coverage/inclusion identities potentially relevant to finite-sample one-point distributions, but a complete copy was unavailable for comparison; no priority claim is made about the general semicircle integral. The contribution considered here is the explicit microscopic two-point covariance and its joint Poisson-chord formulation, together with the Bessel boundary-window marginal.

## Limitations

The geometry is the planar unit circle with uniform boundary sampling. No extension to arbitrary smooth curves, different sampling densities, disk-interior sampling, or separated macroscopic angular locations is established. The point-process convergence is finite-dimensional (with polynomial moments), not a global uniform-process theorem. The local covariance cannot simply be integrated over an entire circle to recover global fixed-count missing-area variance: the fixed sample count produces weak long-range correlations that affect that variance. Earlier literature may implicitly contain related local gap limits; historical priority has not been independently certified.

## References

1. A. Ismailov, *With what probability does an inscribed triangle contain a given point?*, arXiv:2601.02929 (first posted 2026-01-06), https://arxiv.org/abs/2601.02929 .
2. M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442 (first posted 2025-08-22), https://arxiv.org/abs/2508.16442 .
3. N. P. Jewell and J. P. Romano, *Coverage problems and random convex hulls*, *Journal of Applied Probability* 19 (1982), 546–561, DOI:10.2307/3213513, https://doi.org/10.2307/3213513 .
4. J. G. Wendel, *A Problem in Geometric Probability*, *Mathematica Scandinavica* 11 (1962), 109–111, DOI:10.7146/math.scand.a-10655, https://doi.org/10.7146/math.scand.a-10655 .
5. *Local curvature from the logarithmic containment law of random inscribed polygons* (publicly archived mathematical result, 2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-local-curvature-from-the-logarithmic-containment-law-of-random-i--a0ac1da8caab .
6. *Marked Wendel law and convex-order optimal sampling for random inscribed polygons* (publicly archived mathematical result, 2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-marked-wendel-law-and-convex-order-optimal-sampling-for-random-i--6fc92189d743 .
