# Arithmetic contact and density laws for two-rate Gaussian semigroups

## Finding

There is a sharp arithmetic change in the geometry of the complex-time boundedness region of a two-rate Ornstein–Uhlenbeck semigroup on complex \(L^p\). This change has three connected manifestations: the exact group of imaginary periods, a linear-versus-quadratic small-real-time law for the density of bounded imaginary times, and a contact constant determined by Diophantine approximation.

Fix \(1<p<\infty\), \(p\ne2\), and \(\alpha,\beta>0\). Put
\[
 k_p=\tan\bigl(\arccos|1-2/p|\bigr)=\frac{2\sqrt{p-1}}{|p-2|},
 \qquad \theta=\frac{\beta}{\alpha}.
\]
On \(X=L^p(\mathbb R^2,\gamma\otimes\gamma;\mathbb C)\), with \(\gamma\) the standard one-dimensional Gaussian probability measure, let
\[
 A=\alpha(-\partial_x^2+x\partial_x)+\beta(-\partial_y^2+y\partial_y).
\]
Initially define \(S(z)=\exp(-zA)\) on the algebraic span of tensor-product Hermite polynomials. Write \(\mathcal B\) for the set of \(z\in\mathbb C\) at which this operator extends boundedly to \(X\). Then, **including every boundary point**, 
\[
\boxed{\mathcal B=\left\{t+is:\ t\ge0,\quad
 |\sin(\alpha s)|\le k_p\sinh(\alpha t),\quad
 |\sin(\beta s)|\le k_p\sinh(\beta t)\right\}.}
\]
The extended operator has norm exactly one at every point of \(\mathcal B\), and the maximal locally bounded holomorphy domain is \(\operatorname{int}\mathcal B\). Define its lower real-time boundary at imaginary height \(s\) by
\[
 h(s)=\inf\{t\ge0:t+is\in\mathcal B\}
 =\max\left\{\frac{\operatorname{arsinh}(|\sin(\alpha s)|/k_p)}{\alpha},
 \frac{\operatorname{arsinh}(|\sin(\beta s)|/k_p)}{\beta}\right\}.
\]

**Period group.** If \(\theta=m/n\in\mathbb Q_{>0}\) in lowest terms and \(\omega=\alpha/n=\beta/m\), then \(\{u\in\mathbb R:\mathcal B+iu=\mathcal B\}=\frac{\pi}{\omega}\mathbb Z\). If \(\theta\) is irrational, this group is \(\{0\}\).

**Sharp vertical-density asymptotics.** For each \(t>0\), the limit
\[
 d(t)=\lim_{R\to\infty}\frac1R\left|\{s\in[0,R]:t+is\in\mathcal B\}\right|
\]
exists. For irrational \(\theta\), its exact value is
\[
\boxed{d(t)=\frac4{\pi^2}\arcsin\!\bigl(\min\{1,k_p\sinh(\alpha t)\}\bigr)
\arcsin\!\bigl(\min\{1,k_p\sinh(\beta t)\}\bigr),}
\]
so
\[
\boxed{d(t)=\frac{4k_p^2\alpha\beta}{\pi^2}t^2+O(t^4)\qquad(t\downarrow0).}
\]
For rational \(\theta=m/n\), with \(\omega\) as above, the density is the normalized length of the intersection of the two allowed sets in one common period \([0,\pi/\omega]\), and satisfies
\[
\boxed{d(t)=\frac{2k_p\omega}{\pi}t+O(t^3)\qquad(t\downarrow0).}
\]
Thus the small-real-time vertical density has exponent two for irrational rate ratios and exponent one for rational ratios, even though either constituent one-dimensional semigroup has density of first order.

**Sharp Diophantine contact.** If \(\theta\) is irrational, set \(\lambda(\theta)=\liminf_{m\to\infty}m\|m\theta\|_{\mathbb R/\mathbb Z}\). Then
\[
\boxed{\liminf_{|s|\to\infty}|s|h(s)=\frac{\pi^2}{2k_p\alpha\beta}\lambda(\theta).}
\]
For \(\theta=(1+\sqrt5)/2\), \(\lambda(\theta)=1/\sqrt5\), giving an explicit nonzero contact constant. For an irrational with \(\lambda(\theta)=0\), the contact constant vanishes despite the absence of a nonzero exact imaginary period. The formula specifies a \(\liminf\), **not** a uniform two-sided estimate for every large \(s\).

## Assumptions and scope

The Banach space is the complexification of the usual Gaussian \(L^p\) space on the *product* of two independent one-dimensional Gaussian coordinates. Both relaxation rates are strictly positive, and the exponent satisfies \(1<p<\infty\), \(p\ne2\). No nonnormal drift or correlated Gaussian invariant law is claimed. Periods and densities refer to bounded extensions of the polynomial-defined complex-time family, not just its positive-real-time \(C_0\)-semigroup. The asymptotic parameter is the real part \(t\downarrow0\) *after* the vertical-density limit \(R\to\infty\).

## Proof

