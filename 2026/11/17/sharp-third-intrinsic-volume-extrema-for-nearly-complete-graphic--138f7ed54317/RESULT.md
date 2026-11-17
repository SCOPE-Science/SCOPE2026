# Sharp third-intrinsic-volume extrema for nearly complete graphical zonotopes

## Finding

Fix integers \(n\ge4\) and \(2\le k\le\lfloor n/2\rfloor\). Let \(D\) be any simple graph with vertex set \([n]\) and exactly \(k\) edges. Delete its edges from \(K_n\) and form the standard Euclidean graphical zonotope
\[
 Z_{K_n\setminus D}=\sum_{\{u,v\}\in E(K_n)\setminus E(D)}[0,e_u-e_v]\subset\mathbf1^\perp.
\]
Write \(V_3\) for the third intrinsic volume in Steiner normalization. Then \(V_3(Z_{K_n\setminus D})\) is **uniquely maximized**, up to relabeling, when \(D\) is a matching of \(k\) edges, and **uniquely minimized** when \(D\) is a star of \(k\) edges.

Here is an exact evaluation for arbitrary \(D\). Define \(P(D)=\sum_{v=1}^n\binom{\deg_D(v)}2\) and \(U(D)=V_3(Z_D)\), with \(U(D)=0\) if \(Z_D\) has dimension less than three. Set
\[
\begin{aligned}
 A_n&=6\sqrt2\binom{n-2}{4}+\sqrt6\left(3\binom{n-2}{3}+2(n-2)\binom{n-3}{2}\right)+8(n-2)(n-3),\\
 B_\mathrm{a}(n)&=6(n-3)+\sqrt6\binom{n-3}{2},\\
 B_\mathrm{d}(n)&=8+4\sqrt6(n-4)+2\sqrt2\binom{n-4}{2},\\
 \Delta_n&=B_\mathrm{d}(n)-B_\mathrm{a}(n).
\end{aligned}
\]
With the convention that binomial coefficients vanish when the upper argument is smaller than the nonnegative lower argument,
\[
\boxed{
V_3(Z_{K_n\setminus D})
=\left(\frac1{3}\binom n2-k\right) A_n
+\binom k2 B_\mathrm{d}(n)-\Delta_nP(D)-U(D).
}
\]
In particular, the sharp extremal values are
\[
\begin{aligned}
V_\max&=\left(\frac1{3}\binom n2-k\right) A_n+\binom k2 B_\mathrm{d}(n)-2\sqrt2\binom k3,\\
V_\min&=\left(\frac1{3}\binom n2-k\right) A_n+\binom k2 B_\mathrm{a}(n)-2\binom k3.
\end{aligned}
\]
The strict, exact gap is
\[
\boxed{V_\max-V_\min=\Delta_n\binom k2-(2\sqrt2-2)\binom k3>0.}
\]

## Assumptions and scope

All graphs are finite, simple, unweighted, and have the common labeled vertex set \([n]\); isolated vertices in the deleted graph \(D\) are allowed. The graph \(K_n\setminus D\) is connected because \(k<n-1\), so its zonotope has intrinsic dimension \(n-1\ge3\). Segments are the unscaled type-A root segments \([0,e_u-e_v]\), with the Euclidean metric inherited from \(\mathbb R^n\). The normalization of \(V_3\) is fixed by the Steiner parallel-body formula; in dimension three, \(V_3\) is ordinary Euclidean volume. The theorem does not claim extremality among arbitrary weighted graphs or all possible edge counts.

## Proof

**1. Triple-edge determinant weights.** For any finite graph \(G\), the zonotope intrinsic-volume formula gives
\[
V_3(Z_G)=\sum_{F\in\binom{E(G)}3}\sqrt{\det(B_F^{\mathsf T}B_F)},
\]
where \(B_F\) is the vertex-edge incidence matrix of the three selected edges. A three-edge cycle contributes zero. For a forest, the Gram determinant is the product of the orders of its nontrivial tree components: this follows from the matrix-tree determinant identity, or by elementary Gram elimination on trees. Thus, for three edges, the only possible weights are \(2\sqrt2\) (three isolated edges), \(\sqrt6\) (a two-edge path plus an isolated edge), and \(2\) (a tree on four vertices). The triangle has weight zero. This proves the graph interpretation of \(U(D)\).

**2. Inclusion-exclusion and exact coefficients.** Regard the full three-edge sum for \(K_n\) as a multilinear polynomial in the edge indicator variables. Setting the \(k\) variables belonging to \(E(D)\) to zero and expanding produces four terms: the complete-graph total, minus the sum of triples containing a specified deleted edge, plus the sum containing each specified pair of deleted edges, minus the sum of triples entirely deleted.

The weight of all triples through a specified edge of \(K_n\) equals \(A_n\). Indeed, there are \(3\binom{n-2}{4}\) triples of mutually disjoint edges through that edge, \(3\binom{n-2}{3}+2(n-2)\binom{n-3}{2}\) triples consisting of a two-edge path and a disjoint edge, and \(4(n-2)(n-3)\) connected three-edge trees. The triangle triples have zero weight. Every triple is counted at each of its three edges, so \(V_3(Z_{K_n})=\binom n2A_n/3\).

