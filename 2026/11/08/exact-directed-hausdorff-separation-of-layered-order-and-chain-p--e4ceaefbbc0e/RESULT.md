# Exact directed Hausdorff separation of layered order and chain polytopes

## Finding

Let \(k\ge 1\) and \(m_1,\ldots,m_k\) be positive integers. Let \(P=A_{m_1}\oplus\cdots\oplus A_{m_k}\) be the ordinal sum of antichains, each lower layer being below every point of every higher layer. Equip Stanley's ordinary order and chain polytopes \(O(P),C(P)\subset\mathbb R^{N}\), \(N=\sum_i m_i\), with the same *canonical* coordinate Euclidean metric and position. For compact sets, write \(h(X,Y)=\sup_{x\in X}\operatorname{dist}_2(x,Y)\) and \(d_H(X,Y)=\max\{h(X,Y),h(Y,X)\}\).

If \(k=1\), the two polytopes coincide with the cube and all distances below are zero. If \(k\ge2\), let \(\lambda>0\) be the unique solution of
\[
\sum_{i=1}^{k}\left(1-\frac{\lambda}{m_i}\right)_+=1, \qquad t_i=\left(1-\frac{\lambda}{m_i}\right)_+,
\]
where \((a)_+=\max\{0,a\}\). Set \(U_i=\sum_{j=i+1}^{k}m_j\), and interpret the last summand at \(U_k=0\) as zero. Then **both directed distances are determined exactly**:
\[
\boxed{h(O(P),C(P))^2=\sum_{i=1}^{k}m_i(1-t_i)^2
=\sum_{i:m_i>\lambda}\frac{\lambda^2}{m_i}+\sum_{i:m_i\le\lambda}m_i,}
\]
\[
\boxed{h(C(P),O(P))^2=\max_{1\le i\le k}\frac{m_iU_i}{m_i+U_i}.}
\]
In particular, \(d_H(O(P),C(P))=h(O(P),C(P))\). For \(k=2\), the two directed distances coincide; for every \(k\ge3\), the first is **strictly larger** than the second. The unique farthest point of \(O(P)\) from \(C(P)\) is the all-ones vertex. Among the vertices of \(C(P)\), the farthest ones from \(O(P)\) are exactly the characteristic vectors of entire layers attaining the displayed maximum (for \(k\ge2\)).

The symmetric Hausdorff distance is unchanged by *any permutation of the layer sizes*, while the reverse directed distance generally changes. For instance, size sequences \((1,2,3)\) and \((3,2,1)\) both give \(d_H^2=11/5\), but the reverse directed squared distances are \(6/5\) and \(3/2\), respectively. For \(k\ge2\) equal-sized layers of cardinality \(a\),
\[
 h(O,C)^2=\frac{a(k-1)^2}{k},\quad h(C,O)^2=\frac{a(k-1)}{k},\quad \frac{h(O,C)}{h(C,O)}=\sqrt{k-1}.
\]
Thus the asymmetry between directed Hausdorff distances is unbounded although the two polytopes have equal Ehrhart polynomials and volumes.

## Assumptions and scope

Every \(m_i\) is a strictly positive integer and all coordinates are those of the elements of the specified poset, without translating, rotating, optimally aligning, or rescaling either polytope. This is the *position-sensitive* Euclidean Hausdorff metric between their two canonical realizations, not an infimum over isometries, and not graph distance in their one-skeleta. The orientation convention for the order polytope is \(x_p\le x_q\) for \(p<_Pq\); the opposite convention amounts to reflecting the order polytope and is not silently substituted.

The order polytope has vertices given by filters (up-sets) of \(P\). The chain polytope has vertices given by antichains; for this layered \(P\), every nonempty antichain lies entirely within one layer. The chain polytope has the explicit description
\[
 C(P)=\left\{x\in\mathbb R_{\ge0}^{N}:\sum_{i=1}^k\max_{p\in A_{m_i}}x_p\le1\right\}.
\]
The expression in terms of maxima is shorthand for a finite system of linear inequalities, one for each choice of a coordinate from every layer. No assertion is made for arbitrary (not fully layered) finite posets.

## Proof

**Step 1: The first directed distance is attained at the all-ones vertex.** Every coordinate of every order-polytope point lies in \([0,1]\), and the all-ones vector \(\mathbf1\) belongs to \(O(P)\). For a closed, coordinatewise downward-closed set \(K\subseteq\mathbb R_{\ge0}^N\), and for \(0\le a\le b\) coordinatewise, a closest point \(c\in K\) to \(b\) may be chosen with \(0\le c\le b\) (replace \(c\) by its coordinatewise minimum with \(b\)). Then \(c'=\min(a,c)\in K\) and \(\|a-c'\|_2\le\|b-c\|_2\). The chain polytope is such a downward-closed set; hence \(\operatorname{dist}(x,C(P))\le\operatorname{dist}(\mathbf1,C(P))\) for all \(x\in O(P)\).

**Step 2: Compute the projection of \(\mathbf1\).** The Euclidean nearest-point projection onto a convex set is unique. It must be invariant under arbitrary permutations within each layer, so its coordinates on layer \(i\) all equal some \(t_i\ge0\). The projection is the unique minimizer of
\[
 \min\left\{\sum_i m_i(1-t_i)^2: t_i\ge0,\ \sum_i t_i\le1\right\}.
\]
For \(k\ge2\), the budget constraint is tight. The strictly convex KKT conditions give \(t_i=(1-\lambda/m_i)_+\). The budget function is continuous and strictly decreasing from \(k\) to zero on \([0,\max_i m_i]\), so there is a unique \(\lambda>0\) producing sum one. The formula for \(h(O,C)^2\) follows. Moreover, every \(t_i<1\). If \(x\in O(P)\) differs from \(\mathbf1\) in some coordinate, applying the coordinatewise-minimum construction to the unique projection of \(\mathbf1\) yields a **strictly smaller** squared distance in that coordinate. Thus \(\mathbf1\) is the unique farthest point in \(O(P)\).

