# Exact independent and maximal-packing spectra and triangular-cactus exchange geometry of path blob graphs

## Finding
For each integer \(n\geq1\), let \(P_n\) be the path with vertices \(1,\ldots,n\), and let \(B_n\) be its **blob graph**: the vertices are all nonempty connected vertex subsets (intervals \([a,b]\)) of \(P_n\), and two distinct blobs are adjacent if they overlap or contain adjacent path vertices. A packing is an independent set of \(B_n\). Let \(I_n(z)\) count all packings and \(M_n(z)\) count inclusion-maximal packings by number of blobs.

**Theorem.** Simultaneously, for every \(n\geq1\):

1. The complete packing polynomial is
   \[
   I_n(z)=\sum_{k=0}^{\lfloor(n+1)/2\rfloor}\binom{n+1}{2k}z^k,
   \qquad I_n(1)=2^n.
   \]
   Its degree is \(\alpha(B_n)=\lceil n/2\rceil\), and all its zeros are simple and real negative, explicitly
   \[
   -\tan^2\!\left(\frac{(2j-1)\pi}{2(n+1)}\right),
   \qquad 1\leq j\leq\lfloor(n+1)/2\rfloor.
   \]
2. The complete **inclusion-maximal** packing polynomial is specified by the rational bivariate series
   \[
   \sum_{n\geq1}M_n(z)t^n=\frac{zt(1+t)^2}{1-t-zt^2(1+t)}.
   \]
   More explicitly the number of inclusion-maximal packings of size \(k\) is
   \[
   m_{n,k}=[t^{n-2k+1}](1+t)^{k+1}(1-t)^{-k},
   \qquad 1\leq k\leq\lceil n/2\rceil,
   \]
   and is zero outside this range. Each admissible coefficient is positive, so the sizes of inclusion-maximal packings have no internal gaps.
3. Form the **optimum exchange graph** whose vertices are maximum-cardinality packings; join two if one blob can be replaced by one other blob while preserving maximum size. For odd \(n\), this graph has exactly one vertex. For even \(n=2m\) it is the chain of \(m\) triangles on labeled vertices \(1,\ldots,2m+1\), with triangle \(i\) supported on \(\{2i-1,2i,2i+1\}\). Consecutive triangles share one vertex and there are no other intersections or edges. In particular the number of optima is \(n+1\), the number of exchange edges is \(3n/2\), and the diameter is \(n/2\).

## Assumptions and scope
All graphs are finite and simple. An interval \([a,b]\) consists of **all** integers from \(a\) through \(b\), inclusive. A packing is an unordered set of distinct blobs. Its size counts blobs, **not** the number of original path vertices in their union. “Inclusion-maximal” means no additional blob can be inserted, not necessarily that the packing has maximum size. In the exchange graph, a legal edge is unrestricted one-blob replacement between two already optimal packings, not a sequence passing through smaller packings. The statements include \(n=1\) and \(n=2\).

## Proof
**Boundary encoding.** Write a nonempty packing in increasing interval order as \([a_1,b_1],\ldots,[a_k,b_k]\). Compatibility means \(b_i+1<a_{i+1}\). Thus
\[
1\leq a_1<b_1+1<a_2<b_2+1<\cdots<a_k<b_k+1\leq n+1.
\]
Conversely every increasing choice of \(2k\) elements from \(\{1,\ldots,n+1\}\), paired consecutively, gives exactly one packing; the strict inequality between a pair's ending boundary and the next starting boundary guarantees a vacant path vertex. The empty packing corresponds to the empty choice. This proves the binomial coefficient formula, the degree, and \(I_n(1)=2^n\) by the even-subset identity.

For the root census use the polynomial identity
\[
I_n(z)=\tfrac12\bigl((1+\sqrt z)^{n+1}+(1-\sqrt z)^{n+1}\bigr),
\]
which is independent of the square-root branch. For \(z=-\tan^2\theta\) with \(0<\theta<\pi/2\), this equals \(\cos((n+1)\theta)/\cos^{n+1}\theta\). The displayed angles are precisely its \(\lfloor(n+1)/2\rfloor\) distinct roots in this interval. The degree equality excludes every other complex root, and multiplicity one follows.

**Maximality and length composition.** Define the two boundary gaps \(g_0=a_1-1\), \(g_k=n-b_k\), the interior gaps \(g_i=a_{i+1}-b_i-1\) (each at least one), and interval lengths \(\ell_i=b_i-a_i+1\) (each at least one). A singleton blob can be added if a boundary gap has length at least two or an interior gap at least three: such a singleton has no path edge to any chosen interval. Conversely, if \(g_0,g_k\in\{0,1\}\) and each interior \(g_i\in\{1,2\}\), every unselected vertex is within graph distance at most one of a chosen interval; any blob containing it is adjacent to that interval. Hence these gap conditions are necessary and sufficient for maximality.

