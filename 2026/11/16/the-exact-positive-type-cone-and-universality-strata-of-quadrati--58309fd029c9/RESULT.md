# The exact positive-type cone and universality strata of quadratically modulated Abel kernels on \(SU(2)\)

## Finding
For every real \(0<r<1\), let \(\chi_n\) be the irreducible degree-\(n\) character of \(SU(2)\), with \(\chi_0=1\), \(\chi_1(g)=\mathrm{tr}(g)\), and \(\chi_2=\chi_1^2-1\). Define
\[
A_r(g)=\sum_{n=0}^{\infty}(n+1)r^n\chi_n(g),\qquad
F_{r,s,t}(g)=A_r(g)[1+s\chi_1(g)+t\chi_2(g)]
\]
for arbitrary real \(s,t\). Put
\[
L_0=1+2rs+3r^2t,\qquad
L_1=1+\frac{1+3r^2}{2r}s+(1+2r^2)t,\qquad
L_\infty=1+(r+r^{-1})s+(1+r^2+r^{-2})t.
\]
**Theorem.** The translation-invariant central kernel \(\mathcal K_{r,s,t}(x,y)=F_{r,s,t}(y^{-1}x)\) on \(SU(2)\) is positive semidefinite for every finite point configuration **if and only if**
\[
L_0\ge0,\qquad L_1\ge0,\qquad L_\infty\ge0.
\]
Within that closed region it is \(C\)-universal (its RKHS is dense in continuous real-valued functions) **if and only if** \(L_0>0\), \(L_1>0\), and \(L_\infty\ge0\). In particular, the full feasible part of the boundary \(L_\infty=0\) with \(L_0,L_1>0\) remains \(C\)-universal.

The positivity region has three genuine boundary edges and exactly two finite vertices:
\[
V_{01}=(-2/r,\,r^{-2}),\qquad
V_{1\infty}=\left(-\frac{2r(1+r^2)}{1+3r^2+r^4},\,\frac{r^2}{1+3r^2+r^4}\right).
\]
At \(V_{01}\), the modes numbered zero and one vanish but every higher mode remains positive. At \(V_{1\infty}\), every positive-degree mode vanishes, leaving a constant nonzero kernel. The intersection of \(L_0=L_\infty=0\) is infeasible. No other spectral degeneracies occur.

## Assumptions and scope
The group has normalized Haar probability measure, and all irreducible characters are the standard real-valued \(SU(2)\) characters. The fixed radius satisfies \(0<r<1\); all statements hold for every real pair \((s,t)\). Positivity refers to the Gram matrices on all finite collections of group elements, with repeats allowed. \(C\)-universality refers to density of the real reproducing-kernel Hilbert space in \(C(SU(2),\mathbb R)\). For \(g\) with eigenvalues \(e^{\pm i\theta}\), the Abel kernel has the closed form
\[
A_r(g)=\frac{1-r^2}{(1-2r\cos\theta+r^2)^2}.
\]
This ensures uniform absolute convergence and continuity for each \(r<1\).

## Proof
Write \(b_n=(n+1)r^n\). The character-product (Clebsch–Gordan) identities are \(\chi_1\chi_j=\chi_{j+1}+\chi_{j-1}\) for \(j\ge1\), with \(\chi_1\chi_0=\chi_1\); and \(\chi_2\chi_j=\chi_{j+2}+\chi_j+\chi_{j-2}\) for \(j\ge2\), \(\chi_2\chi_1=\chi_3+\chi_1\), and \(\chi_2\chi_0=\chi_2\). Thus the exact coefficient of \(\chi_0\) in \(F\) is \(a_0=b_0+s b_1+t b_2=L_0\). The coefficient of \(\chi_1\) is
\[
a_1=b_1+s(b_0+b_2)+t(b_1+b_3)=2r L_1.
\]
For each integer \(n\ge2\), the coefficient is
\[
a_n=b_n+s(b_{n-1}+b_{n+1})+t(b_{n-2}+b_n+b_{n+2}).\]
After dividing by the positive \(b_n\), these three cases combine to the identity, valid for **every** \(n\ge1\):
\[
\boxed{\frac{a_n}{(n+1)r^n}=
\frac{2}{n+1}L_1+\frac{n-1}{n+1}L_\infty.}
\]
The compact-group Bochner/Peter–Weyl positivity criterion asserts that a continuous central kernel is positive semidefinite exactly when all its real character coefficients are nonnegative. This proves sufficiency of the three inequalities because the displayed weights are nonnegative and sum to one. Conversely, positivity forces \(a_0\ge0\), \(a_1\ge0\), and, on letting \(n\to\infty\) in the displayed identity, \(L_\infty\ge0\). Therefore no additional inequalities are needed.

