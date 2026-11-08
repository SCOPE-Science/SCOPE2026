# Exact VC dimension of maximal antichains in finite rectangular grid posets

## Finding

Let \(m,n\ge 1\) be integers, and let \(P_{m,n}=[m]\times[n]\) have the coordinatewise (weak) product order. Write \(\mathcal M_{m,n}\) for the family of all **inclusion-maximal** antichains of \(P_{m,n}\). Regard it as a concept class on the ground set \(P_{m,n}\), with membership queries \(p\mapsto\mathbf 1_{p\in A}\) for \(A\in\mathcal M_{m,n}\). Then

\[
\boxed{\operatorname{VCdim}(\mathcal M_{m,n})=\min\!\left\{m,n,\left\lfloor\frac{2(m+n)}5\right\rfloor\right\}.}
\]

In particular, for square grids, \(\operatorname{VCdim}(\mathcal M_{s,s})=\lfloor 4s/5\rfloor\), despite the underlying poset having antichain width \(s\). For fixed \(m\le n\), full width \(m\) is shattered exactly when \(n\ge\lceil 3m/2\rceil\).

## Assumptions and scope

The order is \((i,j)\le(i',j')\) if and only if \(i\le i'\) and \(j\le j'\). An antichain has no two comparable distinct members. A maximal antichain cannot be enlarged while remaining an antichain; it need not have maximum cardinality. A support \(S\subseteq P_{m,n}\) is shattered when for every \(T\subseteq S\) some \(A\in\mathcal M_{m,n}\) satisfies \(A\cap S=T\). Only ordinary binary membership-shattering is asserted, not online/Littlestone dimension or the lattice-valued shattering notion. All cases \(m,n\ge1\), including \(m=n=1\), are covered.

## Proof

**Step 1: Every shattered support is an antichain.** If \(S\) is shattered, its all-positive trace forces \(S\subseteq A\) for an antichain \(A\), so \(S\) itself is an antichain. If \(k=|S|>0\), order its points as \(s_i=(x_i,y_i)\) with \(x_1<\cdots<x_k\); then \(y_1>\cdots>y_k\). Consequently \(k\le\min\{m,n\}\).

**Step 2: A local necessity lemma.** Partition the unoccupied row coordinates relative to \(x_1,\ldots,x_k\) into \(k+1\) gaps, before \(x_1\), between consecutive occupied rows, and after \(x_k\). Similarly partition the unoccupied column coordinates relative to \(y_1>\cdots>y_k\). Call one of these \(k+1\) indexed gaps *slack* if it contains an unoccupied row or column; interior gap \(i\) lies between \(s_i\) and \(s_{i+1}\), and boundary gaps lie outside the first and last marked points. There are exactly \(m+n-2k\) unoccupied coordinate levels altogether.

Every marked position \(s_i\) must be incident to a slack gap (one of the two gaps flanking it). Indeed, shattering the pattern which includes all \(s_j\) except \(s_i\) gives a maximal antichain \(B\) containing every other marked point but omitting \(s_i\). Maximality forces some \(b\in B\) comparable with \(s_i\). This \(b\) must be incomparable with all \(s_j\), \(j\ne i\).

Suppose no flanking gap of \(s_i\) is slack. For \(1<i<k\), this means \(x_i=x_{i-1}+1\), \(x_{i+1}=x_i+1\), \(y_{i-1}=y_i+1\), and \(y_i=y_{i+1}+1\). Any \(b\) comparable with \(s_i\) but incomparable with both neighboring marked points must satisfy \(x_{i-1}<b_x<x_{i+1}\) and \(y_{i+1}<b_y<y_{i-1}\), hence \(b=s_i\), a contradiction. For \(i=1\) with \(k>1\), the no-slack assumption means \(x_1=1\), \(y_1=n\), \(x_2=x_1+1\), \(y_2=y_1-1\). A \(b\) comparable with \(s_1\) and incomparable with \(s_2\) must have \(b_x<x_2\), \(b_y>y_2\), hence it is \(s_1\); the final endpoint is symmetric. For \(k=1\), no slack means \(m=n=1\), so there is no alternative maximal antichain omitting the sole point. Thus the necessity holds for every \(k\ge1\).

Each unoccupied coordinate level belongs to one gap. A boundary gap can serve one marked position and an interior gap at most two. Since every one of the \(k\) marked positions needs a slack gap, the total number of unoccupied levels is at least \(\lceil k/2\rceil\). Therefore \(m+n-2k\ge\lceil k/2\rceil\), which implies \(5k\le2(m+n)\). Together with Step 1, this gives

\[
\operatorname{VCdim}(\mathcal M_{m,n})\le\min\left\{m,n,\left\lfloor2(m+n)/5\right\rfloor\right\}.
\]

**Step 3: Two universal local gadgets.** On a \(2\times3\) grid, designate \(u=(1,3)\) and \(v=(2,1)\). Four *maximal* antichains realize every labeling of \((u,v)\):

