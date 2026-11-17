# Sharp cross-parameter distortion of free Banach lattices over \(\ell_1^n\)

## Finding
For every integer \(n\ge1\) and \(1\le p<q\le\infty\), the canonical homomorphism
\[
J_n^{p,q}:\operatorname{FBL}^{(p)}[\ell_1^n]\longrightarrow\operatorname{FBL}^{(q)}[\ell_1^n]
\]
fixing every free generator is onto and satisfies
\[
\|J_n^{p,q}\|=1,\qquad\|(J_n^{p,q})^{-1}\|=n^{1/p-1/q},\qquad 1/\infty:=0.
\]
The inverse constant is attained by the lattice polynomial \(h_n=\bigvee_{j=1}^{n}|\delta_{e_j}|\). For an infinite index set \(I\), the same witnesses prove that the canonical inclusion for \(\ell_1(I)\) has dense, nonclosed proper range and is not order continuous for **every** \(1\le p<q\le\infty\).

## Assumptions and scope
All spaces and free Banach lattices are real, with the standard \(p\)-convex free norm (convexity constant one). The vector lattice \(\operatorname{FVL}[E]\) consists of lattice polynomials in the evaluation maps \(\delta_x(x^*)=x^*(x)\), regarded as positively homogeneous real-valued functions on \(E^*\). For finite \(1\le r<\infty\), its norm is
\[
\|f\|_r=\sup\left\{\left(\sum_{k=1}^m|f(u_k)|^r\right)^{1/r}:\ m\ge1,\quad\sup_{\|x\|_E\le1}\sum_{k=1}^m|u_k(x)|^r\le1\right\}.
\]
For \(r=\infty\), it is \(\|f\|_\infty=\sup_{\|u\|_{E^*}\le1}|f(u)|\). For \(E=\ell_1^n\), identify the dual with \(\ell_\infty^n\); writing \(u_k=(u_{kj})\), the displayed admissibility condition is exactly
\[
\max_{1\le j\le n}\sum_{k=1}^m|u_{kj}|^r\le1.
\]
These definitions are the standard norm formulas, not new assertions. The canonical map \(J^{p,q}\) fixes \(\operatorname{FVL}[E]\) pointwise in its functional model, is contractive and has dense range; these standard structural facts are used below.

## Proof
**Upper bound for finite \(q\).** Fix an arbitrary \(p\)-admissible finite array \((u_{kj})\), and put \(r_k=\max_{1\le j\le n}|u_{kj}|\). Then
\[
\sum_{k=1}^m r_k^p\le\sum_{j=1}^n\sum_{k=1}^m|u_{kj}|^p\le n.
\]
For \(r_k>0\), set \(v_k=r_k^{p/q-1}u_k\), and put \(v_k=0\) when \(r_k=0\). Since \(|u_{kj}|\le r_k\),
\[
\sum_k|v_{kj}|^q=\sum_{k:r_k>0}|u_{kj}|^p\left(\frac{|u_{kj}|}{r_k}\right)^{q-p}\le\sum_k|u_{kj}|^p\le1.
\]
Thus \((v_k)\) is \(q\)-admissible. Positive homogeneity gives \(|f(u_k)|=r_k^{1-p/q}|f(v_k)|\). Hölder's inequality, with conjugate exponents \(q/(q-p)\) and \(q/p\), yields
\[
\begin{aligned}
\sum_k|f(u_k)|^p&=\sum_k r_k^{p(1-p/q)}|f(v_k)|^p\\
&\le\left(\sum_k r_k^p\right)^{1-p/q}\left(\sum_k|f(v_k)|^q\right)^{p/q}\\
&\le n^{1-p/q}\|f\|_q^p.
\end{aligned}
\]
Taking the supremum over \(p\)-admissible arrays shows \(\|f\|_p\le n^{1/p-1/q}\|f\|_q\) for all lattice polynomials \(f\). If \(q=\infty\), each \(u_k\) satisfies \(|f(u_k)|\le r_k\|f\|_\infty\), so \(\sum_k|f(u_k)|^p\le n\|f\|_\infty^p\), proving the endpoint directly.