**Step 3: Compute the other directed distance.** Distance to a fixed closed convex set is a convex function. Its maximum over \(C(P)\) is achieved at a vertex, hence at the characteristic vector \(\mathbf1_S\) of an antichain \(S\subseteq A_{m_i}\) for some \(i\). Write \(a=|S|\), \(U_i=\sum_{j>i}m_j\). In the isotonic least-squares problem defining \(\operatorname{dist}(\mathbf1_S,O(P))\), all coordinates below layer \(i\), and all unselected coordinates in layer \(i\), can be set to zero. Averaging the remaining coordinates is feasible and does not increase squared error: all selected coordinates have a common value \(s\), and all \(U_i\) higher coordinates a common value \(t\ge s\). The resulting minimization is
\[
 \min_{0\le s\le t\le1}\left\{a(1-s)^2+U_i t^2\right\}.
\]
For \(U_i>0\), its minimizer is \(s=t=a/(a+U_i)\), and the minimum equals \(aU_i/(a+U_i)\); if \(U_i=0\), it is zero. This quantity is strictly increasing in \(a\) for \(U_i>0\), so among nonzero antichain vertices its maximum on layer \(i\) occurs exactly for the entire layer. Taking the maximum over \(i\) yields the second formula and the vertex equality classification.

**Step 4: Sharp comparison.** For the optimal \((t_i)\) in Step 2 and any fixed \(i<k\), we have \(t_j\le1-t_i\) for each \(j>i\). Consequently
\[
 \sum_j m_j(1-t_j)^2\ge m_i(1-t_i)^2+U_i t_i^2
 \ge\frac{m_iU_i}{m_i+U_i}.
\]
For \(k=2\), direct substitution gives equality: both squares equal \(m_1m_2/(m_1+m_2)\). For \(k\ge3\), each comparison is strict. For \(i\ge2\), at least one preceding layer contributes a strictly positive omitted term because \(t_j<1\). For \(i=1\), there are at least two later layers and they cannot both satisfy \(t_j=1-t_1\) when \(t_1<1\), except if \(t_1=0\), in which case the quadratic lower bound itself is strict. The last-layer reverse value is zero. Hence the first directed distance strictly dominates for all \(k\ge3\).

**Step 5: Symmetry and unbounded contrast.** The objective in Step 2 is unchanged by permuting the \(m_i\), proving permutation invariance. In Step 3 the suffix sums \(U_i\) retain ordering information. For equal \(m_i=a\), the KKT solution is \(t_i=1/k\), so the two squared-distance formulas reduce to those in the statement. Their ratio of directed distances is \(\sqrt{k-1}\), which tends to infinity with \(k\). This proves all claimed consequences.

## Verification

A standalone enumerative/numerical checker is provided in `check_hausdorff.py`. It enumerates the vertex sets of \(O(P)\) and \(C(P)\), solves Euclidean projection problems with the corresponding explicit linear inequalities, and checks both formulae against the extrema over all vertices. It tests 33 profiles of two to four layers (including unbalanced examples with entries above two). The reported result was `LAYERED_ORDER_CHAIN_HAUSDORFF_CHECKS_PASSED profiles= 33`. These finite numerical checks are diagnostic; Steps 1–5 constitute the proof for all positive integer layer sizes. Runtime dependencies for the optional checker are Python 3, NumPy and SciPy; execute `python check_hausdorff.py` from the directory containing the file.

A second reproducibility method needs no numerical optimization: for each list of positive integers, solve the one-variable strictly monotone piecewise-linear budget equation in the Finding, then compute the two rational squared distances. For example, for \((1,2,3)\), \(\lambda=6/5\), \((t_1,t_2,t_3)=(0,2/5,3/5)\), giving the stated values.

## Relationship to prior work

Stanley's construction of the two polytopes, the vertex descriptions and Ehrhart equivalence are prior results. Ahmad–Fourier–Joswig (first posted September 4, 2023) studies the same maximal ranked/fully layered posets, with a face-number comparison for chain-order interpolants. Freij-Hollanti–Lundström (first posted December 21, 2023) treats face-vector inequalities under ordinal sums. Lee (first posted October 5, 2026) compares edges, edge lengths and graph diameters. Those comparisons do not, in the material examined, evaluate the position-sensitive ambient Euclidean directed Hausdorff distances or the order-dependent reverse-to-forward separation. The projection and isotonic regression steps use standard convex optimization facts; novelty is claimed for their combined exact two-direction classification and unbounded contrast, not for those general tools.

## Limitations

The results concern precisely the canonical shared-coordinate embeddings and complete layered posets. No Hausdorff statement is proved for arbitrary posets, for weighted norms, or for optimally aligned realizations. Strict uniqueness is shown for the farthest point in \(O(P)\), while on the chain side only the **vertex extremizers** are classified; nonvertex extremizers are not claimed to be classified. The literature comparison cannot exclude every unindexed or alternative-terminology treatment, so independent historical priority review remains useful. Numerical verification is finite and is not a substitute for the proof.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23, DOI: 10.1007/BF02187680.
2. I. Ahmad, G. Fourier and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first posted 2023-09-04, https://arxiv.org/abs/2309.01626.
3. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first posted 2023-12-21, https://arxiv.org/abs/2312.13890.
4. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413, first posted 2026-10-05, https://arxiv.org/abs/2610.07413.
