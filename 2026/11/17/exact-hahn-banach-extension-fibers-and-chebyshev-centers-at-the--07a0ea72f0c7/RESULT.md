# Exact Hahn–Banach extension fibers and Chebyshev centers at the Bochner one-endpoint

## Finding
Let \((\Omega,\Sigma,\mu)\) be a complete finite measure space with \(0<\mu(\Omega)<\infty\), let \(Y,Z\) be nonzero separable real Hilbert spaces, and fix \(1\le r\le\infty\). Set \(X=Y\oplus_r Z\), with its standard absolute direct-sum norm, and identify \(Y\) with \(Y\oplus\{0\}\). Let \(\phi\ne0\) belong to \((L^1(\mu,Y))^*\). Write its unique Bochner-dual representative as \(g\in L^\infty(\mu,Y)\); define
\[
M=\operatorname*{ess\,sup}_{\omega}\|g(\omega)\|>0,\qquad m=\operatorname*{ess\,inf}_{\omega}\|g(\omega)\|.
\]
Write \(q\) for the Hölder conjugate of \(r\), with \(q=\infty\) if \(r=1\) and \(q=1\) if \(r=\infty\). Define the nonnegative measurable slack function
\[
a(\omega)=\begin{cases}(M^q-\|g(\omega)\|^q)^{1/q},&1\le q<\infty,\\M,&q=\infty,\end{cases}
\]
and \(A=\|a\|_\infty\).

**Complete fiber and center theorem.** Every norm-preserving Hahn–Banach extension of \(\phi\) to \(L^1(\mu,X)\), and no other extension, has the unique dual representative \((g,h)\), where \(h\in L^\infty(\mu,Z)\) satisfies \(\|h(\omega)\|\le a(\omega)\) almost everywhere. The norm diameter of this fiber is exactly \(2A\), attained by explicit opposite extensions. In the affine Banach space of **all** extensions \(\{(g,k):k\in L^\infty(\mu,Z)\}\), its Chebyshev radius is exactly \(A\), and **all** relative Chebyshev centers are
\[
\left\{(g,k):\ \|k(\omega)\|\le A-a(\omega)\text{ for almost every }\omega\right\}.
\]
Consequently,
\[
A=\begin{cases}M,&r=1,\\(M^q-m^q)^{1/q},&1<r\le\infty.\end{cases}
\]
For \(r=1\), the canonical extension \((g,0)\) is the **unique** relative Chebyshev center, even though the extension fiber has the maximal diameter \(2M\). For \(r>1\), the relative Chebyshev center is unique exactly when the norm-preserving extension is unique; this occurs precisely when \(\|g(\omega)\|=M\) almost everywhere.

**Attainment and sharp endpoint spectrum.** For nonzero \(\phi\), norm attainment holds if and only if \(\mu\{\omega:\|g(\omega)\|=M\}>0\). If the measure algebra contains a measurable set and its complement both of positive measure, then for \(r>1\) every diameter in \([0,2]\) is attained by the extension fiber of some **norm-one norm-attaining** functional; for \(r=1\), all nonzero norm-one functionals, including norm-attaining ones, have diameter \(2\). Thus the inclusion has properties \((U)\), \((wU)\), and \((SU)\) simultaneously if and only if \(r>1\) and the measure algebra consists of a single atom up to null sets.

## Assumptions and scope
All spaces and linear functionals are real. The finite measure is complete and nonzero, and the two Hilbert summands are separable and nonzero; no atomicity, countability, or nonatomicity hypothesis is imposed on the measure algebra. The familiar absolute direct-sum norm is \(\|(y,z)\|_r=(\|y\|^r+\|z\|^r)^{1/r}\) for finite \(r\), and \(\|(y,z)\|_\infty=\max\{\|y\|,\|z\|\}\). The Chebyshev centers are taken in the explicitly specified affine space of extensions, not in the entire ambient dual. Properties \((U)\), \((wU)\), and \((SU)\) mean unique norm-preserving extension for all, respectively all norm-attaining, functionals, with the standard ideal condition added for \((SU)\).

