# Sharp mass balancing of minimal atomic prediction measures on the disk

## Finding

Let \(n\ge1\), \(0<a<1\), and \(R=1/a\). Among probability measures \(\mu\) on the closed unit disk, consider *optimal degree-\(n\) prediction measures* at the exterior point \(R\), i.e. maximizers of
\[
\lambda_n(\mu,R)=\min_{p\in\mathbb C[z],\ \deg p\le n,\ p(R)=1}\int|p(z)|^2\,d\mu(z).
\]
The optimal value is \(R^{-2n}\), and every optimal measure has support on the unit circle. Let \(\mathcal A_{n,a}\) consist of the optimal measures with the **smallest possible number of distinct atoms**, namely \(n+1\). For \(\mu=\sum_{j=1}^{n+1}w_j\delta_{\zeta_j}\in\mathcal A_{n,a}\) define \(M(\mu)=\max_jw_j\) and \(m(\mu)=\min_jw_j\).

Define the finite Blaschke product
\[
B_{n,a}(z)=z^n\frac{z-a}{1-az}.
\]
Each \(\mu\in\mathcal A_{n,a}\) corresponds to exactly one phase \(\eta\in\mathbb T\). Its nodes are the \(n+1\) distinct solutions of \(B_{n,a}(\zeta)=\eta\) on \(\mathbb T\), and its masses are
\[
w_j=\frac{1-a^2}{1-a^2+n|\zeta_j-a|^2}.
\]

**Sharp load-balancing theorem.** The largest mass \(M\) is uniquely minimized over \(\mathcal A_{n,a}\) by \(\eta=-1\). Let \(\theta_{n,a}\in(0,\pi)\) be the unique solution of
\[
(n+1)\theta+2\arctan\frac{a\sin\theta}{1-a\cos\theta}=\pi.
\]
Then
\[
\min_{\mu\in\mathcal A_{n,a}} M(\mu)=\frac{1-a^2}{1-a^2+n(1+a^2-2a\cos\theta_{n,a})}.
\]
The smallest mass \(m\) is uniquely maximized by \(\eta=(-1)^n\). Let \(\delta_{n,a}\in(0,\pi)\) be the unique solution of
\[
(n+1)\delta-2\arctan\frac{a\sin\delta}{1+a\cos\delta}=\pi.
\]
Then
\[
\max_{\mu\in\mathcal A_{n,a}}m(\mu)=\frac{1-a^2}{1-a^2+n(1+a^2+2a\cos\delta_{n,a})}.
\]
Consequently the two optimal phase choices **coincide precisely when \(n\) is odd** (an even number of atoms); for even \(n\), they are different, so no minimal-atomic optimal prediction measure can simultaneously minimize its largest mass and maximize its smallest mass. For every fixed \(a\in(0,1)\), their sharp large-degree scales are
\[
\lim_{n\to\infty} n\min_{\mu\in\mathcal A_{n,a}}M(\mu)=\frac{1+a}{1-a},\qquad
\lim_{n\to\infty} n\max_{\mu\in\mathcal A_{n,a}}m(\mu)=\frac{1-a}{1+a}.
\]

## Assumptions and scope

The measure is a positive Borel probability measure, degree \(n\ge1\) and \(a\in(0,1)\) are fixed, and point \(R=1/a\) lies outside the closed unit disk. Atom counts mean distinct positive-mass support points. Rotating both the exterior point and the measures rotates the result, but the theorem is written with positive real \(R\) to fix phases. The mass objectives are optimized **only among measures using the minimum admissible \(n+1\) atoms**; there is no assertion about uniform bounded-density or higher-cardinality designs.

## Proof

