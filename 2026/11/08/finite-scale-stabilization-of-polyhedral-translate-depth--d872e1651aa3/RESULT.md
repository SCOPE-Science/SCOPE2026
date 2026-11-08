# Finite-scale stabilization of polyhedral translate depth

## Finding
Let \(d\ge2\), and let \(K\subset\mathbb R^d\) be any full-dimensional compact convex polytope, with an irredundant facet description
\[
K=\{z:\langle u_i,z\rangle\le b_i,\quad 1\le i\le m\},
\]
where the outward facet normals \(u_i\) are unit vectors. For each facet \(F_i=\{z\in K:\langle u_i,z\rangle=b_i\}\), fix \(p_i\in\operatorname{relint}F_i\), and define
\[
s(K;p)=\min_{1\le i\le m}\min_{j\ne i}
 \bigl(b_j-\langle u_j,p_i\rangle\bigr)>0.
\]
For a Borel probability measure \(\mu\), define its translate depth at \(y\) by
\[
\mathsf d_{tK}(y;\mu)=1-\sup_{x:\,y\notin tK+x}\mu(tK+x).
\]
**Theorem.** If \(\operatorname{supp}\mu\subset c+RB_2^d\) for some \(c\in\mathbb R^d\) and \(R>0\), then, simultaneously for **every** \(y\in\mathbb R^d\) and every \(t\ge2R/s(K;p)\),
\[
\boxed{\displaystyle
\mathsf d_{tK}(y;\mu)=\min_{1\le i\le m}
\mu\bigl(\{z:\langle u_i,z\rangle\ge\langle u_i,y\rangle\}\bigr).}
\]
The equality allows atoms, including positive measure on the displayed hyperplanes. In contrast, for an everywhere-positive continuous probability density (in particular, a nondegenerate Gaussian), the left side is strictly larger than the right side for **every** finite \(t>0\) and **every** \(y\). Thus compact support gives exact finite-scale stabilization, whereas full support can forbid it completely.

The cutoff is explicit, geometrically computable from facet interiors, and **sufficient, not claimed optimal**. For finite samples, beyond this cutoff, all depth values are computable by finitely many scalar projection ranks.

## Assumptions and scope
A polytope is the intersection of the displayed finitely many halfspaces and is assumed bounded, full-dimensional and nonempty. The inequalities are irredundant: each one defines a distinct facet. The Euclidean ball \(B_2^d\) has radius one. The support inclusion is a literal compact-support hypothesis (not a high-probability truncation). The definition takes the supremum over *closed* translates that **do not contain** \(y\); hence the right-hand side uses closed halfspaces \(\langle u_i,z\rangle\ge\langle u_i,y\rangle\). No continuity or boundary-nullness of \(\mu\) is assumed in the theorem.

## Proof
**1. Facet slack is positive.** For fixed \(i\), the relative-interior point \(p_i\) lies on its own facet but on none of the others. Thus \(b_j-\langle u_j,p_i\rangle>0\) for every \(j\ne i\). Finitely many strict positive slacks yield \(s=s(K;p)>0\).

**2. A universal upper bound on missed-translate mass.** Write
\[
M_t(y)=\sup_{x:\,y\notin tK+x}\mu(tK+x),\qquad
M_\infty(y)=\max_i\mu\{z:\langle u_i,z\rangle<\langle u_i,y\rangle\}.
\]
If \(y\notin tK+x\), at least one facet inequality is violated:
\(\langle u_i,y\rangle>tb_i+\langle u_i,x\rangle\). Every \(z\in tK+x\) satisfies \(\langle u_i,z\rangle\le tb_i+\langle u_i,x\rangle<\langle u_i,y\rangle\). Consequently \(M_t(y)\le M_\infty(y)\) for every positive \(t\).

