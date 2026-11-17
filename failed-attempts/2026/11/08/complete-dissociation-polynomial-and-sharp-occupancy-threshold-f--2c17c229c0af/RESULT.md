# Complete dissociation polynomial and sharp occupancy threshold for rook graphs

## Finding
For positive integers \(m,n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on an \(m\)-by-\(n\) rectangular board. Its vertices are the named squares; two distinct squares are adjacent if they lie in a common row or column. A *dissociation set* is a set \(S\) of squares whose induced subgraph has maximum degree at most one. Define \(d_{m,n}(k)\) to be the number of dissociation sets of cardinality \(k\), and their polynomial
\[
\mathcal D_{m,n}(z)=\sum_{k=0}^{mn}d_{m,n}(k)z^k.
\]
**Theorem.** For every pair \(m,n\ge 1\),
\[
\boxed{\mathcal D_{m,n}(z)=
\sum_{\substack{p,q,a\ge0\\p+2q+a\le m\\2p+q+a\le n}}
\frac{m!n!\,z^{2p+2q+a}}{2^{p+q}p!q!a!(m-p-2q-a)!(n-2p-q-a)!}.}
\]
Consequently, the maximum number of selected squares is exactly
\[
\boxed{\beta_2(R_{m,n})=\min\!\left\{2m,\,2n,\,\left\lfloor\frac{2(m+n)}{3}\right\rfloor\right\}.}
\]
This describes the **entire cardinality distribution**, including the exact number of maximum dissociation sets from the leading coefficient. The sharp maximum changes regime when the longer side reaches twice the shorter side. For example, the complete polynomial for a \(2\)-by-\(3\) board is
\[
\mathcal D_{2,3}(z)=1+6z+15z^2+6z^3.
\]

## Assumptions and scope
The board has labelled, distinguishable row and column positions. Graphs are finite, undirected, simple; \(m,n\ge1\). The empty set is counted. The degree condition concerns the **induced selected-square graph**, not the original rook-graph degree, and allows isolated selected vertices and disjoint selected edges. No proper colouring or ordinary domination condition is assumed.

## Proof
**Step 1: translate to a bipartite graph.** Identify a square \((i,j)\) with the edge between row vertex \(i\) and column vertex \(j\) in \(K_{m,n}\). This identifies the rook graph with the line graph \(L(K_{m,n})\). For the selected edge set \(S\), let \(H\) be its spanning bipartite edge subgraph. At an edge \(uv\) of \(H\), the number of neighbours of the corresponding rook-graph vertex inside \(S\) equals
\[
(d_H(u)-1)+(d_H(v)-1)=d_H(u)+d_H(v)-2.
\]
Thus \(S\) is dissociating precisely when every selected edge \(uv\) satisfies \(d_H(u)+d_H(v)\le3\). In particular, every nonisolated vertex of \(H\) has degree at most two, and an edge incident to a degree-two vertex must have a degree-one other endpoint. Therefore, **every nontrivial component** of \(H\) is either an isolated edge \(K_2\) or a two-edge path \(P_3\). Conversely, any vertex-disjoint union of such components has the required property.

**Step 2: count component types without overcounting.** Write \(p\) for the number of two-edge paths whose central vertex is a row, \(q\) for those whose centre is a column, and \(a\) for isolated edges. These components occupy exactly \(p+2q+a\) row vertices and \(2p+q+a\) column vertices, giving precisely the constraints in the displayed summation. All component types and their central vertices are intrinsic to \(H\), so the decomposition is unique.

Choose an ordered list of \(p\) row centres and an ordered list of \(q\) column centres; assign their disjoint pairs of opposite-side leaves (each pair has two interchangeable endpoints); then match the remaining \(a\) chosen row and column vertices in isolated edges. Dividing by the unordered component factorials \(p!,q!,a!\), by \(2!\) per two-leaf pair, and by the factorials for unused vertices yields exactly
\[
\frac{m!n!}{2^{p+q}p!q!a!(m-p-2q-a)!(n-2p-q-a)!}.
\]
The total number of selected squares is \(2p+2q+a\), which proves the polynomial coefficient by coefficient, including the unique empty choice.

**Step 3: upper bound for the degree.** Let \(s=2(p+q)+a\). Every row and column vertex has at most two selected edges, hence \(s\le2m\) and \(s\le2n\). Every nontrivial component uses at least three vertices for two edges, and the isolated edge uses two vertices for one edge; therefore
\[
3s\le 2(m+n).
\]
Taking the floor gives the asserted three-part upper bound.

**Step 4: attain it uniformly.** By symmetry suppose \(m\le n\). If \(n\ge2m\), take \(p=m,q=a=0\), consisting of \(m\) row-centred two-edge paths with disjoint column leaves. This has \(2m\) squares and meets the upper bound.

Otherwise \(m\le n<2m\). Set
\[
t=\left\lfloor\frac{m+n}{3}\right\rfloor,
\qquad a=\begin{cases}1,&m+n\equiv2\pmod{3},\\0,&\text{otherwise},\end{cases}
\qquad p=\max\{0,2t+a-m\},\quad q=t-p.
\]
Since \(m\le n<2m\), we have \(t+a\le m\). Consequently \(0\le p\le t\), so \(q\ge0\). Also \(2t+a-p\le m\). For the other side, if \(p=0\), then \(t+a\le n\). If \(p>0\), then
\[
t+a+p=3t+2a-m\le n,
\]
because \(3t+2a\le m+n\) in all three residue classes of \(m+n\) modulo three. Hence \((p,q,a)\) is feasible. It has
\[
2(p+q)+a=2t+a=\left\lfloor\frac{2(m+n)}{3}\right\rfloor
\]
selected edges. In this regime this equals the asserted minimum, because \(n<2m\) and \(m\le n\). The proof is valid also at \(m=n=1\) and other one-row/one-column boundaries. \(\square\)

## Verification
Run `python3 artifacts/verify.py` from the package root (Python 3.10 or later, standard library only). Its direct checker enumerates all \(2^{mn}\) square subsets for the listed small boards, tests the induced degree bound directly, and compares every coefficient with the component-count formula. It also checks the extremal formula and explicit feasibility construction for every ordered pair of dimensions from \(1\) through \(39\). The known PUMaC 2010 \(6\)-by-\(6\) result is also independently reproduced at eight rooks and 8100 maximum arrangements. All cases pass with final marker `VERIFY_OK`. These finite checks test the implementations and boundaries; the unrestricted assertions follow from Steps 1–4, not from the finite range.

## Relationship to prior work
The 2026 paper *Sub-quorum colorings of graphs* (arXiv:2609.25128, first public September 20, 2026) develops the link between sub-quorum colouring and \(2\)-independence, motivating the search for exact dissociation data on familiar Cartesian products. Its rectangular grids have path factors \(P_m\square P_n\), unlike the clique-factor rook graphs here. Because \(\psi_{sq}(G)\ge\beta_2(G)\) there, the sharp degree formula gives an explicit lower bound for that parameter on rook graphs; no equality for \(\psi_{sq}\) is claimed.

Orlovich, Dolgui, Finke, Gordon and Werner (2011) studied dissociation sets of line graphs, including a theorem for graphs with a Hamiltonian path that implies the maximum-size part of this result on balanced complete bipartite hosts. That special-case maximum is credited, **not claimed as new**. Their stated results do not enumerate dissociation sets of all cardinalities on arbitrary rectangular rook boards. Mertens (2024) derives the rook-graph **domination** polynomial, which counts a different subset predicate; it does not imply this polynomial. The classical nonattacking-rook polynomial counts only the special case \(p=q=0\), with all selected vertices isolated. A 2010 PUMaC combinatorics problem specifically asks for the maximum and the number of optimal arrangements on a \(6\)-by-\(6\) board under the **same at-most-one-attacker constraint**. Its solution \(8\) rooks in exactly \(8100\) arrangements is a previously known special coefficient and is independently reproduced by the present formula; **that particular finite result is not claimed as new**.

## Limitations
The finding concerns dissociation sets on rectangular rook graphs only. It does not count maximal dissociation sets separately, nor determine sub-quorum colouring numbers. The maximum-cardinality formula overlaps a prior line-graph theorem in balanced regimes; the all-coefficient, all-aspect-ratio distribution is the principal distinct contribution. The 2010 \(6\)-by-\(6\) optimum and its count are known and credited. Independent mathematical assessment and exhaustive historical priority verification have not been performed. In particular, equivalent enumerations under another combinatorial name remain a residual priority risk.

## References
1. R. Sahbi (initial version); H. Ma, R. Sahbi and W. Zhang (later versions), *Sub-quorum colorings of graphs*, arXiv:2609.25128 (first publicly posted September 20, 2026), https://arxiv.org/abs/2609.25128 .
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics (2011), DOI:10.1016/j.dam.2011.04.023 .
3. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), Article 24.3.7, arXiv:2401.00716, https://arxiv.org/html/2401.00716v2 .
4. Princeton University Mathematics Competition, *PUMaC 2010 Combinatorics B Solutions*, Problem 7, pp. 4–5, https://static1.squarespace.com/static/570450471d07c094a39efaed/t/58b09455893fc05441866dbd/1487967317870/PUMaC2010_CombinatoricsBSol.pdf .
5. B.-J. Yuan, N. Yang, H.-Y. Ge and S.-C. Gong, *The number of dissociation sets in connected graphs*, arXiv:2412.17095 (2024).