\[
\begin{array}{c|c}
(u,v)\text{ labels}&\text{chosen maximal antichain}\\\hline
(1,1)&\{(1,3),(2,1)\}\\
(1,0)&\{(1,3),(2,2)\}\\
(0,1)&\{(1,2),(2,1)\}\\
(0,0)&\{(1,1)\}.
\end{array}
\]

The transposed \(3\times2\) grid has the same property with rows and columns exchanged. On a \(1\times2\) grid, designate \((1,1)\) and use singleton maximal antichains \(\{(1,1)\}\) and \(\{(1,2)\}\) for labels one and zero; transpose for \(2\times1\).

**Step 4: Anti-diagonal concatenation.** Set \(k=\min\{m,n,\lfloor2(m+n)/5\rfloor\}\). For \(k=0\) the lower bound is immediate. For \(k\ge1\), put \(r=\lceil k/2\rceil\). Because \(k\le m,n\) and \(5k\le2(m+n)\), we have \((m-k)+(n-k)\ge r\). Choose an integer \(a\in[0,r]\) so that \(a\le m-k\) and \(r-a\le n-k\). Such an integer exists by the previous inequality.

Construct \(\lfloor k/2\rfloor\) pair-gadgets, each either \(2\times3\) or \(3\times2\), plus (when \(k\) is odd) one singleton gadget, either \(1\times2\) or \(2\times1\). Orient exactly \(a\) gadgets so that their extra coordinate level lies in the row direction, and the other \(r-a\) in the column direction. Their total row/column spans are \(k+a\le m\) and \(k+(r-a)\le n\).

Place these rectangles in disjoint consecutive row intervals from top to bottom and in disjoint consecutive column intervals in *reverse* order. A point from an earlier rectangle has a smaller row but a larger column than every point in a later rectangle; hence points in different rectangles are automatically incomparable. The union of a locally selected maximal antichain from each rectangle is therefore an antichain. For an arbitrary binary labeling of the \(k\) designated points, choose the appropriate local antichain from each gadget and take their union \(U\). Extend \(U\) to some inclusion-maximal antichain \(A\) of the full finite grid. Any designated point with label zero was excluded from its local maximal antichain and is comparable to a point of that local antichain; it cannot be introduced during extension. Every designated point labeled one already belongs to \(U\). Thus \(A\) realizes the prescribed labeling. All \(2^k\) labelings are realizable, and the \(k\)-point support is shattered.

Combining Steps 2 and 4 proves the formula. \(\square\)

## Verification

The standalone script `verify_maximal_antichain_grid.py` independently enumerates all antichains as decreasing coordinate matchings and filters them by the definition of maximality. It computes shattered supports directly from all possible traces, without using the theorem to decide shattering. It checks all \(28\) unordered rectangles with \(1\le m\le n\le7\) (\(8750\) candidate antichain supports visited), and validates the four local \(2\times3\) patterns and the \(1\times2\) gadget. The script reproduces the known count of \(817\) maximal antichains on \(7\times7\). Run `python3 verify_maximal_antichain_grid.py` with Python 3. The program uses no external dependencies. These bounded tests are corroboration; the proof establishes the unrestricted formula.

## Relationship to prior work

Bouyssou, Marchant and Pirlot (first publicly available October 21, 2024) give bijections and exact enumeration methods for maximal antichains in products of two chains, including restricted alignments and grid walks. Those enumerative results provide natural motivation and the right objects, but do not state the exact binary membership VC dimension proved here. Tsai's 2017 theorem concerns a *strict-coordinate* product order, whose maximal antichains differ from those under the weak-coordinate order. Cambie, Chornomaz, Dvir, Filmus and Moran develop a different, lattice-element form of shattering and general bounds; their assertions do not supply the present incidence-family dimension formula.

## Limitations

This result is about maximal, not maximum-cardinality, antichains and about the coordinatewise weak order, not the strict product order. It does not determine the Littlestone dimension, the complete shattering polynomial, or the exact collection of all shattered supports. The finite verifier is not an infinite proof. The literature comparison is bounded and does not establish exhaustive historical priority; independent validation has not been conducted.

## References

- D. Bouyssou, T. Marchant, M. Pirlot, *About maximal antichains in a product of two chains: A catch-all note*, arXiv:2410.16243, first posted 2024-10-21, https://arxiv.org/abs/2410.16243.
- S.-F. Tsai, *Two properties of maximal antichains in strict chain product posets*, arXiv:1701.06750, first posted 2017-01-24, https://arxiv.org/abs/1701.06750.
- S. Cambie, B. Chornomaz, Z. Dvir, Y. Filmus, S. Moran, *A Sauer–Shelah–Perles Lemma for Lattices*, arXiv:1807.04957, first posted 2018-07-13, https://arxiv.org/abs/1807.04957.
