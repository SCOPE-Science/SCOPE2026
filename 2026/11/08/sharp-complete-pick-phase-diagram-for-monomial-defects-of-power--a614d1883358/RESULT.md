# Sharp complete-Pick phase diagram for monomial defects of power kernels

## Finding

Let \(d,m\) be positive integers, \(\gamma>0\), and let \(\mathbb B_d\) be the complex unit ball. Consider the normalized positive kernel
\[
k_\gamma(z,w)=(1-\langle z,w\rangle)^{-\gamma},
\qquad \varphi_{m,s}(z)=\sqrt{s}\,z_1^m,
\qquad K_{d,\gamma,m,s}(z,w)=
\frac{1-sz_1^m\overline{w_1}^{m}}{(1-\langle z,w\rangle)^\gamma}.
\]
Only parameters for which \(\varphi_{m,s}\) is a contractive multiplier are considered. Set
\[
a_m(\gamma)=\frac{(\gamma)_m}{m!},\qquad
b_m(\gamma)=(-1)^{m+1}\binom{\gamma}{m}\quad(0<\gamma\le1).
\]

**Theorem (complete monomial-defect classification).** Multiplier contractivity holds exactly when \(0\le s\le a_m(\gamma)\) for \(0<\gamma<1\), and when \(0\le s\le1\) for \(\gamma\ge1\). Within this admissible range, the defect kernel \(K_{d,\gamma,m,s}\) is a complete Nevanlinna–Pick kernel **if and only if** one of the following holds:

1. \(0<\gamma\le1\), any \(d\ge1\), with \(0\le s\le b_m(\gamma)\).
2. \(1<\gamma\le2\), \(d=1\), \(m=1\), and \(s=1\).

There are no further cases. At \(\gamma=1\), \(b_1(1)=1\) and \(b_m(1)=0\) for \(m\ge2\).

For \(0<\gamma<1\), the fractional threshold relative to the contractive-multiplier maximum has the exact form
\[
\frac{b_m(\gamma)}{a_m(\gamma)}=
\frac{\Gamma(1+\gamma)}{\Gamma(1-\gamma)}
\frac{\Gamma(m-\gamma)}{\Gamma(m+\gamma)}
=\frac{\Gamma(1+\gamma)}{\Gamma(1-\gamma)}m^{-2\gamma}(1+O_\gamma(m^{-1})).
\]
This is strictly less than one for \(m\ge2\); at each fixed fractional exponent the share of contractive squared amplitudes retaining the complete Pick property shrinks with the monomial order. The result exhibits a dimension transition for \(\gamma>1\) and a noninjective-symbol transition at the Hardy exponent \(\gamma=1\).

For example, at \(\gamma=1/2\) and \(m=2\), the admissible interval is \(0\le s\le3/8\), whereas the complete Pick interval is precisely \(0\le s\le1/8\), in *every* dimension.

## Assumptions and scope

All kernels act on the **open** complex unit ball, use the usual Hermitian inner product, and are normalized at the origin. The complete Pick property is the all-matrix-size interpolation property, equivalently the McCullough–Quiggin–Agler–McCarthy criterion that for a normalized, everywhere nonvanishing kernel \(K\), the kernel \(1-1/K\) be positive semidefinite. The factor \(\varphi\) is a single coordinate monomial with real nonnegative squared amplitude \(s\); a constant complex phase does not change the defect kernel. Endpoint equalities are included. Falling/rising factorials have their standard meanings; in particular \((\gamma)_m=\gamma(\gamma+1)\cdots(\gamma+m-1)\).

## Proof