**1. The prediction constraint.** The polynomial \(p_*(z)=(z/R)^n\) is admissible and has boundary modulus \(R^{-n}\), so \(\lambda_n(\mu,R)\le R^{-2n}\). The Poisson probability \(d\omega_a(e^{it})=(1-a^2)|e^{it}-a|^{-2}dt/(2\pi)\) satisfies \(\int z^k\,d\omega_a=a^k\) for \(k\ge0\). For \(1\le k\le n\), the perturbation \(q_k(z)=z^{n-k}-R^{-k}z^n\) vanishes at \(R\). On the unit circle,
\[
\langle z^n,q_k\rangle_{\mu}=\int z^k\,d\mu-R^{-k}.
\]
Thus for a circle-supported measure \(p_*\) minimizes the squared norm precisely when the first \(n\) complex moments equal \(a^k\). For an optimal measure on the whole disk, equality in \(\int|p_*|^2d\mu\le R^{-2n}\) forces circle support; the same orthogonality condition applies. Conversely the Poisson law has these moments, proving the optimum. An optimal measure needs at least \(n+1\) atoms: with at most \(n\) support points one can choose a polynomial vanishing there but equal to one at \(R\), making \(\lambda_n=0\).

**2. All smallest-support designs.** For any positive \((n+1)\)-atomic measure with the required moments define its Herglotz transform
\[
H(z)=\int_{\mathbb T}\frac{\zeta+z}{\zeta-z}\,d\mu(\zeta)
=\frac{1+az}{1-az}+O(z^{n+1})
\]
at zero. Set \(F=(H-1)/(H+1)\). As a rational inner function with \(n+1\) boundary preimages of \(1\), \(F\) is a finite Blaschke product of degree \(n+1\), and \(F(0)=0\). Then \(f=F/z\) is a finite Blaschke product of degree \(n\) with \(f(z)=a+O(z^n)\). Consequently
\[
\frac{f(z)-a}{1-af(z)}=\lambda z^n,\qquad |\lambda|=1,
\]
since a degree-\(n\) finite Blaschke product with a zero of order \(n\) at zero is a unimodular monomial. Rearranging gives
\[
F_\lambda(z)=z\frac{a+\lambda z^n}{1+a\lambda z^n}.
\]
Conversely every such \(F_\lambda\) is finite Blaschke of degree \(n+1\), and \((1+F_\lambda)/(1-F_\lambda)\) represents an \((n+1)\)-atomic probability measure whose first \(n\) moments match \(\omega_a\). Its atoms solve \(F_\lambda(\zeta)=1\), equivalently \(B_{n,a}(\zeta)=\lambda^{-1}=\eta\). Positive boundary angular derivative makes every node simple, and \(\eta\) is unique for each measure.

To derive the masses without a residue convention, the polynomials \(1\) and \(z^{k-1}(z-a)/\sqrt{1-a^2}\), \(1\le k\le n\), are orthonormal for \(\omega_a\). Thus its degree-\(n\) diagonal Christoffel kernel is
\[
K_n(\zeta,\zeta)=1+\frac{n|\zeta-a|^2}{1-a^2}.
\]
Exactness of the atomic quadrature on Laurent frequencies \(-n,\ldots,n\), applied to products of degree-\(n\) Lagrange polynomials, yields \(w_j=1/K_n(\zeta_j,\zeta_j)\), giving the stated formula.

**3. Extremal phase geometry.** Write \(B_{n,a}(e^{it})=e^{i\Phi(t)}\) with continuous unwrapped phase \(\Phi(0)=0\). Direct differentiation gives
\[
\Phi'(t)=n+\frac{1-a^2}{1+a^2-2a\cos t}>0.
\]
The phase is odd about zero, and \(\Phi(\pi)=(n+1)\pi\). Since \(w(\zeta)\) strictly decreases with angular distance from \(1\), the largest mass is attached to the node nearest \(1\). For any phase level \(\eta=e^{iu}\), \(0\le u\le2\pi\), the nearest positive and negative node angles to zero are \(\Phi^{-1}(u)\) and \(-\Phi^{-1}(2\pi-u)\). Their minimum distance from zero is maximized only at \(u=\pi\), where the two nodes tie. This proves unique minimization of \(M\) at \(\eta=-1\) and gives the formula through \(\Phi(\theta_{n,a})=\pi\).

