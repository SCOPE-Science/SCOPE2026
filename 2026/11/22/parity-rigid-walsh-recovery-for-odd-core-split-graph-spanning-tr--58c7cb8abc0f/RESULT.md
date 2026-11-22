# Parity-rigid Walsh recovery for odd-core split-graph spanning trees

## Finding

Let \(m\ge3\) be odd and \(n\ge1\). Let \(G_{m,n}=K_m\vee\overline{K_n}\), the graph consisting of an \(m\)-vertex clique joined to \(n\) mutually nonadjacent vertices. Let \(f_{m,n}\) be the indicator, on the Boolean group \(\mathbb F_2^{E(G_{m,n})}\), of edge sets forming spanning trees. Write \(T_{m,n}h=f_{m,n}*h\), where convolution is **unnormalized**. Then:

1. \(T_{m,n}\) is invertible **if and only if \(n\) is even**. Every multiplier is odd in the invertible cases.
2. For odd \(n\), every Walsh multiplier is divisible by \(2^{m-1}\), and at least
   \[\binom{m}{(m+1)/2}\,2^{m(n-1)/2}\]
   distinct Walsh multipliers vanish. Consequently, the nullity is at least this number.
3. For the triangular core \(m=3\), the **sharp smallest positive absolute** multiplier is \(1\) when \(n\) is even and \(4\) when \(n\) is odd. In both cases the maximum absolute multiplier is \(3^{n-1}(n+3)^2\); hence the positive-spectrum \(\ell^2\) condition number is exactly \(3^{n-1}(n+3)^2\) for even \(n\) and \(3^{n-1}(n+3)^2/4\) for odd \(n\).

This gives a two-parameter parity classification of Fourier recoverability for spanning-tree signals on a natural family of threshold graphs, with an explicit stable cancellation mechanism and a fully sharp gap in the smallest nontrivial odd clique.

## Assumptions and scope

The clique vertices are labelled \(1,\ldots,m\) and the independent vertices \(u_1,\ldots,u_n\). The edge set consists of all clique edges and all edges between a clique vertex and an independent vertex. A Fourier character is indexed by an arbitrary subset \(S\subseteq E(G_{m,n})\), with signs \(\sigma_e=(-1)^{\mathbf1_{e\in S}}\). The unnormalized Walsh multiplier is
\[\Lambda_{m,n}(S)=\sum_{F\text{ a spanning tree of }G_{m,n}}\prod_{e\in F}\sigma_e.\]
The group has \(2^{\binom m2+mn}\) elements. Convolution is invertible precisely when all these multipliers are nonzero. The positive-spectrum condition number is the ratio between the largest and smallest **nonzero absolute** multiplier; for singular cases it concerns recovery only on the orthogonal complement of the nullspace.

## Proof

**Tree count and the even case.** Kirchhoff's matrix-tree theorem identifies \(\Lambda_{m,n}(S)\) with any cofactor of the signed Laplacian formed using the real edge weights \(\sigma_e\). At all-plus signs, the Laplacian eigenvalues are \(0\) once, \(m+n\) with multiplicity \(m\), and \(m\) with multiplicity \(n-1\). Thus
\[\tau_{m,n}=|\mathcal T(G_{m,n})|=m^{n-1}(m+n)^{m-1}.\]
Since each tree contributes \(\pm1\), every multiplier is congruent to \(\tau_{m,n}\) modulo \(2\). For odd \(m\) and even \(n\), this count is odd, so no multiplier vanishes.

**The uniform dyadic obstruction at odd \(n\).** Reduce the signed Laplacian modulo \(2\), so all signs become \(+1\). Delete the last clique vertex and order the remaining vertices with the other \(m-1\) clique vertices first. For odd \(n\), because \(m+n\) is even, the reduced matrix over \(\mathbb F_2\) has block form
\[\begin{pmatrix}J_{m-1}&J_{m-1,n}\\J_{n,m-1}&I_n\end{pmatrix}.\]
Its Schur complement over \(\mathbb F_2\) of the bottom block is \(J_{m-1}-nJ_{m-1}=0\). Its mod-two nullity is therefore \(m-1\). An integral square matrix with mod-two nullity \(r\) has determinant divisible by \(2^r\) (by integral row/column elimination, or Smith normal form). Hence \(2^{m-1}\mid\Lambda_{m,n}(S)\) for all \(S\) when \(n\) is odd.

**A zero multiplier for one independent vertex.** For \(n=1\), the graph is the complete graph on \(m+1\) vertices. Give every clique edge sign \(+1\). Set \(p=(m+1)/2\), and give the \(m\) edges from the remaining vertex to the clique exactly \(p\) positive and \(p-1\) negative signs. Delete that remaining vertex in the Laplacian. The resulting cofactor is \(\operatorname{diag}(m+\sigma_i)-J_m\); the matrix determinant lemma gives
\[\Lambda_{m,1}=(m+1)^p(m-1)^{p-1}\left(1-\frac p{m+1}-\frac{p-1}{m-1}\right)=0.\]
There are exactly \(\binom{m}{p}\) distinct signings of this displayed form.

