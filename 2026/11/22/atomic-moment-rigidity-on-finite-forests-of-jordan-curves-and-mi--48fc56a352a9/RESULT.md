# Atomic-moment rigidity on finite forests of Jordan curves and minimal diagonal commutants

## Finding

**Theorem.** Let \(m\geq1\), and let \(\Gamma_1,\ldots,\Gamma_m\subset\mathbb C\) be **pairwise disjoint Jordan curves**, with no rectifiability, smoothness, concentricity, or separation-of-eigenvalues assumption. For every sequence of **pairwise distinct** points \((\lambda_n)_{n\geq1}\) contained in \(\bigcup_{j=1}^{m}\Gamma_j\), the diagonal operator \(D e_n=\lambda_n e_n\) on \(\ell^2(\mathbb N)\) has the minimal commutant property:

\[
\overline{\{p(D):p\in\mathbb C[z]\}}^{\mathrm{WOT}}
=\{D\}'
=\{\operatorname{diag}(b_n):(b_n)\in\ell^\infty\}.
\]

Equivalently, **every** absolutely summable complex family \((a_n)_{n\geq1}\) on these sites obeys the analytic-moment rigidity implication

\[
\left(\sum_{n=1}^{\infty} a_n\lambda_n^k=0\ \text{for every integer }k\geq0\right)
\quad\Longrightarrow\quad a_n=0\ \text{for all }n.
\]

Both statements hold even when every listed curve carries a dense countable collection of sites and when the curves have arbitrary finite nesting depth. For example, a dense enumeration on the two nonconcentric nested circles \(2\mathbb T\) and \(\tfrac14+\tfrac12\mathbb T\) has a minimal commutant. Here \(\mathbb T=\{z:|z|=1\}\).

## Assumptions and scope

All curves are Jordan images of the unit circle, so each bounds a simply connected Jordan domain \(\Omega_j\). They are compact and pairwise disjoint, so the inclusions among their closed Jordan disks \(E_j=\Omega_j\cup\Gamma_j\) form a finite rooted forest: any two disks are disjoint or one is strictly contained in the other. The eigenvalue sequence is infinite and pairwise distinct; its boundedness follows from finite compact containment. There is no condition on its distribution along a curve, and the coefficients in the moment assertion may be complex with no positivity assumption.