Similarly the smallest mass is at the node nearest \(-1\). Centering the unwrapped phase at \(t=\pi\), its strictly increasing, odd angular increment shows that the distance to the nearest node is maximized uniquely when the phase level is opposite to \(B_{n,a}(-1)=(-1)^{n+1}\), namely \(\eta=(-1)^n\). For the nearest nodes \(t=\pi\pm\delta_{n,a}\), the condition \(\Phi(\pi)-\Phi(\pi-\delta_{n,a})=\pi\) gives the displayed equation and the exact smallest-mass optimum. Since \(a>0\) makes the mass strictly monotone in angular distance, both phase optimizers are unique. Their coincidence is exactly the parity statement.

**4. Sharp asymptotics.** At the reference endpoints, the phase derivatives are \(\Phi'(0)=n+(1+a)/(1-a)\) and \(\Phi'(\pi)=n+(1-a)/(1+a)\). Taylor expansion of the two defining angular equations gives, for fixed \(a\),
\[
\theta_{n,a}=\frac{\pi}{n+(1+a)/(1-a)}+O_a(n^{-4}),\qquad
\delta_{n,a}=\frac{\pi}{n+(1-a)/(1+a)}+O_a(n^{-4}).
\]
Substitution into the exact mass formulas yields the two limits. The \(O_a\) bounds are not asserted uniform as \(a\uparrow1\).

## Verification

The accompanying `check.py` reconstructs node polynomials, checks unit-circle roots and positive masses, recomputes the first \(n\) moments for several distinct phases and parameters, checks both optimizing phases against competing phases, and tests large-degree limits via monotone scalar root equations. It reports 2,424 passing finite diagnostics in the stated environment. These checks are supplemental to, not substitutes for, the analytic proof; no finite sampling certifies phase uniqueness or all-degree validity.

A small exact illustration is \(a=1/2\), \(n=2\). At \(\eta=-1\), masses are \((3/7,3/7,1/7)\), so the best largest mass is \(3/7\). At \(\eta=1\), masses are \((3/5,1/5,1/5)\), giving the best smallest mass \(1/5\). The two criteria genuinely conflict in this odd-atom example.

## Relationship to prior work

Bos, Levenberg, and Ortega-Cerdà identify the exterior disk prediction optimum and the Poisson moment construction, and explicitly note the availability of discrete optimal designs by Szegő quadrature. Charpentier, Levenberg, and Wielonsky study asymptotic behavior of optimal prediction measures and treat the disk's Poisson law. Classical paraorthogonal/Szegő quadrature theory covers the one-parameter construction and exactness mechanism. The added result here is the pair of **sharp phase optimizations of the extreme atomic loads, their uniqueness, and their parity compatibility**, over the full family of minimal-cardinality disk-optimal designs. A distinct older quadrature-weight balancing theorem could potentially imply the phase optimization; historical priority is not independently certified.

## Limitations

The result fixes an exterior point and a minimal-atom design; it does not optimize predictor variance (already known), cover general planar domains, or rule out better mass balances using additional atoms. It does not claim effective uniform-in-\(a\) asymptotics. The classical quadrature family is background, not claimed as a new discovery. Historical-priority comparison is best-knowledge rather than exhaustive, and no independent mathematical audit is asserted.

## References

1. S. Charpentier, N. Levenberg, F. Wielonsky, *An extremal problem for the Bergman kernel of orthogonal polynomials*, arXiv:2207.04662, first submitted 11 July 2022. https://arxiv.org/abs/2207.04662
2. L. Bos, N. Levenberg, J. Ortega-Cerdà, *Optimal Polynomial Prediction Measures and Extremal Polynomial Growth*, Constructive Approximation 54 (2021), 431–453, first online 2 November 2020. https://doi.org/10.1007/s00365-020-09522-1
3. B. de la Calle Ysern, *Optimal extension of the Szegő quadrature*, IMA Journal of Numerical Analysis 35 (2015), 722–748, first online 3 April 2014. https://doi.org/10.1093/imanum/dru012
4. W. B. Jones, O. Njåstad, W. J. Thron, *Moment theory, orthogonal polynomials, quadrature, and continued fractions associated with the unit circle*, Bulletin of the London Mathematical Society 21 (1989), 113–152, as cited in reference 2.
