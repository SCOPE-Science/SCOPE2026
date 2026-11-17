# Sharp near-extension diameters for finite-atomic Hilbert-valued \(L^p\)

## Finding

For finite atomic Bochner spaces over a Hilbert pair, the **complete sharp diameter** of the set of almost norm-preserving Hahn–Banach extensions can be computed in terms of only one statistic: the least normalized coefficient mass. The geometry changes at the Hilbert exponent. Above this exponent in the dual variable, worst perturbations concentrate on a least-mass atom; below it, worst perturbations spread proportionally across all atoms.

Let \(\mathcal E_R(\phi)\) be the extension set and \(\phi_0\) its unique norm-preserving member, as defined below. Then
\[
\boxed{\quad\tfrac12\operatorname{diam}\mathcal E_R(\phi)
=\max_{\Phi\in\mathcal E_R(\phi)}\|\Phi-\phi_0\|
=\begin{cases}
\sqrt{R^2-1},&1<q\le2,\\
\sqrt{(u_*+R^q-1)^{2/q}-u_*^{2/q}},&q>2.
\end{cases}\quad}
\]
Both maxima are attained. The formula includes functionals having zero coefficients on some atoms.

## Assumptions and scope

Fix an integer \(n\ge2\), weights \(w_1,\ldots,w_n>0\) with \(\sum_jw_j=1\), and a real or complex Hilbert space \(H\). Let \(Y\subset H\) be closed and nonzero, with nonzero orthogonal complement \(Y^\perp\). Fix \(1<p<\infty\) and the conjugate exponent \(q=p/(p-1)\). Equip \(\ell_p(w;H)=H^n\) with
\[
\|(h_j)\|_{p,w}=\left(\sum_{j=1}^n w_j\|h_j\|^p\right)^{1/p},
\]
and give \(\ell_p(w;Y)\) the induced norm. For each norm-one \(\phi\in\ell_p(w;Y)^*\), finite-dimensional atomic duality and Riesz representation give unique vectors \(y_j\in Y\) such that
\[
\phi((v_j))=\sum_jw_j\langle v_j,y_j\rangle,\qquad
\sum_jw_j\|y_j\|^q=1.
\]
Either Hilbert inner-product convention may be used, with conjugations adjusted accordingly. Define \(u_j=w_j\|y_j\|^q\), \(u_*=\min_j u_j\), and the canonical extension
\[
\phi_0((h_j))=\sum_jw_j\langle h_j,y_j\rangle.
\]
For each real \(R>1\), let \(\mathcal E_R(\phi)\) be all continuous scalar linear functionals \(\Phi\) on \(\ell_p(w;H)\) that extend \(\phi\) and satisfy \(\|\Phi\|\le R\). Norms and diameters are those of the dual space. For \(R=1\), this set is the singleton \(\{\phi_0\}\).

## Proof

**Step 1: exact extension geometry.** Every extension \(\Phi\) is represented by \(y_j+z_j\), where \(z_j\in Y^\perp\). The weighted Bochner dual norm yields
\[
\|\Phi\|^q=\sum_j w_j(\|y_j\|^2+\|z_j\|^2)^{q/2},\qquad
\|\Phi-\phi_0\|^q=\sum_jw_j\|z_j\|^q.
\tag{1}
\]
Orthogonality also proves that \(\phi_0\) is the **unique** norm-preserving extension: equality with \(\|\phi\|=1\) forces every \(z_j=0\). The norm constraint and objective in (1) depend only on the nonnegative magnitudes \(a_j=\|y_j\|\) and \(b_j=\|z_j\|\). Every such finite choice of \(b_j\) is realized by taking each \(z_j\) along a fixed unit vector in \(Y^\perp\).