For a bounded operator \(D\), \(\{D\}'\) denotes its commutant and \(\mathrm{WOT}\) the weak-operator topology. This result concerns **polynomial** approximation, not rational approximation or norm approximation of arbitrary bounded diagonal operators.

## Proof

### Step 1: An atomic Jordan-boundary elimination lemma

Let \(\Gamma=\partial\Omega\) be any Jordan curve. Suppose \(\mu_{\partial}\) is a finite purely atomic complex measure carried by \(\Gamma\), and \(\mu_{\circ}\) a finite purely atomic complex measure carried by \(\Omega\). Assume

\[
\int z^k\,d(\mu_{\partial}+\mu_{\circ})(z)=0
\qquad(k=0,1,2,\ldots).
\]

We prove \(\mu_{\partial}=0\) and \(\int z^k\,d\mu_{\circ}=0\) for all \(k\geq0\). Let \(\omega_w\) be harmonic measure on \(\Gamma\) as viewed from \(w\in\Omega\). For each polynomial \(p\), the harmonic/holomorphic mean-value property gives \(p(w)=\int_\Gamma p(\zeta)\,d\omega_w(\zeta)\). Write \(\mu_{\circ}=\sum_{j\geq1}c_j\delta_{w_j}\), where \(w_j\in\Omega\) and \(\sum_j|c_j|<\infty\). Then

\[
\nu:=\sum_{j\geq1}c_j\omega_{w_j}
\quad\text{satisfies}\quad
\|\nu\|_{\mathrm{TV}}\leq\sum_j|c_j|
\quad\text{and}\quad
\int_\Gamma p\,d\nu=\int_\Omega p\,d\mu_{\circ}.
\]

Fix \(w_0\in\Omega\). By the Riemann map and Carathéodory's boundary extension, each \(\omega_{w_j}\) is absolutely continuous with respect to the non-atomic measure \(\omega_{w_0}\): under a conformal homeomorphism of the closed disk, these are ordinary Poisson measures, with strictly positive density relative to normalized arc measure. A countable total-variation-convergent sum preserves absolute continuity, so \(\nu\ll\omega_{w_0}\).

Thus \(\sigma=\mu_{\partial}+\nu\) is a finite complex measure carried by \(\Gamma\) that annihilates all analytic polynomials. The **F. and M. Riesz theorem on a Jordan boundary** implies \(\sigma\ll\omega_{w_0}\). To verify its general-Jordan form rather than assume a smooth boundary: pull \(\sigma\) back by a Carathéodory conformal boundary homeomorphism \(\phi:\overline{\mathbb D}\to\overline\Omega\). For every \(k\geq0\), the function \((\phi^{-1}(z))^k\) belongs to the Jordan-domain disk algebra \(A(\overline\Omega)\), and Mergelyan's theorem approximates it uniformly on \(\overline\Omega\) by polynomials. Hence the pullback measure annihilates every positive monomial on \(\mathbb T\). The circle F. and M. Riesz theorem makes the pullback absolutely continuous with respect to arc measure, which pushes forward to \(\omega_{\phi(0)}\), equivalent to \(\omega_{w_0}\).

Consequently \(\mu_{\partial}=\sigma-\nu\ll\omega_{w_0}\). A purely atomic measure absolutely continuous with respect to the non-atomic \(\omega_{w_0}\) must vanish. Subtracting it from the moment equations gives the stated conclusion for \(\mu_{\circ}\). **No lower bound on the distances of interior atoms from \(\Gamma\) was used.**

### Step 2: Polynomial isolation of outermost Jordan disks

Let \(\mu=\sum_{n\geq1}a_n\delta_{\lambda_n}\) have finite total variation and vanish on all monomials. Consider the maximal (outermost) Jordan disks \(E_{j_1},\ldots,E_{j_r}\) among the \(E_j\). These finitely many closed disks are pairwise disjoint and their union \(E\) has connected planar complement. For each \(\ell\), the function that equals \(1\) on \(E_{j_\ell}\) and \(0\) on every other maximal disk is continuous on \(E\) and holomorphic on its interior. By Mergelyan's theorem, it is a uniform limit on \(E\) of polynomials \(q_s\).

For each \(k\geq0\), the polynomial moments of \(\mu\) give \(\int z^k q_s(z)\,d\mu(z)=0\). Uniform convergence, finite total variation and boundedness of \(E\) imply

\[
\int_{E_{j_\ell}} z^k\,d\mu(z)=0
\qquad(k\geq0).
\]

Thus each maximal disk's restricted atomic measure separately annihilates analytic polynomials.

### Step 3: Descend the finite nesting forest

Within each maximal disk, split its restricted measure into atoms on its outer curve and atoms on curves strictly inside. Step 1 removes the outer-curve atomic measure and leaves all inner-curve moments zero. The remaining curves form a smaller finite forest, and Step 2 can again separate its maximal closed disks. Repeat this argument at most \(m\) times. Every curve's measure is zero. Since the sites \(\lambda_n\) are pairwise distinct, \(\mu=0\) means each coefficient \(a_n=0\). This proves the moment-rigidity assertion.

### Step 4: Convert moment rigidity to a commutant identity

Pairwise distinct diagonal entries imply that every bounded operator commuting with \(D\) is diagonal: the \((i,j)\) matrix entry of a commuting operator satisfies \((\lambda_i-\lambda_j)T_{ij}=0\). The diagonal algebra identifies with \(\ell^\infty\), and the weak-operator topology restricted to it agrees with \(\sigma(\ell^\infty,\ell^1)\), because \(\langle\operatorname{diag}(b)x,y\rangle=\sum_n b_nx_n\overline{y_n}\), and every \(\ell^1\) coefficient sequence is realized by a pair \(x,y\in\ell^2\).

The preannihilator of the polynomial-value subspace \(\{(p(\lambda_n))_n:p\in\mathbb C[z]\}\) consists exactly of sequences satisfying \(\sum_n a_n\lambda_n^k=0\) for all \(k\geq0\). Steps 1–3 show that this preannihilator is zero. The Hahn–Banach annihilator criterion therefore gives weak-star density in \(\ell^\infty\), equivalently the asserted WOT minimal-commutant identity. All quantifiers in the theorem are now proved.

## Verification

The proof is analytic and does not rely on finite enumeration or a computational certificate. Independently checkable critical implications are: (i) polynomial isolation uses Mergelyan only on a **finite disjoint union of filled outermost Jordan disks**; (ii) the harmonic-measure series converges in total variation, making absolute continuity valid without uniformly separated atoms; (iii) Jordan-boundary F. and M. Riesz follows from Carathéodory and Mergelyan as detailed; (iv) induction terminates after at most \(m\) layers; (v) diagonal WOT and weak-star topology have identical linear functionals. The nested nonconcentric two-circle example tests a regime in which uniform **norm** polynomial separation of the two boundary circles is impossible: a polynomial bounded near zero on the outer full circle is bounded near zero throughout its filled disk by the maximum principle.

## Relationship to prior work

Bayart, Wang and Yao [1] study minimal commutants for composition operators on spaces of holomorphic functions; their setup motivates isolating the spectral-geometric question in a diagonal model. González and León-Saavedra [2] relate weak-star polynomial generation to analytic Toeplitz minimal commutants, with different operators and hypotheses. Wang and Yao [3], in subsequent diagonal-operator work, prove an abstract \(\ell^1\)-moment criterion (Theorem 3.2), a **single Jordan curve** criterion (Theorem 3.9(2)), a Jordan boundary plus a convergent interior sequence (Corollary 3.6), and a countable **concentric** circle criterion (Lemma 4.1). Those are credited. Their statements do not supply the finite, arbitrarily nested **nonconcentric Jordan-curve** classification without the present forest-isolation and harmonic-balayage argument. Their direct-sum separation theorem also requires uniform polynomial separation, which is impossible for a nested pair of full curves by the maximum principle; this emphasizes the strictness of the additional case. The F. and M. Riesz theorem, Carathéodory's extension theorem, Mergelyan approximation and weak-star duality are classical inputs, not new assertions.

## Limitations

The number of curves is finite, the curves are pairwise disjoint Jordan loops, and the diagonal entries are pairwise distinct. No assertion is made for countably infinite families, intersecting loops, arbitrary planar compact sets, repeated eigenvalues, or nonnormal off-diagonal perturbations. The result establishes WOT density, not uniform operator-norm approximation. An older specialized result in approximation theory or analytic-measure theory could implicitly contain the forest rigidity statement; the closest identified published diagonal literature and the inspected public mathematical records did not produce such coverage. Source [1] was accessible at abstract level but not in full text during this investigation; source [3] was read in HTML. Independent review has not been performed.

## References

1. F. Bayart, M. Wang, X. Yao, *Commutants of composition operators on function spaces of several complex variables*, arXiv:2608.00448 (first public 2026-08-01), https://arxiv.org/abs/2608.00448.
2. M. J. González and F. León-Saavedra, *Minimal commutant and double commutant property for analytic Toeplitz operators*, Banach J. Math. Anal. 19 (2025), article 37, https://doi.org/10.1007/s43037-025-00426-5.
3. M. Wang and X. Yao, *Commutants of diagonal operators*, arXiv:2611.22802v1 (first public 2026-11-17), https://arxiv.org/html/2611.22802v1.
4. F. and M. Riesz theorem; Riemann–Carathéodory boundary correspondence; S. N. Mergelyan polynomial-approximation theorem (classical results, used in the explicit steps above).