The group universality criterion follows directly from Peter–Weyl: all coefficient matrices on each irreducible representation must be strictly positive; here each matrix is the scalar \(a_n/(n+1)\) times identity. The formula shows all positive-degree coefficients are strictly positive exactly when \(L_1>0\) and \(L_\infty\ge0\), apart from the impossible case \(L_1=0\) (which always removes the first mode). Combined with \(a_0=L_0\), universality is therefore precisely \(L_0>0,L_1>0,L_\infty\ge0\).

To classify the boundary, solve the three pairs of linear equations. For \(L_0=L_1=0\), \((s,t)=(-2/r,r^{-2})\) and \(L_\infty=(1-r^2)/r^4>0\). For \(L_1=L_\infty=0\), the solution is \(V_{1\infty}\) above and \(L_0=(1-r^2)/(1+3r^2+r^4)>0\). For \(L_0=L_\infty=0\), the remaining value is \(L_1=(r^2-1)/[2r^2(r^2+2)]<0\), so this intersection lies outside the positivity region. The two feasible vertices and the unbounded edge rays show all three inequalities are irredundant. At \(V_{1\infty}\), the multiplier factors as
\[
1+s\chi_1(g)+t\chi_2(g)=\frac{(1-r\chi_1(g)+r^2)^2}{1+3r^2+r^4},
\]
so \(F\) is identically \((1-r^2)/(1+3r^2+r^4)\). At \(V_{01}\), the coefficient identity makes \(a_0=a_1=0\) and all \(a_n>0\) for \(n\ge2\). On the interior of \(L_\infty=0\), \(a_n=2r^n L_1>0\) for every \(n\ge1\), exhibiting universality along a limiting high-frequency boundary. This concludes the classification.

## Verification
A standalone exact-symbolic script, `su2_cone_verify.py`, reconstitutes all SU(2) fusion contributions in each degree from zero through thirty and compares them with the closed coefficient identity. It algebraically verifies all three pairwise facet intersections, the signs of the third constraint, and the rank-one multiplier factorization, with additional rational specializations \(r=1/2,2/3,3/4\). The proof covers all degrees and all \(0<r<1\); the finite symbolic checks are diagnostics, not a substitute for the displayed general identity or the underlying Peter–Weyl theorem.

## Relationship to prior work
Said, Da Costa, Steinert and Mostajeran (2026), §6.1.2, give a compact-Lie-group universality criterion and a strictly positive-type baseline of the form \(|1-q\chi_f|^{-2}\). Our \(A_r\) is an explicitly rescaled instance of that baseline with \(q=r/(1+r^2)\). Their results justify the positivity-versus-universality representation-theoretic framework but do not supply the signed quadratic \(SU(2)\) multiplier, three-facet cone, finite vertices or boundary spectral rigidity. The Clebsch–Gordan formulas and compact-group Bochner theorem are classical ingredients; the exact family-specific classification is the claim made here. Other related published results on central \(SU(2)\) character moments estimate higher \(L^p\) norms rather than the positive-type cone of this Abel-regularized family.

## Limitations
The theorem is restricted to degree at most two character modulation, one Abel radius \(r\in(0,1)\), and central translation-invariant real kernels on \(SU(2)\). It does not classify arbitrary character polynomials, noncentral kernels, or higher compact Lie groups. The finite explicit parameter cone is established from standard harmonic-analysis facts; no novelty claim is made for the general Peter–Weyl positivity or universality criteria themselves. Equivalent boundary formulas may exist in older specialized representation-ring or positive-type-kernel literature and independent mathematical validation has not been performed.

## References
- Salem Said, Nathaël Da Costa, Franziskus Steinert and Cyrus Mostajeran, *Universality of kernels on Riemannian symmetric spaces*, 2026, arXiv:2608.00010, first publicly posted 2026-06-19. Full text: https://arxiv.org/abs/2608.00010; particularly Theorem 2.1 and §6.1.2.
- Franziskus Steinert, Salem Said and Cyrus Mostajeran, *Universal kernels via harmonic analysis on Riemannian symmetric spaces*, 2025, arXiv:2506.19245, https://arxiv.org/abs/2506.19245; earlier context, not the signed cone.
- Standard compact-group Peter–Weyl and \(SU(2)\) Clebsch–Gordan character identities; stated explicitly in the proof.
