# Singleton-tube control of Minkowski asymmetry in cardinality-weighted cyclohedra

## Finding
Fix an integer \(n\ge3\), write \([n]=\mathbb Z/n\mathbb Z\), and let \(\mathcal I_\ell\) be the family of its \(n\) cyclic intervals of size \(\ell\), for \(1\le\ell<n\). Set \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\). For arbitrary positive real weights \(w_1,\ldots,w_n\), consider the weighted cycle-graph associahedron
\[
K_n(\mathbf w)=\sum_{\ell=1}^{n-1}w_\ell\sum_{I\in\mathcal I_\ell}\Delta_I+w_n\Delta_{[n]}\subset\mathbb R^n.
\]
Its affine hull is \(H_T=\{x:\sum_i x_i=T\}\), where \(T=n\sum_{\ell<n}w_\ell+w_n\). Define the affine-invariant Minkowski asymmetry by
\[
\operatorname{asym}(K)=\inf\{\lambda\ge1:\exists c\in\operatorname{aff}(K),\;-(K-c)\subseteq\lambda(K-c)\}.
\]
Then
\[
\boxed{\operatorname{asym}(K_n(\mathbf w))
=\frac{\displaystyle\sum_{\ell=2}^{n-1}(\ell-1)w_\ell+\frac{n-1}{n}w_n}
{\displaystyle\sum_{\ell=2}^{n-1}w_\ell+\frac1n w_n}.}
\tag{1}
\]
The **unique** minimizing Minkowski center is \(c=(T/n)\mathbf1\). Among the proper-tube facets, exactly the \(n\) singleton tubes realize the worst reflected-to-original support ratio at this center. No facet of a cyclic interval of cardinality \(2,\ldots,n-1\) attains it.

In particular, the standard unweighted simplex-sum cyclohedron satisfies
\[
\boxed{\operatorname{asym}(K_n(\mathbf1))=\frac{n^2-2n+2}{2(n-1)}=\frac{n-1}{2}+\frac1{2(n-1)}.}
\tag{2}
\]
For any fixed \(n\), the possible asymmetries over positive cardinality weights comprise exactly the open interval \((1,n-1)\). The parameter \(w_1\) affects only translation and has no effect on the invariant.

## Assumptions and scope
All sums are Minkowski sums, and the weights are positive real numbers. The polytope is the canonical simplex-sum realization of the cycle graph's nestohedron, with a constant weight on all tubes of a given cardinality; the result does not apply to arbitrary affine-inequivalent realizations or to independently weighted individual tubes. The full simplex summand with \(w_n>0\) guarantees intrinsic dimension \(n-1\). A proper tube is a nonempty connected proper vertex subset of \(C_n\), equivalently one cyclic interval. The phrase *worst facet* refers to the containment inequality for reflection about the minimizing center, not to Euclidean distance.

## Proof
**1. Support bounds and facet description.** For any index set \(S\) and any simplex \(\Delta_I\),
\[
\min_{x\in\Delta_I}x(S)=\mathbf1_{\{I\subseteq S\}},\qquad
\max_{x\in\Delta_I}x(S)=\mathbf1_{\{I\cap S\ne\varnothing\}},
\]
where \(x(S)=\sum_{i\in S}x_i\). The normal fan of a positive Minkowski sum is the common refinement of the normal fans of its summands. Hence the stated positive-weight sum has the standard nested fan, and its facets are precisely the lower inequalities indexed by proper tubes \(S\), as in the graph-associahedron facet description cited below. If \(S\) has cardinality \(s\), both \(S\) and its complement are paths, so its exact minimum and maximum supports are
\[
L_s=\sum_{\ell=1}^{s}(s-\ell+1)w_\ell,
\qquad M_s=T-L_{n-s}.
\tag{3}
\]
The full weight \(w_n\) contributes to \(T\) but not to either \(L_s\) when \(s<n\).

**2. Support ratios at the symmetric center.** Rotation of the cycle preserves the positive-weight polytope. Its invariant point in the affine hull is \(b=(T/n)\mathbf1\). Define the inward and outward centered support margins
\[
D_s=\frac{sT}{n}-L_s,
\qquad U_s=M_s-\frac{sT}{n}.
\]
Expanding (3), the contribution from singleton summands cancels, and, for every \(1\le s<n\),
\[
\begin{aligned}
D_s&=\sum_{\ell=2}^{n-1}w_\ell\min\{s,\ell-1\}+\frac{s}{n}w_n,\\
U_s&=\sum_{\ell=2}^{n-1}w_\ell\min\{n-s,\ell-1\}+\frac{n-s}{n}w_n.
\end{aligned}
\tag{4}
\]
All margins are positive. The reflected-and-contracted set \(b-(K-b)/\lambda\) lies in \(K\) exactly when each lower facet inequality is respected, or, equivalently, when \(\lambda\ge U_s/D_s\) for every \(s\).

