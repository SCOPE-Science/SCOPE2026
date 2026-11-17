# Exact codimension-one constrained widths of Euclidean cross-polytopes

## Finding

For every integer \(m\ge2\), let \(K_m=\{x\in\mathbb R^m:\|x\|_1\le1\}\) inside real Euclidean \(\ell_2^m\). The self-constrained Kolmogorov width in codimension one is exactly \[d_{m-1}^{c}(K_m;\ell_2^m)=\frac12\sqrt{\frac{m}{m-1},\] whereas the unconstrained width is \[d_{m-1}(K_m;\ell_2^m)=\frac1{\sqrt m}.\] Every optimal constrained subspace of dimension at most \(m-1\) is, necessarily of dimension exactly \(m-1\), a hyperplane \[V_\varepsilon=\{x:\sum_{j=1}^m\varepsilon_jx_j=0\},\qquad\varepsilon_j\in\{-1,1\},\] and every such hyperplane is optimal. The ratio of constrained to unconstrained widths is \(m/(2\sqrt{m-1})\), asymptotic to \(\sqrt m/2\).

## Assumptions and scope

Throughout \(m\) is an integer at least two, \(K_m\) is the real \(\ell_1\) unit ball in \(\mathbb R^m\), and errors are measured using Euclidean norm. The self-constrained width is
\[
d_n^c(K_m;\ell_2^m)=\inf_{\dim V\le n}\sup_{x\in K_m}\inf_{y\in V\cap K_m}\|x-y\|_2.
\]
The ordinary width removes the condition \(y\in K_m\).

## Proof

**Reduction to vertices.** The set \(V\cap K_m\) is nonempty, closed, and convex. Its distance function is convex in the argument. Since \(K_m=\operatorname{conv}\{\pm e_1,\ldots,\pm e_m\}\), the supremum of the distance over \(K_m\) equals the maximum of its values at \(e_i\), by central symmetry.

**Universal lower bound.** Any subspace of dimension at most \(m-1\) is contained in a hyperplane \(H_u=\{x:\langle u,x\rangle=0\}\) with nonzero normal \(u\). Choose \(i\) with \(|u_i|=\|u\|_\infty\). For any \(y\in H_u\cap K_m\), the hyperplane equation yields \(|y_i|\le\sum_{j\ne i}|y_j|\). Since \(\|y\|_1\le1\), this implies \(|y_i|\le1/2\). If \(y_i\le0\) then \(\|e_i-y\|_2\ge1\), already stronger than required. Otherwise put \(t=y_i\in(0,1/2]\). Cauchy–Schwarz gives
\[
\|e_i-y\|_2^2=(1-t)^2+\sum_{j\ne i}y_j^2
\ge(1-t)^2+\frac{t^2}{m-1}
\ge\frac{m}{4(m-1)}.
\]
The last inequality uses that the quadratic is decreasing for \(0\le t\le1/2\), since its minimum occurs at \(t=(m-1)/m\ge1/2\). Thus every admissible subspace has worst-case error at least \(\frac12\sqrt{m/(m-1)}\).

**Matching construction.** For arbitrary signs \(\varepsilon_j\in\{-1,1\}\), take \(V_\varepsilon=\{x:\sum_j\varepsilon_jx_j=0\}\). For each vertex \(e_i\), define
\[
y^{(i)}_i=\frac12,\qquad y^{(i)}_j=-\frac{\varepsilon_i\varepsilon_j}{2(m-1)}\quad(j\ne i).
\]
This vector has zero signed coordinate sum and \(\ell_1\) norm one. Its squared distance from \(e_i\) is \(m/[4(m-1)]\). The vertex reduction proves the matching upper bound.

**Rigidity of optimizers.** If a codimension-one hyperplane \(H_u\) achieves this bound, pick \(i\) with largest normal magnitude. At an optimal approximation to \(e_i\), equality must hold in every preceding inequality. In particular, equality holds in \(|\sum_{j\ne i}u_jy_j|\le\|u\|_\infty\sum_{j\ne i}|y_j|\), and Cauchy–Schwarz forces all \(|y_j|=1/[2(m-1)]\ne0\) for \(j\ne i\). Hence each \(|u_j|=\|u\|_\infty\), so the normal has equal-magnitude coordinates. Conversely those hyperplanes are optimal as constructed. A lower-dimensional optimizer would be contained in some such optimal hyperplane. But in its equality case the unique best approximants \(y^{(i)}\) of all coordinate vertices must lie in the smaller subspace. Their span is the entire optimal hyperplane (for \(m\ge3\), they are images of the standard basis under a rank \(m-1\) matrix; for \(m=2\) each nonzero vector spans the optimal line). This contradicts smaller dimension. Alternatively the ordinary width of a smaller subspace can be bounded using the projection trace and gives a strict larger lower bound for \(m\ge3\): \(d_n(K_m)\ge\sqrt{(m-n)/m}\), which is not always larger, so the rank argument is used here.

**Ordinary width.** For any hyperplane with unit normal \(u\), the worst Euclidean distance of \(K_m\) to that hyperplane is \(\max_i|u_i|\). Its minimum over unit normals is \(m^{-1/2}\), attained exactly when the absolute normal coordinates are equal. Lower-dimensional spaces have no smaller width by containment in a hyperplane. Dividing the exact expressions proves the ratio.

## Verification

The script `CHECK.py` verifies the constructive signed-hyperplane witnesses and the lower-bound quadratic over rational test points in dimensions 2 through 30. These finite checks are diagnostics only; the proof above applies to every integer \(m\ge2\).

## Relationship to prior work

DeVore, Petrova, Siegel and Wojtaszczyk introduce self-constrained widths and obtain a dimension-independent lower bound \(1/2\) for the \(\ell_1\) unit ball measured in \(\ell_\infty\) (Lemma 4.8 of arXiv:2606.28587). The present claim concerns a *different ambient norm*, exact finite-dimensional values, unique optimal hyperplane normal patterns, and comparison with the ordinary Euclidean width. Their Lemma 4.8 does not establish this formula; its simple dominant-coordinate argument motivates the stronger Euclidean estimate here. Published general width estimates and related cross-polytope projection results were compared for direct mathematical implication.

## Limitations

Only real coordinate cross-polytopes and the codimension-one case are classified. This result does not determine other constrained dimensions or arbitrary convex bodies. Although targeted literature checks did not locate an identical theorem, classical relative-width literature may contain an equivalent formulation; an independent literature review has not been performed.

## References

- R. DeVore, G. Petrova, J. W. Siegel and P. Wojtaszczyk, *Constrained Kolmogorov widths*, arXiv:2606.28587, first public 26 June 2026, especially definitions (1.6)–(1.10) and Lemma 4.8. https://arxiv.org/abs/2606.28587
- A. Pinkus, *n-Widths in Approximation Theory*, Springer, 1985. Background on classical widths; not asserted to settle this constrained formula.
