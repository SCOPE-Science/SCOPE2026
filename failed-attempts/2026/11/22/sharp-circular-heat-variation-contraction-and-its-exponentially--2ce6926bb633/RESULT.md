# Sharp circular heat variation contraction and its exponentially flat onset

## Finding

On the real circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), the heat semigroup \(H_t=e^{t\partial_\theta^2}\) has the **sharp, attained bounded-variation contraction coefficient**
\[
K(t)=\sup_{V(f)>0}\frac{V(H_tf)}{V(f)}
=2\int_{-\pi/2}^{\pi/2}k_t(u)\,du-1
=\frac{4}{\pi}\sum_{j=0}^\infty\frac{(-1)^j e^{-(2j+1)^2t}}{2j+1}, \qquad t>0.
\]
The unique nonconstant norming functions, up to adding a constant and multiplying by a nonzero real scalar, are indicators of semicircles, at arbitrary angular positions. In particular \(0<K(t)<1\) for each positive time. The coefficient is strictly decreasing and strictly submultiplicative:
\[
K'(t)<0,\qquad K(s+t)<K(s)K(t)\quad(s,t>0).
\]
Its two sharp time regimes are
\[
1-K(t)=\frac{8}{\pi^{3/2}}\sqrt t\,e^{-\pi^2/(16t)}\left(1-\frac{8t}{\pi^2}+O(t^2)\right)\quad (t\downarrow0),
\]
\[
K(t)=\frac4\pi e^{-t}-\frac4{3\pi}e^{-9t}+O(e^{-25t})\quad(t\to\infty).
\]

## Assumptions and scope

A real periodic function \(f\) has distributional derivative \(Df\), a finite real signed Borel measure, precisely when \(f\in BV(\mathbb T)\). Define \(V(f)=|Df|(\mathbb T)\); this includes both jumps of a periodic two-step function and the seam jump when present. Functions are identified almost everywhere and constants have zero variation. The Laplacian normalization is \(\partial_\theta^2\), so its \(n\)-th Fourier multiplier is \(e^{-n^2t}\). The circular heat density of total mass one is
\[
k_t(u)=\frac1{\sqrt{4\pi t}}\sum_{m\in\mathbb Z}e^{-(u+2\pi m)^2/(4t)}=\frac1{2\pi}\left(1+2\sum_{n=1}^\infty e^{-n^2t}\cos(nu)\right).
\]
All claims hold for every positive real \(t\) and every real circular BV function, without an a priori boundedness or continuity condition beyond BV. Equality cases are nonconstant only.

## Proof