**1. Exact multiplier range.** Expand the base kernel into normalized orthogonal monomials:
\[
k_\gamma(z,w)=\sum_{\alpha\in\mathbb N^d}
\frac{(\gamma)_{|\alpha|}}{\alpha!}z^\alpha\overline w^\alpha,
\qquad \|z^\alpha\|^2=\frac{\alpha!}{(\gamma)_{|\alpha|}}.
\]
For multiplication by \(z_1^m\), the squared shift weight at \(\alpha\) is
\[
\frac{\|z^{\alpha+me_1}\|^2}{\|z^\alpha\|^2}=
\frac{(\alpha_1+1)_m}{(\gamma+|\alpha|)_m}.
\]
For \(0<\gamma<1\), this ratio is at most its value at \(\alpha=0\), namely \(m!/(\gamma)_m\). Indeed it decreases when an index outside the first coordinate is added, and each factor \((j+r)/(\gamma+j+r-1)\) decreases with \(r\ge0\). For \(\gamma\ge1\) every squared shift weight is at most one and the weights along \(\alpha=re_1\) approach one. This yields exactly the multiplier-amplitude bounds in the theorem. In particular every admissible \(s\le1\), so the defect kernel is nonvanishing on \(\mathbb B_d\times\mathbb B_d\).

**2. The positive-coefficient criterion.** Write \(u=\langle z,w\rangle\), \(v=z_1\overline w_1\). For a normalized nonvanishing kernel, complete Pick is equivalent to positivity of
\[
F(z,w)=1-\frac1{K_{d,\gamma,m,s}(z,w)}
=\frac{\sum_{n\ge1}b_n(\gamma)u^n-sv^m}{1-sv^m},
\qquad b_n(\gamma)=(-1)^{n+1}\binom{\gamma}{n}.
\]
The identity is analytic near the origin and extends throughout the ball. For a diagonal monomial expansion \(\sum_\alpha c_\alpha z^\alpha\overline w^\alpha\), kernel positivity is equivalent to \(c_\alpha\ge0\) for every multiindex: sufficiency follows from the feature-vector expansion and necessity from positive derivative-evaluation Gram forms at the origin (equivalently, independent torus Fourier coefficients). These facts apply to \(F\), which is invariant under coordinatewise rotations.

**3. Fractional and Hardy exponents.** If \(0<\gamma\le1\), then \(b_n(\gamma)\ge0\) for every \(n\ge1\). The numerator of \(F\) has nonnegative diagonal monomial coefficients exactly when \(s\le b_m(\gamma)\): the only coefficient potentially reduced is that of \(v^m\). The reciprocal \((1-sv^m)^{-1}=\sum_{j\ge0}s^jv^{mj}\) is a positive kernel, and Schur products preserve positivity; hence that inequality is sufficient. It is also necessary because the coefficient of \(v^m\) in \(F\) itself is precisely \(b_m(\gamma)-s\). This proves the first branch, including all equality cases.

**4. Higher exponents and the dimension obstruction.** If \(\gamma>1\) and \(d\ge2\), the coefficient of \(z_2^2\overline{w_2}^{2}\) in \(F\) is
\[
-\binom\gamma2=-\frac{\gamma(\gamma-1)}2<0.
\]
The denominator depends only on the first coordinate, so no monomial defect can cancel this coefficient. Thus no admissible parameter is complete Pick in higher dimensions. When \(d=1\) and \(m\ge2\), the coefficient of \((z\overline w)^2\) is \(-\binom\gamma2-s\mathbf1_{\{m=2\}}<0\); these cases also fail.

It remains to take \(d=m=1\) and \(\gamma>1\), for which contractivity requires \(0\le s\le1\). If \(s=1\), cancellation gives \(K=(1-z\overline w)^{-(\gamma-1)}\), whose complete Pick property is equivalent to \(0<\gamma-1\le1\), hence \(1<\gamma\le2\). For \(s<1\) and \(1<\gamma<2\), the real function \(F(t)=1-(1-t)^\gamma/(1-st)\) has
\[
F''(t)=-\frac{\gamma(\gamma-1)}{1-s}(1-t)^{\gamma-2}(1+o(1))<0
\quad(t\uparrow1),
\]
contradicting the nonnegative Taylor coefficients required of a positive radial kernel (which would force \(F''(t)\ge0\) on \((0,1)\)). For \(\gamma=2\), the quadratic coefficient is \(-(1-s)^2<0\) when \(s<1\). For \(\gamma>2\), the quadratic coefficient \(-\gamma(\gamma-1)/2+\gamma s-s^2\) is negative throughout \(0\le s\le1\) (its maximum occurs at \(s=1\), where it equals \(-(\gamma-1)(\gamma-2)/2\)). This proves that no remaining parameter works.

