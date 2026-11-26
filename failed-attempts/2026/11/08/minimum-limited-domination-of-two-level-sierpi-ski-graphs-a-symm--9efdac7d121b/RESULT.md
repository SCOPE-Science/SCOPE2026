# Minimum limited domination of two-level Sierpiński graphs: a symmetric-matrix classification

## Finding
For every integer \(m\ge 2\) and every integer \(1\le k\le m-1\), every minimum \(k\)-limited dominating set of the two-level Sierpiński graph \(S(2,m)\) is classified by a symmetric binary \(m\times m\) matrix with constant row sum \(k\). More precisely, label the graph vertices by ordered pairs \((i,j)\), \(0\le i,j<m\). A set \(D\) is a minimum \(k\)-limited dominating set if and only if the matrix \(A\) defined by
\[
A_{ij}=\begin{cases}1,&(i,j)\notin D,\\0,&(i,j)\in D\end{cases}
\]
is symmetric and every row has exactly \(k\) ones. In particular, \(\gamma_k^{\mathrm L}(S(2,m))=m(m-k)\). The minimum cardinality alone is not claimed as the new contribution; the all-minimizer classification and enumeration are.

The exact number \(N_{m,k}\) of distinct labelled minimum sets is
\[
N_{m,k}=[x_1^k\cdots x_m^k]\prod_{i=1}^{m}(1+x_i)\prod_{1\le i<j\le m}(1+x_ix_j).
\]
The factors indexed by a single index correspond to diagonal entries (loops count once toward row sums), and the factors indexed by pairs correspond to symmetric off-diagonal entries. Consequently, \(N_{m,k}=N_{m,m-k}\). For \(k=1\), and therefore also for \(k=m-1\), the minimum sets are in bijection with involutions of \(m\) labelled objects, so
\[
N_{m,1}=N_{m,m-1}=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{2^j j!(m-2j)!}.
\]
For \(k=2\) and \(m\ge3\), the symmetric matrices correspond to disjoint unions of ordinary cycles of length at least three and ordinary paths of length at least two with a loop at each endpoint. Hence the exponential generating function for the number of minima is
\[
\sum_{m\ge0}N_{m,2}\frac{z^m}{m!}
=\exp\left(\sum_{s\ge2}\frac{z^s}{2}+\sum_{s\ge3}\frac{z^s}{2s}\right),
\]
where the terms for \(m\le2\) count matrices but are outside the range \(2\le m-1\) when applicable. For instance, \(N_{4,2}=18\), \(N_{5,2}=112\), and the assembly formula gives \(N_{6,2}=820\).

## Assumptions and scope
The graph is finite, undirected and simple. Its vertices are \(\{(i,j):0\le i,j<m\}\); pairs with a common first coordinate are adjacent whenever distinct, and \((i,j)\) is additionally adjacent to \((j,i)\) when \(i\ne j\). A dominating set \(D\) is \(k\)-limited when every selected vertex has at most \(k\) neighbours outside \(D\). All vertex labels are fixed. The theorem covers exactly \(m\ge2\) and \(1\le k\le m-1\). The matrices are binary and symmetric, with the diagonal allowed; their row sums count each diagonal one once.

## Proof
**Row-capacity lower bound.** Fix a row \(R_i=\{(i,j):0\le j<m\}\), which induces a clique \(K_m\). The diagonal vertex \((i,i)\) has no neighbour outside \(R_i\). Consequently no dominating set can avoid an entire row: if \(D\cap R_i=\varnothing\), then \((i,i)\) is undominated. For a selected vertex \(u\in R_i\cap D\), all \(|R_i\setminus D|\) vertices of that row outside \(D\) are its neighbours, and hence \(|R_i\setminus D|\le k\). Summing over rows gives \(|D|\ge m(m-k)\).

**Sharpness.** Construct a symmetric binary matrix with row sum \(k\) by using a cyclic labelling of the rows. If \(k\) is even, put ones at circular offsets \(\pm1,\ldots,\pm k/2\). If \(k\) is odd, use a one on the diagonal plus offsets \(\pm1,\ldots,\pm(k-1)/2\). All offsets are distinct because \(k\le m-1\). Let the complement of \(D\) consist of the \((i,j)\) at which the matrix is one. Every row has \(m-k\ge1\) selected vertices, so every omitted vertex is dominated within its own row. A selected vertex sees exactly \(k\) omitted neighbours within its row. If it has an extra neighbour through a cross-row edge \((i,j)(j,i)\), symmetry would make its opposite endpoint selected as well, so it has no additional omitted neighbour. Thus \(D\) is \(k\)-limited, giving equality in the lower bound.