**Sharpness.** Set \(h_n(u)=\max_j|u_j|\). For finite \(1\le r<\infty\), every \(r\)-admissible array satisfies
\[
\sum_k h_n(u_k)^r\le\sum_{j=1}^n\sum_k|u_{kj}|^r\le n.
\]
The array with exactly \(n\) rows \(u_k=e_k\) is admissible and gives equality. Hence \(\|h_n\|_r=n^{1/r}\); for \(r=\infty\), \(\|h_n\|_\infty=1\). Thus the reverse inequality is sharp. The canonical map has norm one: it is contractive and fixes generators of norm one. Norm equivalence on dense \(\operatorname{FVL}[\ell_1^n]\) extends the algebraic identity to a bounded inverse between the two completions, proving surjectivity and the exact inverse norm. The case \(n=1\) is included.

**Infinite generators.** Let \(I\) be infinite and select any distinct \(i_1,\ldots,i_n\in I\). The same lattice polynomial \(h_n=\bigvee_{j=1}^n|\delta_{e_{i_j}}|\) has \(\|h_n\|_r=n^{1/r}\) for each \(r\): admissibility bounds follow from these selected coordinate columns, and the finitely supported coordinate evaluations realize equality. Consequently, for fixed \(p<q\),
\[
\frac{\|J_{\ell_1(I)}^{p,q}h_n\|_q}{\|h_n\|_p}=n^{1/q-1/p}\longrightarrow0.
\]
The canonical map is therefore not bounded below. It is injective with dense range by the standard representation, hence its range is not closed and not all of the target. The established equivalence between surjectivity and order continuity (Pariente-Martín–Tradacete, Theorem 5.1) then proves failure of order continuity, including \(p<q\le2\).

## Verification
All inequalities above are algebraic or applications of Hölder and the defining norm formula. The only dimension-dependent upper estimate is \(\sum_k r_k^p\le n\), and the exact lower witness consists of the \(n\) coordinate rows; neither uses finite experimental extrapolation. The endpoint \(q=\infty\), zero rows and one-dimensional case have separate coverage. No numerical computation is necessary. The independent implications used are explicitly identified: the standard norm representation, functorial contractivity/dense range, and Theorem 5.1 for the order-continuity conclusion.

## Relationship to prior work
The 2026 paper of Pariente-Martín and Tradacete studies the canonical cross-parameter map and, in Theorem 5.1, characterizes surjectivity/order continuity through equivalence of free norms. Its Corollary 5.3 proves finite-dimensional equivalence by a general finite-norming-set bound (equation (5.1)), without this exact \(p,q,n\)-dependent inverse norm, and notes that infinite-dimensional Hilbert generators can have equivalence for \(p<q\le2\). The present calculation identifies the opposite behavior for infinite \(\ell_1\), as well as sharp constants for all finite coordinate dimensions. Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky give the underlying norm formula and nonlinear summing comparisons, not the cross-parameter sharp norm computed here. Oikhberg, Taylor, Tradacete and Troitsky give broader qualitative structure and automatic-convexity comparisons. A published result on transitive permutation-invariant free lattices already computes norms in a fixed-point sublattice; such restricted norm information alone does not give the global inverse norm estimate for arbitrary lattice polynomials. These are implication comparisons, not a claim of absolute publication priority.

## Limitations
The sharp formula concerns the canonical comparison for real \(\ell_1^n\), and the stated obstruction for real infinite-dimensional \(\ell_1(I)\); it does not determine comparison constants for general finite-dimensional generators. The finite-dimensional result has a short direct proof and is not a new general interpolation theorem. The infinite-dimensional order-continuity conclusion invokes an established published equivalence rather than independently reproving it. An older quantitative statement under different terminology may exist; no independent audit has been performed.

## References
1. R. E. Pariente-Martín and P. Tradacete, *Order continuity of induced homomorphisms between free Banach lattices*, arXiv:2611.00451v1 (first public 2026-10-30), Theorem 5.1 and Corollary 5.3, https://arxiv.org/html/2611.00451v1.
2. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices under convexity conditions*, RACSAM 116 (2022), article 15, https://doi.org/10.1007/s13398-021-01155-8, especially Sections 6–7.
3. T. Oikhberg, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices*, JEMS 28 (2026), 4387–4514 (first publicly submitted 2022), https://doi.org/10.4171/JEMS/1552, especially Section 9.6.
4. *Transitive permutation invariants of free \(p\)-convex Banach lattices are isometric AM-spaces*, public research result dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-transitive-permutation-invariants-of-free-p-convex-banach-lattic--f6413894fb60 (restricted fixed-point result; full text not accessible for this comparison).