**5. Sharp asymptotic fraction.** For \(0<\gamma<1\), Euler's Gamma identities give
\[
b_m(\gamma)=\frac{\gamma\Gamma(m-\gamma)}{\Gamma(1-\gamma)\Gamma(m+1)},\qquad
a_m(\gamma)=\frac{\Gamma(m+\gamma)}{\Gamma(\gamma)\Gamma(m+1)}.
\]
Their ratio is the exact expression in the theorem. The standard Gamma-ratio expansion proves the stated asymptotic, completing the proof.

## Verification

The supplied standalone `CHECK.py` checks the multiplier and complete-Pick coefficient formulas with exact rational arithmetic at twelve representative exponents and monomial orders through eight, including threshold equality and strict non-Pick cases. It also checks the positive-amplitude noninjective example \(\gamma=1/2,m=2\) through 96 Taylor coefficients and confirms finite-order monotonicity of the exact admissible fraction. The general theorem is proved analytically above; finite coefficient calculations are not an infinite-dimensional proof. Run with `python CHECK.py` using Python's standard library.

## Relationship to prior work

Dellepiane and Seco (2026) study polynomial structure of classical de Branges–Rovnyak spaces with primary MSC 30H45; their structural focus motivates an explicit determination of other analytic invariants. Sau (2026) studies when defect kernels admit a *complete Pick factor*, a weaker property than being complete Pick, and treats the classical Szegő and Bergman examples. Ahmed, Das and Panja (2024) provide general necessary-and-sufficient formulations for complete-Pick defect kernels. Their characterization is compatible with the explicit coefficient test used here but does not state the fractional-power, monomial-amplitude and dimension phase diagram. Luo and Zhu (2023) establish a stronger disk theorem in the generalized weighted Bergman range corresponding to \(1<\gamma\le2\), subsuming the disk higher-exponent branch: **no novelty is claimed for that branch in isolation**. The central resolved parameters are \(0<\gamma<1\), where the noninjective monomial defect remains complete Pick below a sharp positive threshold, and the exact higher-dimensional contrast.

## Limitations

This is an explicit classification within coordinate-monomial defect kernels, **not** a characterization of all contractive multipliers. The calculations do not assert that the underlying de Branges–Rovnyak spaces have any particular boundary-regularity, cyclicity, or zero-set property beyond complete Pick. Positive definiteness of finite sampled matrices alone would not prove the global criterion. The literature comparison is based on the accessible cited manuscripts and records; exhaustive worldwide priority is unproved. The high-exponent disk cases overlap known stronger results as stated above.

## References

1. E. Dellepiane and D. Seco, *Orthogonal polynomials in de Branges–Rovnyak spaces*, arXiv:2603.03093 (first submitted 2026-03-03), https://arxiv.org/abs/2603.03093.
2. H. Sau, *On de Branges–Rovnyak Kernels Admitting a Complete Pick Factor*, arXiv:2606.09680 (first submitted 2026-06-08), https://arxiv.org/abs/2606.09680.
3. H. Ahmed, B. K. Das and S. Panja, *de Branges–Rovnyak spaces which are complete Nevanlinna–Pick spaces*, arXiv:2403.19377 (2024), https://arxiv.org/abs/2403.19377.
4. S. Luo and K. Zhu, *Sub-Bergman Hilbert spaces on the unit disk III*, arXiv:2302.01980 (2023), https://arxiv.org/abs/2302.01980.
5. C. Chu, *Which de Branges–Rovnyak spaces have complete Nevanlinna–Pick property?*, arXiv:1910.04830 (2019), https://arxiv.org/abs/1910.04830.
6. J. Agler and J. E. McCarthy, *Complete Nevanlinna–Pick kernels*, Journal of Functional Analysis 175 (2000), 111–124.