For two prescribed deleted edges sharing a vertex, the third edge gives a connected tree in \(3(n-3)\) ways (weight \(2\) each), a two-edge path plus an isolated edge in \(\binom{n-3}{2}\) ways (weight \(\sqrt6\)), and a triangle in one way (weight zero); hence the pair contribution is \(B_\mathrm a(n)\). For two disjoint prescribed deleted edges, the third edge either connects their endpoints in four ways (weight \(2\)), joins one of their four endpoints to one of the \(n-4\) other vertices (weight \(\sqrt6\)), or lies wholly outside their four endpoints in \(\binom{n-4}{2}\) ways (weight \(2\sqrt2\)). This gives \(B_\mathrm d(n)\). Exactly \(P(D)\) deleted-edge pairs are adjacent. The last inclusion-exclusion term is \(U(D)\), proving the boxed identity.

**3. Quantitative pair-separation inequality.** Direct subtraction yields
\[
\Delta_n=8+4\sqrt6(n-4)+2\sqrt2\binom{n-4}{2}-6(n-3)-\sqrt6\binom{n-3}{2}.
\]
The successive difference is
\[
\Delta_{n+1}-\Delta_n=(2\sqrt2-\sqrt6)(n-4)+3\sqrt6-6>0
\quad(n\ge4).
\]
Also, \(\Delta_4=2\) and
\[
\Delta_6-\Delta_4=-12+2\sqrt2+5\sqrt6>2\sqrt2.
\]
Because \(\Delta_{n+2}-\Delta_n\) increases strictly with \(n\), these inequalities imply
\[
\Delta_n>2\sqrt2(k-2)\quad\text{whenever}\quad n\ge2k,\ k\ge2.
\]

**4. Unique maximum.** Let \(D_{\mathrm m}\) be a matching of \(k\) deleted edges, and let \(P=P(D)\). Every three deleted edges have triple weight at most \(2\sqrt2\). A triple whose weight is less than \(2\sqrt2\) contains an adjacent pair, so the number of such triples is at most \(P(k-2)\). Consequently
\[
0\le U(D_{\mathrm m})-U(D)\le2\sqrt2\,P(k-2),
\qquad U(D_{\mathrm m})=2\sqrt2\binom k3.
\]
The exact evaluation therefore gives
\[
V_3(Z_{K_n\setminus D_{\mathrm m}})-V_3(Z_{K_n\setminus D})
\ge\bigl(\Delta_n-2\sqrt2(k-2)\bigr)P.
\]
This is strictly positive unless \(P=0\), in which case the deleted edges form a matching. Thus the matching is the unique maximizer up to graph isomorphism.

**5. Unique minimum.** Let \(D_{\mathrm s}\) be a star of \(k\) deleted edges. All of its three-edge subsets are trees on four vertices, so \(U(D_{\mathrm s})=2\binom k3\) and \(P(D_{\mathrm s})=\binom k2\). Put \(Q=\binom k2-P(D)\), the number of disjoint deleted-edge pairs. For each three-edge subset of \(D\), the excess of its wedge weight over \(2\) is nonpositive if it contains no disjoint pair, and is otherwise at most \(2\sqrt2-2\). Every triple containing a disjoint pair is counted among the at most \(Q(k-2)\) pair-plus-third-edge incidences. Hence
\[
U(D)-U(D_{\mathrm s})\le(2\sqrt2-2)Q(k-2).
\]
The exact evaluation gives
\[
V_3(Z_{K_n\setminus D})-V_3(Z_{K_n\setminus D_{\mathrm s}})
\ge\bigl(\Delta_n-(2\sqrt2-2)(k-2)\bigr)Q.
\]
This is strict when \(Q>0\). If \(Q=0\), all deleted edges pairwise intersect. A finite simple set of pairwise-intersecting edges is either a star or the three edges of a triangle. The latter has \(U(D)=0<2\binom33\), so the exact evaluation still gives a strict increase relative to a star. Thus the unique minimum is the deleted star. Substitution gives both extremal values and their positive gap.

## Verification

The accompanying standard-library checker is `artifacts/verify.py`. Extract the files and execute `python3 artifacts/verify.py`. It directly enumerates the three-edge wedge weights, checks the inclusion-exclusion identity and both sharp extrema for every deletion pattern with \(4\le n\le7\) and \(2\le k\le\lfloor n/2\rfloor\), and checks additional reproducibly sampled cases with \(8\le n\le10\). The calculations compare exact coefficient triples for \(1,\sqrt2,\sqrt6\) and use numerical comparison only for ordering in finite instances. The infinite-family extremum is proved above rather than inferred from the finite tests.

## Relationship to prior work

Brazitikos and McIntyre (arXiv:2102.05900, first available 2021-02-11) study wedge-volume inequalities; Joós and Lángi (arXiv:2206.03204, first available 2022-06-07) prove the general intrinsic-volume formula for zonotopes used in Step 1. Padrol, Pilaud and Poullot (arXiv:2111.12422, first available 2021-11-24) study graphical zonotope deformations and relate the complete-graph zonotope to the permutahedron. Those established facts are not asserted as new here. The new contribution is the exact deletion-subgraph identity and the sharp global two-sided extremum, including uniqueness and gap, among all graphs with exactly \(k\) missing edges in the specified dense regime.

## Limitations

The theorem only concerns the third Steiner intrinsic volume and exactly the dense range \(2\le k\le\lfloor n/2\rfloor\); it makes no claim for larger deletion budgets. The numerical code confirms only finitely many instances. An earlier equivalent extremal inequality under three-edge forest statistics could exist, so historical priority is not established independently. The proof does not depend on any such absence.

## References

1. S. Brazitikos and F. McIntyre, *Vector-Valued Maclaurin Inequalities*, arXiv:2102.05900 (2021), https://arxiv.org/abs/2102.05900.
2. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204 (2022), https://arxiv.org/abs/2206.03204.
3. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (2021), https://arxiv.org/abs/2111.12422.