## Proof
**1. Dual identification.** The finite direct sum \(X=Y\oplus_r Z\) is reflexive. Its dual is isometrically \(Y\oplus_q Z\), by the Hilbert Riesz identifications. Since this dual has the Radon–Nikodým property, the standard Bochner duality theorem gives \((L^1(\mu,X))^*=L^\infty(\mu,X^*)\) and \((L^1(\mu,Y))^*=L^\infty(\mu,Y)\), isometrically. Thus every functional extending \(\phi\) is uniquely of the form \((g,h)\), and its norm is
\[
\operatorname*{ess\,sup}_\omega \|(g(\omega),h(\omega))\|_q.
\]
This norm is at least \(M\) because restriction to \(Y\) has norm \(M\). Consequently norm preservation is equivalent to the pointwise inequality \(\|(g(\omega),h(\omega))\|_q\le M\) almost everywhere. Resolving the \(\ell_q\)-norm gives exactly the stated slack bound. For \(r=1\), the \(\ell_\infty\)-condition is \(\|h\|\le M\), independently of \(g\); otherwise it is \(\|h\|^q\le M^q-\|g\|^q\).

**2. Exact diameter.** The difference of two elements \((g,h_1)\) and \((g,h_2)\) has norm \(\|h_1-h_2\|_{L^\infty(\mu,Z)}\le2A\). Fix any unit vector \(e\in Z\). The two fields \(h_\pm(\omega)=\pm a(\omega)e\) are admissible and differ in norm by \(2\|a\|_\infty=2A\). This proves the *attained* diameter, even if \(a\) has no pointwise maximizing argument.

**3. Exact Chebyshev centers.** Let \((g,k)\) be any affine extension, without assuming norm preservation. The largest distance from \((g,k)\) to a norm-preserving extension is
\[
\sup_{\|h(\omega)\|\le a(\omega)}\|k-h\|_\infty
=\operatorname*{ess\,sup}_\omega\bigl(a(\omega)+\|k(\omega)\|\bigr).
\]
The upper bound is the triangle inequality. For the opposite inequality, take \(h(\omega)=-a(\omega)k(\omega)/\|k(\omega)\|\) when \(k(\omega)\ne0\), and \(h(\omega)=a(\omega)e\) otherwise. This is a strongly measurable admissible field and attains the pointwise upper bound everywhere. Symmetric opposite extensions yield the universal lower bound \(A\) for the covering radius of any center; \(k=0\) attains it. Hence a center is optimal precisely if \(a+\|k\|\le A\) almost everywhere, yielding the complete center set. If \(r=1\), then \(a\equiv M=A\) and the sole center has \(k=0\). If \(r>1\), the essential infimum of \(a\) is zero, because \(M\) is the essential supremum of \(\|g\|\). Thus \(a\equiv A\) almost everywhere can hold only when \(A=0\), i.e. \(\|g\|=M\) almost everywhere. Otherwise \(\{a<A\}\) has positive measure and supports a nonzero \(k\) bounded by \(A-a\); the center is not unique.

**4. Norm attainment.** Suppose \(M>0\) and \(\phi\) attains its norm at \(f\in L^1(\mu,Y)\) with \(\|f\|_1=1\). Equality in
\[
\phi(f)\le\int\|g\|\|f\|\,d\mu\le M\int\|f\|\,d\mu=M
\]
forces \(\|g(\omega)\|=M\) on the essential support of \(f\), which must have positive measure. Conversely, if \(E=\{\|g\|=M\}\) has positive measure, \(f(\omega)=\mu(E)^{-1}\mathbf1_E(\omega)g(\omega)/M\) is a Bochner-integrable unit vector attaining \(\phi(f)=M\).