**3. Universal singleton dominance.** For every \(s\ge1\), each summand of \(D_s\) is at least its \(s=1\) counterpart, while each summand of \(U_s\) is at most its \(s=1\) counterpart. Thus \(D_s\ge D_1\) and \(U_s\le U_1\). If \(s>1\), the strict positivity of \(w_n\) makes both inequalities strict. Consequently
\[
\frac{U_s}{D_s}<\frac{U_1}{D_1}\quad(2\le s<n),
\qquad \frac{U_1}{D_1}=
\frac{\sum_{\ell=2}^{n-1}(\ell-1)w_\ell+(n-1)w_n/n}
{\sum_{\ell=2}^{n-1}w_\ell+w_n/n}.
\tag{5}
\]
This gives an explicit feasible center with factor (1), and exactly the singleton facets attain the maximal ratio.

**4. Sharpness for every center, and uniqueness.** Suppose \(c\in H_T\) achieves a reflection-containment factor \(\lambda\). For each singleton facet \(x_i\ge L_1=w_1\), take a point of \(K\) with its \(i\)-th coordinate maximal, equal to \(M_1\). The reflection criterion forces
\[
(\lambda+1)c_i\ge M_1+\lambda L_1\quad(i\in[n]).
\]
Summing and using \(\sum_i c_i=T\) yields
\[
\lambda\ge\frac{nM_1-T}{T-nL_1}=\frac{U_1}{D_1}.
\tag{6}
\]
Thus (1) is globally optimal, not just optimal among symmetric centers. Equality in (6) forces equality in every singleton inequality, hence \(c_i=T/n\) for every \(i\); uniqueness follows.

**5. Sharp weight range.** Formula (1) is a weighted mean of the values \(1,2,\ldots,n-2,n-1\), with strictly positive weights \(w_2,w_3,\ldots,w_{n-1},w_n/n\). Therefore it lies strictly between \(1\) and \(n-1\). Holding the other weights fixed, letting \(w_2\) dominate gives limit \(1\), and letting \(w_n\) dominate gives limit \(n-1\). Continuity and connectedness of the positive weight domain yield every intermediate value. Putting all weights equal to \(1\) and summing the arithmetic progression gives (2).

## Verification
The independent enumerative and optimization checker `cyclo_weighted_asymmetry_check.py` constructs all coordinate-order greedy vertices of each simplex sum for \(3\le n\le7\), using exact integer coordinates for four positive integral profiles at each size. For every proper tube it independently computes both extreme subset sums and compares them to (3). It then verifies (1), strict dominance of singleton support ratios, and the optimal value and center of a transformed linear program solved by HiGHS. It checks 20 weighted profiles, 440 tube instances, and 5,088 distinct profile-specific vertices. Run `python cyclo_weighted_asymmetry_check.py` in an environment with Python 3 and SciPy installed. These finite checks are supplementary: (3)--(6) constitute the general proof.

## Relationship to prior work
Jevtić, Jelić, and Živaljević (2017) explicitly identify cyclohedra with sums of simplex faces over cycle tubes and give general hypergraphic-polytope facet inequalities (Section 5, Proposition 20). Padrol, Pilaud, and Poullot (2021) study deformation cones and graph-associahedron nested fans, again recording the simplex-sum realization (Theorem 2.2). Neither inspected paper gives a Minkowski asymmetry formula for cardinality-weighted cycles.

Previously reported exact Euclidean inradius and center results for the unweighted simplex-sum cyclohedron concern an intrinsically Euclidean optimization, not the affine reflection-containment factor. The known Minkowski asymmetry theorem for simplex-sum stellohedra concerns the star graph and does not cover cycle tubes or the present positive weight parameters. The support comparison in (4)--(6) and resulting entire positive-weight range are additional statements.

## Limitations
The theorem concerns cyclically invariant cardinality weights only. In particular, arbitrary independent tube weights need not possess a uniform invariant center and are not classified. Different affine realizations with the same cyclohedral face lattice need not have the same affine asymmetry. Novelty is assessed relative to inspected sources and searched records, not certified exhaustively by absence of a search hit. No independent mathematical audit has yet been performed.

## References
1. F. D. Jevtić, M. Jelić, and R. T. Živaljević, *Cyclohedron and Kantorovich-Rubinstein polytopes*, arXiv:1703.06612, first public version 2017-03-20; Section 5, especially Proposition 20.
2. A. Padrol, V. Pilaud, and G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public version 2021-09-19; Theorem 2.2 and Section 2.
3. A. Postnikov, *Permutohedra, associahedra, and beyond*, International Mathematics Research Notices (2009), underlying generalized-permutahedron realization.