**1. Strict radial monotonicity.** Set \(q=e^{-t}\in(0,1)\). The Jacobi triple product gives
\[
2\pi k_t(u)=\prod_{m=1}^\infty(1-q^{2m})(1+2q^{2m-1}\cos u+q^{4m-2}).
\]
Every factor is positive. Each second factor strictly decreases in \(u\in(0,\pi)\); logarithmic differentiation of the absolutely convergent product shows \(k_t'(u)<0\) there. The kernel is even and periodic, and hence has a unique maximum at angle zero and minimum at the antipode. Strict geodesic monotonicity itself is a classical heat-kernel property, used here as input, not claimed as a discovery.

**2. Reduction to two atoms.** Write \(\mu=Df\). Its total mass is zero. If \(V(f)>0\), the Jordan decomposition has the form \(\mu=(V(f)/2)(p-q)\) for probability measures \(p,q\). Commuting distributional differentiation with circular convolution gives
\[
D(H_tf)=k_t*\mu=\frac{V(f)}2\int_{\mathbb T\times\mathbb T}\left[k_t(\cdot-a)-k_t(\cdot-b)\right]p(da)q(db).
\]
By the triangle inequality and Fubini,
\[
\frac{V(H_tf)}{V(f)}\le\max_{a,b\in\mathbb T}\frac12\int_\mathbb T|k_t(u-a)-k_t(u-b)|\,du.
\]
The half-factor is essential: two opposite unit atoms have total variation two. This reduction is a specialization of the classical Dobrushin zero-mass kernel bound; the general measure-theoretic reduction is not claimed as new.

**3. Exact optimization of the angular shift.** Rotations, reflection and evenness reduce the distance to a shift \(0\le h\le\pi\). Because \(k_t\) decreases strictly with geodesic distance, the positive part of \(k_t(u)-k_t(u-h)\) is the arc \(u\in(h/2-\pi,h/2)\) modulo \(2\pi\). Its integral equals
\[
\delta_t(h)=2\int_{h/2-\pi}^{h/2}k_t(u)\,du-1,
\]
where the second translated arc integral equals the first arc's complement by reflection symmetry. Consequently
\[
\delta_t'(h)=k_t(h/2)-k_t(\pi-h/2)>0\quad (0<h<\pi).
\]
The sole maximizing angular separation is \(h=\pi\). Thus \(K(t)=\delta_t(\pi)\), the first displayed formula. Inserting the Fourier kernel and integrating \(\cos(nu)\) over a semicircle gives the absolutely convergent odd-frequency series.

**4. Equality characterization.** Equality in the upper bound demands \(\delta_t(d(a,b))=K(t)\) for \(p\otimes q\)-almost every pair, because all intermediate integral norms are bounded by \(K(t)\). Strict growth of \(\delta_t\) forces \(b=a+\pi\) almost everywhere under \(p\otimes q\). Since \(p\) and \(q\) are independent probability factors, each is a point mass, at opposite sites. Hence \(Df\) is a nonzero multiple of \(\delta_a-\delta_{a+\pi}\), whose BV primitives are precisely scaled semicircle indicators plus constants. Conversely each such indicator attains \(K(t)\).

**5. Strict time laws.** The density solves \(\partial_tk_t=\partial_u^2k_t\); hence
\[
K'(t)=2\int_{-\pi/2}^{\pi/2}\partial_u^2k_t(u)\,du=4k_t'(\pi/2)<0.
\]
The semigroup inequality gives \(K(s+t)\le K(s)K(t)\). Were there equality for positive times, a maximizer for \(H_{s+t}\) would also maximize both intermediate norm ratios. The unique initial maximizer is a semicircle step; after any positive heat time its derivative is a nonconstant smooth density, not an antipodal two-atom measure, so it cannot maximize the next step. Thus the inequality is strict.

**6. Endpoint asymptotics.** For \(a=\pi/2\), let \(\Phi\) denote the standard Gaussian CDF. Periodizing the Gaussian and counting the mass outside the central semicircle gives
\[
1-K(t)=4\Phi\!\left(-\frac{a}{\sqrt{2t}}\right)+O\left(e^{-9a^2/(4t)}\right),\qquad t\downarrow0.
\]
The Gaussian Mills expansion \(\Phi(-z)=e^{-z^2/2}(z\sqrt{2\pi})^{-1}(1-z^{-2}+O(z^{-4}))\) proves the stated sharp exponential and first relative correction. The first two nonzero odd Fourier terms establish the large-time expansion with the next term of order \(e^{-25t}\).

## Verification

Run `python3 verification/check_heat_bv.py` with Python 3 standard library; no third-party packages are required. The script independently compares the Fourier and periodized-Gaussian kernel formulae, integrates the total variation of antipodal and non-antipodal shifted densities, checks 105 randomly generated Jordan-measure pairs at three times, checks sample strict submultiplicativity, and checks both asymptotic expansions. A successful run ends with `ALL_CIRCLE_HEAT_BV_CHECKS_PASS`.

These are numerical consistency tests with explicitly bounded resolution, **not a replacement for** the universal analytical argument. The infinite sums and all-time claims are justified by analytic convergence and the proof above, not by the finite tests.

## Relationship to prior work

The classical Dobrushin formula expresses the norm of a Markov kernel on zero-mass measures as its largest pairwise kernel separation (see the historical discussion in the references). That general reduction is used rather than rediscovered. Baudoin's archival notes supply the wrapped-Gaussian circle heat kernel and ordinary \(L^2\) Markov contraction, but not the exact BV operator constant, unique semicircular equality class, strict semigroup coefficient, or exponentially flat small-time defect. Angeloni and Vinti survey convergence in BV for convolution-type approximation operators, without this sharp periodic heat coefficient. Radial strict heat-kernel monotonicity is established in generality by Alonso-Orán and collaborators and is treated here as prior structure.

The additional content is the circle-specific exact optimization, the equality classification and the two sharp time profiles. Searches did not locate a prior full statement containing all of these conclusions; this is not a guarantee of historical priority.

## Limitations

This result concerns real-valued scalar BV on the one-dimensional circle with its standard homogeneous Laplacian, and distributional first variation. It does not address weighted variation, inhomogeneous diffusivity, higher-dimensional tori or complex-valued variation. Generic Markov-kernel norm reduction and radial monotonicity are known ingredients. An older unindexed source might have the same explicit sharp heat coefficient or asymptotics; absolute historical novelty remains an open priority question. Numerical checks alone cannot certify the infinite-dimensional theorem. Independent audit has not been carried out.

## References

1. F. Baudoin, *Lecture 8. The heat semigroup on the circle*, publicly posted June 28, 2013. https://fabricebaudoin.blog/2013/06/28/lecture-8-the-heat-semigroup-on-the-circle/
2. L. Angeloni and G. Vinti, *A Review on Approximation Results for Integral Operators in the Space of Functions of Bounded Variation*, Journal of Function Spaces (first published September 26, 2016). https://onlinelibrary.wiley.com/doi/10.1155/2016/3843921
3. Classical Dobrushin contraction theorem for zero-total-mass signed measures; historical discussion of the exact norm formula, October 2014. https://mathoverflow.net/questions/185643/on-the-inverse-problem-of-dobrushin
4. D. Alonso-Orán, F. Chamizo, Á. D. Martínez and A. Mas, *Pointwise monotonicity of heat kernels*, first online December 13, 2021. https://link.springer.com/article/10.1007/s13163-021-00417-8