**Step 2: the case \(1<q<2\).** Put \(S=\|\Phi\|\) and \(B=\|\Phi-\phi_0\|\). On the nonzero coordinates define
\[
v_j=\frac{w_j(a_j^2+b_j^2)^{q/2}}{S^q},\quad
x_j=\frac{a_j}{(a_j^2+b_j^2)^{1/2}},\quad
t_j=\frac{b_j}{(a_j^2+b_j^2)^{1/2}}.
\]
Set \(v_j=x_j=t_j=0\) at a zero coordinate. The \(v_j\) sum to one, and \(x_j^2+t_j^2=1\) whenever \(v_j>0\). Since the probability-space \(L^q\) norm is bounded by the \(L^2\) norm when \(q<2\),
\[
\frac{1}{S^2}=\biggl(\sum_jv_jx_j^q\biggr)^{2/q}\le\sum_jv_jx_j^2,
\qquad
\frac{B^2}{S^2}=\biggl(\sum_jv_jt_j^q\biggr)^{2/q}\le\sum_jv_jt_j^2.
\]
Adding gives \(1+B^2\le S^2\le R^2\); hence \(B\le\sqrt{R^2-1}\). Equality is achieved by \(b_j=\sqrt{R^2-1}\,a_j\). Since equality in the strict power-mean inequality requires constant \(x_j\) and \(t_j\) on positive-weight coordinates, these proportional magnitudes (with arbitrary orthogonal-complement directions) describe all maximizing perturbations, including the requirement \(b_j=0\) when \(a_j=0\).

**Step 3: the Hilbert case \(q=2\).** Equation (1) becomes \(\|\Phi\|^2=1+B^2\). Thus every perturbation with \(B^2=R^2-1\) is maximizing, irrespective of its atomic support.

**Step 4: the case \(q>2\).** Write \(s=2/q\in(0,1)\) and \(\Delta=R^q-1>0\). For each atom define its excess norm cost
\[
d_j=w_j\bigl[(a_j^2+b_j^2)^{q/2}-a_j^q\bigr]\ge0.
\]
Then \(\sum_jd_j\le\Delta\). Using \(u_j=w_ja_j^q\), direct algebra gives the *exact* identity
\[
w_jb_j^q=F_{u_j}(d_j),\qquad
F_u(d)=\bigl[(u+d)^s-u^s\bigr]^{1/s},\qquad F_u(0)=0.
\tag{2}
\]
For every \(d>0\), the function \(u\mapsto F_u(d)\) is nonincreasing, because \(s<1\). Also \(d\mapsto F_u(d)/d\) is nondecreasing: indeed
\[
\frac{F_u(d)}d=
\left[\left(1+\frac ud\right)^s-\left(\frac ud\right)^s\right]^{1/s},
\]
and \(t\mapsto (1+t)^s-t^s\) decreases for \(t\ge0\). The ratio is strictly increasing in \(d\) when \(u>0\), and equals one when \(u=0\). It follows that
\[
\begin{aligned}
B^q&=\sum_jF_{u_j}(d_j)
\le\sum_j\frac{d_j}{\Delta}F_{u_j}(\Delta)
\le\frac{F_{u_*}(\Delta)}{\Delta}\sum_jd_j
\le F_{u_*}(\Delta).
\end{aligned}
\]
Take the \(q\)-th root, noting that \(sq=2\), to obtain
\[
B\le\sqrt{(u_*+\Delta)^{2/q}-u_*^{2/q}}.
\]
Equality is attained by selecting any index \(k\) with \(u_k=u_*\), setting every \(z_j=0\) except \(z_k\), and choosing
\[
\|z_k\|^2=
 w_k^{-2/q}\bigl[(u_*+\Delta)^{2/q}-u_*^{2/q}\bigr].
\]
If \(u_*>0\), strict monotonicity of the cost ratio rules out a maximizing perturbation with two positive excess costs: each maximizer is supported on exactly one least-mass atom. If \(u_*=0\), equation (2) gives \(F_0(d)=d\); the equality condition is precisely that all nonzero excess costs are on indices with \(u_j=0\), with total cost \(\Delta\). This proves the complete classification including zero coefficients.