**3. Exact realization of every facet-direction mass beyond the finite cutoff.** Translate the origin so that \(c=0\); this does not change either side of the theorem. Fix \(i\), put \(\alpha=\langle u_i,y\rangle\), and suppose \(t\ge2R/s\). If \(\alpha\le-R\), then \(\mu\{\langle u_i,z\rangle<\alpha\}=0\), requiring no construction. If \(-R<\alpha\le R\), take arbitrary \(h\) with \(-R\le h<\alpha\); if \(\alpha>R\), take \(h=R\). Define
\[
x_h=h u_i-tp_i,\qquad T_h=tK+x_h.
\]
Its \(i\)-th facet is the hyperplane \(\langle u_i,z\rangle=h\), so \(y\notin T_h\). For every \(z\in\operatorname{supp}\mu\) satisfying \(\langle u_i,z\rangle\le h\), the \(i\)-th inequality of \(T_h\) holds. For each \(j\ne i\), unit normality, \(\|z\|\le R\), and \(|h|\le R\) give
\[
\langle u_j,z-hu_i\rangle\le\|z-hu_i\|
\le R+|h|\le2R\le t\bigl(b_j-\langle u_j,p_i\rangle\bigr).
\]
Therefore all the other inequalities of \(T_h\) hold as well. Hence
\[
\mu(T_h)=\mu\{z:\langle u_i,z\rangle\le h\}.
\]
In the middle case, letting \(h\uparrow\alpha\), while always \(h\ge-R\), gives by continuity from below
\(M_t(y)\ge\mu\{\langle u_i,z\rangle<\alpha\}\). In the last case \(T_R\) contains all of the support and misses \(y\), so \(M_t(y)=1\). Maximizing over all facets and using Step 2 gives \(M_t(y)=M_\infty(y)\), and taking complements proves the displayed formula. The argument is uniform in \(y\) and uses no atomlessness assumptions.

**4. Full-support boundary.** Suppose \(\mu\) has a continuous, strictly positive density everywhere. For fixed \(t>0,y\), the function \(x\mapsto\mu(tK+x)\) is continuous and tends to zero at infinity. The closure of the admissible shifts \(\{x:y\notin tK+x\}\) is \(\{x:y\notin\operatorname{int}(tK+x)\}\); the same supremum is achieved on that closed set, since boundary shifts are limits of excluding shifts. Let \(x_*\) achieve it. Some facet has
\(tb_i+\langle u_i,x_*\rangle\le\langle u_i,y\rangle\), so \(tK+x_*\) is contained in the corresponding closed halfspace through \(y\). Because \(tK+x_*\) is bounded and the density is everywhere positive, the halfspace has strictly greater mass. Its boundary has zero mass, giving
\[
M_t(y)=\mu(tK+x_*)<\mu\{\langle u_i,z\rangle<\langle u_i,y\rangle\}\le M_\infty(y).
\]
This proves strict non-stabilization at all finite dilations.

## Verification
The stand-alone standard-library Python program `check_depth.py` tests rational-coordinate finite samples in dimensions \(2,3,4,5\), together with a non-axis-aligned triangle. It constructs explicit translates witnessing the formula at its sufficient cube dilation scale, including atomic ties and points outside the sample support, and checks every facet containment inequality using exact `fractions.Fraction` arithmetic. The program passed \(1,480\) exact support/query tests, together with four supplementary Gaussian-tail positivity checks. The finite experiments are auxiliary: the universal theorem and full-support obstruction follow from Steps 1–4 rather than from sample enumeration. Execute `python check_depth.py` from the package directory.

## Relationship to prior work
Molchanov and Nagy (2026), Section 5, define translate depth, show monotonicity in dilation, and prove convergence toward a tangent-cone depth under boundary-nullness assumptions; see their Theorem 5.2. Their Section 7 gives an arrangement-based algorithm for empirical polytope depth. The present theorem proves the stronger **finite, explicit, uniform cutoff** for polytopal testing bodies with compactly supported measures, with no boundary-null assumption, and identifies the limiting function as a minimum over only facet-normal halfspace masses. Neither asymptotic convergence nor an arrangement procedure logically supplies this finite uniform threshold.

The relation to ordinary halfspace depth is exact only when the available facet-normal directions suffice. General halfspace depth minimizes over **all** directions; the displayed minimum only uses the finitely many outward facet normals. Classical halfspace-depth literature supplies the comparison concept but not this finite cutoff for translated polytopes.

## Limitations
The cutoff \(2R/s(K;p)\) is a conservative sufficient bound, not the optimal stabilization scale. The argument requires a full-dimensional polytope with finitely many irredundant facets; smooth bodies can behave differently. The compact-support hypothesis cannot simply be dropped, as Step 4 shows. No assertion is made that the facet-direction depth equals classical Tukey depth, or that arbitrary nonpolyhedral testing bodies stabilize at finite scale. Historical priority is assessed against the specified primary literature and targeted searches, not certified exhaustively.

## References
Molchanov, I., and Nagy, S. (2026). *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*. arXiv:2610.26108, first publicly posted 2026-10-19. https://arxiv.org/abs/2610.26108 . In particular, Sections 2, 5, 6 and 7.

Pokorný, D., Laketa, P., and Nagy, S. (2024). *Another look at halfspace depth: flag halfspaces with applications*. Journal of Nonparametric Statistics 36(1), 165–181. https://doi.org/10.1080/10485252.2023.2236721 .