**1. Tensor reduction and boundary.** Let \(L=-\frac{d^2}{dx^2}+x\frac{d}{dx}\) on one-dimensional Gaussian \(L^p\). The one-dimensional complex Hermite multiplier \(e^{-wL}\) is bounded exactly on the closed Epperson region \(E_p=\{t+is: |\sin s|\le k_p\sinh t\}\), with norm one there. This is the established Gaussian complex-hypercontractivity theorem, including its boundary; see Janson's general operator criterion and van Neerven–Portal's Gaussian-region discussion. On the tensor-Hermite core,
\[
 S(z)=e^{-\alpha z L}\otimes e^{-\beta z L}.
\]
If both factors are bounded, Fubini and iterated \(L^p\) bounds make the tensor bounded, with norm at most one; it fixes the constant function, so its norm is one. Conversely, restricting the tensor to functions of only \(x\), or only \(y\), shows that boundedness forces boundedness of each factor. This gives the boxed region and, by solving the two monotone inequalities in \(t\), the exact formula for \(h\). The Hermite-polynomial dependence is entire, while bounded extensions have constant norm one; local uniform boundedness on \(\operatorname{int}\mathcal B\) yields Banach-space-valued holomorphy, hence operator-norm holomorphy. No larger open subset of \(\mathcal B\) exists.

**2. Exact period group.** On the imaginary axis, the two inequalities force \(\alpha s\in\pi\mathbb Z\) and \(\beta s\in\pi\mathbb Z\). If \(\beta/\alpha=m/n\) in lowest terms, these common imaginary-axis points are precisely \((\pi/\omega)\mathbb Z\); if the ratio is irrational, the only point is zero. Every vertical period of \(\mathcal B\) must translate \(0\in\mathcal B\) into another point of \(\mathcal B\) on the imaginary axis, so it must be among these points. Conversely the common zero lattice translates both sine inequalities into themselves, giving all periods.

**3. Vertical densities.** Put \(a_t=\min\{1,k_p\sinh(\alpha t)\}\) and \(b_t=\min\{1,k_p\sinh(\beta t)\}\). The allowed sets are products of \(\pi\)-periodic arc indicators of total normalized lengths \(2\arcsin(a_t)/\pi\) and \(2\arcsin(b_t)/\pi\), respectively. If \(\alpha/\beta\) is irrational, the linear flow \(s\mapsto(\alpha s,\beta s)\bmod\pi\) equidistributes on the two-torus. The indicators are Riemann integrable (their boundaries are null sets), so the time average is the product of their means. Expanding \(\sinh u=u+O(u^3)\) and \(\arcsin u=u+O(u^3)\) proves the quadratic law with an \(O(t^4)\) remainder.

If \(\alpha=n\omega\) and \(\beta=m\omega\), the joint indicator has period \(\pi/\omega\), proving existence of its mean. Within one period, the zero sets of \(\sin(n\omega s)\) and \(\sin(m\omega s)\) meet only at its identified endpoints because \(m,n\) are coprime. Hence for all sufficiently small \(t\), the two allowed arc sets intersect only near that common zero. The individual half-widths there equal
\[
 \frac{\arcsin(k_p\sinh(n\omega t))}{n\omega}=k_p t+O(t^3),\qquad
 \frac{\arcsin(k_p\sinh(m\omega t))}{m\omega}=k_p t+O(t^3).
\]
Their intersection is one circular interval of length \(2k_p t+O(t^3)\). Dividing by \(\pi/\omega\) proves the rational law.

**4. Contact and best rational approximations.** For \(r>0\) put \(Z_r=(\pi/r)\mathbb Z\) and \(\delta_r(s)=\operatorname{dist}(s,Z_r)\). Uniformly as \(h(s)\to0\), the exact boundary formula and the Taylor expansions of sine, arcsine and inverse hyperbolic sine imply
\[
 h(s)=\frac1{k_p}\max\{\delta_\alpha(s),\delta_\beta(s)\}\,[1+O(h(s)^2)]. \tag{1}
\]
To obtain an upper bound, let \(m_j\to\infty\) be integers with \(m_j\|m_j\theta\|\to\lambda(\theta)\), and choose nearest integers \(n_j\) to \(m_j\theta\). Dirichlet's theorem ensures this liminf is finite. The two nearest zero sites
\[
 a_j=\frac{\pi m_j}{\alpha},\qquad b_j=\frac{\pi n_j}{\beta}
\]
are separated by \(\Delta_j=\pi\|m_j\theta\|/\beta=O(1/m_j)\). At their midpoint \(s_j=(a_j+b_j)/2\), the distances to both zero lattices equal \(\Delta_j/2\) for sufficiently large \(j\). Applying (1) gives
\[
 s_jh(s_j)=\frac{\pi^2}{2k_p\alpha\beta}
 m_j\|m_j\theta\|+o(1),
\]
which yields the required upper bound.