For \(k\geq1\), the \(k\) positive interval lengths contribute \((t/(1-t))^k\), the \(k-1\) interior gaps contribute \((t+t^2)^{k-1}\), and the two boundary gaps contribute \((1+t)^2\). Their product is
\[
F_k(t)=\frac{t^{2k-1}(1+t)^{k+1}}{(1-t)^k}.
\]
This counts each maximal packing exactly once, since its ordered intervals and all gaps are unique. Summing \(z^kF_k(t)\) over \(k\geq1\) yields \(zt(1+t)^2/(1-t-zt^2(1+t))\). Extracting \([t^n]\) proves the stated formula and positivity (the required exponent \(n-2k+1\) is nonnegative exactly in the claimed range).

**Exchange geometry.** For \(n=2m-1\), an optimal packing has \(m\) intervals of lengths at least one separated by \(m-1\) required empty vertices. This uses all \(2m-1\) vertices, forcing the unique singleton intervals \([1,1],[3,3],\ldots,[2m-1,2m-1]\).

For \(n=2m\), precisely one unit of length remains after the same \(2m-1\)-vertex minimum. It may occur in one of the \(m\) interval lengths, one of the \(m-1\) interior gaps, or either boundary gap: \(2m+1\) states. Under the boundary encoding these states are indexed by their unique omitted element \(r\in\{1,\ldots,2m+1\}\) from the ordered list of \(2m\) endpoints. Two optimal states share \(m-1\) blobs exactly when their omitted labels both belong to one of the triples \(\{2i-1,2i,2i+1\}\): labels in such a triple change only the \(i\)-th interval, leaving all others fixed. If the labels lie in no common such triple, changing the omitted boundary shifts the endpoint pairings across at least two intervals, so no one-blob exchange is possible (this also follows directly by comparing the consecutively paired endpoint lists). Thus the edge set is exactly the union of the indicated triangles. They form a block path; the largest distance is between the two end vertices, equal to \(m\). This proves all three assertions.

## Verification
A standalone standard-library Python checker, `verify.py`, independently enumerates every family of mutually compatible intervals on \(P_n\) for \(1\leq n\leq12\). For each \(n\) it compares every coefficient of \(I_n(z)\) and \(M_n(z)\), every optimum, and the full optimum-exchange edge set, against the theorem. It reports `VERIFY_OK`, with 8190 packings enumerated across all twelve orders. These finite experiments corroborate but do not replace the above unrestricted proofs.

## Relationship to prior work
The blob graph and its use in reducing induced connected-subgraph packing to maximum independent set are established in Martin–Paulusma–Smith–van Leeuwen (2023) and Bonnet–Czyżewska–Masařík–Pilipczuk–Rzążewski (2026); see the references. The latter's Section 4 defines the blob graph and proves induced-minor/optimization transfer theorems. These are not cardinality enumerations or optimum exchange classifications of path blob graphs. The univariate total sequence of maximal-packing counts agrees with a known tribonacci-type integer sequence; that sequence alone is not asserted to be novel. The contribution assessed here is the joint **blob-graph-specific** all-cardinality and root classification, maximal cardinality profile, and exact chain-of-triangles optimum exchange structure, including the proven structural bijections.

## Limitations
Only base graphs \(P_n\) and unweighted blob cardinalities are covered. The theorem does not classify connected blobs in arbitrary trees or general graph families, weighted optima, or exchanges permitting intermediate nonoptimal states. Priority beyond the inspected sources and searched records is not independently established; independently indexed literature could contain equivalent interval-scheduling formulas or stronger results. No independent mathematical audit has been performed.

## References
1. É. Bonnet, J. Czyżewska, T. Masařík, M. Pilipczuk, P. Rzążewski, *QPTAS for MWIS and finding large sparse induced subgraphs in graphs with few independent long holes*, arXiv:2602.18317v1 (first public 2026-02-20), especially Section 4. https://arxiv.org/html/2602.18317v1
2. B. Martin, D. Paulusma, S. Smith, E. J. van Leeuwen, *Induced Disjoint Paths and Connected Subgraphs for H-Free Graphs*, Algorithmica 85 (2023), 2580–2604, especially Sections 2 and 3.1. https://doi.org/10.1007/s00453-023-01109-z
3. OEIS Foundation, *A000213*, known tribonacci-number sequence, https://oeis.org/A000213 (used only to identify known total counts).