**5. Spectrum and global uniqueness properties.** Suppose \(\mu(A_0)>0\) and \(\mu(\Omega\setminus A_0)>0\). Fix unit \(u\in Y\). For every \(s\in[0,2]\) and \(r>1\), choose \(m_s=(1-(s/2)^q)^{1/q}\), and set \(g=u\) on \(A_0\), \(g=m_su\) on its complement. Then \(\|g\|_\infty=1\), the representing functional attains its norm on \(A_0\), and the already proved formula gives diameter \(s\). For \(r=1\), the formula gives diameter two regardless of the nonzero norm-one representative. In particular the choice \(g=u\mathbf1_{A_0}\) always produces a norm-attaining functional with multiple norm-preserving extensions: neither \((wU)\) nor \((U)\) holds for the inclusion. When the measure algebra has only one atom up to null sets, every essentially bounded Hilbert-valued representative is essentially constant. For \(r>1\), the finite-\(q\) slack vanishes identically, so every functional has exactly one extension. The coordinate projection onto \(Y^*\) in \(X^*\) has norm one and kernel the annihilator of \(Y\), and the same holds on the Bochner dual; hence the inclusion is an ideal, giving \((SU)\). For \(r=1\), a nonzero constant \(g\) has slack \(M>0\), so even the one-atom case fails \((wU)\). This exhausts the cases.

## Verification
The proof uses exact dual norm identities and a pointwise measurable construction, not a finite sample or numerical extrapolation. In finite two-atom models, one may choose \(\|g\|\in\{1,m_s\}\) to recover the continuum of diameters. The two opposite fields \(\pm ae\) and the negative-radial field in Step 3 certify sharpness and the minimax identity without auxiliary software. Every essential supremum and infimum is interpreted modulo null sets.

## Relationship to prior work
Karak and Paul (2026, arXiv:2611.03203v1) prove Bochner stability of the unique Hahn–Banach extension properties for \(1<p<\infty\), using dual representations and common scalar liftings. Their Theorems 3.1, 3.3, and 3.7 exclude the \(L^1\) endpoint. The present result instead gives the entire endpoint extension fiber, its diameter and Chebyshev center set, the norm-attaining diameter spectrum, and the sharp measure/exponent uniqueness dichotomy for Hilbert direct sums. Its ingredients are classical Bochner duality and absolute-sum geometry; the novelty claim concerns the combined endpoint *exact classification*, not those ingredients. Related earlier studies include Phelps (1960) on unique extensions and Karak, Paul, and Rao (2026) on weak unique extension stability; a complete priority comparison to the latter's full text was unavailable.

## Limitations
The conclusion concerns real separable Hilbert summands, a complete finite nonzero measure space, and the specific inclusion into an absolute two-summand Banach space. The Chebyshev centers are **relative to the affine space of all extensions** and are not asserted to describe centers in the larger ambient dual. No general arbitrary-Banach-fiber analogue or optimal nonlinear modulus beyond these exact formulas is claimed. The result has not undergone independent mathematical review; equivalent statements might exist in the classical geometry of \(L^\infty\) direct-sum balls.

## References
1. S. Karak and T. Paul, *Unique Hahn–Banach extensions in Bochner \(L^p\) spaces*, arXiv:2611.03203v1, first public 2 November 2026, https://arxiv.org/html/2611.03203v1.
2. J. Diestel and J. J. Uhl, *Vector Measures*, Mathematical Surveys 15, American Mathematical Society, 1977 (standard dual representation background).
3. R. R. Phelps, *Uniqueness of Hahn–Banach extensions and unique best approximation*, Transactions of the American Mathematical Society 95 (1960), 238–255.
4. S. Karak, T. Paul, and T. S. S. R. K. Rao, *On subspaces of Banach spaces which admit unique norm preserving extensions under various embeddings*, Contemporary Mathematics 833 (2026), 149–159, DOI:10.1090/conm/833/16666 (abstract-level comparison only).