**Step 5: diameter and finite-size limit.** If \(\Phi=\phi_0+Z\) is an admissible extension, so is \(\phi_0-Z\), by (1). Thus the fiber is centrally symmetric about \(\phi_0\). Its diameter equals twice its maximal radius: the triangle inequality gives the upper bound, and a pair \(\phi_0\pm Z\) achieving the radius gives equality.

If \(w_j=1/n\) and \(\|y_j\|=1\) for all \(j\), then \(u_*=1/n\). For \(q>2\), writing \(\Delta=R^q-1\), the exact radius is
\[
M_{n,q}(R)=\sqrt{(\Delta+1/n)^{2/q}-n^{-2/q}}.
\]
Since \(2/q<1\), the binomial expansion at positive \(\Delta\) gives
\[
M_{n,q}(R)=\Delta^{1/q}-\frac{n^{-2/q}}{2\Delta^{1/q}}+o(n^{-2/q}).
\]
This is a sharp quantitative finite-atom correction, realized by the one-atom perturbation in Step 4.

## Verification

The proof is deterministic and requires no numerical inference. For supplementary stress tests, `checks/verify.py` samples positive atomic weights, real dual exponents on both sides of two, functional coefficient vectors (including zero coordinates), and norm budgets. It checks that random admissible extensions obey the exact bound and that the analytic extremizers meet it, using standard-library arithmetic only. The checker tests 36,288 assertions and can be run with `python checks/verify.py` after extracting that file. Finite tests do not establish optimality or uniqueness; those follow from the inequalities and equality cases above.

## Relationship to prior work

Karak and Paul (2026, Theorems 3.1 and 3.3) establish **qualitative** preservation of uniqueness and linearity of Hahn–Banach extension under passage to Bochner \(L^p\). Daptari, Paul, and Rao (2020/2021) prove an earlier transfer result under a Radon–Nikodým hypothesis. The present theorem assumes Hilbert geometry and finite atoms, but supplies an **exact near-minimal radius and diameter** together with support of every maximizing perturbation; it is not implied by qualitative uniqueness alone.

Gayathri, Shunmugaraj, and Thota (2024, Sections 2–3) use precisely the near-extension sets and their diameters to characterize strong and uniform extension properties. Their statements bound diameters existentially and qualitatively, whereas the formula here gives the exact value for each finite-atomic Hilbert pair and each prescribed coefficient profile. Classical power-mean inequalities underlie the calculation and are not presented as new.

## Limitations

The result is a complete formula only for finite atomic measures and **Hilbert-valued** subspaces. It does not assert corresponding formulas for arbitrary Banach targets or nonatomic Bochner spaces. The phase transition is in the conjugate exponent \(q\), and the sharp asymptotic correction assumes fixed \(R>1\). Originality relative to older literature on strongly Chebyshev subspaces and uniform convexity remains a possible priority risk; an equivalent formula in different terminology cannot be excluded solely by database searches. 

## References

1. S. Karak and T. Paul, *Unique Hahn-Banach extensions in Bochner \(L^p\) spaces*, arXiv:2611.03203v1, first public 2026-11-02. https://arxiv.org/html/2611.03203v1
2. S. Daptari, T. Paul, and T. S. S. R. K. Rao, *Uniqueness of Hahn-Banach extension and related norm-1 projections in dual spaces*, arXiv:2009.09581v1, 2020; journal version 2021. https://arxiv.org/html/2009.09581v1
3. P. Gayathri, P. Shunmugaraj, and V. Thota, *Extensions of Continuous Linear Functionals and Smoothness of Banach Spaces*, Journal of Convex Analysis 31 (2024), 195–226. https://doi.org/10.68381/jca31012
4. E. F. Oja, *Strong uniqueness of the extension of linear continuous functionals according to the Hahn–Banach theorem*, Mathematical Notes 43 (1988), 134–139. https://doi.org/10.1007/BF01152551