For the reverse bound, the previous construction guarantees a sequence along which \(|s|h(s)\) stays bounded. Consequently only sequences with \(h(s)=O(1/|s|)\) need be considered for the liminf. For each such \(s\), choose nearest lattice points \(a=\pi m/\alpha\) and \(b=\pi n/\beta\). Since \(\delta_\alpha,\delta_\beta=O(1/|s|)\), we have \(m\sim\alpha|s|/\pi\) in absolute value. The triangle inequality and (1) give
\[
 h(s)\ge\frac{|a-b|}{2k_p}(1+o(1))
 =\frac{\pi}{2k_p\beta}|m\theta-n|(1+o(1)),
\]
and therefore
\[
 |s|h(s)\ge\frac{\pi^2}{2k_p\alpha\beta}
 |m|\|m\theta\|(1+o(1)).
\]
Taking the liminf proves equality. Symmetry \(h(-s)=h(s)\) handles both signs. The classical continued-fraction identity \(\lambda((1+\sqrt5)/2)=1/\sqrt5\) supplies the explicit example.

## Verification

The standalone `CHECK.py` uses only the Python standard library and can be run with `python CHECK.py`. It tests the exact lower-boundary function against both original operator-region inequalities, checks periodicity for four coprime rate pairs, computes normalized intersection lengths for three small-real-time scales, checks the irrational torus-mean expansion, and evaluates golden-ratio continued-fraction near-contacts. The executed output was: `PASS: 1616 periodicity, 12 rational-density, 9 irrational-density, 11 golden-contact, 597 epigraph tests.` It also reported the golden contact constant `0.787474464789772` for \(p=4,\alpha=1,\beta=(1+\sqrt5)/2\). These tests do **not** prove equidistribution, the boundary contractivity theorem, or the infinite-sequence liminf; those facts are handled by the argument and cited theorems above.

## Relationship to prior work

The one-dimensional closed Epperson region and norm-one dichotomy are due to complex Gaussian hypercontractivity. Janson's general second-quantization criterion [2, Theorem 2] already **covers the boundedness and contractivity test for diagonal multi-rate Gaussian operators**; the tensor formula is not presented as a new operator theorem. Van Neerven and Portal [3, especially Section 6] develop another route to the complex-time Gaussian criterion. The recent analysis by Bruno, Casarino, Ciatti and Sjögren [1] of the *inverse* Ornstein–Uhlenbeck semigroup distinguishes its spectral and mapping behavior from that of the classical Gaussian semigroup, and makes variable drift and \(L^p\)-semigroup boundedness a natural comparison problem. We instead examine complex-time geometry for the simpler *classical* invariant-Gaussian model; no inverse-Gaussian result is claimed. Perelmuter [5] subsequently emphasized imaginary-time covariance and periodicity for a common-rate Gaussian semigroup; it is included only as a subsequent scientific comparison.

The new assertion is the *exact arithmetic geometry* of the two-rate boundedness region: its full period group, a rational/irrational change in the small-real-time vertical-density exponent, and the precise Lagrange-constant contact law. The derivation uses equidistribution and sharp simultaneous zero-lattice approximation beyond the general Gaussian norm criterion; it does not contradict, replace or strengthen that norm criterion. Generic facts about irrational rotations and continued fractions are standard ingredients, not claimed as new results.

## Limitations

This is a two-independent-coordinate Gaussian model, not an arbitrary matrix-valued Ornstein–Uhlenbeck drift. The density is a large-imaginary-window asymptotic at each *fixed* positive real time; no uniform convergence rate in the window length is asserted. The contact identity is a liminf, not an all-heights bound or a claim of positive contact for every irrational ratio. The small-real-time asymptotics are not uniform when rational rate ratios have unbounded denominators. The result depends on established complex hypercontractivity at the boundary and classical equidistribution and Diophantine approximation. 

## References

[1] T. Bruno, V. Casarino, P. Ciatti, and P. Sjögren, *Spectral and mapping properties of the inverse Ornstein–Uhlenbeck operator*, arXiv:2611.06826v1 (first public submission 4 November 2026), Sections 1–6, https://arxiv.org/html/2611.06826v1. Primary MSC2020 47A10.

[2] S. Janson, *On complex hypercontractivity*, Journal of Functional Analysis **151** (1997), 270–280, Theorems 1–2; author-hosted text https://www2.math.uu.se/~svantejs/papers/sj119.pdf.

[3] J. van Neerven and P. Portal, *Weyl calculus with respect to the Gaussian measure and restricted \(L^p\)–\(L^q\) boundedness of the Ornstein–Uhlenbeck semigroup in complex time*, Bulletin de la Société Mathématique de France **146** (2018), 691–712, especially Section 6, arXiv:1702.03602, https://arxiv.org/pdf/1702.03602.

[4] J. B. Epperson, *The hypercontractive approach to exactly bounding an operator with complex Gaussian kernel*, Journal of Functional Analysis **87** (1989), 1–30; discussed and recovered in [2] and [3].

[5] M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1 (first public submission 11 November 2026), Sections 1–4, https://arxiv.org/html/2611.15455v1. Later scientific comparison, not the motivating work.