**Cancellation-preserving pairs.** For any signed \(G_{m,n}\), delete one clique vertex when forming the signed Laplacian cofactor. A leaf attached to the clique by a sign vector \(s=(s_1,\ldots,s_m)\in\{\pm1\}^m\) has signed degree \(d(s)=\sum_i s_i\), which is odd and thus nonzero. Its Schur-complement contribution to the \((m-1)\)-by-\((m-1)\) clique block is
\[H(s)=\operatorname{diag}(s_1,\ldots,s_{m-1})-\frac{s's'^{\mathsf T}}{d(s)},\qquad s'=(s_1,\ldots,s_{m-1})^{\mathsf T}.\]
The cofactor is \((\prod_j d(s^{(j)}))\det(C+\sum_j H(s^{(j)}))\), where \(C\) is the clique-only reduced signed Laplacian. The identity \(H(-s)=-H(s)\) gives, after adjoining two labelled independent vertices with incident signs \(s\) and \(-s\),
\[\Lambda_{m,n+2}=-d(s)^2\Lambda_{m,n}.\]
Iterating from the one-leaf zero proves singularity for every odd \(n\). The first independent vertex has \(\binom m p\) allowed initial sign vectors, and each of the \((n-1)/2\) labelled successive pairs has \(2^m\) independent choices of its first sign vector; different choices give different Fourier characters. This proves the displayed zero-count lower bound.

**Sharp gap for the triangular core.** When \(m=3\), the parity result already gives \(|\Lambda|\ge1\) at even \(n\), and the dyadic obstruction gives \(|\Lambda|\ge4\) whenever \(n\) is odd and \(\Lambda\ne0\). Both bounds are attained. With every clique edge positive, take \(n=2\) and consecutive leaf sign vectors \((+1,+1,-1)\), \((+1,-1,+1)\). Their signed degrees are \(1\), and deleting the third clique vertex gives Schur complement
\[\begin{pmatrix}2&-1\\-1&0\end{pmatrix},\]
whose determinant is \(-1\). For \(n=1\), take all clique signs positive and leaf signs \((+1,-1,-1)\); the signed cofactor is \(-4\). Repeatedly add a pair \(((+1,+1,-1),(-1,-1,+1))\); its signed degrees are \(1,-1\), so the extension identity preserves both absolute determinant values. This attains the bound in every even or odd order. Finally, \(|\Lambda_{m,n}(S)|\le\tau_{m,n}\) by the triangle inequality, with equality at the all-positive character; the condition numbers follow.

## Verification

The companion \(verify.py\) uses only the Python standard library. It directly enumerates spanning trees by Prüfer words, forms the complete incidence-support indicator, and computes a full integer fast Walsh-Hadamard transform for \((m,n)=(3,1),(3,2),(3,3),(3,4),(5,1)\). Every multiplier is compared against an independently constructed signed Laplacian cofactor evaluated by the fraction-free Bareiss algorithm. These finite checks also test the dyadic divisibility, zero/nonzero parity, sharp triangular-core gaps, and the weighted determinant extension identity under deterministic sign samples for larger odd cores. The script completed **248,034 exact assertions**. The first four triangular-core zero counts are \(30,0,1088,0\) respectively; at \((m,n)=(5,1)\), there are \(15000\) zero multipliers. The infinite-dimensional quantifiers in the theorem follow from the proof above, not from finite enumeration.

Run directly with \(\texttt{python verify.py}\). No downloaded papers, datasets or third-party packages are required for these computations.

## Relationship to prior work

Martin and Reiner (2003) prove weighted enumerator factorizations for threshold graphs under specialized vertex-based edge weights, not all independent signed edge assignments. Chestnut and Fishkind (2012) establish unsigned threshold spanning-tree enumeration. Klee and Stamps (2019) give weighted matrix-tree and Schur-complement methods for several families, including threshold graphs with vertex-factorized weights. Those results supply the enumerative context and determinant tools, but their stated formulas do not determine the arbitrary-edge-character zero set, the odd-core parity classification, or the complete sharp gap for the triangular core. Generic weighted Kirchhoff identities are used as known machinery, not presented as a new result. The same Fourier question for complete graphs, bipartite graphs and graphs with two-vertex cores does not directly imply the odd-core join classification, because joining an extra universal clique vertex alters all spanning-tree edge supports.

## Limitations

The bound on nullity for odd \(n\) is not asserted to be exact. For odd cores \(m\ge5\), this result does **not** identify the smallest positive multiplier, except for the proved divisibility lower bound. The condition number given for \(m=3\) at odd \(n\) applies only to recoverable Fourier modes, not an inverse on the whole space. No claim is made about even clique sizes. The priority comparison is bounded by the referenced sources and available searchable records; an unindexed edge-signed threshold-tree specialization remains a possible antecedent.

## References

- J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, first publicly posted 2003-02-18, arXiv:math/0302213, https://arxiv.org/abs/math/0302213 .
- S. R. Chestnut and D. E. Fishkind, *Counting Spanning Trees of Threshold Graphs*, first publicly posted 2012-08-20, arXiv:1208.4125, https://arxiv.org/abs/1208.4125 .
- S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, first publicly posted 2019-02-27, arXiv:1903.03575, https://arxiv.org/abs/1903.03575 .