**Classification of equality.** In a minimum set each row must achieve its row-capacity bound, so each row contains exactly \(k\) omitted vertices. Every selected vertex already sees exactly \(k\) omitted neighbours inside its row. If an off-diagonal omitted vertex \((i,j)\) had a selected partner \((j,i)\), the selected partner would see one further omitted vertex beyond its row, violating the limit. Therefore omission of \((i,j)\) is equivalent to omission of \((j,i)\). This proves symmetry of \(A\). Conversely every symmetric row-\(k\) matrix gives a minimum set by the sharpness argument. The claimed bijection follows.

**Exact counts.** Choose each diagonal one independently, giving \(1+x_i\), and each symmetric off-diagonal pair independently, giving \(1+x_ix_j\). The exponent of \(x_i\) counts the ones in row \(i\). Extracting simultaneous exponent \(k\) yields precisely the stated number. Complementation \(A\mapsto J-A\) is an involution from constant row sum \(k\) to constant row sum \(m-k\), proving the symmetry of counts. When \(k=1\), each row chooses either its diagonal one or exactly one symmetric off-diagonal pair. These choices partition the labels into fixed points and transpositions, giving the familiar involution formula. When \(k=2\), a vertex of the associated graph without a loop has ordinary degree two; a vertex with a loop has ordinary degree one. Thus its components are either cycles of length at least three with no loops, or paths of length at least two with loops precisely on their endpoints. There are \(s!/2\) labelled paths of order \(s\ge2\) and \((s-1)!/2\) labelled cycles of order \(s\ge3\). The exponential formula for labelled components proves the stated generating function.

## Verification
The accompanying `verify.py` constructs adjacency lists directly from the two-level Sierpiński definition and checks domination and the \(k\)-limited condition without using the symmetric-matrix criterion. It enumerates every candidate with \(k\) omitted vertices in each row for \(2\le m\le5\), then compares the counts with an independent enumeration of symmetric binary matrices. It separately checks all vertex subsets for \(m=2,3\) to confirm the lower-bound boundary. Results are \(N_{2,1}=2\); \(N_{3,1}=N_{3,2}=4\); \(N_{4,1}=N_{4,3}=10\), \(N_{4,2}=18\); \(N_{5,1}=N_{5,4}=26\), \(N_{5,2}=N_{5,3}=112\). These finite experiments corroborate, but do not prove, the unrestricted theorem.

## Relationship to prior work
Božović's October 2026 preprint, *On \(k\)-limited domination: complexity and Sierpiński graphs* (arXiv:2610.01584v1), establishes the scalar \(1\)-limited value for all Sierpiński graphs and the scalar \(k\)-limited values for \(S(n,3)\), and proposes a broader scalar conjecture. In particular, its \(n=2,k=1\) result and its \(m=3\) cases are already known. The prior paper's displayed construction corresponds to one of the many matrices classified here. The 2026 initiating preprint *On \(k\)-limited domination in graphs* (arXiv:2606.22422) establishes the parameter's definition and general results. These results do not enumerate all optimal sets on \(S(2,m)\), identify their regular-looped-graph correspondence, or derive the minimum-set generating counts. Known enumeration of involutions and regular graph matrices is background combinatorics and is not separately claimed as new. Searches reported in the accompanying review are bounded rather than an exhaustive historical priority determination.

## Limitations
Only the two-level graph \(S(2,m)\) is classified. The argument does not assert an analogous matching/matrix correspondence at higher levels \(S(n,m)\) with \(n\ge3\). The coefficient-extraction formula is exact but is not a uniformly elementary closed form for arbitrary \(k\); the more explicit involution and component formulas concern \(k=1\) and \(k=2\). Historical priority has not been independently certified, and no independent mathematical audit has been performed.

## References
- D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1, submitted 2026-10-01, especially Section 2 and Theorems 10–11 in Section 5. https://arxiv.org/html/2610.01584v1
- D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422, submitted 2026-06-21. https://arxiv.org/abs/2606.22422
- S. Klavžar and U. Milutinović, *Graphs \(S(n,k)\) and a variant of the Tower of Hanoi problem*, Czechoslovak Mathematical Journal 47 (1997), 95–104. Historical definition reference; no claim of full-text inspection.
